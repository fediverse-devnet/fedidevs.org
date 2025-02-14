---
id: communecter
title: Communecter
tags:
  - Event
  - News 
  - Projects
  - Badges
  - Organizations
  - Social Networking
  - Federation
---


## What is Communecter ActivityPub?

Communecter ActivityPub is an implementation of the ActivityPub protocol tailored for the Communecter platform. It enables federation and interaction between users on different instances of Communecter, as well as with other federated platforms.

## Functionality

Communecter ActivityPub provides the following functionality:

### Notes

Notes are short, text-based messages that users can create to share their thoughts, updates, or announcements. They can include hashtags to categorize the content and make it more discoverable. Users can:

- Create a new note by sending a `Create` activity with the `Note` object.
- Like or react to a note by sending a `Like` activity.
- Reply to a note by sending a `Create` activity with the `Note` object as the reply's `inReplyTo` field.
- Share or repost a note by sending a `Create` activity with the `Note` object and adding their own commentary.

### Events

Events represent specific occurrences or gatherings that users can create and share with others. Users can:

- Create a new event by sending a `Create` activity with the `Event` object.
- Join an event by sending a `Join` activity to indicate their participation or interest in attending.
- Follow an event by sending a `Follow` activity to receive updates and notifications about the event.
- Intercept events using the event interception feature, especially with platforms like Mobilizon, allowing users to discover and import events from other platforms into Communecter.
- Leave an event by sending a `Leave` activity to withdraw their participation or interest.
- Delete an event by sending a `Delete` activity to indicate the removal of the event from Communecter.

Events can have various details, such as the date, time, location, description, and associated tags or categories. Users can search for events based on their interests or browse through events happening in their community or network.


### Projects

Projects represent collaborative initiatives or tasks that users can create and manage within Communecter. Users can:

- Create a new project by sending a `Create` activity with the `Project` object.
- Update an existing project by sending an `Update` activity to modify its details or progress.
- Delete a project by sending a `Delete` activity to indicate its removal from Communecter.
- Invite other users to join a project by sending an `Invite` activity, requesting their participation.
- Join a project by sending a `Join` activity, expressing their interest in contributing to the project.
- Offer specific roles or privileges to users within a project by using the `instrument` field, such as `asadmin` or `contributor`.
- Leave a project by sending a `Leave` activity to withdraw their participation or contribution.
- Accept or reject an invitation to join a project by sending an `Accept` or `Reject` activity, respectively.

Projects can have various attributes, such as a description, goals, milestones, associated members, and related resources. Users can search for projects based on their interests or browse through existing projects in their community or network.

> **Please note that project federation is currently under experimentation and development in Communecter, aiming to enable the exchange and collaboration of projects across federated instances. This feature is being actively worked on to enhance the federation capabilities of projects in the future.**
>



### Organizations

Organizations represent groups, businesses, or communities within Communecter. The federation of organizations allows for broader networking and collaboration across different Communecter instances. Users can:

- Create a new organization by sending a `Create` activity with the `Organization` object.
- Update an existing organization by sending an `Update` activity to modify its details or structure.
- Delete an organization by sending a `Delete` activity to indicate its removal from Communecter.
- Join an organization by sending a `Join` activity, expressing their interest in becoming a member.
- Leave an organization by sending a `Leave` activity to withdraw their membership.
- Invite users to join an organization by sending an `Invite` activity.
- Accept or reject an invitation to join an organization by sending an `Accept` or `Reject` activity, respectively.
- Follow an organization by sending a `Follow` activity to receive updates and notifications about the organization's activities.

Organizations can have various attributes such as:
- Name and description
- Location information
- Contact details
- Member list and roles
- Associated projects and events
- Social media links
- Tags or categories

Users can search for organizations based on their interests, location, or type, and browse through existing organizations across federated instances.

> **Note: The federation of organizations in Communecter is an ongoing development. While basic functionality is available, more advanced features and cross-instance collaboration tools are being actively worked on to enhance the federation capabilities of organizations in the future.**

### Badges

The Badge Federation System within Communecter allows users and organizations to create, manage, and interact with badges, enhancing community engagement and recognition. Users can:

- Create a Badge: Introduce a new badge by sending a `Create` activity with the Badge object, defining its criteria, appearance, and purpose.
- Edit a Badge: Update an existing badge by sending an `Update` activity to modify its details, criteria, or visual design.
- Delete a Badge: Remove a badge by sending a `Delete` activity, indicating its removal from the system.
- Self-Assign a Badge: Claim a badge for themselves by sending a Self-Assign activity, acknowledging their own achievements.
- Assign a Badge to Someone: Grant a badge to another user by sending an Assign activity, recognizing their contributions or accomplishments.
- Assign a Badge to an Organization: Award a badge to an organization by sending an Assign to Organization activity, recognizing collective efforts and milestones.
- Refuse a Badge: Decline a badge by sending a Refuse activity, if they feel the badge is undeserved or not applicable.
- Accept a Badge: Accept a badge by sending an `Accept` activity, acknowledging the recognition.
- Reject a Badge: Reject a badge by sending a `Reject` activity, declining the recognition.


Badges can have various attributes, such as a description, criteria, visual design, associated users, and related activities. Users can search for badges based on their interests or browse




## Interoperability

Communecter ActivityPub supports interoperability with other federated platforms implementing ActivityPub. This enables users to interact with users on other platforms, including:

- **Mastodon**
- **Mobilizon**
- **PeerTube**

Users can follow accounts from these platforms, receive their updates, and interact with their content.


Supported Activities

- [**Create**](activities/create)
- [**Accept**](activities/accept)
- [**Follow**](activities/follow)
- [**Undo**](activities/undo)
- [**Update**](activities/update)
- [**Delete**](activities/delete)
- [**Invite**](activities/invite)
- [**Join**](activities/join)
- [**Leave**](activities/leave)
- [**Undo**](activities/undo)
- [**Remove**](activities/remove)
- [**Reject**](activities/reject)
- [**Offer**](activities/offer)

Supported Objects

- [**Note**](objects/note)
- [**Event**](objects/event)
- [**Project**](objects/project)
- [**Group**](objects/group)
- [**Badge**](objects/badge)
