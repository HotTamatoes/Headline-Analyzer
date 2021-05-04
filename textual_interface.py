import Model.mySQL_interface as mySQL_interface
import Model.politico_scraper as politico_scraper

## IMPORTANT NOTES:
#      - for the switches, the functions pointed to must have no arguments
#                          also need to be the names without the parentheses





global last_switch_used

def welcome_message():
    print("Hello and welcome to the Headline Analyzer!\n Please type one of the following commands to interact with our program!\n")

def options():
    print("\t - \"1\" to begin\n\t - \"2\" for sorting options\n\t - \"3\" for deletion options\n\t - \"4\" to see all data in the table\n\t - \"0\" to exit\n")

def sorting_options():
    print("Sorry there are none")

def deletion_options():
    print("\t - \"1\" to delete all (including database)\n\t - \"2\" to delete all entries with the title containing a snippet\n\t - \"3\" to delete at a specific date\n\t = \"0\" to go back to the main menu\n")

def beep_boop():
    print("Beep Boop it's main menu time")

def death_message():
    print("Goodbye! *waves*")


def retryInput():
    nput = input("Invalid input, Try again: ")
    last_switch_used(int(nput))

def switch(argument):
    switches = {
        0: death_message,
        1: build_scrape_and_database,
        2: sorting,
        3: deletion,
        4: mySQL_interface.printAllData
    }
    func = switches.get(argument, retryInput)
    last_switch_used = switch
    func()

def sorting_switch(argument):
    switches = {} ### !!! Todo
    func = switches.get(argument, retryInput)
    last_switch_used = sorting_switch
    func()
    
def deletion_switch(argument):
    switches = {
        0: beep_boop,
        1: mySQL_interface.clearDatabase,
        2: delete_snippet,
        3: delete_date,
    }
    func = switches.get(argument, retryInput)
    last_switch_used = deletion_switch
    func()

def sorting():
    sorting_options()
    nput = input("")
    #sorting_switch(int(nput)) ## !!! uncomment when implemented

def deletion():
    deletion_options()
    nput = input("")
    deletion_switch(int(nput))

def delete_snippet():
    nput = input("Enter the snippet here (ex: \"the\" deletes all entries containing the word the): ")
    mySQL_interface.deleteHeadlineContaining(nput)
    
def delete_date():
    nput1 = input("Enter the day here: ")
    nput2 = input("Enter the month here: ")
    nput3 = input("Enter the year here: ")
    mySQL_interface.deleteHeadlineAtDate(nput1 + "/" + nput2 + "/" + nput3) ##### !!! THIS NEEDS FIXING <- based on how the year month day are stored in the db

def build_scrape_and_database():
    nput = input("Type 1 if you have already created a database, otherwise hit enter\n")
    if(nput == "1"):
        mySQL_interface.point_cursor_to_db("politico")
    else:
        ##start scraper!!!!!!
        print("Beep Boop we are filling your database now! (This may take up to 10 mins)\n")
        dataTuples = politico_scraper.create_tuple()
        mySQL_interface.initiate_database(dataTuples, "politico")
        print("database is served!\n")

# RUNNING STARTS HERE

welcome_message()
nput = -1
while(nput != 0):
    options()
    nput = int(input(""))
    switch(nput)