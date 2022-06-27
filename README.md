# swe_fundamentals

My basic database-like application for my Software Engineering Fundamentals Assignment.

## PURPOSE

This application has been created to log Projects used by the team and record information regarding who worked on it. This is so that a team member who is new to a project can find a little more information about it.

## BASIC USAGE:

CREATE A NEW PROJECT
Input the following fields; name, version, description, start date, last modified, languages, contributors, link to the repository

REMOVE PROJECTS
Delete a project that has been abandoned/no longer needs to be recorded

UPDATE PROJECTS
Edit an existing project
PLEASE NOTE: When changing values for 'Languages Used' or 'Contributors', please enter all new values in one entry. Values should be separated by a comma. (I'm aware this changes the type from a list to a string and adding a comma would break it being read as a CSV again, but that's on the never ending TODO list)

DISPLAY PROJECTS
Print the Projects currently contained within the Project Manager
