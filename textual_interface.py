import Model.mySQL_interface as mySQL_interface
import Model.politico_scraper as politico_scraper

def welcome_message():
    print("Hello and welcome to the Headline Analyzer!\n Please type one of the following commands to interact with our program!\n")

def options():
    print("\t - \"b\" to begin\n\t - \"s\" for sorting options\n\t - \"d\" for deletion options\n\t = \"x\" to exit\n")

def sorting_options():
    print("")

def deletion_options():
    print("")

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

def sorting():
    sorting_options()
    nput = input("")
    sorting_switch(nput)

def deletion():
    deletion_options()
    nput = input("")
    deletion_switch(nput)

def build_scrape_and_database():
    ##start scraper!!!!!!
    dataTuples = politico_scraper.create_tuple()
    mySQL_interface.initiate_database(dataTuples, "politico")

# RUNNING STARTS HERE

welcome_message()
options()
nput = input("")
switch(nput)
while(nput != "x"):
    options()
    nput = input("")
    switch(nput)