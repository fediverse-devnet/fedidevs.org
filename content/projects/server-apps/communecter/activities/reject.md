---
id: reject
title: Reject
tags:
  - Reject
---

The `Reject` activity is used to indicate the rejection of an invitation or a join request in Communecter.

### Reference

- **Activity**: [Reject](https://www.w3.org/TR/activitypub/#reject-activity-inbox)
- **Object**: The invitation or join request being rejected

### Internal Logic

When an actor wants to reject an invitation or a join request, they can send a Reject activity. The Reject activity includes the invitation or join request being rejected, specified as the object.

### Examples

#### Rejecting an Invitation

In this example, **Armel Wanes** sends a Reject activity to decline an invitation:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Undo",
  "actor": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "id": "https://communecter.org/api/activitypub/activity/id/649d3b54b3a53",
  "object": "https://communecter.org/api/activitypub/activity/id/649d39d47e6c3",
  "target" : "https://communecter.org/api/activitypub/activity/id/888d3b54b3a53",
}

```
### Rejecting an badge


Here's a simplified explanation for someone who doesn't code:

This message describes a situation where someone named ArmelWanes offered a badge called 'Community Meetup' to Hajavololona. However, Hajavololona decided not to accept this offer, and the rejection was communicated back to ArmelWanes through this message.


```json
{
  "@context" : "https://www.w3.org/ns/activitystreams",
  "type" : "Reject",
  "object" : "https://communecter.org/api/activitypub/activity/id/652e90cf0b894",
  "id" : "https://communecter.org/api/activitypub/activity/id/652e912ddeba6",
  "actor" : "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "instrument" : {
    "revokeAuthor" : "https://communecter.org/api/activitypub/users/u/ArmelWanes",
    "revokeReason" : "Hajavololona rejected the offer of the 'Community Meetup' badge from ArmelWanes."
  },
  "summary" : "Hajavololona has reject your badge"
}
```
