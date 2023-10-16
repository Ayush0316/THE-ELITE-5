###### PROJECT OVERVIEW

### The "H1B Data Analysis using Django" project is a comprehensive data analysis and web application built with Django, a popular Python web framework. This project is designed to perform in-depth analysis on H1B visa application data for the years 2016 to 2019. H1B visas are non-immigrant visas that allow U.S. employers to temporarily employ foreign workers in specialized occupations.

Within the project, a robust Django-powered API is constructed, presenting endpoints for various functionalities associated with the H1B data. These functionalities encompass:
. Enumeration of the total record count in the database.
. Computation of the mean (average) salary of H1B applicants.
. Determination of the median salary among H1B applicants.
. Calculation of the 25th percentile salary.
. Derivation of the 75th percentile salary.

###### REQUIREMENTS
### We need to install the following programs/libraries for this project.
1. Python 
2. Django
3. PostgreSQL
4. psycopg2
5. Additional Python libraries for CSV file handling and database connectivity


###### Setting Up the App in Your Local Environment:

Follow these steps to set up and use the app on your local environment:

1. *Clone the Repository*:

   Clone the GitHub repository containing the app to your local machine. You can do this using the git command:

   bash
   git clone <repository_url>
   

2. *Navigate to the Project Directory*:

   Go to the project directory using the cd command:

   bash
   cd THE_ELITE_5
   

3. *Install Python Dependencies*:

   Install all the python dependencies required as mentioned above.

4. *Database Setup*:
  
   - Create a new PostgreSQL database for the project. In views.py change the db parameters for accesing postgreSQL.
   - Update the database connection settings in the project's settings.py file, typically found in the project's directory (project-name/settings.py).
   - Configure the DATABASES section to use your PostgreSQL settings, including the database name, user, and password.

5. *Migrate the Database*:
   Use Django's built-in migration system to set up the database schema. Run the following commands:

   bash
   python manage.py makemigrations
   python manage.py migrate
   
6. *Load Data*:
   If you have H1B data in CSV files, write a Python script to read and import the data into your PostgreSQL database. This script should be added to your Django app.

7. *Run the Development Server*:
   Start the development server to run the app locally. Use the following command:

   bash
   python manage.py runserver
   
   Your app should be accessible at http://localhost:8000 in your web browser.


Now you have the app up and running in your local environment, and you can start using it to perform the required calculations and performing data analysis.


###### CONCLUSION
The "H1B Data Analysis using Django" project provides a structured approach to analyzing H1B visa application data and offers an API for accessing valuable statistics. This project can be a valuable resource for anyone interested in H1B visa trends, data analysis, or Django web application development. It allows users to explore and gain insights from the H1B data for informed decision-making.