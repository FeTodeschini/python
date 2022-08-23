This program manipulates csv files before inserting their records into the database. These are the functions in the program:

- Remove trailer from input file
- Look up for the missing key in the cashtransactions.csv file. The key is obtained in the BALANCE.csv file, using the ACCOUNTID (common field between cashtransactions.csv and BALANCES.csv)
- Batch loads the transactions file specified in the function's argument into the database

pip install pandas
pip install pyodbc
pip install sqlalchemy