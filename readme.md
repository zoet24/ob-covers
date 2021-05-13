# OB Covers

## Code Institute: Milestone Project 4

![OB Covers on multiple devices](static/images/readme/ob-app-responsive.png)

I have worked for Open Bionics since 2016 - we are a medical engineering company that uses a combination of digital scanning and 3D printing to manufacture prosthetics. The main product - the Hero Arm - is a fully functional, bespoke prosthetic arm but our users can also customise their devices with a wide range of cover choices that come in different colours and styles. The current website that we use to sell covers hasn't been updated since 2018 and the backend is difficult to edit for anyone without software development knowledge - as a result, the user experience when using the website is poor, the product range is out of date and our cover sales are low. I wanted to develop a website - _OB Covers_ - with an easy-to-use backend that would make it easier for our customer base to purchase additional covers and hopefully boost cover sales.

This was the final of four Milestone Projects required to pass the Full Stack Web Development Program at _Code Institute_. The main requirements were to build a full-stack site based around business logic to control a centrally-owned dataset using HTML, CSS, JavaScript, Python and Django.

Click **[here](https://github.com/zoet24/ob-covers)** to view the Github repository for the project, and click **[here](#)** to view the live website.

## Table of Contents

- [UX Design](#ux-design)
    - [Design Process](#design-process)
        - [Strategy Plane](#strategy-plane)
        - [Scope Plane](#scope-plane)
        - [Structure Plane](#structure-plane)
        - [Skeleton Plane](#skeleton-plane)
        - [Surface Plane](#surface-plane)
    - [Information Architecture](#information-architecture)
    - [Features](#features)
        - [Existing features](#existing-features)
        - [Defensive design features](#defensive-design-features)
        - [Features left to implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
    - [Languages and frameworks](#languages-and-frameworks)
    - [Additional tools used](#additional-tools-used)
- [Git Commit Messages](#git-commit-messages)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## UX Design
### Design Process
#### Strategy Plane

I started the design process for _OB Covers_ by considering the goals of the developer (me), the site owner (the sales team at Open Bionics) and the site users (our current customer base and prospective future customers) and categorised them into groups of functionality.

_General_

1. As the developer, I want to create a full-stack e-commerce platform where site users can browse and purchase products and where site owners can add, edit and delete products to complete the fourth Code Institute Milestone Project.
2. As the developer, I want the website to function well to demonstrate my ability to code in JavaScript, Python and Django and to create a positive UX experience for the site users.

_Aesthetic, Branding and UX_

3. As the developer, I want the website to be aesthetically pleasing and easy to use to demonstrate my ability to code in HTML and CSS and to create a positive UX experience for the site users.
4. As the site owner, I want the aesthetic of the website to match our existing brand to adhere to our established brand identity.
5. As the site owner, I want the site users to have a positive UX experience while browsing the product range to increase the likelihood of making a sale.
6. As the site owner, I want to be able to advertise new products or deals to our customer base to increase the likelihood of making a cover sale.
7. As the site owner, I want to promote our main product to increase the likelihood of making a Hero Arm sale.
8. As a site user, I want feedback when I successfully/unsuccessfully complete an action on the website.

_Registration and User Accounts_

9. As a site user, I want to be able to easily register for an account.
10. As a site user, I want to be able to easily log in and log out of my account.
11. As a site user, I want to be able to recover my password and log in details if I’ve forgotten them.
12. As a site user, I want to have a personalised profile page so I can save my delivery details and see what I have ordered in the past.
13. As a site user, I want to be able to easily report an issue with my product if it arrives damaged or if it breaks while I’m using it.
14. As a site user, I want to receive a confirmation email when I create a new account to confirm my details.

_Viewing and Navigation_

15. As the site owner, I want it to be easy for a site user to navigate to our main website in case they have come to OB Covers by mistake.
16. As a site user, I want to be able to view a list of products to select some to purchase.
17. As a site user, I want to be able to view specific product details (price, description, warranty) to inform my decision.
18. As a site user, I want to be able easily identify deals to take advantage of special savings.
19. As a site user, I want to be able to easily identify any "low stock" items so I can make my purchase before they run out.
20. As a site user, I want to be able to easily identify any "out of stock" items that I won’t be able to buy, so I don’t waste time trying to buy them.
21. As a site user, I want to be able to easily identify "newly added" products in case I am interested in purchasing them.
22. As a site user, I want to be able to view my selection of products and see how much they will cost to avoid spending too much.

_Sorting and Searching_

23. As a site user, I want to be able to customise my product to match my specific style.
24. As a site user, I want to be able sort products based on name, price, type, colour and brand.
25. As a site user, I want to be able to search for products based on name and description.

_Purchasing and Checkout_

26. As a site user, I want to be able to easily adjust the quantity of products from my shopping basket to reflect what I actually want to buy.
27. As a site user, I want to be able to save products that I might buy in the future but don’t want to buy immediately.
28. As a site user, I want to be able to easily enter my payment and delivery details so I can check out quickly with no hassle.
29. As a site user, I want to be confident that my payment information is safe and secure.
30. As a site user, I want to see an order confirmation after I pay to ensure I haven’t made any mistakes.
31. As a site user, I want to receive a confirmation email when I place an order to confirm my details.

_Admin_

32. As a site owner, I want to be able to add products when we add new designs to our product range.
33. As a site owner, I want to be able to edit products when our product range changes.
34. As a site owner, I want to be able to delete products when we remove them from our product range.
35. As a site owner, I want products to automatically update to "out of stock" if we don’t have any in our inventory to prevent customers from placing orders we can’t fulfill.
36. As a site owner, I want to be able to temporarily mark products as "new" when new products are added to our range.
37. As a site owner, I want to be able to temporarily mark products as "unavailable" if there is an issue with supply.

#### Scope Plane

I used my user stories to create a list of "must-have" features which I organised using the same categories as above. I also made a "nice-to-have" list of features that I could include after completing the MVP if I had time.

_**"Must-haves"**_

_Aesthetic, Branding and UX_

1. The site must be aesthetically pleasing across all platforms and create a positive UX experience for all users.
2. The aesthetic of the site must match the current branding of Open Bionics.
3. The site must have spaces to advertise new products, deals and promotions for the Hero Arm.
4. The site must provide the user with positive/negative feedback whenever they complete an action on the site (eg. add a product to their basket, sign up for a new account).

_Registration and User Accounts_

5. The site must allow users to create an account that they can log in and out of.
6. The site must confirm the details of the user's account in an email after they have registered, and allow them to recover their log in details in an email if they have forgotten them.
7. The user’s account must be personalised with their delivery details and order history.

_Viewing and Navigation_

8. The site must have clear navigation to the main Open Bionics page.
9. The site must have a variety of clearly displayed products for the user to look through, with additional details that are easily accessible.
10. It must be clear if these products are "low stock", "out of stock", "newly added" or in some sort of promotion.
11. The sum of the products in the user's shopping basket must be easily accessible.

_Sorting and Searching_

12. The site must allow users to sort products based on name, price, type, colour and brand.
13. The site must allow users to search for products based on name and description.

_Purchasing and Checkout_

14. The site must allow users to easily adjust and remove items from their shopping basket.
15. The site must allow users to save items for purchase at a later date.
16. The site must allow users to input their delivery and payment information easily and not create unnecessary hassle at the checkout.
17. The site must present the user with a confirmation of their order after they pay and send them details of their order in a confirmation email.

_Admin_

18. The site must allow admin users to add, edit and delete products and mark them as "newly added" or "unavailable".
19. The site must automatically mark products as "low stock" or "out of stock" depending on inventory availability.

_**"Nice-to-haves"**_

1. The user's account could be personalised with additional details (photos of them wearing the products that could be used to generate social media content, link to the Open Bionics App etc).
2. The site could allow users to report issues about their orders and Hero Arm.
3. The site could allow users to customise the colours of their covers (ie. instead of buying a full set of one colour, they could mix and match multiple colours).
4. The site could have a more advanced search filter for the products instead of the basic template shown on the Boutique Ado mini project.

#### Structure Plane

Based on the features outlined in my scope and the pages included in the Boutique Ado mini project, I decided I wanted to include the following pages on my website:

- The Home page welcomes the user to the site, presents the user with calls to action to explore the product range and has space for advertising deals, new products and the Hero Arm.
- There are five Products pages - "All Covers", "Classic", "Stylish", "Premium" and "Disney" - which show tiles of the products with name and price. Hovering over the product image allows you to add the product to your favourites or your shopping basket, and clicking on the product image takes you to the individual product page.
- Individual Product Detail pages show product image, name, price, colour options, delivery information and description with buttons to increase/decrease desired quantity of covers, add them to the shopping basket or save them as a favourite. The warranty information is also available on this page.
- The Log In and Sign Up pages allow the user to log in to/create their profile so they can access their personalised information.
- The Profile page has the user’s saved delivery information and order history.
- The Favourites and Shopping Basket pages are available across the site as a sidebar that expands when you click on the corresponding icon in the navbar. The Favourites sidebar has the user’s saved products with the option to add them to the basket, and a link to the main Open Bionics website. The Shopping basket sidebar has the user’s selected items with the option to increase/decrease the quantity, a drop down selection for delivery information, a total sum of the order cost, and a link to the main Open Bionics website.
- The Checkout page has a form for the user to enter their delivery information and a summary of their order on the right. When the user submits their order they are taken to an order confirmation page which shows them their order details and a link back to the main site.
- The Product Management page has a form that allows the admin user to add new products to the product range. The admin user can edit and remove products from the Product and Product Details pages.
- The navbar contains the Open Bionics logo which links to the Home page, a search bar which allows the user to search for products based on name and description, icons for the Profile page, Favourites sidebar and Shopping Basket sidebar and links to all of the Products pages.
- The site provides the user with feedback on their actions in the form of a message bubble at the top left of the screen - the message bubble will be formatted differently depending on the content of the message.

At this stage I added a "Customiser" page to my "nice-to-have" list - this would be a page where users can mix and match different colours of Classic covers. It was an unnecessary addition to include in the initial MVP, but I decided to be optimistic and include it in my wireframe mock-ups.

#### Skeleton Plane
I used Balsamiq to develop wireframes (click **[here](readme-wireframes.md)** to view all of them) of what I wanted my website to look like on mobile and desktop. I kept my scope at the forefront of this design process to make sure that there was going to be a place to put all of my key features.

![Wireframes - home page](media/notproducts/readme-home.png)

#### Surface Plane

### Information Architecture

### Features
#### Existing features

#### Defensive design features

#### Features left to implement

## Technologies used
### Languages and frameworks

### Additional tools used

## Git Commit Messages

## Testing
Click **[here](readme-testing.md)** to view the complete testing process.

## Deployment
vid#1
- go to heroku website, name app and choose region closest to you
- provision a new postgres database, use free plan
- go back to gitpod to install dj database url and psycopg2 (using pip3)
- freeze requirements.txt to ensure heroku installs all requirements on deployment
- import dj database to settings.py
- comment out default database settings and replace default with a call to dj database
- give it database url for heroku (command line heroku config/environment variables)
- connect to heroku database and run migrations
- import all product data by loading in categories, and then products
- give yourself a superuser to log in to the admin with
- before you commit changes, remove database url and un-comment out default to prevent url ending up in version control
vid#2
- set up if statement to connect to postgres/sql lite
- install gunicorn and freeze that into requirements
- create procfile to tell heroku to run app
- temporarily disable collect static
- add host name of heroku app to allowed hosts in settings.py
- add local host so app still works with gitpod too
- git push and git push heroku master to deploy to heroku
- set auto deploy - connect to github through heroku and connect to repository
- generate django secret key and add to config vars on heroku
- change settings.py to get new secret key from environment
- set debug to true only when in development defined in environment
- naviagte to heroku to check auto deployments are working
vid#3
- AWS account


## Credits

__Code:__
I used the following snippets of code for...

__Acknowledgements:__
I'd like to thank...