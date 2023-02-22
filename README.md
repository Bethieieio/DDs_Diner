# DD's Diner
This is a website about a fictional diner where you can book a table, view your bookings and also edit or delete them too. It is my forth project for Code Institute, it uses [Django](https://www.djangoproject.com/). It is for educational purposes only.
You can view it [HERE](https://project-four-dds-diner.herokuapp.com/) on [Heroku](https://dashboard.heroku.com/), a cloud hosting provider.

![image](assets/readme_assets/am-i-responsive.png)

## Target Audience
- The main  
## User Stories
I have two types of user. The first is an admin user that can manage and delete booking, also delete reviews if they show inapporopriate langauge. The second type of user is the customers of DD's Diner. They can create, edit and delete their bookings, they can also write and like reviews.  The user can only do this, if they have created an account.

Here are the user stories, I made them into GitHub issues and created a project so I can track them using Kanban.
Please view this [HERE](https://github.com/users/Bethieieio/projects/2).

## Feature Priority
Here are the simplified user stories with their priority score. This is so I can prioritise time for the most important features.
1 being the least important, while 5 being the most.

| Feature      | Priority   |
| ----------- | ----------- |
| create reviews | 3 |
| like reviews | 2 |
| admin delete review | 2 |
| user create booking  | 5  |
| user edit booking  |  5 |
| user delete booking  |  5 |
| user to view bookings  |  5 |
| display resturant menu  | 3 |
| user can login / sign up    |  5 |
| overbooking validation  |  2 |
| create map  |  2 |

## Styles
### Wireframes
Here are the wireframes I created before starting this project. As you can see certain ideas never made it to the final project, for example the preorder section on the table booking page and some CSS styles and positions. But as a whole, the final site is accurate to these wireframes.
![image](assets/readme_assets/wireframe-home.png)
![image](assets/readme_assets/wireframe-book-table.png)
![image](assets/readme_assets/wireframe-edit-booking.png)
![image](assets/readme_assets/wireframe-menu.png)
![image](assets/readme_assets/wireframe-reviews.png)
![image](assets/readme_assets/wireframe-login.png)

### Colour Schemes
I got inspiration from to use my chosen colours of red, yellow, off white from [Coolors](https://coolors.co/ebebeb-a82428-ffbe33-000000) (press link to see colours). Red and yellow stand out from eachother. They also represent colours from diners and two very famous fast food restuarants...
I chose black as it is bold and stands out from the other colours I have chosen. I chose an off white instead of a 'normal' white as I just wanted something different. I used the red mainly in the background border and navigation text. The off white as the main colour of text containers including the navigation bar background, the yellow as the main titles, accents on the off white containers, the hover colour on the nav, the main button colour and the colour the accordion title colour when they are clicked on. The black is used mostly for the main  text colour in the white containers.
### Typeography
I used two font types for this webite.
I used [Google Fonts]()
Pacifico  - for the the main titles and the logo. I felt that it was fancy and looked like a font that diners have. But I made sure it was wasy enough for people to read. 
Anek Gujarati - for the main text on the website. I felt it did not over power the page. easy for everyone to read. It look sleek and simple enough not to clash with the title font.
### Media (Pictures)
## Testing
### Manual Testing
- make sure user can create edit view delete booking
- make sure user can make review
- make sure user can like / unlike reviews
- make sure user can sign up / log in  / log out 
- make sure admin can view reviews and bookings 
- make sure admin can delete reviews and bookings
- make sure manu accordions work and google map.
### HTML VALIDATION
### CSS VALIDATION
### PEP8 

installed pycodestyle which is a global command
used pycodestyle to point out validation failure by running `pycodestyle --first */*.py`
fixed each one manually and committed

## Packages, Languages and Frameworks
### Django
Django is an MVC (Model View Controller) framework. I have used Django as a backend service to provide endpoints, which render HTML using templates and handle POST form data. Django also handles user authentication tokens and sessions.
### AllAuth Customisation
- Because I wanted to add the first and last name of the user on sign up, I need to create a custom [AllAuth](https://django-allauth.readthedocs.io/en/latest/) adapter and cudtomer AllAuth signup form.
I did this by extending the default AllAuth adapter adding the first and last name field. Because I did not want to use the 'username' field, in the adapter, I set the username to be the email field and configured AllAuth to use the my custom adapter and email for sign in.
- I had some complications, which resulted in the need to set the username field to be the same as the email.
- I also found complications using my custom form on the homepage, when storing first name and last name, which required configuring AllAuth to use my custom sign up form.

### Crispy Forms
I installed [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) so I could automatically render HTML from Django form classes. This also enables me to user Django forms to handle model data.

### Bootstrap
I installed [Bootstrap](https://getbootstrap.com/) to utilise it's style classes and components. I have used Bootstrap components with JavaScript events such as the mobile menu and accordion components.

### White Noise 
- [White Noise](http://whitenoise.evans.io/en/latest/) was used to host static files on Heroku.

### Other
- [Gunicorn](https://gunicorn.org/) - http server
- [SQLParse](https://pypi.org/project/sqlparse/) - SQL Driver
- [Python3](https://www.python.org/downloads/)
- [GitHib](https://github.com/) - version control
- [VS Code](https://code.visualstudio.com/) - IDE, where I wrote my codes.
- [ElephantSQL](https://www.elephantsql.com/) - PostGRES database, where all my tables are stored.
- Pip3 is a package manager for python
- HTML/CSS structures and styles user interface.
- Mark Down - This read me in in Mark Down.

## Database
### Database Structure
This is the plan for my database structure. I have one table per model and I have included relationships. I used [DrawSQL](https://drawsql.app/).

<iframe width="100%" height="500px" style="box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); border-radius:15px;" allowtransparency="true" allowfullscreen="true" scrolling="no" title="Embedded DrawSQL IFrame" frameborder="0" src="https://drawsql.app/teams/penny-flight-pirates/diagrams/project-four/embed"></iframe>

#### User
- This table will be created using [AllAuth](https://django-allauth.readthedocs.io/en/latest/). It will supply basic user account functionality.
- The user will have to enter their email address, first and last names and a password to create an account.

#### Booking
- The table will be used for storing bookings against the user. 
- The user ID column as seen above, will be a foreign key that will relate to the user table.
- I would like to prevent overbooking by using group sizes to determine whether the time slot is fully booked.

#### Preorders
- I ended up not doing this as I was running out of time.
#### Reviews
- This table stores all the reviews about the restaurant written by the customers.
- Users can write more than review.
- The user ID column will be a foreign key that relates to the reviews table.

#### Review Likes
- This table stores all the likes the users leave to other users reviews.
- Users can like more than one review.
- This will have 2 foreign keys that relate it; user ID and review ID.

### Migrations
- In order to keep my database in sync with my database models in my application, I used Django models to create and update my database table structure.
- When running `python3 manage.py makemigrations` Django will check my database tables against my models in my application and create a unique migration file  which we can use to update table changes.
- Running `python3 manage.py migrate` will execute these migration changes.

## Resources 
### General Resources
- [Stack Overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)
The above helped me the most with this project when I needed guidence.
### Tools
- [PyCodeStyle](https://pypi.org/project/pycodestyle/) Used to test Python, as [PEP8 Validator](http://ww7.pep8online.com/) is still being weird.
- [W3C HTML Validator](https://validator.w3.org/) was used to test the HTML.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to test the CSS.
- [Balsamiq](https://balsamiq.com/) created by wireframes
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - self explanatory. 

## Deployment to Heroku 
- I commit and pushed all my work to Github
- Signed in and clicked on "New" and "New App".
- I named the deployment, and chose "Europe" region.
- Input all necessary config vars on the Heroku settings tab.
- I made a procfile to start Gunicorn on Heroku and commited these changes.
- On the deploy tab on Heroku, I connected my Github account and DD's Diner repository to it.
- Clicked 'Deploy Branch'. 
- Cliked on 'Open App' to view the DD's Diner site. 
- Now whenever I make a commit, it automatically deploys to Heroku.

> Because my local and heroku use the same database, there is no need formigrations ehen deploying.

## Hourable Mentions
- [Girlfriend](https://github.com/bashleigh) Kept me as sane is she possibly could, and answered all the questions I had as simply as possible.
- My Mentor Rich, big ups to him. Thank you (:



note
fixed nav