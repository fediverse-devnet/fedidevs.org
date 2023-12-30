---
title: Actor sample files
description: A selection of Actor files as produced by common Fediverse apps
---

As of 2023-12-30 15:59:05 UTC. To regenerate, run `make`
in directory `scripts`.

## App: Mastodon, handle ``@gargron@mastodon.social``

Endpoint: https://mastodon.social/users/Gargron

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "toot": "http://joinmastodon.org/ns#",
      "featured": {
        "@id": "toot:featured",
        "@type": "@id"
      },
      "featuredTags": {
        "@id": "toot:featuredTags",
        "@type": "@id"
      },
      "alsoKnownAs": {
        "@id": "as:alsoKnownAs",
        "@type": "@id"
      },
      "movedTo": {
        "@id": "as:movedTo",
        "@type": "@id"
      },
      "schema": "http://schema.org#",
      "PropertyValue": "schema:PropertyValue",
      "value": "schema:value",
      "discoverable": "toot:discoverable",
      "Device": "toot:Device",
      "Ed25519Signature": "toot:Ed25519Signature",
      "Ed25519Key": "toot:Ed25519Key",
      "Curve25519Key": "toot:Curve25519Key",
      "EncryptedMessage": "toot:EncryptedMessage",
      "publicKeyBase64": "toot:publicKeyBase64",
      "deviceId": "toot:deviceId",
      "claim": {
        "@type": "@id",
        "@id": "toot:claim"
      },
      "fingerprintKey": {
        "@type": "@id",
        "@id": "toot:fingerprintKey"
      },
      "identityKey": {
        "@type": "@id",
        "@id": "toot:identityKey"
      },
      "devices": {
        "@type": "@id",
        "@id": "toot:devices"
      },
      "messageFranking": "toot:messageFranking",
      "messageType": "toot:messageType",
      "cipherText": "toot:cipherText",
      "suspended": "toot:suspended",
      "memorial": "toot:memorial",
      "indexable": "toot:indexable",
      "focalPoint": {
        "@container": "@list",
        "@id": "toot:focalPoint"
      }
    }
  ],
  "id": "https://mastodon.social/users/Gargron",
  "type": "Person",
  "following": "https://mastodon.social/users/Gargron/following",
  "followers": "https://mastodon.social/users/Gargron/followers",
  "inbox": "https://mastodon.social/users/Gargron/inbox",
  "outbox": "https://mastodon.social/users/Gargron/outbox",
  "featured": "https://mastodon.social/users/Gargron/collections/featured",
  "featuredTags": "https://mastodon.social/users/Gargron/collections/tags",
  "preferredUsername": "Gargron",
  "name": "Eugen Rochko",
  "summary": "<p>Founder of <span class=\"h-card\" translate=\"no\"><a href=\"https://mastodon.social/@Mastodon\" class=\"u-url mention\">@<span>Mastodon</span></a></span>. Film photography, prog metal, Dota 2.</p>",
  "url": "https://mastodon.social/@Gargron",
  "manuallyApprovesFollowers": false,
  "discoverable": true,
  "indexable": true,
  "published": "2016-03-16T00:00:00Z",
  "memorial": false,
  "devices": "https://mastodon.social/users/Gargron/collections/devices",
  "alsoKnownAs": [
    "https://tooting.ai/users/Gargron"
  ],
  "publicKey": {
    "id": "https://mastodon.social/users/Gargron#main-key",
    "owner": "https://mastodon.social/users/Gargron",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvXc4vkECU2/CeuSo1wtn\nFoim94Ne1jBMYxTZ9wm2YTdJq1oiZKif06I2fOqDzY/4q/S9uccrE9Bkajv1dnkO\nVm31QjWlhVpSKynVxEWjVBO5Ienue8gND0xvHIuXf87o61poqjEoepvsQFElA5ym\novljWGSA/jpj7ozygUZhCXtaS2W5AD5tnBQUpcO0lhItYPYTjnmzcc4y2NbJV8hz\n2s2G8qKv8fyimE23gY1XrPJg+cRF+g4PqFXujjlJ7MihD9oqtLGxbu7o1cifTn3x\nBfIdPythWu5b4cujNsB3m3awJjVmx+MHQ9SugkSIYXV0Ina77cTNS0M2PYiH1PFR\nTwIDAQAB\n-----END PUBLIC KEY-----\n"
  },
  "tag": [],
  "attachment": [
    {
      "type": "PropertyValue",
      "name": "Patreon",
      "value": "<a href=\"https://www.patreon.com/mastodon\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\" translate=\"no\"><span class=\"invisible\">https://www.</span><span class=\"\">patreon.com/mastodon</span><span class=\"invisible\"></span></a>"
    },
    {
      "type": "PropertyValue",
      "name": "GitHub",
      "value": "<a href=\"https://github.com/Gargron\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\" translate=\"no\"><span class=\"invisible\">https://</span><span class=\"\">github.com/Gargron</span><span class=\"invisible\"></span></a>"
    }
  ],
  "endpoints": {
    "sharedInbox": "https://mastodon.social/inbox"
  },
  "icon": {
    "type": "Image",
    "mediaType": "image/png",
    "url": "https://files.mastodon.social/accounts/avatars/000/000/001/original/1a8137d3b26704e0.png"
  },
  "image": {
    "type": "Image",
    "mediaType": "image/png",
    "url": "https://files.mastodon.social/accounts/headers/000/000/001/original/e6b0f3cf210ad2a9.png"
  }
}
```

## App: PeerTube, handle ``@peertube@framapiaf.org``

Endpoint: https://framapiaf.org/users/peertube

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "toot": "http://joinmastodon.org/ns#",
      "featured": {
        "@id": "toot:featured",
        "@type": "@id"
      },
      "featuredTags": {
        "@id": "toot:featuredTags",
        "@type": "@id"
      },
      "alsoKnownAs": {
        "@id": "as:alsoKnownAs",
        "@type": "@id"
      },
      "movedTo": {
        "@id": "as:movedTo",
        "@type": "@id"
      },
      "schema": "http://schema.org#",
      "PropertyValue": "schema:PropertyValue",
      "value": "schema:value",
      "discoverable": "toot:discoverable",
      "Device": "toot:Device",
      "Ed25519Signature": "toot:Ed25519Signature",
      "Ed25519Key": "toot:Ed25519Key",
      "Curve25519Key": "toot:Curve25519Key",
      "EncryptedMessage": "toot:EncryptedMessage",
      "publicKeyBase64": "toot:publicKeyBase64",
      "deviceId": "toot:deviceId",
      "claim": {
        "@type": "@id",
        "@id": "toot:claim"
      },
      "fingerprintKey": {
        "@type": "@id",
        "@id": "toot:fingerprintKey"
      },
      "identityKey": {
        "@type": "@id",
        "@id": "toot:identityKey"
      },
      "devices": {
        "@type": "@id",
        "@id": "toot:devices"
      },
      "messageFranking": "toot:messageFranking",
      "messageType": "toot:messageType",
      "cipherText": "toot:cipherText",
      "suspended": "toot:suspended",
      "memorial": "toot:memorial",
      "indexable": "toot:indexable",
      "focalPoint": {
        "@container": "@list",
        "@id": "toot:focalPoint"
      }
    }
  ],
  "id": "https://framapiaf.org/users/peertube",
  "type": "Person",
  "following": "https://framapiaf.org/users/peertube/following",
  "followers": "https://framapiaf.org/users/peertube/followers",
  "inbox": "https://framapiaf.org/users/peertube/inbox",
  "outbox": "https://framapiaf.org/users/peertube/outbox",
  "featured": "https://framapiaf.org/users/peertube/collections/featured",
  "featuredTags": "https://framapiaf.org/users/peertube/collections/tags",
  "preferredUsername": "peertube",
  "name": "PeerTube",
  "summary": "<p>PeerTube Software Official Account - No support here // Compte officiel du logiciel PeerTube (anim\u00e9 par Framasoft). Nous ne faisons pas de support depuis ce compte. Merci de contacter l&#39;administrateur\u22c5ice de l&#39;instance concern\u00e9e ou   de vous rendre sur <a href=\"https://framacolibri.org/c/peertube\" target=\"_blank\" rel=\"nofollow noopener noreferrer\" translate=\"no\"><span class=\"invisible\">https://</span><span class=\"\">framacolibri.org/c/peertube</span><span class=\"invisible\"></span></a></p>",
  "url": "https://framapiaf.org/@peertube",
  "manuallyApprovesFollowers": false,
  "discoverable": false,
  "indexable": false,
  "published": "2019-10-01T00:00:00Z",
  "memorial": false,
  "devices": "https://framapiaf.org/users/peertube/collections/devices",
  "publicKey": {
    "id": "https://framapiaf.org/users/peertube#main-key",
    "owner": "https://framapiaf.org/users/peertube",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn1y53r+ymOmDoP8iYxa1\nb1VvXkldZVpxJg1ZVeq4SijVS3oNurrQQhpTwTmCCAue2m+UvG4eEEYAYSfb5+C3\nbqH3kLlQrptkp8y/qz3d4tk/b8RConAaws7/SwksDC5rs+cYLnnXgD7rAaT1uH/B\nVTzG79YLgnasK6IxpnBth6Vru+9g2U8PzIUOfuwPV3aZeu9q2xEdC5/GnnjsfKZv\nWEzpG3HkRAlaTRDYadl9dWOPlfhy/LMkknAP02j+Qt/s7y83YqsrUyvQcfTSy3Zf\nLNNFrpU4u1ACyZXzvaoDXQH8HetKSA06xqa4pJO4xmM2PWMoBq1KX3Us4sP291w4\nEQIDAQAB\n-----END PUBLIC KEY-----\n"
  },
  "tag": [],
  "attachment": [],
  "endpoints": {
    "sharedInbox": "https://framapiaf.org/inbox"
  },
  "icon": {
    "type": "Image",
    "mediaType": "image/png",
    "url": "https://stockage.framapiaf.org/framapiaf/accounts/avatars/000/223/824/original/03ed95406a9a3cd0.png"
  },
  "image": {
    "type": "Image",
    "mediaType": "image/png",
    "url": "https://stockage.framapiaf.org/framapiaf/accounts/headers/000/223/824/original/2fbb4d6268c2fb20.png"
  }
}
```

## App: Firefish, handle ``@kainoa@firefish.social``
## App: Misskey, handle ``https://misskey.io/@syuilo``

Endpoint: https://misskey.io/users/7rkrarq81i

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "sensitive": "as:sensitive",
      "Hashtag": "as:Hashtag",
      "quoteUrl": "as:quoteUrl",
      "toot": "http://joinmastodon.org/ns#",
      "Emoji": "toot:Emoji",
      "featured": "toot:featured",
      "discoverable": "toot:discoverable",
      "schema": "http://schema.org#",
      "PropertyValue": "schema:PropertyValue",
      "value": "schema:value",
      "misskey": "https://misskey-hub.net/ns#",
      "_misskey_content": "misskey:_misskey_content",
      "_misskey_quote": "misskey:_misskey_quote",
      "_misskey_reaction": "misskey:_misskey_reaction",
      "_misskey_votes": "misskey:_misskey_votes",
      "_misskey_summary": "misskey:_misskey_summary",
      "isCat": "misskey:isCat",
      "vcard": "http://www.w3.org/2006/vcard/ns#"
    }
  ],
  "type": "Person",
  "id": "https://misskey.io/users/7rkrarq81i",
  "inbox": "https://misskey.io/users/7rkrarq81i/inbox",
  "outbox": "https://misskey.io/users/7rkrarq81i/outbox",
  "followers": "https://misskey.io/users/7rkrarq81i/followers",
  "following": "https://misskey.io/users/7rkrarq81i/following",
  "featured": "https://misskey.io/users/7rkrarq81i/collections/featured",
  "sharedInbox": "https://misskey.io/inbox",
  "endpoints": {
    "sharedInbox": "https://misskey.io/inbox"
  },
  "url": "https://misskey.io/@syuilo",
  "preferredUsername": "syuilo",
  "name": ":peroro_sama:\u3057\u3085\u3044\u308d:peroro_sama:",
  "summary": "<p><span>Misskey\u3092\u958b\u767a\u3057\u3066\u3044\u308b\u4eba<br><br></span><a href=\"https://misskey.io/tags/misskey\" rel=\"tag\">#misskey</a><span> </span><a href=\"https://misskey.io/tags/\u85cd\u3061\u3083\u30d5\u30a1\u30f3\u30af\u30e9\u30d6\" rel=\"tag\">#\u85cd\u3061\u3083\u30d5\u30a1\u30f3\u30af\u30e9\u30d6</a><span> </span><a href=\"https://misskey.io/tags/\u308f\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\" rel=\"tag\">#\u308f\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc</a><span> </span><a href=\"https://misskey.io/tags/VisualSnowSyndrome\" rel=\"tag\">#VisualSnowSyndrome</a></p>",
  "_misskey_summary": "Misskey\u3092\u958b\u767a\u3057\u3066\u3044\u308b\u4eba\n\n#misskey #\u85cd\u3061\u3083\u30d5\u30a1\u30f3\u30af\u30e9\u30d6 #\u308f\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc #VisualSnowSyndrome",
  "icon": {
    "type": "Image",
    "url": "https://s3.arkjp.net/misskey/webpublic-b2dc591e-58b6-4df7-b7c9-1cba199f6619.png",
    "sensitive": false,
    "name": null
  },
  "image": {
    "type": "Image",
    "url": "https://s3.arkjp.net/misskey/361d91a4-da15-4367-a0c7-771569e28ca2.png",
    "sensitive": false,
    "name": null
  },
  "tag": [
    {
      "id": "https://misskey.io/emojis/peroro_sama",
      "type": "Emoji",
      "name": ":peroro_sama:",
      "updated": "2023-07-31T11:34:35.167Z",
      "icon": {
        "type": "Image",
        "mediaType": "image/gif",
        "url": "https://s3.arkjp.net/misskey/761a28c4-6702-4844-a63b-c6b4a345e981.gif"
      }
    },
    {
      "type": "Hashtag",
      "href": "https://misskey.io/tags/misskey",
      "name": "#misskey"
    },
    {
      "type": "Hashtag",
      "href": "https://misskey.io/tags/%E8%97%8D%E3%81%A1%E3%82%83%E3%83%95%E3%82%A1%E3%83%B3%E3%82%AF%E3%83%A9%E3%83%96",
      "name": "#\u85cd\u3061\u3083\u30d5\u30a1\u30f3\u30af\u30e9\u30d6"
    },
    {
      "type": "Hashtag",
      "href": "https://misskey.io/tags/%E3%82%8F%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC%E3%83%BC",
      "name": "#\u308f\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc\u30fc"
    },
    {
      "type": "Hashtag",
      "href": "https://misskey.io/tags/visualsnowsyndrome",
      "name": "#visualsnowsyndrome"
    }
  ],
  "manuallyApprovesFollowers": false,
  "discoverable": true,
  "publicKey": {
    "id": "https://misskey.io/users/7rkrarq81i#main-key",
    "type": "Key",
    "owner": "https://misskey.io/users/7rkrarq81i",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA5HmF4+D3i7XK4g90x16r\nFf0oMHwTWqXM8oxlwa2d1NUivcGByZdjNlK2zMC/RkXDing5VwgFC3foQnhv6drz\nSKJ8fqQDB97iuz+AIIcXKKt6Y6N7nJgN+LIOIhgppEjxHsaaS3W8v9vFdecyU3tI\nnRNHt7LBGssaZZfOB/ZAiED1yUAqt4NGxvY0gKl4+/GK9k+cHBPQTZCAuo/Vb8tq\n9L1yZcLz8JbZRC74OZaDBbcD9cHudHBq6evd0VYC/ybHKS+jN0eKoNwnI2jQf/Zv\nJK2kbXQPdPwmPeJgrqZ4Qyw/hFRT9sC5CRkWRaCc0dKfAjT6PHJlyaCbGaXwEM7f\nt1fhr5STRG/22XKGqGBPkXaaAKyClng80WDTcUF4FU87Ht2P4TcXhXOYXcOfw2q3\nNpk4p9ky1Pe7hyFRtcduaJCgKbMVt+PqyYZPoI9INpRxFMymon6nt7JqLFf2vh9B\n8sAeF8dFZeW4gevOpUk51XPDoHIo2RNmMQRufAMS2Ow8f6kg3c+GYamdJ2Y8onVW\nxbyZE6kswMkTeCK3w3Vk5J/fBxmnvqLRHnyyHnWH3CkHIWf2iY1EUARrmHdR7rQj\nzT3SRdGLVu3mqpZ0ruA2tbm/HuNrzfuROxMDlItAZbmJpuSie0vJJXvfGOcKjXYF\nU6ev3zq8cTQkP0D0Ov8LF60CAwEAAQ==\n-----END PUBLIC KEY-----\n"
  },
  "isCat": true,
  "attachment": [
    {
      "type": "PropertyValue",
      "name": "\u5199\u771f\u96c6",
      "value": "<a href=\"https://syuilo.github.io/photos.html\" rel=\"me nofollow noopener\" target=\"_blank\">https://syuilo.github.io/photos.html</a>"
    }
  ],
  "vcard:bday": "1997-12-06",
  "vcard:Address": "Japan"
}
```

## App: Streams, handle ``@mike@macgirvin.com``

Endpoint: https://macgirvin.com/channel/mike

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/multikey/v1",
    {
      "nomad": "https://macgirvin.com/apschema#",
      "toot": "http://joinmastodon.org/ns#",
      "litepub": "http://litepub.social/ns#",
      "sm": "http://smithereen.software/ns#",
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "oauthRegistrationEndpoint": "litepub:oauthRegistrationEndpoint",
      "sensitive": "as:sensitive",
      "movedTo": "as:movedTo",
      "EmojiReact": "as:EmojiReact",
      "discoverable": "toot:discoverable",
      "indexable": "toot:indexable",
      "wall": "sm:wall",
      "capabilities": "litepub:capabilities",
      "acceptsJoins": "litepub:acceptsJoins",
      "nomadicLocations": "nomad:nomadicLocations",
      "Hashtag": "as:Hashtag",
      "canReply": "toot:canReply",
      "approval": "toot:approval",
      "isContainedConversation": "nomad:isContainedConversation",
      "conversation": "nomad:conversation",
      "commentPolicy": "nomad:commentPolicy",
      "eventRepeat": "nomad:eventRepeat",
      "emojiReaction": "nomad:emojiReaction",
      "expires": "nomad:expires",
      "directMessage": "nomad:directMessage",
      "Category": "nomad:Category",
      "replyTo": "nomad:replyTo",
      "copiedTo": "nomad:copiedTo",
      "canSearch": "nomad:canSearch",
      "searchContent": "nomad:searchContent",
      "searchTags": "nomad:searchTags"
    }
  ],
  "type": "Person",
  "id": "https://macgirvin.com/channel/mike",
  "preferredUsername": "mike",
  "name": "Mike Macgirvin",
  "created": "2022-11-25T21:18:42Z",
  "updated": "2023-07-07T09:24:00Z",
  "icon": {
    "type": "Image",
    "mediaType": "image/jpeg",
    "updated": "2022-11-25T22:10:44Z",
    "url": "https://macgirvin.com/photo/profile/l/5",
    "height": 300,
    "width": 300
  },
  "url": "https://macgirvin.com/channel/mike",
  "location": {
    "type": "Place",
    "name": "Bugger All, Australia"
  },
  "tag": [
    {
      "type": "Note",
      "name": "Protocol",
      "content": "zot6"
    },
    {
      "type": "Note",
      "name": "Protocol",
      "content": "nomad"
    },
    {
      "type": "Note",
      "name": "Protocol",
      "content": "activitypub"
    }
  ],
  "inbox": "https://macgirvin.com/inbox/mike",
  "outbox": "https://macgirvin.com/outbox/mike",
  "followers": "https://macgirvin.com/followers/mike",
  "following": "https://macgirvin.com/following/mike",
  "wall": "https://macgirvin.com/outbox/mike",
  "endpoints": {
    "sharedInbox": "https://macgirvin.com/inbox",
    "oauthRegistrationEndpoint": "https://macgirvin.com/api/client/register",
    "oauthAuthorizationEndpoint": "https://macgirvin.com/authorize",
    "oauthTokenEndpoint": "https://macgirvin.com/token",
    "searchContent": "https://macgirvin.com/search/mike?search={}",
    "searchTags": "https://macgirvin.com/search/mike?tag={}"
  },
  "discoverable": true,
  "canSearch": [
    "https://macgirvin.com/followers/mike"
  ],
  "indexable": false,
  "publicKey": {
    "id": "https://macgirvin.com/channel/mike?operation=getkey",
    "owner": "https://macgirvin.com/channel/mike",
    "signatureAlgorithm": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAoaTPG5iYKsHJ1cK5CJUy\niN2y6B7aI4JkKMjjZO0gy8+6oa5kx6H5w7qED937a/SvwuYxh1A5yO9nwoEarM5s\nPoYZ+Z+GGbAcvzdWURtDDdRMNgktAayDiOvEdiEbgPVx8f39YnpX39ngM8ukob16\nS8eNwjWG6uwBs6rxSA409fkWjjbQwbe8fNOpynFWoG8jrB+dK6huryYqkyf9S18u\n01IAJOo1ErtaUNkSzkeudXSWokRbN/P77N8LQXorwPF9U6ODblX9QXCWl6EnQ0CX\nfcC/3NM6uXfda2KTn83G1+mo5QgGYBjGzE9K1VngoyX4J8AqvQxoXkqV20vwFSqW\nccB13F5kqRQ4BoQm2v2/e65YzjrHwkUecj7tS8TVXu8z4mdbDDbso/UrS14JmrJh\njnbwPOYpHX/6p2SdYDTF/vUWUmeSatS7sHK92eTRukuONig+PNvx8GUtxgMWPIgH\njIupGnR5lZxFMP+iaAmfxOSbVNeLn/Nka7+UfkDThApfhesBA6P8jAdStTCyqAYB\nY3rTTwplcaKKnNv+pLqBqyhYEghmGvv2EC2UGsL6rFit1RaZgSXWCIcLzdRZo4Ak\nznvz8+juMjyPLp7DdSHhKss9kV9HDxZXjrstDxOR61j0vifaMh6bUVrOAMm0Ffs+\n41v+D6pSA5p0OI2aqNJzLZ8CAwEAAQ==\n-----END PUBLIC KEY-----\n"
  },
  "assertionMethod": {
    "id": "https://macgirvin.com/channel/mike?operation=ed25519key",
    "type": "Multikey",
    "controller": "https://macgirvin.com/channel/mike",
    "publicKeyMultibase": "z6MkoeUtTDPBt4Rwxe65DJPnB62vfaH8R58hjFrNGGXgRHkV"
  },
  "manuallyApprovesFollowers": true,
  "copiedTo": "https://fediversity.site/channel/mike",
  "alsoKnownAs": "https://fediversity.site/channel/mike",
  "image": {
    "type": "Image",
    "mediaType": "image/jpeg",
    "url": "https://macgirvin.com/photo/aea3d61f-5f31-4572-8249-dd01e70ab7d8-7"
  },
  "summary": "Farmer in Bugger All, Australia. Plays a mean guitar, upside down and backwards. Systems integration, software development, and robot repair.",
  "attachment": [
    {
      "type": "Note",
      "name": "birthday",
      "content": "0000-00-00"
    }
  ],
  "signature": {
    "type": "RsaSignature2017",
    "nonce": "06c1843c84235dd492933f2641f4dde1931b74cb085772c77e4af3597662ca14",
    "creator": "https://macgirvin.com/channel/mike",
    "created": "2023-12-30T15:59:09Z",
    "signatureValue": "QBrzgRvfWgI7kUJCXRhm/qjxk9Cq+QRNgs0gyL2PbbNho7pmP0xx8sHIc903ABx4A3Iuni78ledSHTPf0mR9Pcsrja+2JdCpRC2ZA8UoG3Rh26vATGNU+Nqcu5V47ZU6JSoI33M1i4sfgDhH+IzU0s9idyV3sjMkJTzNEN6qaSLMJQG6Km8HUXEDcJYCmMIQjxJdo5lM1HBOQ0h1MoAFZIYs3jmBh2yERFYcPHEdblYdwzwOeyLUT/qlW8rfi7CP/ymrqJogd0I+BVEL2NAqbGfhUATt+2xgrN0u/5eBCsg4MZhWPlGIjr/Ac7+OTtbC53DkyDWJTsGIHSkbUs+3FDo9UQ4RGVUrcE8hbD87aybDwFIHqLuzzPRL76U8n4HQmgv3pCD7qXDGsw80wsFPIUunW6JkLj2Z7xzNjvvNYmCx523d+KbQeVpoWQoUa6ElZTyj/NvJE87gEaVwDTKu5IKr9lP1NvrNhl/lyhI7i3MbhYMNqRz+H1Zz6/x90iZGk4dJj6wUSRjVQU/P9UBXZFIbCBPzqH2iymFt6a72v91TYDrZNQ/yzalkFTgSWwdOnUpWZD0A0QAeEPTYtj/G1sYnc9qhPp50165rEcZoeJf9E30PdaPxnVnYLwpl2sL+/JB1KVYgsDQPkC3ndff0QEZYqCYE9uBLh/f3AdW0EvE="
  }
}
```

## App: Hubzilla, handle ``@contribute@hubzilla.org``
## App: GNU Social, handle ``@administrator@gnusocial.net``

Endpoint: https://gnusocial.net/index.php/user/1

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers"
    }
  ],
  "id": "https://gnusocial.net/index.php/user/1",
  "type": "Person",
  "following": "https://gnusocial.net/user/1/following.json",
  "followers": "https://gnusocial.net/user/1/followers.json",
  "liked": "https://gnusocial.net/user/1/liked.json",
  "inbox": "https://gnusocial.net/user/1/inbox.json",
  "outbox": "https://gnusocial.net/user/1/outbox.json",
  "preferredUsername": "administrator",
  "name": "admin de gnusocial.net",
  "summary": "Admin de gnusocial.net. Servidor ofrecido por https://elbinario.net",
  "url": "https://gnusocial.net/administrator",
  "manuallyApprovesFollowers": false,
  "publicKey": {
    "id": "https://gnusocial.net/index.php/user/1#public-key",
    "owner": "https://gnusocial.net/index.php/user/1",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzd2KFM2gHLq1b/zh3MtU\niuYmhRbxIIeuuXmm93bWbrldf7XomEMRvgbmvZJCQag60ZnVz7u2h76OpY/pyLmc\nkfjM5Xqy4lBv2wirYRdEMNcCVEi361IHrtYhJY4n/2d+Q0RCupAh6/ugTNSCnc9M\npMP6nAbNPkGEYa6y1C+oENUhjmOsKo0VIlpddJUb0adXBtj5LKRBkZmpBfZWf4jj\n/xQdsVH908p9NVsvJsgXNLaJRfFo4zmJ+YvMjJUmSoYWnIhpjMfDdqErXyaVpLbk\njnWd0tKyQYCUU5suJI1s0/7QPUQynLLnb8bKI4MAuKn7c/kfDJkM7RgV+3Q7k83T\nhwIDAQAB\n-----END PUBLIC KEY-----"
  },
  "tag": [],
  "attachment": [],
  "icon": {
    "type": "Image",
    "mediaType": "image/png",
    "height": 96,
    "width": 96,
    "url": "https://gnusocial.net/avatar/1-96-20200119102924.jpeg"
  },
  "endpoints": {
    "sharedInbox": "https://gnusocial.net/inbox.json"
  }
}
```

## App: Pleroma, handle ``@karolat@stereophonic.space``

Endpoint: https://stereophonic.space/users/karolat

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://stereophonic.space/schemas/litepub-0.1.jsonld",
    {
      "@language": "und"
    }
  ],
  "alsoKnownAs": [],
  "attachment": [],
  "capabilities": {
    "acceptsChatMessages": true
  },
  "discoverable": false,
  "endpoints": {
    "oauthAuthorizationEndpoint": "https://stereophonic.space/oauth/authorize",
    "oauthRegistrationEndpoint": "https://stereophonic.space/api/v1/apps",
    "oauthTokenEndpoint": "https://stereophonic.space/oauth/token",
    "sharedInbox": "https://stereophonic.space/inbox",
    "uploadMedia": "https://stereophonic.space/api/ap/upload_media"
  },
  "featured": "https://stereophonic.space/users/karolat/collections/featured",
  "followers": "https://stereophonic.space/users/karolat/followers",
  "following": "https://stereophonic.space/users/karolat/following",
  "icon": {
    "type": "Image",
    "url": "https://stereophonic.space/media/a94a0a3f51c49c4a5d9f8849cbb75634fddf234cbd49cd6029b4a9364b5da03e.png"
  },
  "id": "https://stereophonic.space/users/karolat",
  "image": {
    "type": "Image",
    "url": "https://stereophonic.space/media/78a7cad0ba10cff6dd1f696d66347db73e0bbf3bdb331f3219188be03fd237e7.jpg"
  },
  "inbox": "https://stereophonic.space/users/karolat/inbox",
  "manuallyApprovesFollowers": true,
  "name": ":blobcatcomfnightxmas: karolat",
  "outbox": "https://stereophonic.space/users/karolat/outbox",
  "preferredUsername": "karolat",
  "publicKey": {
    "id": "https://stereophonic.space/users/karolat#main-key",
    "owner": "https://stereophonic.space/users/karolat",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuT04r5Fo9nf4IvD0WVPh\nyq87qx9bZEha4gtwi15V+U/d0IoZZn5gR5aQUAi7+712NvARwJUmVkkUC3K+FcF1\nTI7oNI96HlIGPvFbacnisuRzM8lKzt5eKzXzB1ZMtk29sgMwLp7tEwLVhLzAPfOT\nsuleNdl1ZCOXVAr+jGh1K27YMEf8U1QiKF0HsriANPxGujhj5S0etotxHa+ur+l4\nJ9V9Q8eMNN1Pd0bhcfd9RSigFQ4jA5KmwS+drryLj6NNq2D6z2Xy7V/PVjGFSUIm\nh8RtuoBOIKrXboKyirKNqNpejYyqPoIIyji6Y5RUaUkXdw0rrYnC2YvF6U6Clr+7\nmwIDAQAB\n-----END PUBLIC KEY-----\n\n"
  },
  "summary": "<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>i&#39;m here to have a good time",
  "tag": [
    {
      "icon": {
        "type": "Image",
        "url": "https://stereophonic.space/emoji/custom/for_loyal_client.png"
      },
      "id": "https://stereophonic.space/emoji/custom/for_loyal_client.png",
      "name": ":blobcatcomfnightxmas:",
      "type": "Emoji",
      "updated": "1970-01-01T00:00:00Z"
    }
  ],
  "type": "Person",
  "url": "https://stereophonic.space/users/karolat"
}
```

## App: Pixelfed, handle ``@dansup@pixelfed.social``

Endpoint: https://pixelfed.social/users/dansup

```js
{
  "@context": [
    "https://w3id.org/security/v1",
    "https://www.w3.org/ns/activitystreams",
    {
      "toot": "http://joinmastodon.org/ns#",
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "alsoKnownAs": {
        "@id": "as:alsoKnownAs",
        "@type": "@id"
      },
      "movedTo": {
        "@id": "as:movedTo",
        "@type": "@id"
      },
      "indexable": "toot:indexable"
    }
  ],
  "id": "https://pixelfed.social/users/dansup",
  "type": "Person",
  "following": "https://pixelfed.social/users/dansup/following",
  "followers": "https://pixelfed.social/users/dansup/followers",
  "inbox": "https://pixelfed.social/users/dansup/inbox",
  "outbox": "https://pixelfed.social/users/dansup/outbox",
  "preferredUsername": "dansup",
  "name": "dansup",
  "summary": "Hi, I'm the developer behind <a class=\"u-url mention\" href=\"https://pixelfed.social/Pixelfed\" rel=\"external nofollow noopener\" target=\"_blank\">@Pixelfed</a>! \n\nAlso <a class=\"u-url list-slug\" href=\"https://pixelfed.social/@dansup@mastodon.social\" rel=\"external nofollow noopener\" target=\"_blank\">@dansup@mastodon.social</a> \n\n<a href=\"https://pixelfed.social/discover/tags/pixelfed?src=hash\" title=\"#pixelfed\" class=\"u-url hashtag\" rel=\"external nofollow noopener\">#pixelfed</a> <a href=\"https://pixelfed.social/discover/tags/design?src=hash\" title=\"#design\" class=\"u-url hashtag\" rel=\"external nofollow noopener\">#design</a> <a href=\"https://pixelfed.social/discover/tags/webdev?src=hash\" title=\"#webdev\" class=\"u-url hashtag\" rel=\"external nofollow noopener\">#webdev</a> <a href=\"https://pixelfed.social/discover/tags/pixelfedApp?src=hash\" title=\"#pixelfedApp\" class=\"u-url hashtag\" rel=\"external nofollow noopener\">#pixelfedApp</a> <a href=\"https://pixelfed.social/discover/tags/supApp?src=hash\" title=\"#supApp\" class=\"u-url hashtag\" rel=\"external nofollow noopener\">#supApp</a>",
  "url": "https://pixelfed.social/dansup",
  "manuallyApprovesFollowers": false,
  "indexable": true,
  "published": "2018-06-01T00:00:00Z",
  "publicKey": {
    "id": "https://pixelfed.social/users/dansup#main-key",
    "owner": "https://pixelfed.social/users/dansup",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn9TEqiXOvCKBS7dK8+ZV\ncO/UmPRejL77hmO74sHIyteJVHUhnhzBz3PAWaQWdv9A4ViL8ghhSV50NzO6HIrk\nzlclmK0GeGrxRFDBLGHpa4KFErqcQgIG3uRjJ5UDhUijEsbusmnVhpLWUFEO7Atw\nbhd/XVciruF6ea3ryyco6ZES7IHKdUBwM3IKpZqIb/h2ObXcVVC1I2oggHRxR+eP\nqst0qU31MryUkBqX7DVcNV/yXdRUuEc+ZiK/rNkr3RCzE3J7PePH5RNpJDIfj4Jn\n+lW7ErT5Susn1+VHP7NHpAK8pe8atUpXEtogAbgt7KYi0Kq+XCxLv7YZuOqSaX2p\nZwIDAQAB\n-----END PUBLIC KEY-----\n"
  },
  "icon": {
    "type": "Image",
    "mediaType": "image/jpeg",
    "url": "https://pixelfed.social/storage/avatars/000/000/000/000/000/000/2/mLZr2R47XEwbmasH2M3P_avatar.jpg?v=57"
  },
  "endpoints": {
    "sharedInbox": "https://pixelfed.social/f/inbox"
  },
  "alsoKnownAs": [
    "https://mastodon.social/users/dansup"
  ]
}
```

## App: Friendica, handle ``@tobias@friendi.ca``

Endpoint: https://friendi.ca/author/tobias/

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "PropertyValue": "schema:PropertyValue",
      "schema": "http://schema.org#",
      "pt": "https://joinpeertube.org/ns#",
      "toot": "http://joinmastodon.org/ns#",
      "webfinger": "https://webfinger.net/#",
      "litepub": "http://litepub.social/ns#",
      "lemmy": "https://join-lemmy.org/ns#",
      "value": "schema:value",
      "Hashtag": "as:Hashtag",
      "featured": {
        "@id": "toot:featured",
        "@type": "@id"
      },
      "featuredTags": {
        "@id": "toot:featuredTags",
        "@type": "@id"
      },
      "alsoKnownAs": {
        "@id": "as:alsoKnownAs",
        "@type": "@id"
      },
      "moderators": {
        "@id": "lemmy:moderators",
        "@type": "@id"
      },
      "postingRestrictedToMods": "lemmy:postingRestrictedToMods",
      "discoverable": "toot:discoverable",
      "indexable": "toot:indexable",
      "sensitive": "as:sensitive",
      "resource": "webfinger:resource"
    }
  ],
  "id": "https://friendi.ca/author/tobias/",
  "type": "Person",
  "attachment": [
    {
      "type": "PropertyValue",
      "name": "Blog",
      "value": "<a rel=\"me\" title=\"https://friendi.ca/\" target=\"_blank\" href=\"https://friendi.ca/\">friendi.ca</a>"
    },
    {
      "type": "PropertyValue",
      "name": "Profile",
      "value": "<a rel=\"me\" title=\"https://friendi.ca/author/tobias/\" target=\"_blank\" href=\"https://friendi.ca/author/tobias/\">friendi.ca</a>"
    }
  ],
  "name": "Tobias",
  "icon": {
    "type": "Image",
    "url": "https://secure.gravatar.com/avatar/7faf7abf39f117b7bb2cf8e08f4eded7?s=120&#038;d=mm&#038;r=g"
  },
  "published": "2016-08-14T19:38:30Z",
  "summary": "",
  "tag": [],
  "url": "https://friendi.ca/author/tobias/",
  "inbox": "https://friendi.ca/wp-json/activitypub/1.0/users/2/inbox",
  "outbox": "https://friendi.ca/wp-json/activitypub/1.0/users/2/outbox",
  "following": "https://friendi.ca/wp-json/activitypub/1.0/users/2/following",
  "followers": "https://friendi.ca/wp-json/activitypub/1.0/users/2/followers",
  "preferredUsername": "tobias",
  "publicKey": {
    "id": "https://friendi.ca/author/tobias/#main-key",
    "owner": "https://friendi.ca/author/tobias/",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxbgUisSe02ZxAR7J031G\nd4HtjzTlC30pylguZa2NmB1yLXd0n5xznzWavgFQpD10V9IwypLrbe+84oadZgn+\nZlUSKC/Qbl4ifoj9FJr7GPYXrX6olef6dpRsGLOXMrP8LTphTiyhxy5XtoSWXPZg\njBTJcQuh+BT3s1TX5zzGmHw77xil0HccRl2mr1oL2fDXi85DSE7cfdF9WX6NIN7K\nsnP5N/RFe0FYb9T/kn+KAB/cRE8RRNmKDejWCohkg846ciX1B+3d34uRWFBFjgTN\nQVbuIxCVACmGP2rb6KlaHZqD5SdwZ7r26v8zz5o31c8uxbSkiMwNMgcTFeky0BOv\naQIDAQAB\n-----END PUBLIC KEY-----\n"
  },
  "manuallyApprovesFollowers": false,
  "featured": "https://friendi.ca/wp-json/activitypub/1.0/users/2/collections/featured",
  "discoverable": true,
  "indexable": true,
  "resource": "tobias@friendi.ca"
}
```

## App: Funkwhale, handle ``@Greensky@open.audio``

Endpoint: https://open.audio/federation/actors/Greensky

```js
{
  "id": "https://open.audio/federation/actors/Greensky",
  "outbox": "https://open.audio/federation/actors/Greensky/outbox",
  "inbox": "https://open.audio/federation/actors/Greensky/inbox",
  "preferredUsername": "Greensky",
  "type": "Person",
  "name": "Greensky",
  "followers": "https://open.audio/federation/actors/Greensky/followers",
  "following": "https://open.audio/federation/actors/Greensky/following",
  "manuallyApprovesFollowers": false,
  "summary": "<p>Hola soy GreenSky y es un placer tenerte por ac\u00e1, en mis canales tanto dentro como fuera del fediverso te hablo de Educaci\u00f3n y los retos que atraviesa a d\u00eda de hoy, te invito a escuchar este podcast.</p>",
  "url": [
    {
      "type": "Link",
      "href": "https://open.audio/@Greensky",
      "mediaType": "text/html"
    }
  ],
  "icon": {
    "type": "Image",
    "url": "https://s3.eu-central-2.wasabisys.com/open-audio/attachments/c3/7b/14/img_20221123_125817.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=69ST19MZXMKJ5ZP4NF6L%2F20231230%2Feu-central-2%2Fs3%2Faws4_request&X-Amz-Date=20231230T155911Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=3e95083563f67c0feb28308a19aa9f59c94725c6c679c3c74904f1c6c8b4734d",
    "mediaType": "image/jpeg"
  },
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    "https://funkwhale.audio/ns",
    {
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "Hashtag": "as:Hashtag"
    }
  ],
  "publicKey": {
    "owner": "https://open.audio/federation/actors/Greensky",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1apOT2uC7KoWogTWWW4s\nrB91U+orZmgiWlzMlxHV/nRiGXbm27ChWeR1l0P+DobOB6qiw5jyHMIctkRyYYbG\nI5/gKKeZuqAwEGBzkaAjmjuVTG8HL6LDfYkL3cNDoQrcuLqQ2o4e2DsWWJuO2Bh9\nuQEm2tQhhuSkoP/5Y1sfpX3jqM/GDmRW9sd+5xwMTzMpZaxUpNqm0NcIvSjdB852\nVnWJJtGS4ZHL53N1i6YnppBQDzYLJ8MOLb6vzeOvDX/D/vDxIdAf3oz+4ewJC7Cq\nDrmKcpWySNJQwCut1qkoXyeGeOnGVC4bR4F5mcolgy2yr9XNZ1UCfiPTd80OBrP+\nCQIDAQAB\n-----END PUBLIC KEY-----\n",
    "id": "https://open.audio/federation/actors/Greensky#main-key"
  },
  "endpoints": {
    "sharedInbox": "https://open.audio/federation/shared/inbox"
  }
}
```

## App: WriteFreely, handle ``@matt@write.as``

Endpoint: https://write.as/api/collections/matt

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1"
  ],
  "type": "Person",
  "id": "https://write.as/api/collections/matt",
  "inbox": "https://write.as/api/collections/matt/inbox",
  "outbox": "https://write.as/api/collections/matt/outbox",
  "preferredUsername": "matt",
  "url": "https://write.as/matt/",
  "name": "Matt",
  "icon": {
    "type": "Image",
    "mediaType": "image/png",
    "url": "https://cdn.writeas.net/img/avatars/m.png"
  },
  "following": "https://write.as/api/collections/matt/following",
  "followers": "https://write.as/api/collections/matt/followers",
  "summary": "Founder, [Musing Studio](https://musing.studio) / [Write.as](https://write.as).",
  "publicKey": {
    "id": "https://write.as/api/collections/matt#main-key",
    "owner": "https://write.as/api/collections/matt",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnUauwxWlUrkSFENqEgDl\n877Ci3QOQMDGTnZwjCFFEemW47AfNSAxRURzyi520V7UO1yVNEuvnV66hJN0kbhn\n3f9pHE8LTIalUJTpi+FxU2Qm8le82j7dsQc4gx7U7muHDPg8AiasSHvvS+qaKMvo\n+NSTwzQSrstngHeexiolGeGEfJLUirAtPgZVCPfAFnw5Z7sk9SBkZEpjoNqq+kA0\nHyV66/J8UYl/HZT4kVSXjc2hjlkJlhsjaVEXNuS/xaLyCJoanYY4wYe8EbP/e50+\nyKdRBznNJGbOvHNy14rmkGg9S8slEvQSg2UnrstrEaFrCnMkHzK3h/e96Xfw/T3Q\nDwIDAQAB\n-----END PUBLIC KEY-----\n"
  },
  "endpoints": {}
}
```

## App: Plume, handle ``@actapopuli@fediverse.blog``

Endpoint: https://fediverse.blog/@/actapopuli/

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "Emoji": "toot:Emoji",
      "Hashtag": "as:Hashtag",
      "atomUri": "ostatus:atomUri",
      "conversation": "ostatus:conversation",
      "featured": "toot:featured",
      "focalPoint": {
        "@container": "@list",
        "@id": "toot:focalPoint"
      },
      "inReplyToAtomUri": "ostatus:inReplyToAtomUri",
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "movedTo": "as:movedTo",
      "ostatus": "http://ostatus.org#",
      "sensitive": "as:sensitive",
      "toot": "http://joinmastodon.org/ns#"
    }
  ],
  "endpoints": {
    "sharedInbox": "https://fediverse.blog/inbox"
  },
  "followers": "https://fediverse.blog/@/actapopuli/followers",
  "icon": {
    "type": "Image",
    "url": "https://fediverse.blog/static/media/B1434302-79AF-128D-AA78-B2AF0499C60F.png"
  },
  "id": "https://fediverse.blog/@/actapopuli/",
  "inbox": "https://fediverse.blog/@/actapopuli/inbox",
  "name": "actapopuli",
  "outbox": "https://fediverse.blog/@/actapopuli/outbox",
  "preferredUsername": "actapopuli",
  "publicKey": {
    "id": "https://fediverse.blog/@/actapopuli/#main-key",
    "owner": "https://fediverse.blog/@/actapopuli/",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyTRo83oDsK2V0ZmIIsjP\naesrEfeJPQlmedCuMFFLxUtRLXZCrf6KjCBWKYYu9wO4kZCeOIc7e+1WfAWgEXT3\na+Cjc8kYa4tNnT9j2nbjdbWOs2xFR286vXIbj97zjXmTJqMHQiaLDaUmvuGKaY2Y\nHAaFvbjkSTcPIrimFGhEerYl+q0thfLq+geHYC8rLVkdd2np7Do0Wjm+Z69VI4y2\n/lXQ9ou0JFuXJtUAtjEYUh1Ey7Or2R7NkrSpSd5MVrMRyhpsxT8NzjNXJCx7E/Vt\nXbDnQ2uKso0LsTmpZtDDjvQh9zCkvunFlWxgedv3tuC4Zrj3mlruCZXURg2Ssr0W\nEQIDAQAB\n-----END PUBLIC KEY-----\n"
  },
  "summary": "<p>Dissemination of views and interesting, important and controversial perspectives largely excluded from the mainstream media.</p>\n",
  "type": "Person",
  "url": "https://fediverse.blog/@/actapopuli/"
}
```

## App: Mobilizon, handle ``@framasoft@mobilizon.fr``

Endpoint: https://mobilizon.fr/@framasoft

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "addressRegion": "sc:addressRegion",
      "timezone": {
        "@id": "mz:timezone",
        "@type": "sc:Text"
      },
      "isOnline": {
        "@id": "mz:isOnline",
        "@type": "sc:Boolean"
      },
      "pt": "https://joinpeertube.org/ns#",
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "inLanguage": "sc:inLanguage",
      "address": {
        "@id": "sc:address",
        "@type": "sc:PostalAddress"
      },
      "status": {
        "@id": "ical:status",
        "@type": "ical:status"
      },
      "discoverable": "toot:discoverable",
      "repliesModerationOption": {
        "@id": "mz:repliesModerationOption",
        "@type": "mz:repliesModerationOptionType"
      },
      "sc": "http://schema.org#",
      "mz": "https://joinmobilizon.org/ns#",
      "category": "sc:category",
      "joinModeType": {
        "@id": "mz:joinModeType",
        "@type": "rdfs:Class"
      },
      "Hashtag": "as:Hashtag",
      "propertyID": "sc:propertyID",
      "PostalAddress": "sc:PostalAddress",
      "discussions": {
        "@id": "mz:discussions",
        "@type": "@id"
      },
      "remainingAttendeeCapacity": "sc:remainingAttendeeCapacity",
      "streetAddress": "sc:streetAddress",
      "anonymousParticipationEnabled": {
        "@id": "mz:anonymousParticipationEnabled",
        "@type": "sc:Boolean"
      },
      "externalParticipationUrl": {
        "@id": "mz:externalParticipationUrl",
        "@type": "sc:URL"
      },
      "addressLocality": "sc:addressLocality",
      "joinMode": {
        "@id": "mz:joinMode",
        "@type": "mz:joinModeType"
      },
      "location": {
        "@id": "sc:location",
        "@type": "sc:Place"
      },
      "toot": "http://joinmastodon.org/ns#",
      "participantCount": {
        "@id": "mz:participantCount",
        "@type": "sc:Integer"
      },
      "uuid": "sc:identifier",
      "maximumAttendeeCapacity": "sc:maximumAttendeeCapacity",
      "participationMessage": {
        "@id": "mz:participationMessage",
        "@type": "sc:Text"
      },
      "openness": {
        "@id": "mz:openness",
        "@type": "@id"
      },
      "members": {
        "@id": "mz:members",
        "@type": "@id"
      },
      "events": {
        "@id": "mz:events",
        "@type": "@id"
      },
      "resources": {
        "@id": "mz:resources",
        "@type": "@id"
      },
      "addressCountry": "sc:addressCountry",
      "posts": {
        "@id": "mz:posts",
        "@type": "@id"
      },
      "commentsEnabled": {
        "@id": "pt:commentsEnabled",
        "@type": "sc:Boolean"
      },
      "value": "sc:value",
      "PropertyValue": "sc:PropertyValue",
      "repliesModerationOptionType": {
        "@id": "mz:repliesModerationOptionType",
        "@type": "rdfs:Class"
      },
      "todos": {
        "@id": "mz:todos",
        "@type": "@id"
      },
      "ical": "http://www.w3.org/2002/12/cal/ical#",
      "postalCode": "sc:postalCode",
      "memberCount": {
        "@id": "mz:memberCount",
        "@type": "sc:Integer"
      },
      "@language": "und"
    }
  ],
  "discoverable": true,
  "discussions": "https://mobilizon.fr/@framasoft/discussions",
  "endpoints": {
    "discussions": "https://mobilizon.fr/@framasoft/discussions",
    "events": "https://mobilizon.fr/@framasoft/events",
    "members": "https://mobilizon.fr/@framasoft/members",
    "posts": "https://mobilizon.fr/@framasoft/posts",
    "resources": "https://mobilizon.fr/@framasoft/resources",
    "sharedInbox": "https://mobilizon.fr/inbox",
    "todos": "https://mobilizon.fr/@framasoft/todos"
  },
  "events": "https://mobilizon.fr/@framasoft/events",
  "followers": "https://mobilizon.fr/@framasoft/followers",
  "following": "https://mobilizon.fr/@framasoft/following",
  "icon": {
    "mediaType": "image/jpeg",
    "type": "Image",
    "url": "https://mobilizon.fr/media/890f5396ef80081a6b1b18a5db969746cf8bb340e8a4e657d665e41f6646c539.jpg?name=framasoft%27s%20avatar.jpg"
  },
  "id": "https://mobilizon.fr/@framasoft",
  "image": {
    "mediaType": "image/jpeg",
    "type": "Image",
    "url": "https://mobilizon.fr/media/a8227a16cc80b3d20ff5ee549a29c1b20a0ca1547f8861129aae9f00c3c69d12.jpg?name=framasoft%27s%20banner.jpg"
  },
  "inbox": "https://mobilizon.fr/@framasoft/inbox",
  "location": {
    "address": {
      "addressCountry": "France",
      "addressLocality": "Lyon",
      "addressRegion": "Auvergne-Rh\u00f4ne-Alpes",
      "postalCode": "69007",
      "streetAddress": "10 bis rue Jangot",
      "type": "PostalAddress"
    },
    "id": "https://mobilizon.fr/address/0438c134-963c-4c2e-bae1-3fec8e9dbe33",
    "name": "Lyon",
    "type": "Place"
  },
  "manuallyApprovesFollowers": false,
  "memberCount": 15,
  "members": "https://mobilizon.fr/@framasoft/members",
  "name": "Framasoft",
  "openness": "moderated",
  "outbox": "https://mobilizon.fr/@framasoft/outbox",
  "posts": "https://mobilizon.fr/@framasoft/posts",
  "preferredUsername": "framasoft",
  "publicKey": {
    "id": "https://mobilizon.fr/@framasoft#main-key",
    "owner": "https://mobilizon.fr/@framasoft",
    "publicKeyPem": "-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAuy0YgN9pPTSzMHhEnRCyXf98xQV8fRqKcAAo53edoFa7Cpkow5mM\nXowJGi7uqsMpLnyOEKvify7Y7gfLzbH8IuCfJxLJ19EsTte+xzWDkiqMZ9HC3HPQ\n0ZEIkBIeDbExBZZwPRbku9ft5ZxU+PRqn1E93pcPM9qEC0vQ2f+LggDX4x89M6UG\nLPbXVOMPMQwizt5Zi4b5WpZOi7YL4nIEUodkqAZAtVO51HGTtBX64uGxg3xQTt2c\nl/fOO6LwWus4wu0HALMQGy/CMG7oDBiccDYEshDLRmORxWukG1iYSUgphLXZb0ks\nsT+if9DwBA6S6WpIJ7/BiZxv/aqTIlGAIQIDAQAB\n-----END RSA PUBLIC KEY-----\n\n"
  },
  "resources": "https://mobilizon.fr/@framasoft/resources",
  "summary": "",
  "todos": "https://mobilizon.fr/@framasoft/todos",
  "type": "Group",
  "url": "https://mobilizon.fr/@framasoft"
}
```

## App: Lemmy, handle ``@lemmy_support@lemmy.ml``
## App: Micro.blog, handle ``@manton@manton.org``

Endpoint: https://manton.org/activitypub/manton

```js
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1"
  ],
  "id": "https://manton.org/activitypub/manton",
  "url": "https://manton.org/activitypub/manton",
  "type": "Person",
  "preferredUsername": "manton",
  "name": "Manton Reece",
  "summary": "I created Micro.blog. I also have 2 podcasts: Core Intuition and Timetable.",
  "inbox": "https://micro.blog/activitypub/manton/inbox",
  "outbox": "https://micro.blog/activitypub/manton/outbox",
  "followers": "https://micro.blog/activitypub/manton/followers",
  "following": "https://micro.blog/activitypub/manton/following",
  "endpoints": {
    "sharedInbox": "https://micro.blog/activitypub/shared/inbox"
  },
  "publicKey": {
    "id": "https://manton.org/activitypub/manton#key",
    "owner": "https://manton.org/activitypub/manton",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuR/w8q5qb2jbya4mT+Qb\n8mcEuBciT1csv19wltGdEajvOfFP7IoC5CQKIEFBFOIx04e7PzUd2I3Cm0rmHM4V\nIKs6aMXAtgGd9Bz8gfl98VmVukN2QZbJs/MyImj0LXgDsgr8wzABA/BX2sCloPjE\nDBSuJG1pA6n6/+BNlV9/Jfz37AUhewRTfuUnaNp5X/BGcfNTD12ZsHNhD3DorrKC\nV03db0V0LBoNTECRAIBgMeOoq+U+VU/a9bIRWLglBjKZuUGhxmg1/6o0+dxKMzI6\nZtuMUsRC0E9RHTCiLGW4DAYFKxIF2yFcOgm24PCDuUjSgMmP4FiGlUsU5hMMVrHC\nZQIDAQAB\n-----END PUBLIC KEY-----\n"
  },
  "icon": {
    "url": "https://micro.blog/manton/avatar.jpg",
    "type": "Image",
    "mediaType": "image/jpeg"
  },
  "image": {
    "url": "https://avatars.micro.blog/avatars/2023/07/3_header.jpg",
    "type": "Image",
    "mediaType": "image/jpeg"
  },
  "alsoKnownAs": [
    "https://mastodon.social/users/manton"
  ],
  "attachment": [
    {
      "type": "PropertyValue",
      "name": "Blog",
      "value": "<a href=\"https://manton.org/\">manton.org</a>"
    }
  ]
}
```

