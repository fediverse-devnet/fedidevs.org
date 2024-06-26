---
title: Delete
tags:
  - delete
---

The `Delete` activity is used to remove objects from Funkwhale's database.

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Undo](https://www.w3.org/TR/activitypub/#delete-activity-inbox) |
| Object    | A Funkwhale `Library` or `Audio` object                              |

## Internal logic

When Funkwhale receives a `Delete` activity, it deletes the associated object from the database.

Funkwhale ensures the actor initiating the activity is the owner of the associated object before handling it.

## Example

In this example, **Bob** deletes a library and notifies its followers.

```json
{
   "@context": [
      "https://www.w3.org/ns/activitystreams",
      "https://w3id.org/security/v1",
      {}
   ],
   "type": "Delete",
   "to": [
      "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6/followers"
   ],
   "actor": "https://awesome.music/federation/actors/Bob",
   "object": {
      "type": "Library",
      "id": "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6"
   }
}
```

In this example, **Bob** deletes three audio objects in a library and notifies the library's followers.

```json
{
   "@context": [
      "https://www.w3.org/ns/activitystreams",
      "https://w3id.org/security/v1",
      {}
   ],
   "type": "Delete",
   "to": [
      "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6/followers"
   ],
   "actor": "https://awesome.music/federation/actors/Bob",
   "object": {
      "type": "Audio",
      "id": [
         "https://awesome.music/federation/music/uploads/19420073-3572-48a9-8c6c-b385ee1b7905",
         "https://awesome.music/federation/music/uploads/11d99680-23c6-4f72-997a-073b980ab204",
         "https://awesome.music/federation/music/uploads/1efadc1c-a704-4b8a-a71a-b288b1d1f423"
      ]
   }
}
```
