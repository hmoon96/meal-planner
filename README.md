# PYM - Plan Your Meals

PYM aims to provide a straightforward and intuitive solution, as it will allow individuals to plan and keep track of their meals for the week. This will allow individuals to reduce stress, save money and improve health.

![Website Mockup](docs/images/all-devices-black.png)

## Purpose
Life is busy. Many families struggle to stay organised and plan their meals effectively, potentially leading to increased stress, a more expensive food bill and a less nutritious diet.
In addition to the general stresses of day to day life, we are going through a cost of living crisis. The House of Commons reported in 2022/23 that around 11% of households live in food poverty. As such, it is more important than ever to start being more savvy with our money. This is where PYM comes in. Using PYM to help you plan your meals every week can help make your money go further and reduce your food waste. 

So, our purpose is simple - to help our users plan their meals, saving their time and money.

### Target Audience
Our primary target audience includes busy professionals, families, and anyone looking for help planning their weekly meals. This can be anyone that would benefit from saving time, money or both.

### Key Aims
**Simple and intuitive UX** - This will be straightforward to use from the get go, making meal planning easier, not adding more challenge.\
**User authentication** - Users will be able to login to their own accounts, meaning their meal plans are safe and saved to look back on. \
**CRUD functionality** - Users will be able to create, view, edit and delete their meal plans as they wish, making it fully adaptable.\
**Responsive design** - This will be responsive across all screen sizes, making it easy to edit your meal plan, no matter the device.\

## Minimum Viable Product
The MVP will include a meal planner, which will be in the form of a card. There will be the days of the week listed in the card and users will then be able to type the meals they are going to eat into each of these boxes. As users will be able to log in, they will have the opportunity to save, update and delete aspects of their planner, so it is always up to date. The meal plans will be listed from most recent at the top and be listed in reverse order, so the most recent plan will be most easily visible. The other plans will be listed below, so it is easy to scroll down and get inspiration from past meal plans.

### Key Features
**Homepage** \
The User first views the homepage. They can see the hero image and read the benefits of using our Meal Planner. From this page, the user can click on the buttons to create and view their meal plans directly.\
![Homepage screenshot](docs/images/screenshots/pym_homepage.png)

**Create your Meal Plan** \
When the User clicks the Create a Meal Plan button (either on the main page or the link on the Navbar), it takes them to this page. They can fill in the form and then click save at the bottom once complete. If any of the boxes are left blank, the page will redirect the user to the empty box for it to be filled in. The form will not submit if any box is empty.\
![Create your Meal Plan screenshot](docs/images/screenshots/pym_create.png) 

When all the boxes are filled in and the user clicks submit, they are redirected to the view page and a notification pops up.\
![Meal Plan created successfully screenshot](docs/images/screenshots/pym_create_notification.png)

**View your Meal Plans**\
When the User clicks the View Your Meal Plan button (either on the main page or the link on the Navbar), it takes them to this page.\ All of the meal plans are listed in reverse order, with the most recent being first. This is so the users can see this week's plan straight away, but they can scroll to look at older plans easily too, for meal inspiration. This enhances the User Experience.\ From here, users can update and delete individual meal plans with ease, further allowing us to meet our aim of building a simple and intuitive app.
![View your Meal Plan screenshot](docs/images/screenshots/pym_view.png) 

**Update your Meal Plan**\
When Users click the Update button next to the plan, they are taken to this page. They are then able to alter any box in the form as they see fit, as well as the date. \
![Update your Meal Plan screenshot](docs/images/screenshots/pym_update.png) 

When the user has updated the plan (all the boxes must still be filled in) and the user clicks submit, they are redirected to the view page and a notification pops up.\
![Meal Plan updated successfully screenshot](docs/images/screenshots/pym_update_notification.png) 

**Delete your Meal Plan**\
If a User wants to delete a plan, they must click on the delete button. This takes them to this page.\
![Delete your Meal Plan screenshot](docs/images/screenshots/pym_delete.png) 

If they click on the "No, take me home button", they are taken back to the view page. Nothing will have changed, their plan will still be there and no notification will display. \
If they click "Yes, Delete". The plan will be deleted from the view, they are redirected to the view page and a notification pops up.\
![Delete your Meal Plan screenshot](docs/images/screenshots/pym_delete_notification.png) 

## Other Features - Prioritisation
There are other features that I would like to include to enhance the user experience and make the app even more useful. I will list these in order of priority:
1) Ability to share and download the meal plan, to share with family members
2) Enhance the log in functionality, so multiple users can log into the same account
3) Meal library with recipes and ingredients
4) To do list which auto fills from the recipe, based on ingredients
5) Include a cost calculator which predicts the average cost of meals, to help with budgeting
6) Include calorie/nutitional information

## Planning

### User Stories and Agile Methodology

I have been using a Kanban board to ensure I work in an Agile way and meet the MVP on time. 

This Kanban Board includes the following 8 User Stories:
- User Story 1: As a user, I want to create a weekly meal plan so that I can stay organized and plan my meals effectively.
- User Story 2: As a user, I want to view my weekly meal plan so that I can see what meals I have planned for the week.
- User Story 3: As a user, I want to edit my weekly meal plan so that I can make changes to my planned meals.
- User Story 4: As a user, I want to delete a meal from my weekly meal plan so that I can remove meals I no longer want to include.
- User Story 5: As a user, I want to generate a shopping list based on my weekly meal plan so that I can easily buy the ingredients I need.
- User Story 6: As a user, I want to download the meal plan so that I can share it or print it out.
- User Story 7: As a user, I want to have multiple logins per account so that my family members can collaborate on the meal plan.
- User Story 8: As a user, I want to create meals and save them in a library so that I can easily add them to my meal plan.

The first four User Stories are the current features, which make up the MVP. The last four features are listed above as other features and were listed on the board as Should haves and Could haves. 

For each of the user stories, there are acceptance criteria and tasks, to really help me to focus and keep on track.

Link to the Canban Board: https://github.com/users/hmoon96/projects/10 

### Database Structure and relationships
**Models**
In my project, I used a PostgreSQL database to store User data. Within this database, I used two models:

#### User Model
The first is the User Model. This uses the Django Built in model to structure the user log in information.
- id (Primary Key, Default in Django model)
- Username (VarCharField, Unique)
- Email (EmailField)
- Password (VarCharField)

#### MealPlan Model 
The Meal Plan model is a custom model. It represents the Users Meal Plans. Each meal plan is associated with a user account (through the User Foreign Key). Only the meal plans that were created by the user are visable to that user, they cannot see anyone else's meal plans. When a User is deleted, all of their meal plans are deleted too. 
| Field | Value | Purpose |
|-------|-------|---------|
| User | models.ForeignKey | This connects the User account to the individual meal plans | 
| Week | models.DateField() | This allows the User to open the calendar and select the date for the meal plan to start. This helps with the structure of the meal plans on the View Meal Plans page |
| monday_food | models.TextField() | Users can write their food for this day in the box, which will then be saved to the plan |
| tuesday_food | models.TextField() | Users can write their food for this day in the box, which will then be saved to the plan |
| wednesday_food | models.TextField() | Users can write their food for this day in the box, which will then be saved to the plan |
| thursday_food | models.TextField() | Users can write their food for this day in the box, which will then be saved to the plan |
| friday_food | models.TextField() | Users can write their food for this day in the box, which will then be saved to the plan |
| saturday_food | models.TextField() | Users can write their food for this day in the box, which will then be saved to the plan |
| sunday_food | models.TextField() | Users can write their food for this day in the box, which will then be saved to the plan |

#### Database model diagram
Please find below the database model diagram. I have made some changes to the model as I developed, such as removing the created at and updated on timestamps. This is because I didn't believe that they really served a purpose or added to the UX. 

![Database Model Diagram](docs/images/database_diagram.png)

### User Flow Diagram
Below is my User Flow Diagram. This is a simple structure, which aims to fulfill the purpose of being a simple and intuative app. Although there have been some changes to the flow throughout the development process, the core of this structure has remained the same. Users cannot perform any of the CRUD functions without logging it, as the meal plans need to be linked to a user in the database. 

![User Flow Diagram](docs/images/flowchart.jpg)

## UX Design 
### Wireframes 
This is how I designed the landing page. I wanted it to have a simple and clean design, which is intuitive for users. I decided to have a hero image, to add a vibrancy to the app from the get go, then include a little bit of information about the purpose of the app below. I also made the nav bar and buttons clear, so the users can easily log in, log out, sign up, create and view plans from the home screen.
![Landing Page](docs/images/landing_page.png)

The Mobile, Tablet and Laptop views of the viewing screen were designed as a table. The idea behind this was that it would be easier for the user to read which meals were for which day. However, as my design evolved, I decided to change this layout to a Bootstrap card. This is because it was easier to make this responsive across all screen sizes, therefore a better User Experience overall. From this page, users can update and delete their plans, completing the CRUD functionality designed.

![Mobile Planner View](docs/images/mobile_planner_view.png) /

![Tablet Planner View copy](docs/images/tablet_planner_view.png) /

![Laptop Planner View ](docs/images/laptop_planner_view.png) /

### Fonts
As the target audience are families and individuals who need help with organising their meals, I wanted to make sure that the fonts chosen were selected carefully to appeal to this audience. 

The font for the H1 elements is Dancing Script. This is a handwritten, cursive font which is friendly and elegant, whilst being easy to read.

The font for the body of the site was Poppins. This is a modern sans-serif font, making it very easy to read. It still adds to the friendly, supportive feel of the site. 

### Colours
The colours were also chosen to evoke calmness for the User, and convey friendliness. 
- The background is a very light shade of green, to add a freshness to the site but maintain the readability, without using white.
- The navbar is a different, darker shade of light, sage green. This keeps a calm, fresh and friendly feel.
- The buttons continued with the green theme, this time with a dark forest type of green. This maintains the colour scheme but adding matching accents.
- The text colour is a dark grey, so that the readability was optimum without using a harsh black.
- The secondary colour chosen was a darker lavendar purple. This is a gentle colour which pairs well with the sage green and adds a classy, calming touch to the app.

## Responsiveness
Using Chrome DevTools, I have been able to screenshot how my app is responsive across multiple screensizes.

iPhone 12 Pro:

![Home on Mobile](docs/images/screenshots/responsivness_mobile_home.png) ![Create page on Mobile](docs/images/screenshots/responsivness_mobile_create.png) 
![View Meal Plans on Mobile](docs/images/screenshots/responsivness_mobile_view.png) ![Update Meal Plans on Mobile](docs/images/screenshots/responsivness_mobile_update.png) 
![Delete page on Mobile](docs/images/screenshots/responsivness_mobile_delete.png) 

iPad Pro:

![Home on Tablet](docs/images/screenshots/responsivness_tablet_home.png) ![Create page on Tablet](docs/images/screenshots/responsivness_tablet_create.png) 
![View Meal Plans on Tablet](docs/images/screenshots/responsivness_tablet_view.png) ![Update Meal Plans on Tablet](docs/images/screenshots/responsivness_tablet_update.png) 
![Delete page on Tablet](docs/images/screenshots/responsivness_tablet_delete.png) 

Laptop:

![Homepage screenshot](docs/images/screenshots/pym_homepage.png)
![Create your Meal Plan screenshot](docs/images/screenshots/pym_create.png) 
![View your Meal Plan screenshot](docs/images/screenshots/pym_view.png) 
![Update your Meal Plan screenshot](docs/images/screenshots/pym_update.png) 
![Delete your Meal Plan screenshot](docs/images/screenshots/pym_delete.png) 


## Manual Testing
| Page |     Feature     |            Action            |                     Effect               |
|------|-----------------|------------------------------|------------------------------------------|
|Homepage | Create New Meal Plan Button | Click | Takes the user to the create a meal plan page If not logged in, it takes users to the sign in page.|
|Homepage | View New Meal Plan Button | Click | Takes the user to the view your meal plans page. If not logged in, it takes users to the sign in page. |
|Navbar | Site initials (PYM) | Click | Sends the user to the homepage from all other pages. |
|Navbar | Create | Click | Takes the user to the create a meal plan page If not logged in, it takes users to the sign in page.|
|Navbar | Home | Click | Sends the user to the homepage from all other pages. |
|Navbar | View | Click | Takes the user to the view your meal plans page. If not logged in, it takes users to the sign in page. |
|Navbar | Sign Up | Click | Takes the user to the sign up page to make an account. |
|Navbar | Sign In | Click | Takes the user to the sign in page to sign into their account. |
|Sign In Page | Sign up link | Click | Takes the user to the sign up page if they don’t have an account. |
|Sign In Page | Username Validation | Enter incorrect username | Error message “The username and/or password you specified are not correct”. |
|Sign In Page | Password Validation | Enter incorrect password | Error message “The username and/or password you specified are not correct”. |
|Sign In Page | Remember Me  | Tick box | Keeps the user signed in. |
|Sign In Page | Sign In Button | Click | Signs the user in and redirects to the home page. A success message pops up. |
|Sign Out Page | Sign Out Button | Click | Signs the user out and redirects the user to the homepage. A success message pops up. |
|Sign Out Page | Cancel Button | Click | Leaves the user signed in and redirects to the homepage. |
|Sign Up Page | Username Validation | Typed Username that exists | Error message “A user with that username already exists” - account not created. |
|Sign Up Page | Password Validation | Typed password that doesn’t match the requirements | Error message that informs the user the exact issue with the password and doesn’t create the account. |
|Sign Up Page | Password Validation | Typed two passwords that didn’t match | Error message “You must type the same password each time” and the account isn’t created.|
Sign Up Page | Sign In | Click | This takes the user to the sign in page if they have an account already. |
Sign Up Page | Sign up button | Click | When all of the fields are filled in correctly, it creates the account, logs the user in and redirects the user to the home page. A success notification is shown. |
Create Meal Plan Page | Week box | Select date from calendar | This sets the date for the meal plan, which is displayed in the View Meal Plan page. |
Create Meal Plan Page | Week box | No date selected | The form doesn’t submit and skips back to the right section, so the user can select a date. |
Create Meal Plan Page | Food boxes | Text in all boxes | Text is shown in the View Meal Plan Page |
Create Meal Plan Page | Food boxes | Any text box empty | The form doesn’t submit and skips back to the right section, so the user can fill out the box. |
Create Meal Plan Page | Save | Click | Meal plan created and the user is redirected to the View Meal plans page, where they can see their plan. Success notification displayed. |
View Meal Plan Page | Create New Meal Plan Button | Click | Takes the user to the Create a Meal Plan page. |
View Meal Plan Page | Update | Click | Takes the user to the Update your Meal Plan page for that specific plan. |
View Meal Plan Page | Delete | Click | Takes the user to the Delete page. |
Update Meal Plan Page | Save | Click | Saves any changes that have been made. Redirects the user back to the view page and the changes are displayed. Success message is shown. |
Delete Meal Plan Page | Yes, Delete | Click | Deletes the plan. Redirects the user back to the view page and the plan will be gone. Success message is shown. |
Delete Meal Plan Page | No, Take Me Home | Click | Takes the user back to the view page. The plan will not be deleted and the view will remain unchanged. |


## Lighthouse
I generated Lighthouse reports for my app. The results are below: 

### Laptop 
- Home
  
![Lighthouse Score - Homepage](docs/images/screenshots/home.html_desktop_lighthouse.png)

- Create

![Lighthouse Score - Create page](docs/images/screenshots/create.html_desktop_lighthouse.png)

- View

![Lighthouse Score - View Meal Plans Page](docs/images/screenshots/view.html_desktop_lighthouse.png)

- Update

![Lighthouse Score - Update page](docs/images/screenshots/update.html_desktop_lighthouse.png)

- Delete

![Lighthouse Score - Delete page](docs/images/screenshots/delete.html_desktop_lighthouse.png)


### Mobile 
- Home
  
![Lighthouse Score - Homepage](docs/images/screenshots/home.html_mobile_lighthouse.png)

- Create

![Lighthouse Score - Create page](docs/images/screenshots/create.html_mobile_lighthouse.png)

- View

![Lighthouse Score - View Meal Plans Page](docs/images/screenshots/view.html_mobile_lighthouse.png)

- Update

![Lighthouse Score - Update page](docs/images/screenshots/update.html_mobile_lighthouse.png)

- Delete

![Lighthouse Score - Delete page](docs/images/screenshots/delete.html_mobile_lighthouse.png)

### To note
Although the Best Practice, Accessibility and SEO scores were consistently 100 throughout testing, the performance score seemed to differ. This depended on whether I was testing the performance on a mobile or a laptop. The laptop score is higher than the mobile, with scores or 98 and 99 across the board. The mobile score has been as low as 85 and as high as 93, depending on the time of testing and the page being tested.


## Code Validation
### HTML
| HTML Doc | Passed Validation? (No Errors) | Any warnings? |
|----------|--------------------------------|---------------|
| home.html | Yes, no errors | Two |
| create.html | Yes, no errors | No |
| view.html (when there are no meal plans to view) | Yes, no errors | No |
| view.html (when there are three meal plans to view) | Yes, no errors | No |
| update.html | Yes, no errors | No |
| delete.html | Yes, no errors | No |

All files were validated using https://validator.w3.org/ 

Here are the screenshots of the home.html page, to show the warnings:

![image](https://github.com/user-attachments/assets/e1a2fc3b-699d-40f8-ae17-3182037731b1)

![image](https://github.com/user-attachments/assets/27e57f3b-af15-4f4d-9c5d-b9279d77dbc4)

I haven't included the screenshots of the others, as there were no errors or warnings to show. 

### CSS
I checked the only CSS file for the project (style.css) and there were no errors. I used https://jigsaw.w3.org/css-validator/

![image](https://github.com/user-attachments/assets/b566cd50-3185-4c38-ac51-102009370b66)


### Python
All of the PY files were tested twice. Throughout the process with the Flake8 extension in VS Code and at the end, with the Code Institute Linter - https://pep8ci.herokuapp.com/#
I tried to format the py files, so that they were compliant with the formatting guidelines. As such, I saved all of the files with a new line, then added, commited and pushed. However, the new line that I added disappeared again. When I look at the code in my VSCode, the extra line is there, but when I deploy, it disappears.

Here is an example of what happens when I copy the code from my Github into the Linter:

![image](https://github.com/user-attachments/assets/21720603-a444-4aa0-a121-da94f233074e)


But this is what it looks like in VS Code:
![image](https://github.com/user-attachments/assets/cdc1d985-deef-4954-8a6c-a19b72e32d65)


## AI
I have used both CoPilot and ChatGPT throughout this project. It has been a great tool, to help me to troubleshoot and give me advice. I've included a cummary below of how AI has supported me throughout the project.

### 🎯 **Code Creation**
- **CRUD Functionality:**  
   - Helped me to set up `CreateMeal`, `UpdateMeal`, and `DeleteMeal` views in Django with appropriate form handling and validation.  
   - Linked CRUD views to templates with proper use of `{% url %}` and ensured seamless navigation.  

- **Navbar and Links:**  
   - Created a dynamic navbar to display different links (`Login`, `Register`, `Logout`) based on user authentication status.  

- **Static Files Setup:**  
   - Assisted in configuring and linking CSS, JS, and image files correctly using `{% static %}` in Django templates.  

- **Hero Section and Homepage Layout:**  
   - Designed a clean and professional hero section with appropriate colors, fonts, and call-to-action buttons.  
   - Provided layout suggestions to keep the homepage simple and approachable.  

- **Favicon and Logo Integration:**  
   - Provided guidance on incorporating a favicon and generated multiple logo iterations to reflect your app’s purpose.  

- **Footer Implementation:**  
   - Created a sticky footer using Bootstrap's flexbox utilities (`d-flex`, `flex-column`, `mt-auto`) to maintain consistent positioning.  

---

### 🐛 **Debugging**
- **NoReverseMatch Error Fix:**  
   - Diagnosed and resolved `NoReverseMatch` errors by checking URL names and ensuring proper view connections.  

- **Static Files Not Loading:**  
   - Debugged and fixed issues with CSS/JS files not loading by configuring `STATIC_URL` and `STATICFILES_DIRS` correctly.  

- **Image and Asset Issues:**  
   - Resolved issues related to displaying images and verifying correct paths in templates.  

- **Form Error Messages:**  
   - Ensured that form error messages were displayed correctly and guided you through debugging `form.errors` and `form.non_field_errors`.  

- **Footer Overlapping Content:**  
   - Fixed the footer positioning issue by adjusting layout and applying flexbox utilities.  

---

### 🎨 **Code Optimization for UX**
- **UI/UX Enhancements:**  
   - Suggested a pastel color palette (soft sage, lavender, and complementary colors) that is accessible and aligns with the app’s family-friendly theme.  
   - Recommended and applied appropriate fonts (`Poppins` and `Dancing Script`) to ensure readability and aesthetic consistency.  

- **Responsive Design:**  
   - Ensured that the app is responsive across all screen sizes using Bootstrap's grid system and suggested which utility classes worked best.  

- **Navigation and Page Flow:**  
   - Recommended easy-to-navigate links for CRUD actions and designed a clean page flow to improve user interaction.  

- **Error Highlighting and Feedback:**  
   - Implemented error highlighting for form fields using Bootstrap’s `is-invalid` class and ensured success/error messages were displayed clearly.  

- **Meal Plan Layout and Button Styling:**  
   - Enhanced the layout of the **View Meal Plan** page by displaying meal plans in a card-based format with consistent button styling.  

---

### 👩‍💻 **Role in Development Process**
- **Mentor/Technical Advisor:**  
   - Provided step-by-step guidance on implementing CRUD functionality and fixing errors, while explaining concepts clearly.  
   - Ensured that your app followed Django best practices to maintain scalability and maintainability.  

- **UI/UX Consultant:**  
   - Assisted with refining the app’s color scheme, fonts, and design aesthetics to ensure a clean and approachable interface.  
   - Provided visual assets (the hero image) to enhance your branding and improve the overall user experience.  

- **Collaborative Debugging Partner:**  
   - Diagnosed issues quickly and guided you through debugging with detailed explanations and solutions.  

---

## Deployment and how to deploy

The project is currently deployed on Heroku, you can find it by following the link below:
- https://hmoon96-meal-planner-9c8cfb97430e.herokuapp.com/

### **Cloning and Setting Up Locally**
Follow these steps to clone the repository and set it up on your local machine:

1. **Clone the Repository**:
   - Open your terminal and run:
     ```bash
     git clone https://github.com/hmoon96/meal-planner.git
     cd meal-planner
     ```

2. **Set Up a Virtual Environment**:
   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

3. **Install Dependencies**:
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory and add the following:
     ```env
     SECRET_KEY=your-secret-key
     DATABASE_URL=sqlite:///db.sqlite3  # Or your database URL
     DEBUG=True
     ```

5. **Run Migrations**:
   - Apply database migrations:
     ```bash
     python manage.py migrate
     ```

6. **Run the Development Server**:
   - Start the Django development server:
     ```bash
     python manage.py runserver
     ```

7. **Access the App**:
   - Open your browser and go to:
     ```
     http://127.0.0.1:8000/
     ```

Your app is now running locally!

## Technologies Used
### Backend
- **Python**: Programming language used for the backend.
- **Django**: Web framework for building the application.
  - `django.shortcuts`: Helper functions for views.
  - `django.contrib.auth.decorators`: Used for authentication and access control.
  - `django.contrib.messages`: Framework for displaying notifications.
  - `django.db.models`: ORM for database management.
- **PostgreSQL**: Database used for development.

### Frontend
- **HTML5**: For structuring the templates.
- **CSS3**: For custom styling.
- **Bootstrap**: CSS framework for responsive design and styling.

### Tools
- **Visual Studio Code (VS Code)**: IDE used for development.
- **Django Development Server**: For testing the application locally.
- **Chrome Developer Tools**: For debugging frontend issues.

### Additional Libraries
- **Font Awesome**: For adding icons to the application.

### Other Resources
https://commonslibrary.parliament.uk/research-briefings/cbp-9209/
- **Heroku** - Used to deploy the project (https://www.heroku.com/)
- **Db Diagram** - Used to create my database diagram (https://dbdiagram.io/home/)
- **Miro** - Used to create my User Flow Diagram (https://miro.com/templates/user-flow/)
- **Google Fonts** - Used to find and import my correct fonts 
- **Coolors.co** - Used to help find colours and decide my colour scheme
- **Cloudinary** - Used to store my hero image for deployment
- **Git** - Used for Version Control via GitHub.
- **Github** - Used to store my project. GitHub project board allowed me to work in an Agile way through the creation of my Kanban board. 
- **Flake8** - VS Code extension used for inbuilt Linting support when developing my Python Code.
- https://ccbv.co.uk/projects/Django/5.0/ - Used for help developing Django code and troubleshooting issues.
- https://docs.djangoproject.com/ - Used for help developing Django code and troubleshooting issues.
- https://websitemockupgenerator.com/ - Used to create my Website Mock Up for the README.
- The Code Institute LMS - I used the 'I think therefore I blog' walkthrough project, as well as other areas, to recap certain skills.

## Credits
Thank you to Code Institute, for helping me come on in leaps and bounds in such a short space of time.
Thanks especially to my three tutors, for your help and guidance throughout:
- My Facilitator, Alexander
- My Coding Coach, John
- My SME tutor, Kevin
Finally, a huge thank you to my entire bootcamp cohort. Your support, advice and help have been vital to me in this process.

