import Model.mySQL_interface as mySQL_interface
import Model.politico_scraper as politico_scraper

def welcome_message():
    print("Hello and welcome to the Headline Analyzer!\n Please type one of the following commands to interact with our program!\n")

def options():
    print("\t - \"b\" to begin\n\t - \"s\" for sorting options\n\t - \"d\" for deletion options\n\t = \"x\" to exit\n")

def sorting_options():
    print("")

def deletion_options():
    print("\t - \"a\" to delete all (including database)\n\t - \"s\" to delete all entries containing a snippet\n\t - \"d\" to delete at a specific date\n\t = \"x\" to go back to the main menu\n")

def retryInput(funcPtr):
    nput = input("Invalid input, Try again: ")
    funcPtr(nput)

def switch(argument):
    switches = {
        "b": build_scrape_and_database(),
        "s": sorting(),
        "d": deletion(),
        "x": print("Goodbye! *waves*")
    }
    func = switches.get(argument, retryInput(switch))
    func()

def sorting_switch(argument):
    switches = {}
    func = switches.get(argument, retryInput(sorting_switch))
    func()
    
def deletion_switch(argument):
    switches = {
        "a": mySQL_interface.clearDatabase(),
        "s": delete_snippet(),
        "d": delete_date(),
        "x": print("Beep Boop it's main menu time")
    }
    func = switches.get(argument, retryInput(sorting_switch))
    func()

def sorting():
    sorting_options()
    nput = input("")
    sorting_switch(nput)

def deletion():
    deletion_options()
    nput = input("")
    deletion_switch(nput)

def delete_snippet():
    nput = input("Enter the snippet here (ex: \"the\" deletes all entries containing the word the): ")
    mySQL_interface.deleteHeadlineContaining(nput)
    
def delete_date():
    nput1 = input("Enter the day here: ")
    nput2 = input("Enter the month here: ")
    nput3 = input("Enter the year here: ")
    mySQL_interface.deleteHeadlineAtDate(nput1 + "/" + nput2 + "/" + nput3) ##### !!! THIS NEEDS FIXING <- based on how the year month day are stored in the db

def build_scrape_and_database():
    ##start scraper!!!!!!
    print("Beep Boop we are filling your database now! (This may take up to 10 mins)\n")
    dataTuples = politico_scraper.create_tuple()
    mySQL_interface.initiate_database(dataTuples, "politico")
    print("database is served!\n")

# RUNNING STARTS HERE

welcome_message()
nput = ""
while(nput != "x"):
    options()
    nput = input("")
    switch(nput)