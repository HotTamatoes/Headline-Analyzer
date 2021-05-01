def welcome_message():
    print("Hello and welcome to the Headline Analyzer!\n Please type one of the following commands to interact with our program!\n")

def options():
    print("\t - \"1\" to begin\n\t - \"2\" for sorting options\n\t - \"3\" for deletion options\n\t = \"0\" to exit\n")

def sorting_options():
    print("")

def deletion_options():
    print("\t - \"1\" to delete all (including database)\n\t - \"2\" to delete all entries containing a snippet\n\t - \"3\" to delete at a specific date\n\t = \"0\" to go back to the main menu\n")

def retryInput(funcPtr):
    nput = input("Invalid input, Try again: ")
    return funcPtr(nput)

def switch(argument):
    print(argument)
    switches = {
        1: print("B\n"),
        2: print("S\n"),
        3: print("D\n"),
        0: print("Goodbye! *waves*\n"),
    }
    func = switches.get(int(argument), retryInput(switch))
    func()

def sorting_switch(argument):
    switches = {}
    func = switches.get(int(argument), retryInput(sorting_switch))
    func()
    
def deletion_switch(argument):
    switches = {
        1: print("A\n"),
        2: print("S\n"),
        3: print("D\n"),
        0: print("Beep Boop it's main menu time\n"),
    }
    func = switches.get(int(argument), retryInput(sorting_switch))
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
    print(nput)
    
def delete_date():
    nput1 = input("Enter the day here: ")
    nput2 = input("Enter the month here: ")
    nput3 = input("Enter the year here: ")
    print(nput1 + "/" + nput2 + "/" + nput3 + "\n")

def build_scrape_and_database():
    ##start scraper!!!!!!
    print("Beep Boop we are filling your database now! (This may take up to 10 mins)\n")
    print("database is served!\n")

# RUNNING STARTS HERE


#welcome_message()
#while(1):
#    options()
#    print("before switch")
#    switch(int(input("")))
#    print("after switch")





## FUNCTIONAL

def zero():
    print("zero")
 
def one():
    print("one")
 
def two():
    print("two")

def nothing():
    print("nothing")
 
switcher = {
        0: zero,
        1: one,
        2: print("two")
    }
 
 
def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, nothing)
    # Execute the function
    func()

while(1):
    numbers_to_strings(int(input("")))