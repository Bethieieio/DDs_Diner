## Database Structure
This is the plan for my database structure. I have one table per model and I have included relationships.

<iframe width="100%" height="500px" style="box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); border-radius:15px;" allowtransparency="true" allowfullscreen="true" scrolling="no" title="Embedded DrawSQL IFrame" frameborder="0" src="https://drawsql.app/teams/penny-flight-pirates/diagrams/project-four/embed"></iframe>


### User
- This table will be created using [AllAuth](https://django-allauth.readthedocs.io/en/latest/). It will supply basic user account functionality.
- The user will have to enter their email address, first and last names and a password to create an account.

### Boooking
- The table will be used for storing bookings against the user. 
- The user ID column as seen above, will be a foreign key that will relate to the user table.
- I would like to prevent overbooking by using group sizes to determine whether the time slot is fully booked.

### Preorders
- This table will store optional information if the customer would like to preorder their meals for time saving purposes.
- There could be more than one preorder per booking.
- The booking ID column will be a foreign key that relates to the booking table.

### Reviews
- This table stores all the reviews about the restaurant written by the customers.
- Users can write more than review.
- The user ID column will be a foreign key that relates to the reviews table.

### Review Likes
- This table stores all the likes the users leave to other users reviews.
- Users can like more than one review.
- This will have 2 foreign keys that relate it; user ID and review ID.
