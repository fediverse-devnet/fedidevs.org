---
id: create
title: Create
tags:
  - Create
---
The `Create` activity is used to create new objects in Communecter, such as `Note`, `Event`, `Project`, or `Badge`.

### Reference

- **Activity**: [Create](https://www.w3.org/TR/activitypub/#create-activity-inbox)
- **Object**: A Communecter object

### Internal Logic

When Communecter receives a `Create` activity with an object, it processes the activity based on the type of object being created. This can include `Note`, `Event`, or `Project`, among others.

## Example

In this example, **Hajavololona** creates a new `Event` in Communecter and sends it to the public audience with a carbon copy (cc) to **ArmelWanes**.

```json
{
  "@context" : "https://www.w3.org/ns/activitystreams",
  "type" : "Create",
  "object" : "https://communecter.org/api/activitypub/object/id/649d514ebb9fa",
  "id" : "https://communecter.org/api/activitypub/activity/id/649d514eba30c",
  "actor" : "https://communecter.org/api/activitypub/users/u/Hajavololona",
  "published" : "2023-06-29T09:39:26+0000",
  "summary" : "Created a new Event: 'Community Meetup'",
  "to" : [ 
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc" : [ 
    "https://instance.communecter.org/api/activitypub/users/u/ArmelWanes"
  ]
}
```

## Example 2

In this example, Hajavololona creates a new badge titled "Advanced Training Badge" in Communecter.

```json

{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "object": {
    "type": "Badge",
    "id": "https://communecter.org/api/activitypub/badge/id/12345",
    "attachment": [
      {
        "type": "Image",
        "url": "https://example.com/badge-image.jpg"
      }
    ],
    "attributedTo": "https://communecter.org/api/activitypub/users/u/Hajavololona",
    "content": "Earned for completing advanced training courses.",
    "name": "Advanced Training Badge",
    "published": "2023-07-02T10:15:00+0000",
    "url": "https://example.com/badge-info"
  },
  "id": "https://communecter.org/api/activitypub/activity/id/649d514eba30c",
  "actor": "https://communecter.org/api/activitypub/users/u/Hajavololona",
  "published": "2023-07-02T10:15:00+0000",
  "summary": "Created a new Badge: 'Advanced Training Badge'",
  "to": [
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc": [
    "https://instance.communecter.org/api/activitypub/users/u/ArmelWanes"
  ]
}

```

The `Create` activity can be used to create a new organization:

Example:
```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "actor": "https://communecter.org/api/activitypub/users/u/JaneDoe",
  "object": {
    "type": "Organization",
    "name": "Green Earth Initiative",
    "summary": "A non-profit dedicated to environmental conservation"
  }
}
```