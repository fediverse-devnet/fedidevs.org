---
title: Webfinger sample files
description: A selection of Webfinger files as produced by common Fediverse apps
---

As of 2024-04-11 03:35:10 UTC. To regenerate, run `make`
in directory `scripts`.

## App: Mastodon, handle ``@gargron@mastodon.social``

Endpoint: https://mastodon.social/.well-known/webfinger?resource=acct%3agargron%40mastodon.social

```js
{
  "subject": "acct:Gargron@mastodon.social",
  "aliases": [
    "https://mastodon.social/@Gargron",
    "https://mastodon.social/users/Gargron"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://mastodon.social/@Gargron"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://mastodon.social/users/Gargron"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://mastodon.social/authorize_interaction?uri={uri}"
    },
    {
      "rel": "http://webfinger.net/rel/avatar",
      "type": "image/png",
      "href": "https://files.mastodon.social/accounts/avatars/000/000/001/original/a0a49d80c3de5f75.png"
    }
  ]
}
```

## App: PeerTube, handle ``@peertube@framapiaf.org``

Endpoint: https://framapiaf.org/.well-known/webfinger?resource=acct%3apeertube%40framapiaf.org

```js
{
  "subject": "acct:peertube@framapiaf.org",
  "aliases": [
    "https://framapiaf.org/@peertube",
    "https://framapiaf.org/users/peertube"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://framapiaf.org/@peertube"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://framapiaf.org/users/peertube"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://framapiaf.org/authorize_interaction?uri={uri}"
    },
    {
      "rel": "http://webfinger.net/rel/avatar",
      "type": "image/png",
      "href": "https://stockage.framapiaf.org/framapiaf/accounts/avatars/000/223/824/original/03ed95406a9a3cd0.png"
    }
  ]
}
```

## App: Misskey, handle ``https://misskey.io/@syuilo``

Endpoint: https://misskey.io/.well-known/webfinger?resource=https://misskey.io/@syuilo

```js
{
  "subject": "acct:syuilo@misskey.io",
  "links": [
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://misskey.io/users/7rkrarq81i"
    },
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://misskey.io/@syuilo"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://misskey.io/authorize-follow?acct={uri}"
    }
  ]
}
```

## App: Streams, handle ``@mike@macgirvin.com``

Endpoint: https://macgirvin.com/.well-known/webfinger?resource=acct%3amike%40macgirvin.com

```js
{
  "subject": "acct:mike@macgirvin.com",
  "aliases": [
    "https://macgirvin.com/channel/mike",
    "https://macgirvin.com/~mike",
    "https://macgirvin.com/@mike",
    "https://macgirvin.com/channel/mike"
  ],
  "properties": {
    "http://webfinger.net/ns/name": "Mike Macgirvin",
    "http://xmlns.com/foaf/0.1/name": "Mike Macgirvin",
    "https://w3id.org/security/v1#publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAoaTPG5iYKsHJ1cK5CJUy\niN2y6B7aI4JkKMjjZO0gy8+6oa5kx6H5w7qED937a/SvwuYxh1A5yO9nwoEarM5s\nPoYZ+Z+GGbAcvzdWURtDDdRMNgktAayDiOvEdiEbgPVx8f39YnpX39ngM8ukob16\nS8eNwjWG6uwBs6rxSA409fkWjjbQwbe8fNOpynFWoG8jrB+dK6huryYqkyf9S18u\n01IAJOo1ErtaUNkSzkeudXSWokRbN/P77N8LQXorwPF9U6ODblX9QXCWl6EnQ0CX\nfcC/3NM6uXfda2KTn83G1+mo5QgGYBjGzE9K1VngoyX4J8AqvQxoXkqV20vwFSqW\nccB13F5kqRQ4BoQm2v2/e65YzjrHwkUecj7tS8TVXu8z4mdbDDbso/UrS14JmrJh\njnbwPOYpHX/6p2SdYDTF/vUWUmeSatS7sHK92eTRukuONig+PNvx8GUtxgMWPIgH\njIupGnR5lZxFMP+iaAmfxOSbVNeLn/Nka7+UfkDThApfhesBA6P8jAdStTCyqAYB\nY3rTTwplcaKKnNv+pLqBqyhYEghmGvv2EC2UGsL6rFit1RaZgSXWCIcLzdRZo4Ak\nznvz8+juMjyPLp7DdSHhKss9kV9HDxZXjrstDxOR61j0vifaMh6bUVrOAMm0Ffs+\n41v+D6pSA5p0OI2aqNJzLZ8CAwEAAQ==\n-----END PUBLIC KEY-----\n"
  },
  "links": [
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://macgirvin.com/channel/mike"
    },
    {
      "rel": "self",
      "type": "application/ld+json; profile=\"https://www.w3.org/ns/activitystreams\"",
      "href": "https://macgirvin.com/channel/mike"
    },
    {
      "rel": "http://webfinger.net/rel/avatar",
      "type": "image/jpeg",
      "href": "https://macgirvin.com/photo/profile/l/5"
    },
    {
      "rel": "http://webfinger.net/rel/blog",
      "href": "https://macgirvin.com/channel/mike"
    },
    {
      "rel": "http://purl.org/nomad",
      "type": "application/x-nomad+json",
      "href": "https://macgirvin.com/channel/mike"
    },
    {
      "rel": "http://purl.org/openwebauth/v1",
      "type": "application/x-nomad+json",
      "href": "https://macgirvin.com/owa"
    },
    {
      "rel": "http://purl.org/openwebauth/v1#redirect",
      "type": "application/x-nomad+json",
      "href": "https://macgirvin.com/magic"
    },
    {
      "rel": "http://purl.org/zot/protocol/6.0",
      "type": "application/x-zot+json",
      "href": "https://macgirvin.com/channel/mike"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://macgirvin.com/follow?url={uri}"
    },
    {
      "rel": "http://a9.com/-/spec/opensearch/1.1/",
      "type": "application/opensearchdescription+xml",
      "href": "https://macgirvin.com/opensearch/mike",
      "title": "mike@macgirvin.com"
    }
  ]
}
```

## App: Hubzilla, handle ``@scott@authorship.studio``

Endpoint: https://authorship.studio/.well-known/webfinger?resource=acct%3ascott%40authorship.studio

```js
{
  "subject": "acct:scott@authorship.studio",
  "aliases": [
    "https://authorship.studio/channel/scott",
    "https://authorship.studio/~scott",
    "https://authorship.studio/@scott",
    "acct:scott@biztechtonics.net",
    "acct:scott@completehostingguide.com",
    "acct:scott@wistex.biz",
    "acct:scott@scottstolz.com"
  ],
  "properties": {
    "http://webfinger.net/ns/name": "Scott M. Stolz",
    "http://xmlns.com/foaf/0.1/name": "Scott M. Stolz",
    "https://w3id.org/security/v1#publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvBaccO+wjQ9hQ6cb23a1\nCV0cv8QVH7Cu/KR55ogX5uJ+IW4uMcxmLQkyw/5oFbZOgjvDxm7zDqkDp45R2aIC\nyRmcpjSy2+sREM7OBzin9GY3N4EYrXNdl6eamrSk8v3gArIe/UbwoEzXzM4lcvut\nZGqgjoo/42j1eaAYGG/Wyzs7K3GFVJBOwYS6us/k9noF8sUE+vJI0c9UEbODNfyU\nsPC+R/n++lECAkV04a/FDqCztkqExtz2xpXnNs+yuHij4e1g3QAvcaUmIKhD2DzG\nU70pt1y4q9vZ+U/D092wGQ6fQ48r6/GG9c4yWwOxeKZfT0E8Bg5YP3NW6aGxrZA4\nOKkW3UFhTWFlBK/7DNcsuzZBA8Svt5kjJYO89xYfTAQ3ywgkKQG13/KdF2iRzlCS\nBv5qq2obBsdqOfoibd9la4tC0RY6R934DLlhHvGX57gKtbm1Fc1fOXwCYd5YMXPa\n1ewG2dD02fZ4h1zeZL2uqlzkrSEE6tiMcaux7I63q1y0MW2NFIp8i65BeSsHDcKR\n1khiDmjxN+OZLgJ7PpJM6C7xKj1V/YxP8lD5uCFFUlD9v4F1j1wa0aQ+I9nOfVwJ\nRcfCyQvXDWyen9vne8XOXV1Kb8qm7FCyrUs4WHt5AZaXC5em+RMlFM7eY+YAnxcs\nRAMnWdbqj5wXroPxEypQn60CAwEAAQ==\n-----END PUBLIC KEY-----\n",
    "http://purl.org/zot/federation": "zot6,activitypub"
  },
  "links": [
    {
      "rel": "http://webfinger.net/rel/avatar",
      "type": "",
      "href": "https://authorship.studio/photo/profile/l/4"
    },
    {
      "rel": "http://microformats.org/profile/hcard",
      "type": "text/html",
      "href": "https://authorship.studio/hcard/scott"
    },
    {
      "rel": "http://openid.net/specs/connect/1.0/issuer",
      "href": "https://authorship.studio"
    },
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "href": "https://authorship.studio/profile/scott"
    },
    {
      "rel": "http://webfinger.net/rel/blog",
      "href": "https://authorship.studio/channel/scott"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://authorship.studio/follow?f=&url={uri}"
    },
    {
      "rel": "http://purl.org/zot/protocol/6.0",
      "type": "application/x-zot+json",
      "href": "https://authorship.studio/channel/scott"
    },
    {
      "rel": "http://purl.org/openwebauth/v1",
      "type": "application/x-zot+json",
      "href": "https://authorship.studio/owa"
    },
    {
      "rel": "magic-public-key",
      "href": "data:application/magic-public-key,RSA.vBaccO-wjQ9hQ6cb23a1CV0cv8QVH7Cu_KR55ogX5uJ-IW4uMcxmLQkyw_5oFbZOgjvDxm7zDqkDp45R2aICyRmcpjSy2-sREM7OBzin9GY3N4EYrXNdl6eamrSk8v3gArIe_UbwoEzXzM4lcvutZGqgjoo_42j1eaAYGG_Wyzs7K3GFVJBOwYS6us_k9noF8sUE-vJI0c9UEbODNfyUsPC-R_n--lECAkV04a_FDqCztkqExtz2xpXnNs-yuHij4e1g3QAvcaUmIKhD2DzGU70pt1y4q9vZ-U_D092wGQ6fQ48r6_GG9c4yWwOxeKZfT0E8Bg5YP3NW6aGxrZA4OKkW3UFhTWFlBK_7DNcsuzZBA8Svt5kjJYO89xYfTAQ3ywgkKQG13_KdF2iRzlCSBv5qq2obBsdqOfoibd9la4tC0RY6R934DLlhHvGX57gKtbm1Fc1fOXwCYd5YMXPa1ewG2dD02fZ4h1zeZL2uqlzkrSEE6tiMcaux7I63q1y0MW2NFIp8i65BeSsHDcKR1khiDmjxN-OZLgJ7PpJM6C7xKj1V_YxP8lD5uCFFUlD9v4F1j1wa0aQ-I9nOfVwJRcfCyQvXDWyen9vne8XOXV1Kb8qm7FCyrUs4WHt5AZaXC5em-RMlFM7eY-YAnxcsRAMnWdbqj5wXroPxEypQn60.AQAB"
    },
    {
      "rel": "self",
      "type": "application/ld+json; profile=\"https://www.w3.org/ns/activitystreams\"",
      "href": "https://authorship.studio/channel/scott"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://authorship.studio/channel/scott"
    }
  ]
}
```

## App: GNU Social, handle ``@administrator@gnusocial.net``

Endpoint: https://gnusocial.net/.well-known/webfinger?resource=acct%3aadministrator%40gnusocial.net

```js
{
  "subject": "acct:administrator@gnusocial.net",
  "aliases": [
    "https://gnusocial.net/index.php/user/1",
    "https://gnusocial.net/administrator",
    "https://gnusocial.net/user/1",
    "https://gnusocial.net/index.php/administrator"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://gnusocial.net/administrator"
    },
    {
      "rel": "http://gmpg.org/xfn/11",
      "type": "text/html",
      "href": "https://gnusocial.net/administrator"
    },
    {
      "rel": "describedby",
      "type": "application/rdf+xml",
      "href": "https://gnusocial.net/administrator/foaf"
    },
    {
      "rel": "http://apinamespace.org/atom",
      "type": "application/atomsvc+xml",
      "href": "https://gnusocial.net/api/statusnet/app/service/administrator.xml"
    },
    {
      "rel": "http://apinamespace.org/twitter",
      "href": "https://gnusocial.net/api/"
    },
    {
      "rel": "http://schemas.google.com/g/2010#updates-from",
      "type": "application/atom+xml",
      "href": "https://gnusocial.net/api/statuses/user_timeline/1.atom"
    },
    {
      "rel": "magic-public-key",
      "href": "data:application/magic-public-key,RSA.lrWlx-ufdZ3OgBuV1ZKHQ1T4Rx99QcThod8Bpn1jhmpOufts8oQ1CV7YK0SKTCHLFU6ZQSjm8f3aftoHnW6W51WxqCFD6VFFpQYO6ur8Vf0rYRIpgLVKKS1dl5OdVdQ0Rtj1fsUC2QMD9f7r4tEJQmHnjM8t7twjlN_x83gxwis=.AQAB"
    },
    {
      "rel": "diaspora-public-key",
      "type": "RSA",
      "href": "LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tDQpNSUdKQW9HQkFKYTFwY2ZybjNXZHpvQWJsZFdTaDBOVStFY2ZmVUhFNGFIZkFhWjlZNFpxVHJuN2JQS0VOUWxlDQoyQ3RFaWt3aHl4Vk9tVUVvNXZIOTJuN2FCNTF1bHVkVnNhZ2hRK2xSUmFVR0R1cnEvRlg5SzJFU0tZQzFTaWt0DQpYWmVUblZYVU5FYlk5WDdGQXRrREEvWCs2K0xSQ1VKaDU0elBMZTdjSTVUZjhmTjRNY0lyQWdNQkFBRT0NCi0tLS0tRU5EIFJTQSBQVUJMSUMgS0VZLS0tLS0="
    },
    {
      "rel": "http://joindiaspora.com/guid",
      "href": "a7ea2e0f4f4b270d6a1b59638171309d5d1225b0a8dfd2473e375ded45bd4982"
    },
    {
      "rel": "salmon",
      "href": "https://gnusocial.net/main/salmon/user/1"
    },
    {
      "rel": "http://salmon-protocol.org/ns/salmon-replies",
      "href": "https://gnusocial.net/main/salmon/user/1"
    },
    {
      "rel": "http://salmon-protocol.org/ns/salmon-mention",
      "href": "https://gnusocial.net/main/salmon/user/1"
    },
    {
      "rel": "http://specs.openid.net/auth/2.0/provider",
      "href": "https://gnusocial.net/administrator"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://gnusocial.net/main/remotefollowsub?profile={uri}"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://gnusocial.net/index.php/user/1"
    }
  ]
}
```

## App: Pleroma, handle ``@karolat@stereophonic.space``

Endpoint: https://stereophonic.space/.well-known/webfinger?resource=acct%3akarolat%40stereophonic.space

```js
{
  "aliases": [
    "https://stereophonic.space/users/karolat"
  ],
  "links": [
    {
      "href": "https://stereophonic.space/users/karolat",
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html"
    },
    {
      "href": "https://stereophonic.space/users/karolat",
      "rel": "self",
      "type": "application/activity+json"
    },
    {
      "href": "https://stereophonic.space/users/karolat",
      "rel": "self",
      "type": "application/ld+json; profile=\"https://www.w3.org/ns/activitystreams\""
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://stereophonic.space/ostatus_subscribe?acct={uri}"
    }
  ],
  "subject": "acct:karolat@stereophonic.space"
}
```

## App: Pixelfed, handle ``@dansup@pixelfed.social``

Endpoint: https://pixelfed.social/.well-known/webfinger?resource=acct%3adansup%40pixelfed.social

```js
{
  "subject": "acct:dansup@pixelfed.social",
  "aliases": [
    "https://pixelfed.social/dansup",
    "https://pixelfed.social/users/dansup"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://pixelfed.social/dansup"
    },
    {
      "rel": "http://schemas.google.com/g/2010#updates-from",
      "type": "application/atom+xml",
      "href": "https://pixelfed.social/users/dansup.atom"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://pixelfed.social/users/dansup"
    },
    {
      "rel": "http://webfinger.net/rel/avatar",
      "type": "image/jpeg",
      "href": "https://pixelfed.social/storage/avatars/000/000/000/000/000/000/2/mLZr2R47XEwbmasH2M3P_avatar.jpg?v=57"
    }
  ]
}
```

## App: Friendica, handle ``@tobias@friendi.ca``

Endpoint: https://friendi.ca/.well-known/webfinger?resource=acct%3atobias%40friendi.ca

```js
{
  "subject": "acct:tobias@friendi.ca",
  "aliases": [
    "acct:tobias@friendi.ca",
    "https://friendi.ca/author/tobias/",
    "https://friendi.ca/author/tobias/",
    "https://friendi.ca/@tobias"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "href": "https://friendi.ca/author/tobias/",
      "type": "text/html"
    },
    {
      "rel": "http://webfinger.net/rel/avatar",
      "href": "https://secure.gravatar.com/avatar/7faf7abf39f117b7bb2cf8e08f4eded7?s=96&#038;d=mm&#038;r=g"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://friendi.ca/author/tobias/"
    }
  ]
}
```

## App: Funkwhale, handle ``@Greensky@open.audio``

Endpoint: https://open.audio/.well-known/webfinger?resource=acct%3aGreensky%40open.audio

```js
{
  "subject": "acct:Greensky@open.audio",
  "links": [
    {
      "rel": "self",
      "href": "https://open.audio/federation/actors/Greensky",
      "type": "application/activity+json"
    }
  ],
  "aliases": [
    "https://open.audio/federation/actors/Greensky"
  ]
}
```

## App: WriteFreely, handle ``@matt@write.as``

Endpoint: https://write.as/.well-known/webfinger?resource=acct%3amatt%40write.as

```js
{
  "subject": "acct:matt@write.as",
  "aliases": [
    "https://write.as/matt/",
    "https://write.as/api/collections/matt"
  ],
  "links": [
    {
      "href": "https://write.as/matt/",
      "type": "text/html",
      "rel": "https://webfinger.net/rel/profile-page"
    },
    {
      "href": "https://write.as/api/collections/matt",
      "type": "application/activity+json",
      "rel": "self"
    }
  ]
}
```

## App: Plume, handle ``@actapopuli@fediverse.blog``

Endpoint: https://fediverse.blog/.well-known/webfinger?resource=acct%3aactapopuli%40fediverse.blog

```js
{
  "subject": "acct:actapopuli@fediverse.blog",
  "aliases": [
    "https://fediverse.blog/@/actapopuli/"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "href": "https://fediverse.blog/@/actapopuli/",
      "type": "text/html"
    },
    {
      "rel": "http://schemas.google.com/g/2010#updates-from",
      "href": "https://fediverse.blog/@/actapopuli/feed.atom",
      "type": "application/atom+xml"
    },
    {
      "rel": "self",
      "href": "https://fediverse.blog/@/actapopuli/",
      "type": "application/activity+json"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://fediverse.blog/remote_interact?target={uri}"
    }
  ]
}
```

## App: Mobilizon, handle ``@framasoft@mobilizon.fr``

Endpoint: https://mobilizon.fr/.well-known/webfinger?resource=acct%3aframasoft%40mobilizon.fr

```js
{
  "aliases": [
    "https://mobilizon.fr/@framasoft"
  ],
  "links": [
    {
      "href": "https://mobilizon.fr/@framasoft",
      "rel": "self",
      "type": "application/activity+json"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://mobilizon.fr/interact?uri={uri}"
    },
    {
      "href": "https://mobilizon.fr/media/890f5396ef80081a6b1b18a5db969746cf8bb340e8a4e657d665e41f6646c539.jpg?name=framasoft%27s%20avatar.jpg",
      "rel": "http://webfinger.net/rel/avatar",
      "type": "image/jpeg"
    },
    {
      "href": "https://mobilizon.fr/@framasoft",
      "rel": "http://webfinger.net/rel/profile-page/",
      "type": "text/html"
    }
  ],
  "subject": "acct:framasoft@mobilizon.fr"
}
```

## App: Lemmy, handle ``@lemmy_support@lemmy.ml``

Endpoint: https://lemmy.ml/.well-known/webfinger?resource=acct%3alemmy_support%40lemmy.ml

```js
{
  "subject": "acct:lemmy_support@lemmy.ml",
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://lemmy.ml/c/lemmy_support",
      "template": null
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://lemmy.ml/c/lemmy_support",
      "template": null,
      "properties": {
        "https://www.w3.org/ns/activitystreams#type": "Group"
      }
    }
  ]
}
```

## App: Micro.blog, handle ``@manton@manton.org``

Endpoint: https://manton.org/.well-known/webfinger?resource=acct%3amanton%40manton.org

```js
{
  "subject": "acct:manton@manton.org",
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://manton.org/activitypub/manton"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://manton.org/activitypub/manton"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://micro.blog/mastodon/follow?url={uri}"
    }
  ]
}
```

## App: Threads, handle ``@mosseri@threads.net``

Endpoint: https://threads.net/.well-known/webfinger?resource=acct%3amosseri%40threads.net

```js
{
  "subject": "acct:mosseri@threads.net",
  "links": [
    {
      "href": "https://www.threads.net/ap/users/mosseri/",
      "rel": "self",
      "type": "application/activity+json"
    },
    {
      "href": "https://www.threads.net/@mosseri",
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html"
    }
  ]
}
```

