# Model Architecture Planning
## Membership
```
- slug
- type (free, pro, enterprise)
- price (monthly)
- stripe plan id
```
## UserMembership
```
- user (foreignkey to default User)
- stripe customer id
- membership type (foreignkey to Membership)
```
## Subscription
```
- user membership (foreignkey to UserMembership)
- stripe subscription id
- active
```
## Course
```
- slug
- title
- description
- allowed memberships (manytomanyfield with Membership)
```
## Lession
```
- slug
- title
- course (foreignkey to Course)
- position
- video
- thumbnail
```
# &copy; Copyright
Fork from: [https://github.com/justdjango/video-membership](https://github.com/justdjango/video-membership)
