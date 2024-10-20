---
id: offer
title: Offer
tags:
  - Offer
---

The `Offer` activity is used to offer a role or specific permissions to an actor for a project or activity in Communecter.

### Reference

- **Activity**: [Offer](https://www.w3.org/TR/activitypub/#offer-activity-outbox)
- **Object**: The project or activity for which the offer is being made

### Internal Logic

When an actor wants to offer a role or specific permissions to another actor for a project or activity, they can send an Offer activity. The Offer activity includes the project or activity for which the offer is being made, specified as the object. The actor making the offer can also provide additional context by using the `instrument` field. Some examples of instruments include:

- `"instrument": "asadmin"`: Offering the role of administrator for the project.
- `"instrument": "withRules"`: Offering specific permissions or rules for the project.

### Examples

#### Offering Administrator Role

In this example, **Oceatoon** sends an Offer activity to **Armel Wanes**, offering him the role of administrator for a project:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Offer",
  "actor": "https://communecter.org/api/activitypub/users/u/oceatoon",
  "object": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "target" : "https://communecter.org/api/activitypub/activity/id/649d514eba30c",
  "instrument": "asadmin"
}

```
#### Offering a badge

This Activity Action describes an `Offer` activity, involving the assignment of a `Badge` from ArmelWanes (actor) to Hajavololona (target).



```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Offer",
  "object": "https://communecter.local/api/activitypub/object/id/653f3c437f1db",
  "id": "https://communecter.local/api/activitypub/activity/id/653f3f9de8d34",
  "actor":  "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "target": "https://communecter.org/api/activitypub/users/u/Hajavololona",
  "instrument": {
    "type": "Object",
    "narrative": "This is a narrative describing the badge assignment activity.",
    "attenteRecepteur": true
  },
  "published": "2023-10-30T05:31:09+0000",
  "summary": "Hajavololona assign Community Meetup to"
}

```

The `Offer` activity can be used to offer roles or responsibilities within an organization:

Example:
```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Offer",
  "actor": "https://communecter.org/api/activitypub/users/u/BoardMember",
  "object": {
    "type": "Role",
    "name": "Treasurer"
  },
  "target": "https://communecter.org/api/activitypub/users/u/FinanceExpert",
  "context": "https://communecter.org/api/activitypub/groups/g/NonProfitOrg"
}
```