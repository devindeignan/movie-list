#To-Do List
#Alma Marhshall and Devin Deignan

#Functions
movies= [ ]

#adds an item to the list
def AddTask(): 
    newmovie = input("Add a movie: ")
    movies.insert(1, newmovie)

#prints the list for the user to view
def view(): 
    print(movies)

#asks the user which item they want to mark off and puts an x next to that item in the list
def MarkTask(): 
    print(movies)
    done = int(input("What movie did you watch?"))
    movies.insert(done, "[X]")

#asks the user for a number and removes the item from the list that corresponds with the number
def Remove():
    watched = int(input("Remove a movie from spaces 0-4."))
    movies.pop(watched)

#removes all items from the list
def removeAll():
    movies.clear()

#sorts the items in list alphabetically from a-z
def alphabet():
    movies.sort()

#prints the number of items in the list
def listLength():
    print(len(movies))

#Presents the user with a menu of options to perform the prior functions created
def movielist(): 
    option = int(input("Welcome! Choose an option to continue: \n 1. Add a Movie \n 2. View List \n 3. Mark Movie as watched, \n 4. Remove Movie from list \n 5. Quit list \n 6. Remove everything from list \n 7. Sort list alphabetically \n 8. Print number of movies in list"))
    if (option == 1):
        AddTask()
        movielist()
    if (option == 2):
        view()
        movielist()
    if (option == 3): 
        MarkTask()
        movielist()
    if (option == 4):
        Remove()
        movielist()
    if (option == 5):
        print("Bye!")
        quit()
    if (option == 6):
        removeAll()
        movielist()
    if (option == 7):
        alphabet()
        movielist()
    if (option == 8):
        listLength()
        movielist()
    elif (option != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
        print ("ERROR")
        movielist()

#Main

movielist()