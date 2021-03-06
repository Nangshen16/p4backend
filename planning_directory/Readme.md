# Project Overview

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Priority Matrix / Timeline `backend`| complete
|Day 1| Create app and configure JWT | complete
|Day 2| Set up models | complete
|Day 3| Set up views | complete
|Day 3| Set up routes| complete
|Day 5| Test the endpoints/routes/CRUD | complete

## Project Description

This app is a simple tool for users to read the recipes at the same time they can purchase all the ingredients to make that recipes.
This app allows users to select recipes to cook and then this apps deliverys ingredients so the users don't need to think about it.
The front-end will be built using Vue.js and leverage the backend API.
Our users will cook and buy the ingredients for their selective recipes faster.
Users will be able to make an account and sign in. 
Users will be able to see their history of recipes.
In future features, users will be able to: 
- log in using social media accounts
- select dates 

## Description of Models
User
- username
- password
- has many recipes

Recipe
- title
- description
- cuisine
- has many ingredients

Ingredient
- title
- serving
- direction

## Time/Priority Matrix 

Full list of features that have been prioritized based on the [Time and Priority Matrix](https://res.cloudinary.com/dcrioc0sw/image/upload/v1600131383/Screen_Shot_2020-09-14_at_8.55.55_PM_xnn5rc.png)

### MVP/PostMVP

The functionality will then be divided into two separate lists: MPV and PostMVP.  Carefully decided what is placed into your MVP as the client will expect this functionality to be implemented upon project completion.  

#### MVP

- Authentication
- User model (username, password)
- Recipes model (ingredients )
- Ingredients model (title,directions,servings)
- Routes
- Allow user to choose favorite recipes
-  sign up

#### PostMVP 

- filter by recipes
- recipes history
-  description route/page


## Functional Components

Based on the initial logic defined in the previous sections try and breakdown the logic further into functional components, and by that we mean functions.  Try and capture what logic would need to be defined if the game was broken down into the following categories.

Time frames are also key in the development cycle.  You have limited time to code all phases of the game.  Your estimates can then be used to evalute game possibilities based on time needed and the actual time you have before game must be submitted. It's always best to pad the time by a few hours so that you account for the unknown so add and additional hour or two to each component to play it safe.

#### MVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Authentication | H | 1hr | -hr | -hr|
| User model | H | 1hr | -hr | -hr|
| Recipes model | H | 1hr | -hr | -hr|
| Ingredients model | H | 2hr| -hr | -hr |
|  View| M | 2hr | -hr | -hr|
| Routes | H | 5hrs| -hr | -hr |
| Sign up  | M | 1hr | -hr | -hr|
| Total | - | 15hrs| -hrs | -hrs |

#### PostMVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Filter | H | 2hr | -hr | -hr|
| history | M | 4hr | -hr | -hr|
|  description | M | 2hr | -hr | -hr|
|   login | M | 2hr | -hr | -hr|
| Total | - | 10hrs| -hrs | -hrs |

## Additional Libraries
 Use this section to list all supporting libraries and thier role in the project. 

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

```
function reverse(string) {
	// here is the code to reverse a string of text
}
```

## Issues and Resolutions
 Use this section to list of all major issues encountered and their resolution.

#### SAMPLE.....
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier                                
**RESOLUTION**: Missing comma after first object in sources {} object

## Previous Project Worksheet
 - 
