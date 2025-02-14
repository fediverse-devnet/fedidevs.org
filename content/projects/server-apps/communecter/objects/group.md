---
id: group
title: Group
---

A `Group` is activity used for federation group in Communecter.The federation of groups in Communecter expands the concept of collaboration by connecting multiple groups across different regions or topics. These groups can:

## Properties

| Property          | Data type    | Description                                                     |
| ----------------- | ------------ | --------------------------------------------------------------- |
| `type`\*          | String       | The object type (`Group`)                                        |
| `id`\*            | String (URI) | The URI that identifies the group                                 |
| `attributedTo`    | String (URI) | The URI of the user who posted the note                          |
| `name`\*       | String       | The name of group
| `description`\*       | String       | The description of group
| `published`\*     | Datetime     | The date and time when the group was published                    |
| `mediaAttachments`| Array        | An array of objects representing the media attached to the group  |
| `tag`             | Array        | An array of strings representing the tags associated with the group |

\* Required properties.

### Attachment Object

| Property         | Data Type    | Description                                     |
| ---------------- | ------------ | ----------------------------------------------- |
| `type`\*         | String       | The object type (`Document` or `Link`)           |
| `name`           | String       | The name or title of the attachment              |
| `url`\*          | String (URL) | The URL of the attachment                        |
| `mediaType`      | String       | The media type of the attachment (e.g., `image/png`, `text/html`) |
| `category`       | String       | The category or classification of the attachment |

### Place Object

| Property         | Data Type         | Description                                     |
| ---------------- | ----------------- | ----------------------------------------------- |
| `type`\*         | String            | The object type (`Place`)                       |
| `id`\*           | String (URI)      | The URI that identifies the place                |
| `name`           | String            | The name of the place                            |
| `address`        | Object (Address)  | The address details of the place                 |

### Address Object

| Property           | Data Type | Description                                     |
| ------------------ | --------- | ----------------------------------------------- |
| `type`\*           | String    | The object type (`PostalAddress`)               |
| `addressCountry`   | String    | The country of the address                       |
| `addressLocality`  | String    | The locality (city, town, etc.) of the address   |
| `addressRegion`    | String    | The region (state, province, etc.) of the address|
| `postalCode`       | String    | The postal code of the address                   |
| `streetAddress`    | String    | The street address of the place                  |

## Example

```json
{
  "type": "Note",
  "id": "https://communecter.org/api/activitypub/object/id/96a15d71d725c",
  "author": "John Doe",
  "content": "This is an example note in Communecter.",
  "published": "2023-07-02T14:30:00Z",
  "tags": ["community", "event"],
  "attachments": [
    {
      "type": "Image",
      "name": "Photo",
      "url": "https://example.com/images/icon.jpg",
      "mediaType": "image/jpeg"
    },
    {
      "type": "Link",
      "name": "Website",
      "url": "https://example.com",
      "mediaType": "text/html"
    }
  ]
}

