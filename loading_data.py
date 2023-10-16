import psycopg2
import csv

# Database connection parameters
db_params = {
    'host': 'localhost',
    'port': 5432,
    'database': 'STGI',
    'user': 'postgres',
    'password': 'AYUSH28@'
}

# CSV file path
csv_file_path = 'D:/STGI/data/H-1B_Disclosure_Data_FY17.csv'

# Table name in the database
table_name = 'NEXT_TESTING'

# Establish a database connection
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Create a table to store the CSV data (if it doesn't exist)
create_table_query = """
    CREATE TABLE IF NOT EXISTS {} (
    CASE_NUMBER VARCHAR PRIMARY KEY,
    CASE_STATUS VARCHAR,
    CASE_SUBMITTED DATE,
    DECISION_DATE DATE,
    VISA_CLASS VARCHAR,
    EMPLOYMENT_START_DATE DATE,
    EMPLOYMENT_END_DATE DATE,
    EMPLOYER_NAME VARCHAR,
    EMPLOYER_BUSINESS_DBA VARCHAR,
    EMPLOYER_ADDRESS VARCHAR,
    EMPLOYER_CITY VARCHAR,
    EMPLOYER_STATE VARCHAR,
    EMPLOYER_POSTAL_CODE VARCHAR,
    EMPLOYER_COUNTRY VARCHAR,
    EMPLOYER_PROVINCE VARCHAR,
    EMPLOYER_PHONE VARCHAR,
    EMPLOYER_PHONE_EXT VARCHAR,
    AGENT_REPRESENTING_EMPLOYER VARCHAR,
    AGENT_ATTORNEY_NAME VARCHAR,
    AGENT_ATTORNEY_CITY VARCHAR,
    AGENT_ATTORNEY_STATE VARCHAR,
    JOB_TITLE VARCHAR,
    SOC_CODE VARCHAR,
    SOC_NAME VARCHAR,
    NAICS_CODE VARCHAR,
    TOTAL_WORKERS INT,
    NEW_EMPLOYMENT INT,
    CONTINUED_EMPLOYMENT INT,
    CHANGE_PREVIOUS_EMPLOYMENT INT,
    NEW_CONCURRENT_EMPLOYMENT INT,
    CHANGE_EMPLOYER INT,
    AMENDED_PETITION INT,
    FULL_TIME_POSITION VARCHAR,
    PREVAILING_WAGE FLOAT,
    PW_UNIT_OF_PAY VARCHAR,
    PW_WAGE_LEVEL VARCHAR,
    PW_SOURCE VARCHAR,
    PW_SOURCE_YEAR INT,
    PW_SOURCE_OTHER VARCHAR,
    WAGE_RATE_OF_PAY_FROM FLOAT,
    WAGE_RATE_OF_PAY_TO FLOAT,
    WAGE_UNIT_OF_PAY VARCHAR,
    H1B_DEPENDENT VARCHAR,
    WILLFUL_VIOLATOR VARCHAR,
    SUPPORT_H1B VARCHAR,
    LABOR_CON_AGREE VARCHAR,
    PUBLIC_DISCLOSURE_LOCATION VARCHAR,
    WORKSITE_CITY VARCHAR,
    WORKSITE_COUNTY VARCHAR,
    WORKSITE_STATE VARCHAR,
    WORKSITE_POSTAL_CODE VARCHAR,
    ORIGINAL_CERT_DATE DATE
    );
""".format(table_name)
cursor.execute(create_table_query)

salary_cols = [33,39,40]

print("starting reading")
# Read the CSV file and insert data into the PostgreSQL table
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row if it exists
    i = 0
    print("Data read")
    for row in csv_reader:
        i += 1
        print(i)
        for data in salary_cols:
            pre = row[data].replace(",","")
            if (pre != ""):
                row[data] = float(pre)

        # print(i)
        # print(row)
        cleaned_row = [value if value != "" else None for value in row]
        # print(cleaned_row)
        insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(cleaned_row))});"
        cursor.execute(insert_query, cleaned_row)
    print("done")

# Commit the changes and close the cursor and connection
conn.commit()
cursor.close()
conn.close()