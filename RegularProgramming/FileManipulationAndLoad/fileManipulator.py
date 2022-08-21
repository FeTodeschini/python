# Developer: Felipe Todeschini
#
# This program manipulates csv files with transactions to be loaded into a database. It has functions for:
#
# - Loading transactions in batch from the csv file using pandas and SQLAlchemy
# - Removing the trailler of the csv files
# - Looking up for the missing key in the cashtransactions file, as it does not contain the same key that is common to the loans and securities files. Hence, 
#   the lookup checks for the KEY in the BALANCES file, based on the account id in the cashtransactions file
# - Adding new empty fields to the cashtransactions.csv file so another program will add value to this newly created fields (those are the country codes of intermediary banks, 
#   beneficiaries and other countries not available in the original cashtransactions.csv file)

import pandas as pd
from sqlalchemy import create_engine
import pyodbc as pc
import sys

class dbConnection:
    server = 'LAPTOP-TC7K0E1C\SQLEXPRESS'
    database = 'AML' # AML stands for Anti-Money Laundering
    user = 'felipe.todeschini'
    #in a real world application, the password must be encrypted
    password = 'felipe.todeschini'

def LoadFileIntoDataFrame(fileName):
    return pd.read_csv(fileName)

#Loads into the database the transactions in the csv file passed as an argument to the function
def LoadTransactions(fileName):
    
    try:
        txnDataFrame = LoadFileIntoDataFrame(fileName)

        #creates the connection to the SQL Server Database based on the dbConnection parameters
        dbCon = dbConnection

        eng = create_engine("mssql+pyodbc://"+ dbCon.user+":"+dbCon.password+"@"+dbCon.server+"/db_pandas_class?driver=SQL+Server")
        txnDataFrame.to_sql('TRANSACTIONS', eng, if_exists='append', index=False)
        return 1
    except:
        return 0
    
# --------------------------------------------------------------------------------------------------------------------------
# Function that add pipes to the end of the cashtransactions file (field delimiter for additional Country fields to be added by the program that enriches the file data)
# --------------------------------------------------------------------------------------------------------------------------
def AddPipesToCashFile():
    
    try:
        i = 0

        with open("CASHTRANSACTIONS.csv") as inputFile:
            
            rows = inputFile.readlines()

            with open("D:\InputFiles\EGITS_PIPE.txt", "w") as outputFile:
                for row in rows:
                    if (i==0) or (i==len(rows)-1):
                        outputFile.write(row)
                    else:
                        outputFile.write(row.strip() + "|" * 12 + "\n")
                    
                    i += 1
        
        return 1
    except:
            return 0

# ------------------------------------------------------------------------------------------------------------------------------
# Function that adds the missing KEY to the Cash Transactions File file based on KEY that is in the Balances file for each AccountNumber
# NOTE: Pandas was not used on purpose so I could play with files and dictionaries
# ------------------------------------------------------------------------------------------------------------------------------
def AddKeyToCashFile():
   
    try:
        #Dictionary with the KEYS from the Balances file
        dicMissingKeys = {}

        #positions of the relevant columns in the EGIFTS file
        debitCreditIndicatorColumn = 92
        debitAccountColumn = 52 
        creditAccountColumn = 53
        shortNameColumn = 56

        i = 0

        #reads the Balance file and creates the shortnames dictionary
        with open("BALANCES.csv") as balancesFile:
                
                rows = balancesFile.readlines()

                for row in rows:
                                
                    if (i!=0) and (i!=len(rows)-1):                    
                        currentRow = row.split(";")
                        dicMissingKeys[currentRow[2].rstrip()] = currentRow[9].rstrip()

                    i += 1  

        with open("CASHTRANSACTIONS.csv") as inputFile:
            
            inputFileRows = inputFile.readlines()
            i = 0
            outputRow = ""

            with open("CASHTRANSACTIONS_WITHKEY.csv", "w") as outputFile:

                for row in inputFileRows:

                    #skips header and trailler
                    if (i!=0) and (i!=len(inputFileRows)-1):

                        currentRow = row.split("|")
                        outputRow = ""

                        for column in range(0, 93):
                            
                            #checks if it is the shortname column and, in case it is, fills it with the shortname from the balances file   
                            if (column == int(shortNameColumn)):
                                #Check if it is a Debit or Credit and if the correspondent account column has a value or if it is empty
                                if (currentRow[debitCreditIndicatorColumn].rstrip() == "D"): 
                                    if (currentRow[debitAccountColumn]) == "":
                                        outputRow += "|"
                                    else:
                                        outputRow += dicMissingKeys.get(currentRow[debitAccountColumn],"") + "|"
                                elif (currentRow[debitCreditIndicatorColumn].rstrip() == "C"):
                                    if (currentRow[creditAccountColumn]) == "":
                                        outputRow += "|"
                                    else:
                                        #treat null value
                                        if (dicMissingKeys.get(currentRow[creditAccountColumn],"")) is None:
                                            outputRow += "|"
                                        else:
                                            outputRow += dicMissingKeys.get(currentRow[creditAccountColumn],"") + "|"
                            else:
                                #simply copies the column content
                                outputRow += currentRow[column] + "|"

                        outputFile.write(outputRow.rstrip(outputRow[-1]))

                    i += 1
        return 1
    except:
        return 0
# ------------------------------------------------------------------------------------------------------------------------------
# Remove trailler from the file passed as a parameter
# ------------------------------------------------------------------------------------------------------------------------------
def RemoveTrailer(fileName):
    
    try:  
        with open(fileName, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            file.writelines(lines[:-1])

        return 1
        
    except:
        return 0

def main():

    # Checks which function is being called by the command line (batch scheduler)
    if sys.argv[1].upper() == "ADDPIPES":
        AddPipesToCashFile()
    elif sys.argv[1].upper() == "ADDKEY":
        AddKeyToCashFile()
    elif sys.argv[1].upper() == "REMOVETRAILER":
        RemoveTrailer(sys.argv[2])
    elif sys.argv[1].upper() ==  "LOADTRANSACTIONS":
        LoadTransactions(sys.argv[2])
        
main()
