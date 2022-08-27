<h1 align=center>Welcome to Mötör-Werks<br>Portfolio Project 5</h1>

<p align=center><img src="static/assets/images/mw-logo.png"><br>
Mötör-Werks is a mobile vehicle repairs and servicing e commerce website.<br>
Take the stress out of vehicle servicing and repairs with our simple revolutionary 5 tier system.</p>
<br>
<h1 align=center></h1>

## FINAL DESIGN
<br>
<img src="static/assets/images/README-images/amiresponsive.png">

#
[Here is a link to the final project](https://motor-werks.herokuapp.com/)
#

## User Experience

### User Stories

<!-- TO DO -->
#
### 1. Strategy

  + **Project Goal**

   Create a platform that allows people (users) to Login and purchase (via [Stripe.com](https://stripe.com/gb)) a Service or Repair for their vehicle.

### 2. Scope

 * A simple, straightforward, intuitive UX experience
 * An explicit content
 * An easy navigation for the user through all of the features
 * A site that is visually appealing on most devices

## Functional Scope

**Motor-werks Flowchart**
<!-- TO DO -->

<details>
<summary>Flowchart</summary>
<br>

![Motor-werks Flowchart](static/assets/img/)
</details>
<br>


**Agile Methodology**

All functionality and development of this project were managed using **Trello** (https://trello.com/b/Ha79yDqn/motor-werks-pp5)

* Credentials to this tool will be provided during submission

### 3. Structure

* A clear and straightforward layout is in place to ensure users can navigate intuitively and have a leisurely experience
* Navbar is fixed on top to facilitate users to navigate through pages easily
* A Small dropdown menu navigation is the same on all pages at small screen sizes to ensure easy navigation
* Create account, Edit/Update profiles are straight forward forms to allow users to use the features without issues


### 4. Skeleton
<!-- TO DO -->
* Wireframes created with Balsamiq. <br>
* The project was developed from initial wireframes, and some modifications were made during the development process in response to user feedback


<details>
<summary>Click to see wireframes:</summary>
<br>

[Home](static/assets/images/README-images/wireframes/Desktop-Home.png) <br>
[Services](static/assets/images/README-images/wireframes/Desktop-services.png) <br>
[Single service](static/assets/images/README-images/wireframes/Desktop-individual-service.png) <br>
[Register](static/assets/images/README-images/wireframes/Desktop-signup.png) <br>
[Login](static/assets/images/README-images/wireframes/Desktop-login.png) <br>
[Home mobile](static/assets/images/README-images/wireframes/Mobile-home.png) <br>
[Services mobile](static/assets/images/README-images/wireframes/Mobile-services.png) <br>
[Single service mobile](static/assets/images/README-images/wireframes/Mobile-individual-services.png) <br>
[Register mobile](static/assets/images/README-images/wireframes/Mobile-Signup.png) <br>
[Login mobile](static/assets/images/README-images/wireframes/Mobile-Login.png) <br>

</details>
<br>


### 5. Surface

* Colours

- I used [Coolors](https://coolors.co/) to randomly generate a colour palette for this project.<br>
I went bold and arguably opposite colours for this project.
The main colours are Light and dark purple with light green accents and text.
<details>
<summary>Click to see Colours:</summary>
<br>

![Main colours](static/assets/images/README-images/Colour-palette-Motor-Werks.png)<br>

</details>
<br>

**Font Selection**
 
Two fonts were chosen with [Google Fonts](https://fonts.google.com/) to be used across the entire site.

The chosen fonts were 'Uchen', with serif as back up fonts for lists, forms, buttons and paragraphs.
<details>
<summary>Click to see Font style:</summary>
<br>

![Main colours](static/assets/images/README-images/uchen-font.png)<br>

</details>
<br>

#
## Existing Features


<!-- To do -->
#
## Future Features

<!--  TO DO -->

#
## Languages Used

<img width="200" height="150" src="static/assets/images/README-images/python3.png"><img width="200" height="150" src="static/assets/images/README-images/html5.png"><img width="200" height="150" src="static/assets/images/README-images/css3.png"><img width="200" height="150" src="static/assets/images/README-images/js.png">

## Frameworks, Libraries & Programs Used

+ Django 3.2: Framework used to add structure to the platform
+ Bootstrap: Framework used to add structure and responsiveness
+ Favicon Generator: Used to create favicon used on the website
+ GitHub: GitHub respository is used to store the project's code after being pushed from Gitpod
+ Google Fonts: Google fonts are used to add fonts for aesthetic and UX purposes
+ Balsamiq: Balsamiq was used to create the wireframes during the design process
+ Git: Gitpod IDE was used for version control by utilizing the Gitpod terminal to commit and Push to GitHub
+ Grammarly: Used to correct any spelling mistakes on readme and app text
+ AmIResponsive: Used to generate mockup image

## Testing and Code validation
<!-- TO DO -->
All testing and code validation details are described in a separate file [TESTING.md](TESTING.md)

## Deployment

Motor-werks is deployed using Heroku

<details>
<summary>Heroku Deployment steps: </summary>

 1. Ensure all dependencies are listed within the requirements.txt file

 Within the terminal in Gitpod type `pip3 --local freeze > requirements.txt`, and a list with all requirements will be created to be read by Heroku.

 2. Setting up Heroku
      
    2.1 Navigate to the [Heroku](https://www.heroku.com/) website

    2.2 Login to Heroku
    
    <img width="300" src="static/assets/images/README-images/herokulogin.png">

    2.3 Click on `New` (top right) and Create a new app
    
    <img width="300" src="static/assets/images/README-images/herokunewapp.png">
    
    2.4 Choose a project name and set your location
    
    <img width="400" src="static/assets/images/README-images/herokucreateapp.png">

    2.5. Navigate to the `Resources` tab

    <img width="700" src="static/assets/images/README-images/herokuresourcestab.png">

    2.6. In the `Add ons` section, search for Heroku Postgres and select it on the list
      - A pop up will appear, select, 'Hobby Dev' and click `Submit order form`
    
    <img width="700" src="static/assets/images/README-images/herokupostgres.png">
    
    2.7. Next, navigate to the `deploy` tab;
      - Click on connect to Github
      - Search for the repository named `Motor-werks`
      - And connect heroku to Github.<br>
        
    2.8. Navigate to the settings tab
    
    2.9.  Click on Config Vars, add Database URL (from Heroku-Postgres) and Secret key,
      - Add relevent secret keys and environment variables

</details>

<details>
<summary>Forking the GitHub Repository </summary>

* By forking the GitHub Repository, you will be able to make a copy of the original repository on your own GitHub account, allowing you to view and/or make changes without affecting the original repository by using the following steps:

    - Log in to your own GitHub and locate the GitHub Repository you wish to fork
    - At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button.
    - You should now have a copy of the original repository in your GitHub account

* Making a Local Clone

    - Log in to your own GitHub and locate the GitHub Repository
    - Under the repository name, click "Clone or download"
    - To clone the repository using HTTPS, under "Clone with HTTPS", copy the link
    - Open Git Bash
    - Change the current working directory to the location where you want the cloned directory to be made
    - Type git clone, and then paste the URL you copied in Step 3

 $ git clone https://github.com/Chr15w1986/Motor-Werks

Press Enter. Your local clone will be created

</details>


## Credits and references

### Images

* All images have been compressed using [tinypng.com](https://tinypng.com/)

* Main home screen image of an audi R8 in the dark, [wallpaperflare.com](https://www.wallpaperflare.com/audi-r8-v8-2014-audi-r8-coupe-car-wallpaper-bhfta)
* Image of two chicks doing a burnout in a toy R8 for the error handler pages (bit of comedy.), [wallpaperflare.com](https://www.wallpaperflare.com/cars-chickens-chicks-chickens-audi-r8-burnout-sports-cars-audi-r8-v8-technology-vehicles-hd-art-wallpaper-sfbhn)
* Motor-werks logo, [squarespace.com](https://static1.squarespace.com/static/5d3f253d3bb01d0001087e06/t/5d3f2734701cda00012936e4/1644943519357/)
* Tool to remove the Motor-werks background to create transparent logo, [remove.bg](https://www.remove.bg/)
* Background image of scratched/worn (border/surround), [pngwing.com](https://www.pngwing.com/en/free-png-bzkyg)


## Acknowledgements
<!-- TO DO -->

<!-- ISSUES -->
white on white text apple iphone 11pro, XR and 13, fixed by setting text input colour to #000 black

future implementation, allow users to purchase more than 1 item at a time