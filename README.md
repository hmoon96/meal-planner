# PYM - Plan Your Meals
A resource to help busy families save time and money.

## Key Features
**Simple and intuitive UX** - This will be straightforward to use from the get go, making meal planning easier, not adding more challenge.\
**User authentication** - Users will be able to login to their own accounts, meaning their meal plans are safe and saved to look back on. \
**CRUD functionality** - Users will be able to create, view, edit and delete their meal plans as they wish, making it fully adaptable.\
**Multiple users per account** - Allowing multiple users to be able to access one account makes this app much more user friendly for families. This creates a centralised space for collaboration, making the meal planning process efficient and adaptable to all families.\ 
**Responsive design** - This will be responsive across all screen sizes, making it easy to edit your meal plan, no matter the device.\

## Our Why
**Draft**
Life is busy. Many families struggle to stay organised and plan their meals effectively, potentially leading to increased stress, a more expensive food bill and a less nutritious diet.
In addition to the general stresses of day to day life, we are going through a cost of living crisis. The House of Commons reported in 2022/23 that around 11% of households live in food poverty. As such, it is more important than ever to start being more savvy with our money. This is where PYM comes in. Using PYM to help you plan your meals every week can help you can help make your money go further and reduce your food waste. 

### Purpose
**Draft**
Our purpose is simple - to help our users plan their meals, saving their time and money.

My meal planning app aims to provide a straightforward and intuitive solution, as it will allow individuals to plan and keep track of their meals for the week. This will allow individuals to reduce stress, save money and improve health.

### Target Audience
**Draft** My primary target audience includes busy professionals, families, and anyone looking for help planning their weekly meals. This can be anyone that would benefot from saving time, money or both.

## Minimum Viable Product
The MVP will include a meal planner, which will be in the form of a table. There will be the days of the week across the top, and Breakfast, Lunch and Dinner down the side. Users will then be able to type the meals they are going to eat into each of these boxes. As users will be able to log in, they will have the opportunity to save, update and delete aspects of their planner, so it is always up to date. 

## Other Features - Prioritisation
There are other features that I would like to include to enhance the user experience and make the app even more useful. I will list these in order of priority:
1) Ability to share and download the meal plan, to share with family members
2) Enhance the log in functionality, so multiple users can log into the same account
3) Meal library with recipes and ingredients
4) To do list which auto fills from the recipe, based on ingredients
5) Include a cost calculator which predicts the average cost of meals, to help with budgeting
6) Include calorie/nutitional information


## Database Structure and relationships
Models
![image](https://github.com/user-attachments/assets/144720bf-992d-4460-be49-d8541c1e8a59)



## User Flow Diagram
Paste diagram and explain
![image](https://github.com/user-attachments/assets/ce7145b7-25b5-4f1a-aba3-96881aae28a5)


## User Stories
Examples

## UI 
Wireframes and theory behind the design



**AI**
I have used CoPilot and Chat GPT on a number of occasions to help me to:
1) Develop my user stories, acceptance criteria and tasks.
2) Develop my code, to implement the CRUD

1. Navbar and Links
Issue: Your navbar links were not working correctly.
Solution:
Ensured the base.html template used {% url %} tags with correct URL names matching those in urls.py.
Added conditional logic in the navbar to show "Login," "Register," or "Logout" links based on the user's authentication status.
2. Restricting Access to Meal Plans
Issue: Users could view, edit, or delete meal plans that didn't belong to them.
Solution:
Updated views (MealView, CreateMeal, UpdateMeal, DeleteMeal) to filter meal plans by the logged-in user using request.user.
Used get_object_or_404 with user=request.user to ensure only the owner of a meal plan could access it.
Applied the @login_required decorator to restrict access to authenticated users.
3. Removing the user Dropdown in the Meal Plan Form
Issue: The user field appeared as a dropdown in the meal plan creation form.
Solution:
Excluded the user field in the MealPlanForm.
Set the user field programmatically in the CreateMeal view using meal_plan.user = request.user.
4. Displaying Meal Plans in a Table
Issue: Meal plans were not displayed in a structured format.
Solution:
Updated the view.html template to display meal plans in a Bootstrap-styled table.
Added an "Actions" column with "Update" and "Delete" buttons for each meal plan.
5. Fixing the Week Field in Meal Plans
Issue: The week field was not displaying correctly in the view.html template.
Solution:
Ensured the week field was accessed inside the {% for meal_plan in meal_plans %} loop.
Provided options to display the week for each meal plan or just the first meal plan.
6. CSS Not Being Applied
Issue: Your custom CSS was not being applied to the project.
Solution:
Verified the STATIC_URL and STATICFILES_DIRS settings in settings.py.
Ensured the CSS file was correctly linked in base.html using {% static %}.
Checked the directory structure to confirm the CSS file was in the css folder.
Suggested clearing the browser cache and using developer tools to debug.
7. Styling the Project
Issue: You wanted to apply consistent styling to the project.
Solution:
Helped define CSS variables in the :root selector for colors and fonts.
Styled headings, the navbar, and buttons using the defined variables.
Ensured the @import rule for Google Fonts was correctly placed at the top of the CSS file.
8. General Debugging and Best Practices
Issue: Various errors and inconsistencies in views, templates, and CSS.
Solution:
Debugged issues like "media query expected" and missing semicolons in CSS.
Ensured proper use of Django's template inheritance system with {% block content %}.
Suggested using get_object_or_404 for secure access to objects in views.


Other resources I have used in this project:
- https://dbdiagram.io/home/
- https://miro.com/templates/user-flow/
- Google Fonts
- Coolors.co
- Cloudinary
- Heroku
- https://ccbv.co.uk/projects/Django/5.0/




Other links
https://commonslibrary.parliament.uk/research-briefings/cbp-9209/
