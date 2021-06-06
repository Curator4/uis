# June 2021 - UIS minSP Project
The main goal of this database implementation prototype is to demonstrate dynamically creating and showing plots from HbA1c tests on minSP.

## User stories:
PAT1:  As a patient, I can log in and log out of the system, so that myinformation in MinSP is only accessible to me.

PAT4:  As a patient, I can see results of previous test samples, so I cansee whether my condition is changing from test to test.

PAT5:  As a patient, I can see an overview of all of my previous tests with analytics, so I can see whether I am improving or deteriorating.

## Rules:  
Creating new accounts(patients) currently have little purpose as you can't add test results.

Use numbers for cpr-number

Passwords are not hashed, care

## Requirements:
Run the code below to install the necessary modules.

>$ pip install -r requirements.txt

## Database init
1. set the database in __init__.py file.
2. run schema.sql, schema_ins.sql in your database.

## To run
1. Install packages, see. 'requirements.txt'. (uses Matplotlib and mpld3)
1. Set up the database
2. Run 'main.py' 

## Issues
- Unsafe password storage, doesn't use Bcrypt to hash passwords (assume this is mandatory?)
- Doesn't use wtforms to gather data (necessary?)
- No feature to limit the amount of test results shown in plot (can be implemented if necessary)
- No in-app way to insert data into the test results table (can be implemented)
- Code breaks on irregular input (ie. string as cpr number)
