import userobjects
import listfunctions

# anime/games/etc. show graphic
# discord bot?

# backend, make an array of classes of anime shows a user has watched
# save users and info to a text file
# load textfile

users = []
currentUser = None

def displayMenu():
    print("Select an Option:")
    print("-----------------")
    print("1. Login to User")
    print("2. Add User")
    print("3. Track New Show")
    print("4. Update Show Information")
    print("5. Search Shows")
    print("6. Exit")
    print("-----------------")

def displaySearchOptions():
    print("Select a search option")
    print("----------------------")
    print("1. Display Full TVShow List A-Z")
    print("2. Display Seasons and Episodes of a TV Show")
    print("----------------------")

try:
    Inital_Object = open("UserInfo.txt","r+")
except IOError:
    Inital_Object = open("UserInfo.txt","a")

# file loop parser
# while True:

while True:
    displayMenu()
    option = input("=> ")
    match option:
        case '1':
            existingUser = input("Enter an existing user: ")
            oldUser = currentUser
            y = 0
            for theUser in users:
                if theUser.username == existingUser:
                    currentUser = y
                    print("Logged into " + users[currentUser].username)
                    break
                y += 1
            if currentUser is None or currentUser == oldUser:
                print("User not found!")
        case '2':
            newUser = input("Enter a new user: ")
            if not listfunctions.userExists(users, newUser):
                users.append(userobjects.user(newUser))
            else:
                print("User Exists!")
        case '3':
            if listfunctions.userNotLoggedIn(currentUser):
                continue
            ShowName = input("Enter the TV show's Name: ")
            ShowWatched = input("Have you finished the TV Show? (Enter y/n): ")
            while True:
                match ShowWatched:
                    case 'y':
                        ShowWatched = True
                        break
                    case 'n':
                        ShowWatched = False
                        break
                    case default:
                        print("Please Enter 'y' or 'n'")
            genre = input("Enter the TV Show's genre: ")
            users[currentUser].tvShowsList.append(userobjects.tvShow(ShowName, ShowWatched, genre, []))
        case '4':
            if listfunctions.userNotLoggedIn(currentUser):
                continue
            ShowName = input("Enter the tracked TV show's Name: ")
            ShowName = listfunctions.showSearch(users[currentUser].tvShowsList, ShowName)
            if ShowName is not None:
                listfunctions.updateShow(users[currentUser].tvShowsList[ShowName])
            else:
                print("TV Show Not Found")
        case '5':
            if listfunctions.userNotLoggedIn(currentUser):
                continue
            displaySearchOptions()
            SearchOption = input("=> ")
            match SearchOption:
                case '1':
                    print(users[currentUser].username + "'s tracked TV Shows")
                    users[currentUser].tvShowsList.sort(key=lambda x: x.tvShowName)
                    listfunctions.displayList(users[currentUser].tvShowsList)
                case '2':
                    currentUserTVShow = input("Enter The TV Show to Display Info For: ")
                    currentUserTVShow = listfunctions.showSearch(users[currentUser].tvShowsList, currentUserTVShow)
                    if currentUserTVShow is not None:
                        listfunctions.displayShowInfo(users[currentUser].tvShowsList[currentUserTVShow])
                    else:
                        print("TV Show not found")
                case default:
                    print("Not a valid option!")
        case '6':
            listfunctions.writeToFile(users, Inital_Object)
            break
        case default:
            print("Enter a number (1-6)")

print("Watch some tv shows!")
