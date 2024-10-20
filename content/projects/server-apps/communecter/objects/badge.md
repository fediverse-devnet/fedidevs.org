---
id: badge
title: Badge
---

An `Badge` is an activity representing a specific badge in Communecter.

## Properties

| Property          | Data Type              | Description                                         |
| ----------------- | ---------------------- |-----------------------------------------------------|
| `type`\*          | String                 | The object type (`Badge`)                           |
| `id`\*            | String (URI)           | The URI that identifies the badge                   |
| `attachment`\*    | Array of Attachments   | Attachments associated with the badge               |
| `attributedTo`\*  | String (URI)           | The URI of the entity or user who created the badge |
| `content`\*       | String                 | The content or description of the badge             |
| `name`\*          | String                 | The name or title of the badge                      |
| `published`\*     | String                 | The date and time when the badge was published      |
| `url`             | String (URL)           | The URL of the badge's website or landing page      |

## Example

```json
{
  "type": "Badge",
  "id" : "https://communecter.org/api/activitypub/object/id/652539d72a857",
  "name" : "Project Leader",
  "published" : "2024-07-02T11:47:35+0000",
  "attachment": [
    {
      "type": "Link",
      "name": "Website",
      "url": "https://example.com",
      "mediaType": "text/html"
    }
  ]
}
