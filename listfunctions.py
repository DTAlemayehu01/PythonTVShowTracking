# listfunctions.py

def userExists(users, aUser):
    for user in users:
        if user.username == aUser:
            return True
    return False

def showExists(showList, show):
    for aShow in showList:
        if aShow.tvShowName == show:
            return True
    return False

def userNotLoggedIn(user):
    if user is None:
        print("User Not Logged in")
        return True
    return False

def updateShowMenu():
    print("Hello World")

def updateShow(tvName):
    updateShowMenu()
