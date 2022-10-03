# DJANGO---REST-API---BANK-DETAILS
I have used the pandas package and openpyxl and imported it to read the csv file of all the bank branches and store.
Also i have used the sqlalchemy for create_engine().

By this method all the bank data was transferred to the Database.

After this it was just a matter of creating api inside the base app and serializing the data to display.
All the api urls are 
        'VIEW ALL COMMANDS: GET /api',
        'VIEW ALL BANK LIST AND IFSC: GET/api/banks',
        'BRANCH DETAILS FOR SPECIFIC BRANCH: GET/api/banks/ifsc',

Here the ifsc is used as the primary key to get a specific bank details.

# THE TIME TAKEN TO COMPLETE THIS ASSIGNMENT WAS 1 DAY.

