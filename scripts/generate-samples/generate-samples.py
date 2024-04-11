#!/usr/bin/python
#
# Generate documentation pages with samples of webfinger and actor files
# from various Fediverse servers/apps
#
# (C) 2023-2024 Johannes Ernst, BSD 3-clause license
#

import argparse
import json
import re
from time import gmtime, strftime
import urllib.request


USER_AGENT = 'fedidevs.org/reference'
# The default python user agent appears to be blocked by various fediverse servers.
# We might as well say who we are


def read_accounts_file(file_name : str) -> dict:
    with open( file_name, 'r' ) as fd :
        sample_accounts_content = fd.read()

    return json.loads( sample_accounts_content )


def handle_to_webfinger_endpoint(handle : str) -> str:
    match = re.match("@([^@]+)@([^@]+)", handle)
    if match:
        ret = f"https://{ match.group(2) }/.well-known/webfinger?resource=acct%3a{ match.group(1) }%40{ match.group(2) }"
        return ret

    match = re.match("https://([^/]+)/", handle)
    if match:
        ret = f"https://{ match.group(1) }/.well-known/webfinger?resource={ handle }"
        return ret

    raise ValueError('Cannot parse: ' + handle)


def emit_header(title : str, description : str, out_fd : 'file') :
    out_fd.write( f"""---
title: {title}
description: {description}
---

As of { strftime("%Y-%m-%d %H:%M:%S UTC", gmtime()) }. To regenerate, run `make`
in directory `scripts`.

""" )


def emit_webfinger(app : str, handle : str, out_fd : 'file' ) :
    try :
        out_fd.write(f"## App: {app}, handle ``{handle}``\n")
        wf_url = handle_to_webfinger_endpoint(handle)
        wf_content = urllib.request.urlopen(urllib.request.Request(wf_url, headers={ 'User-Agent' : USER_AGENT } )).read()
        wf_json = json.loads(wf_content.decode('utf-8'))

        out_fd.write("\n")
        out_fd.write(f"Endpoint: {wf_url}\n" )
        out_fd.write("\n")
        out_fd.write("```js\n" )
        out_fd.write(json.dumps( wf_json, indent=2))
        out_fd.write("\n")
        out_fd.write("```\n" )
        out_fd.write("\n")

    except Exception as e:
        out_fd.write(f"ERROR when attempting to get webfinger data for {handle} at {wf_url}. Skipping: {e}\n")
        out_fd.write("\n")
        print( f"ERROR when attempting to get webfinger data for {handle} at {wf_url}. Skipping: {e}")


def emit_actor(app : str, handle : str, out_fd : 'file' ) :
    try :
        out_fd.write(f"## App: {app}, handle ``{handle}``\n" )
        wf_url = handle_to_webfinger_endpoint( handle )
        wf_content = urllib.request.urlopen(urllib.request.Request(wf_url, headers={ 'User-Agent' : USER_AGENT } )).read()
        wf_json = json.loads(wf_content.decode( 'utf-8' ))

    except Exception as e:
        out_fd.write(f"ERROR when attempting to get webfinger data for {handle} at {wf_url}. Skipping: {e}\n")
        out_fd.write("\n")
        print( f"ERROR when attempting to get webfinger data for {handle} at {wf_url}. Skipping: {e}")
        return

    try :
        actor_url = None
        for wf_link_json in wf_json['links'] :
            if 'type' in wf_link_json and wf_link_json['type'] == 'application/activity+json' :
                actor_url = wf_link_json['href']
                break

        if actor_url :
            actor_content = urllib.request.urlopen( urllib.request.Request( actor_url, headers={ 'Accept' : 'application/activity+json', 'User-Agent' : USER_AGENT } )).read()
            actor_json = json.loads(actor_content.decode('utf-8'))

            out_fd.write("\n")
            out_fd.write(f"Endpoint: {actor_url}\n" )
            out_fd.write("\n")
            out_fd.write("```js\n" )
            out_fd.write(json.dumps( actor_json, indent=2 ))
            out_fd.write("\n")
            out_fd.write("```\n" )
            out_fd.write("\n")

        else :
            out_fd.write( "Actor JSON not found.\n" )
            out_fd.write( "\n")

    except Exception as e:
        out_fd.write(f"ERROR when attempting to get actor data for {handle} at {wf_url}. Skipping: {e}\n")
        out_fd.write("\n")
        print(f"ERROR when attempting to get actor data for {handle} at {wf_url}. Skipping: {e}")


def emit_footer( out_fd : 'file') :
    pass


parser = argparse.ArgumentParser(description='Generate webfinger samples for the docs')
parser.add_argument('--account-file', help='Name of a JSON file that contains the sample accounts')
parser.add_argument('--type', choices=['webfinger', 'actor'], required=True, help='Generate webfinger samples or actor file samples')
parser.add_argument('-o', '--out', help='Name of the output file' )

args = parser.parse_args()

sampleAccountsJson = read_accounts_file( args.account_file )

with open(args.out, 'w') as out_fd :
    if args.type == 'webfinger' :
        emit_header( 'Webfinger sample files', 'A selection of Webfinger files as produced by common Fediverse apps', out_fd )
    else :
        emit_header( 'Actor sample files', 'A selection of Actor files as produced by common Fediverse apps', out_fd )

    for app in sampleAccountsJson :
        for handle in sampleAccountsJson[app] :
            if 'disabled' in sampleAccountsJson[app][handle] :
                print(f"Skipping {handle}: disabled")
            else :
                print(f"Working on: {handle}")
                if args.type == 'webfinger' :
                    emit_webfinger(app, handle, out_fd)
                else :
                    emit_actor(app, handle, out_fd)

    emit_footer(out_fd)
