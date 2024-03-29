# DD's Diner
"Welcome to DD's Diner! Wanna  feel for retro dining atmosphere? Listening to songs from the 'Good Ol' Days?' Yes? Then this is the diner for you! Dreamt of becoming greaser for a evening? Come along to our monthy 50's Night, a (summer) night filled with action. So come on down, have a milkshake and enjoy the dining experience..."
This is a website about a fictional diner where you can have a look at the menu, create an account, book a table, view your bookings and also edit or delete them too. It is my forth project for Code Institute, it uses [Django](https://www.djangoproject.com/). It is for educational purposes only.
You can view it [HERE](https://project-four-dds-diner.herokuapp.com/) on [Heroku](https://dashboard.heroku.com/), a cloud hosting provider.

![image](assets/readme_assets/dds-logo.png)
![image](assets/readme_assets/full-screen-page.png)
![image](assets/readme_assets/medium-sized screen.png)
![image](assets/readme_assets/mobile-page.png)


## Target Audience
- For all ages
- People who are wanting to visit somethere to eat.
- Someone who might want to organise a meet up with friends or family at a restaurant.
- People who are into the 50's 60's era.
- Someone who just like looking at restaurant menus and making themselves hungry.. (so guilty at going this).
## User Stories
I have two types of user. The first is an admin user that can manage and delete booking, also delete reviews if they show inapporopriate langauge. The second type of user is the customers of DD's Diner. They can create, edit and delete their bookings, they can also write and like reviews.  The user can only do this, if they have created an account. Both users will want to view the menu to see what food they are serving. They might also need to know an email or phone number to contact the restaurant. They might also need the address and / or view the location on a Google map. They may want to see what is new in the menu or any events thats might me happening in the near future.


Here are the user stories, I made them into GitHub issues and created a project so I can track them using Kanban.
Please view this [HERE](https://github.com/users/Bethieieio/projects/2).

## Features

### Base
#### Logo
The logo was originally just a black line clipart image. The diners colours was added for it to fit in with the website design. I chose the planet design as when I saw the design on the clipart website, it reminded me of 'Pizza Planet', a fictional pizza place on Disney's Toy Story. Its is on the same white background as the navigation bar and ehrn clicked, it takes the user to the homepage. 
![image](static/css/images/dds_logo.png)

#### Navigation Bar
The navigation bar is located on the top of the page. When the user scrolls down the page, it is fixed to the top of the screen for user convenience. It has the off white background so it stands out from the rest of the website. I used the red for the links with the 'Pacifico' font. In between each link I separated them with a vertical line made using the yellow border-right line. When the user hovers over the red text, it turns yellow this is so the user knows its is a working navigation. Some of the navigation links change when the user is logged. As you can see in the pictures below, if the user is not sign in, it gives them the option to sign in and sign up. If the user is sign in, it gives them the option to sign out.
![image](assets/readme_assets/nav-signed-in.png)
![image](assets/readme_assets/nav-signed-out.png)

#### Footer
At the bottom of the page is the webites footer, it has the red background with white text and the links when hovered over are yellow. On the left hand side is the company email and phone number. These are both links so clicking on them start an email process and calls the diner respectively. On the right is the company address. In the middle the wonderful creator of this side and who she is creating it for. The Font Awesome image is an alternative GitHub logo, it is a link and takes the user to her GitHb profile. (:
![image](assets/readme_assets/project 4/footer.png)

### Home Page
#### Hero Image
The hero image a picture of inside of the diner. It is located underneath the nav on the homepage and covers half the page. It is eye-catching and bold and it gives the customer a sense of what it is like inside.
Half on the hero image is a yellow button with 'Pacifico' which is the main design of button on this site. When signed out, it is a sign up button that takes the user to the sign up section further down the page. When signed in, it goes to the 'Book a Table' page. Depending on what the customers name is, it also days their name. EG: 'Book a Table, Beth'.
![image](assets/readme_assets/hero-sign-in.png)
![image](assets/readme_assets/hero-sign-out.png)
#### Diner Offers
Directly under the hero image are three images with a yellow borders and a shadow. These are current offers that the diner currenly has. The are short straight to the point adverts. Containing an event and two new menu item items. They are all bright and eye catching.
![image](assets/readme_assets/diner-offers.png)

Below the diners current offers is the iframe of Google Map showing the location of the diner. The user can interact, with the map, zoom in and out, switch it to satellite view and see it's Google reviews.
![image](assets/readme_assets/diner-map.png)
#### Sign Up (Homepage)
Other than the separate sign up page, there is a sign up section on the homepage. It is laid out in the classic DD's style white background, red title in 'Pacifico' and has the yellow submit button. The simple yet effective design makes it easy to read and not an overpowering sight. This form can only be seen when the user is not signed in.
![image](assets/readme_assets/sign-up.png)

### Menu Page
The menu page contains an accordion that has four sections. Main meal, sides, drinks and desserts. When the section titles are clicked, the accordion expands showing its contents. Note that when the section of the accordion is open, the background goes yellow and the text goes red, until it closes, it wil go back to its orginal colours. I close to use an accordion as it stops the user from having to scroll to much going up down the menu / page. I also feel it looks tider.
![image](assets/readme_assets/menu1.png)
![image](assets/readme_assets/menu2.png)

### Reviews
The review page is a place where customers can read reviews from other customers. If they have an account they can also post there own reviews. Each review has there own white container with the yellow border and shadow to match the site. If the signed in user clicks the button that says "write a review" it scrolls down to the text area and start writing their review. I did this so it saves the customer from scrolling. If the user is not signed in there is no text area and the botton is replaced with a 'log In' button where it takes them to the sign in page.
![image](assets/readme_assets/review1.png)
![image](assets/readme_assets/review2.png)
![image](assets/readme_assets/review3.png)

### Book a Table
This page when the user is logged in is a form to book a table at the diner. The form is the sites standard white container, yellow border combo. The form asks for the time and date of visit, the number of people going and if any of the guests have any allergies. All of this informaton is then sent to the database and the booking information is also sent to the users 'Your Bookings' page.
If the customer is not logged in, they are sent to the log in page as you can only book a table if you have an account.
![image](assets/readme_assets/book-a-table.png)

### Your Bookings
This is the page where the users bookings are stored. The user can keep track, edit and delete them.
The layout is an accordion style like the menu, when each date is clicked it expands to give the details of that booking. Inside of each booking are two buttons:
Edit - Where the users can change the data, time, guest no and allergie boolean again and this will get updated when resubmitted (to the database too);.
Delete - if the customer changes their mind, they can delete the booking and it is delete from the database as well. Their booking will be cancelled. 
Users who are not logged in do not see this page.
![image](assets/readme_assets/your-booking1.png)
![image](assets/readme_assets/your-booking2.png)

### Log In
This is the page where the user logs into their account.
They need to enter their email and their password, it uses crispy forms.
Users that are not signed in get directed here if they try to book a table.
![image](assets/readme_assets/log-in-form.png)

### Log Out 
When the user would like to log out of their account, they click on the 'Log Out' on the furthest right link on the navigation bar. The user is then asked a question if the are sure they are wanting to log out just in case they click on the button by accident. If they want to sign out, then they click on the 'Signing Off' sumbit button where this signs them out of their account.
![image](assets/readme_assets/log-out.png)

### Message Pop-Ups
I chose to have pop ups as it lets the user know there request has been submitted.
It disappears after a couple of seconds.
- Signing in
![image](assets/readme_assets/pop-up-message2.png)
- Signing out
![image](assets/readme_assets/pop-up-message1.png)
- Create booking
![image](assets/readme_assets/pop-up-message4.png)
- Edit booking
![image](assets/readme_assets/pop-up-message6.png)
- Delete booking
![image](assets/readme_assets/pop-up-message6.png)
- Submitted review
![image](assets/readme_assets/pop-up-message3.png)

### Feature Priority
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
I got inspiration from to use my chosen colours of red (#A82428), yellow (#FFBE33) and off white (#EBEBEB) from [Coolors](https://coolors.co/ebebeb-a82428-ffbe33-000000) (press link to see colours). Red and yellow stand out from eachother. They also represent colours from diners and two very famous fast food restuarants...
I chose black as it is bold and stands out from the other colours I have chosen. I chose an off white instead of a 'normal' white as I just wanted something different. I used the red mainly in the background border and navigation text. The off white as the main colour of text containers including the navigation bar background, the yellow as the main titles, accents on the off white containers, the hover colour on the nav, the main button colour and the colour the accordion title colour when they are clicked on. The black is used mostly for the main  text colour in the white containers.
### Typeography
I used two font types for this webite.
I used [Google Fonts](https://fonts.google.com/)
Pacifico  - for the the main titles and the logo. I felt that it was fancy and looked like a font that diners have. But I made sure it was wasy enough for people to read. 
Anek Gujarati - for the main text on the website. I felt it did not over power the page. easy for everyone to read. It look sleek and simple enough not to clash with the title font.
### Media
#### Photos
Below are the links and names of the people who look the photos I used for my project. They are either from [Unsplash](https://unsplash.com/) or -- [Pexels](https://www.pexels.com/). Thank you!! </br>
[Dayanara Nacion](https://unsplash.com/photos/HuIJUp6gTDI) - Hero Image.  <br/>
[Max Bovkun](https://unsplash.com/photos/UcQ0MLuw8IE ) - 50's night advertisement on hompage.  <br/>
[Valeria Boltneva](https://www.pexels.com/photo/close-up-photo-of-burger-1639562/) - Burger image in menu.  <br/>
[王 大洪](https://unsplash.com/photos/PPwYBaC_g8M) - Hot Dog image in menu.  <br/>
[Glady Francis](https://www.pexels.com/photo/bowl-of-fries-on-table-1586942/) - Fries in menu.  <br/>
[Anton Uniqueton](https://www.pexels.com/photo/crispy-waffle-fries-5384838/) - Waffle fries in menu.  <br/>
[Dana Tentis](https://www.pexels.com/photo/vegetable-salad-with-wheat-bread-on-the-side-1213710/) - Salad in menu.  <br/>
[Esperanza Doronila](https://unsplash.com/photos/4FO9vox0T7M) - Onion rings in menu.  <br/>
[Georgiana Mirela](https://www.pexels.com/photo/close-up-photo-of-potato-wedges-1439177/)
[Louis Hansel](https://unsplash.com/photos/OaGUHIjCdCs) Milkshake advertisement on homepage.  <br/>
[Richard Bell](https://unsplash.com/photos/ZFPz3caOmx8) - English breakfast adverrtisement on homepage.  <br/>
[Food Photographer](https://unsplash.com/photos/h7a8RsZFzgc) - Cola in menu.  <br/>
[Jonathan Borba](https://unsplash.com/photos/7TeR1A1MUpM ) - Milkshake image in menu.  <br/>
[ABHISHEK HAJARE](https://unsplash.com/photos/kkrXVKK-jhg) - Orange juice in menu.  <br/>
[Taisiia Shestopal](https://unsplash.com/photos/xO9NotFY4mU) - Latte in menu.  <br/>
[Paige Ledford](https://unsplash.com/photos/1Di03LTniYE) - Mocktail in menu.  <br/>
[Bao Menglong](https://unsplash.com/photos/y_wGdAJMdOo ) - Ribs in menu.  <br/>
[The Fry Family Food Co.](https://unsplash.com/photos/bA4AIZwauxc) - Vege chicken-style wrap.  <br/>
[Keriliwi](https://unsplash.com/photos/v_JswZL-s3k) - Chicken wings in menu.  <br/>
[Mink Mingle](https://unsplash.com/photos/LGNxQzYmeUk) - Cheesecake in menu.  <br/>
[Céline Druguet](https://unsplash.com/photos/vxWMHx7m8iY) - Sundae in menu.  <br/>
[Shivansh Sethi](https://unsplash.com/photos/dKT6Q7q2UKs) - Chocolate brownie in menu.  <br/>
[Yulia Khlebnikova](https://unsplash.com/photos/HLwc-ne0IQM) - Fruit salad in menu. <br/>
[Edward Howell](https://unsplash.com/photos/ZXmxQ0Ny_IY) - Sticky toffee pudding in menu. 
#### ClipArt
[Logo](http://clipart-library.com/search1/?q=saturn#gsc.tab=1&gsc.q=saturn&gsc.page=1) - This is the logo located in the top left page throughout the website, the colours and DD's text was edited in. <br/>
[Unused image](http://clipart-library.com/clipart/87973.htm) - This was the image I decided not to use, as I felt it did not fit well on the page. It is still in my wireframes.
## Testing
### Manual Testing
- Implementation: During the signing up process of the website, the email has to be a valid looking email address.
- Test: I attempted to sign up without an email structure as an email.
- Result: The page told me that the email I tried did not contain the @ symbol.
![image](assets/readme_assets/sign-up-manual-test-one.png)
- Verdict: Successfull. A valid looking password needs to be input in order to sign up.
***
- Implementation: Makings sure the user cannot sign up with the same email address as before.
- Test: I tried signing up using an email address that is already in the database.
- Result: The page told me that a user has already sign up with the email address I have tried to enter.
![image](assets/sign-up-manual-test-two.png)
- Verdict: Successful. You cannot sign up with a particular email address more than once.
***
- Implementation: User logging into the site.
- Test: I went to the login page of the site and input my email address and password. I also used different ways of logging in by using the button 
 located in on the 'book a table' and 'reviews' pages.
 ![image](assets/readme_assets/booking-table-test-one.png)
- Result: I signed in on the account the three times as explained above. Logging in from the sign in page directed me back to the homepage. Logging in by clicking the login button from the review page redirected me back to the reviews page. Finally, logging in using the log in on the 'book a table' page directs me to the booking form on the 'book a table' page.
![image](assets/readme_assets/log-in-manual-test-two.png)
- Verdict: All three times were a success, every time a pop appeared saying I was signed in. All the extra features were acccessible after I signed in.
***
- Implementation: Booking a table at DD's Dinner succesfully.
- Test: I used website to book a table at a specific time, date and number of guests. I also tried to see if it's possible to submit a blank table.
- Result: Once the tabe has been booked, it appears on the "Your Bookings" page. I saw the success message. You also cannot submit an empty form.
![image](assets/readme_assets/booking-table-test-one.png)
![image](assets/readme_assets/blank-booking-manual-test.png)
![image](assets/readme_assets/book-table-success-page.png)
- Verdict: Success, the user will be able to book a table and are shown they have been booked by a success message.
***
- Implementation: If for whatever reason the user needs to change the date, time, number of heads of allergy needs on a booking they have created, they should be able to do so.
- Test: On the "Your Bookings" page, I found the booking I previously created. I clicked on it and the edit button was shown. I clicked on this and I was able to edit the date from the 24th to the 26th February,
![image](assets/readme_assets/edit-booking-manual-test-one.png)
- Result: When I requested for the date to be changed, I got a messaging saying that I have edited my booking sucessfully.
![image](assets/readme_assets/edit-booking-manual-test-two.png)
- Verdict: Successful. The pop up message appeared and the date can be seen that it was changed by two days.
***
- Implementation: If something came up for the user and they can no longer go to DD's Dinerm they can cancel their booking by deleting their booking. The user needs a quick and easy way to do so.
- Test: I viewed the booking that I recently edited and clicked the delete booking.
- Result: As soon as I clicked the delete button, the booking was deleted and a pop up appeared explaining that the deletion was successful.
![image](assets/readme_assets/delete-booking-manual-test.png)
- Verdict: It was successful, the booking has been deleted off the website and from the database.
***
- Implementation: The user wants to leave a review about their experience at DD's Diner.
- Test: Trying to leave a review before loggin in. When I was logged in, I left a test review on the 'reviews' page. 
- Result: When not logged in, I was unable to see the text area on the 'reviews' page. When I was logged in and after writing a comment on the text area required, the comment I left appeared on the page hastily.
- Verdict: As shown, the user needs to be logged in to be able to leave a review. Once they are logged in, they can leave as many reviews as they like. The pop up message confirms that the user submitted a review.
![image](assets/readme_assets/review-manual-test-one.png)
!![image](assets/readme_assets/review-manual-test-two.png)
![image](assets/readme_assets/review-manual-test-three.png)
***
- Implementation: Liking reviews is a great way to show that you agree with another users review.  If a user liked a review my mistake, clicking the like icon again, will remove the like. Only users that have an account can like reviews.
- Test: While logged in, clicking on the heart shaped icon will change the colour of the heart to DD's Red. Whem not logged in, I will see how many people have liked the review, but unable to like the review myself.
- Result: Logged in by clicking the heart, it changes colour, this means it liked, clicking the heart again removes the like. When not logged in, I cannot like review.
![image](assets/readme_assets/like-reviews-manual-test-two.png)
![image](assets/readme_assets/like-reviews-manual-test-one.png)
- Verdict: This is all working as it should.  The right type of user are able to like the reviews.
***

- Implementation: The websites menu and users booking page accordions that use Bootstrap. As well as adding movement to the website, it also allows the user not to scroll to far down the page.
- Test: I tested this by repeatedly clicking all the avaliable accordion buttons. Making sure they all expand and retract with no issues.
- Result: All of the buttons worked, even spamming them, they worked flawlessly. Each of them changed colour to the DD's yellow when they are expanded.
- Verdict: It was a success, I did everything in my power to try and break them, but they did not. (:
***

- Implementation: By adding /admin at the end on the URL, you appear on the admin side of the site. Only superusers have access to this page. They have an overview of the bookings, users names , email address and reviews.
- Test: Here it is,  By adding /admin at the end on the URL, you appear on the admin side of the site.
![image](assets/readme_assets/admin-page-one.png)
![image](assets/readme_assets/admin-page-two.png)

- Result: All the data is visible from the admin side of the site, only the superusers can access this.
- Verdict: It is successful because it is part of the Django package.
***

- Implementation: The admin needs to remove reviews if they contain words that are not acceptable to be shown on the website. So giving them the ability to delete them needs to be implicated. They may need to also delete a booking themselves if need  be.
- Test: In the "Create Reviewss" link on the left hand side there is a list on all the reviews that were made. If one / more reviews were deemed "inappropriate", tick the box on the side of the review, click the dropdown, click delete and press go! By going onto the "Booking models" I can also have the ability to delete bookings.
- Result: Anytime this process happens, it deletes the review.
- Verdict: It is successful because it is part of the Django package.
![image](assets/readme_assets/admin-reviews.png)
![image](assets/readme_assets/delete-review-admin.png)

### HTML VALIDATION

- Homepage / Base Page
1. Firstly I forgot to add the langauge attribute to the head. I added this
2. I then deleted the endinf '/' on a meta tag.
3. I forgot to add an alt tag to the hero image, I added this.
4. I had to move classes on some buttons to their 'a tag'.
5. I got `<ul>` and `<li>` mixed up, I accedently put the `<ul>` inside the `<li>`. I corrected this.
6. I had a a `</li>` but no `<li>` so I completed this tag.
7. I had an unclosed `a` tag. I closed this.
8. I had a a `</footer>` but no `<footer>` so I completed this tag.
9. I had a a `</footer>` but no `<footer>` so I completed this tag.
[!image](assets/readme_assets/base-index-html-test1.png)
[!image](assets/readme_assets/base-index-html-test2.png)
I fixed all the small errors, the HTML on the base and homepage are now error free.
[!image](assets/readme_assets/base-index-html-test3.png)

- Review Page
The review page have no errors in it's HTML.
![image](assets/readme_assets/review-html-test.png)

- Book a Table and Your Bookings
These pages have an unncessary / on the `<input>` tags.
I cannot resolves these because. The value is a URL and it is generated by Crispy Forms
![image](assets/readme_assets/html-test-book-a-table.png)
![image](assets/readme_assets/your-booking-html-test.png)

- Menu Page
Because of the accordion has more than one button, I copied each accordion button so they all had the same aria-controls. I forgot to edit the these attribute. I changed each of these attributes so they were different to eachother.
![image](assets/readme_assets/html-validator-menu.png)
![image](assets/readme_assets/html-testing-menu.png)


### CSS VALIDATION
My CSS passed threw with no errors.
![image](assets/readme_assets/css-validator.png)
### PEP8 
I had a couple of things that needed adjusting in my python code.
1. This line was too long, I had to divide this line of code to short lines of code.
2. Here I had an indentation that wasnt needed, I just deleted this.
3. This part needed 2 blank spaces here in between the class and the imports. I only had one.
4. I had some comments that did not start with '#', I didnt need this any more, so I removed the comments.
5. At the end of the admin.py page, there was an empty line with a tab. I deleted this.
5. After the code on this line, there was an extra space/tab that was not needed. I deleted this.
6. Here I had one extra line between the code (3), so I removed one.

![image](assets/readme_assets/python-validation-code.png)
![image](assets/readme_assets/python-validation-test2.png)

### Lighthouse Testing
Here are all the results of the Lighthouse Testing 
![image](assets/readme_assets/lighthouse-home.png)
![image](assets/readme_assets/lighthouse-menu.png)
![image](assets/readme_assets/lighthouse-review.png)
![image](assets/readme_assets/lighthouse-book-table.png)
![image](assets/readme_assets/lighthouse-my-bookings.png)


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
- [Font Awesome](https://fontawesome.com/) - for the Github symbol in the footer of the website.
- Pip3 is a package manager for python.
- HTML/CSS - structures and styles user interface.
- Mark Down - This read me in in Mark Down.

## Database
### Database Structure
This is the plan for my database structure. I have one table per model and I have included relationships. I used [DrawSQL](https://drawsql.app/).

![image](assets/readme_assets/database-model.png
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
- [Google Map IFrame Genertor](https://google-map-generator.com/).
The above helped me the most with this project when I needed guidence.
### Tools
- [PyCodeStyle](https://pypi.org/project/pycodestyle/) Used to test Python, as [PEP8 Validator](http://ww7.pep8online.com/) is still being weird.
- [W3C HTML Validator](https://validator.w3.org/) was used to test the HTML.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to test the CSS.
- [Balsamiq](https://balsamiq.com/) created by wireframes
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - self explanatory. 


## Deployment 
### Setting up Django

- Create a new repository
I created a [repository](https://docs.github.com/en/get-started/quickstart/create-a-repo) on github and cloned it to my local machine.
- Install Django
Using pip3, I installed the latest version of Django and initial packages I knew I needed:
 `pip3 install django gunicorn dj_database_url psycopg2`
- Run pip freeze and save to reqirements.txt file.
I used the following command `pip3 freeze --local > requirements.txt` to save the versions I have installed so they can be installed when deploying to Heroku.   
- Create new Django project
I used the command `django-admin startproject DDs_Diner`.
- Create new Django app 
Next I used the command `python3 manage.py startapp restaurant`.
- Run migrate and run server
I ran an inital migration my running `python3 manage.py migrate`. Then I started the server making sure it worked locally, by using the command `python3 manage.py runserver` and checking the port.

### Additional Set Up
- Create my local ENV file.
I created a `env.py` file - this is where I intend to store my secret keys.
- Gitignore File
I added the `env.py` to the `.gitignore` file, this is so that the file is not added to Git and does not end up on the internet.
- Create Inital ENV values
Create a `DATABASE_URL` line in the `env.py` file and add the value of the [ElephantSQL](https://www.elephantsql.com/) database URL that I created earlier.
- Created a secret key in the `env.py` file and assign it a randomly generated string.
- In my `settings.py` file I added some import statements to import my ENV values from my `env.py` file.
- Next in my `settings.py` file I replaced the secret key variable assignment with my ENV value for the secret key and updated the database settings to use my ENV value from my ENV file.
- Later on in this project's development, I installed White Noise for static file hosting on Heroku. I needed to configure Django for White Noise by updating the `STATICFILES_DIRS` to be a relative path to my static directory and `STATIC_ROUTE` to be a relative path to the `staticfiles` directory.

### Installed Apps
Throughout this project, I installed various Django packages that required values to be added to the `INSTALLED_APPS` variable in `settings.py` file. 
Some example are: 
- White Noise 
- All Auth
- My Restaurant App
- Crispy Forms
This involved adding app names to the List as mentioned in the relevent documentation.

### Deployment to Heroku 
- I commit and pushed all my work to Github
- Signed in and clicked on "New" and "New App".
- I named the deployment, and chose "Europe" region.
- Input all necessary config vars on the Heroku settings tab.
- I made a procfile to start Gunicorn on Heroku and commited these changes.
- On the deploy tab on Heroku, I connected my Github account and DD's Diner repository to it.
- Clicked 'Deploy Branch'. 
- Cliked on 'Open App' to view the DD's Diner site. 
- Now whenever I make a commit, it automatically deploys to Heroku.

> Because my local and heroku use the same database, there is no need for migrations when deploying.

## Future Features
In the future I would like to add to the following project:
- The ability for the users to preorder their when they book a table. This will help with faster waiting times for the user.
- To make a more relistic booking process, having a limition on times. For example, the user will not be able to book a table at 3.00am when the restaurant is close, or a time too far into the future or anytime in the past. Only a certain number of bookings can be made on a certain time and day to avoid over booking.
- I would like to add a contact form so that the customer will be able to contact the diner instead of popping in or calling up.

## Honourable Mentions
- [My Partner in crime](https://github.com/bashleigh) Kept me as sane is she possibly could, and answered all the questions I had as simply as possible. She also edited the colours in the logo.
- My Mentor Rich, big ups to him. Thank you (:



note
fixed nav
future fixes