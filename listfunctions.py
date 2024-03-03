# listfunctions.py

import userobjects

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

def showSearch(showList, show):
    y = 0
    for aShow in showList:
        if aShow.tvShowName == show:
            return y
        y += 1
    return None

def userNotLoggedIn(user):
    if user is None:
        print("User Not Logged in")
        return True
    return False

def updateShowMenu():
    print("1. Update Finished Status")
    print("2. Update Genre")
    print("3. Add Episodes")

def updateShow(tvName):
    updateShowMenu()
    option = input("=> ")
    match option:
        case '1':
            watchedStatus = input("Enter new watched status (y/n): ")
            match watchedStatus:
                case 'y':
                    tvName.haveWatched = True
                case 'n':
                    tvName.haveWatched = False
                case default:
                    print("Not a valid input")
        case '2':
            newGenre = input("Input a new genre: ")
            tvName.genre = newGenre
        case '3':
            newEpisodeTitle = input("Input the New Episode's title: ")
            newEpisodeRuntime = input("Input the New Episode's runtime: ")
            whichSeason = input("Input the season this episode belongs to: ")
            try: 
                whichSeason =int(whichSeason)
            except ValueError:
                print("Not a valid season number")
            else:
                if len(tvName.seasons) < whichSeason:
                    for i in range(whichSeason):
                        tvName.seasons.append(userobjects.season([]))
                tvName.seasons[whichSeason-1].episodes.append(userobjects.episode(newEpisodeTitle, len(tvName.seasons[whichSeason-1].episodes) , newEpisodeRuntime))
        case default:
            print("Not a valid option")

def displayList(TVList):
    y = 1
    for x in TVList:
        print(str(y) + ". " + x.tvShowName + ".")
        print("----Watched is: " + str(x.haveWatched))
        print("----For fans of: " + x.genre)
        y += 1

def displayShowInfo(Anime):
    y = 1
    for i in Anime.seasons:
        print("Season " + str(y) + ":")
        z = 1
        for j in i.episodes:
            print(str(z) + ". " + j.Title + ", Runtime: " + j.Time)
            z += 1
        y += 1

def writeToFile(userList, fileObject):
    fileObject.seek(0)
    w = 1
    for user in userList:
        fileObject.write("User " + str(w) + ": \n" + user.username + "\n")
        x = 1
        for tvShows in user.tvShowsList:
            fileObject.write("TV-Show " + str(x) + ": \n" + tvShows.tvShowName + "\n" + str(tvShows.haveWatched) + "\n" + tvShows.genre + "\n")
            y = 1
            for aSeason in tvShows.seasons:
                fileObject.write("Season " + str(y) + ":\n" + str(y) + "\n")
                z = 1
                for aEpisode in aSeason.episodes:
                    fileObject.write("Episode " + str(z) + ": \n" + aEpisode.Title + "\n" + str(aEpisode.Index) + "\n" + aEpisode.Time + "\n")
                    z += 1
                y += 1
            x += 1
        w += 1
    fileObject.write("REND OF FILE")
    fileObject.truncate()

# def readFileToStructs(theList, fileObj):
#     while True:
#         theLine = fileObj.readline()
#         try:
#             firstChar = theLine[0]
#         except IndexError:
#             return
# 
#         currentTVShow = None
#         currentSeason = None
#         currentEpisode = None
#         match firstChar:
#             case 'U':
#                 currentUser = theLine[8]
#                 i = 9
#                 currentChar = theLine[i]
#                 while currentChar != '\n':
#                     currentUser = currentUser + currentChar
#                     i += 1
#                     currentChar = theLine[i]
#                 theList.append(userobjects.user(currentUser, []))
#                 currentUser = len(theList)-1
#             case 'T':
#                 currentTVShow = theLine[11]
#                 i = 12
#                 currentChar = theLine[i]
#                 while currentChar != ':':
#                     currentTVShow = currentTVShow + currentChar
#                     i += 1
#                     currentChar = theLine[i]
#                 i += 2
#                 currentBool = theLine[i]
#                 if currentBool == 'F':
#                     currentBool == False
#                 else:
#                     currentBool == True
#                 i += 7
#                 currentGenre = theLine[i]
#                 i += 1
#                 while currentChar != '\n':
#                     currentGenre = currentGenre + currentChar
#                     i += 1
#                     currentChar = theLine[i]
#                 currentChar = theLine[i]
#                 theList[currentUser].tvShowsList.append(userobjects.tvShow(currentUser, currentBool, currentGenre, []))
#                 currentUser = len(theList)-1
#             case 'S':
#                 currentSeason = None
#             case 'E':
#                 currentEpisode = None
#             case default:
#                 break
def readFileToStructs(theList, fileObj):
    while True:
        theLine = fileObj.readline()
        if theLine[0:4] == "User":
            currentUser = fileObj.readline()
            currentUser = currentUser[0:len(currentUser)-1]
            theList.append(userobjects.user(currentUser, []))
            currentUser = len(theList) - 1
        elif theLine[0:7] == "TV-Show":
            currentTVShow = fileObj.readline()
            currentTVShow = currentTVShow[0:len(currentTVShow)-1]
            currentBool = fileObj.readline()
            currentBool = currentBool[0:len(currentBool)-1]
            bool(currentBool)
            currentGenre = fileObj.readline()
            currentGenre = currentGenre[0:len(currentGenre)-1]
            theList[currentUser].tvShowsList.append(userobjects.tvShow(currentTVShow, currentBool, currentGenre, []))
            currentTVShow = len(theList[currentUser].tvShowsList) - 1
        elif theLine[0:6] == "Season":
            currentSeason = fileObj.readline()
            currentSeason = currentSeason[0:len(currentSeason)-1]
            int(currentSeason)
            theList[currentUser].tvShowsList[currentTVShow].seasons.append(userobjects.season([]))
            currentSeason = len(theList[currentUser].tvShowsList[currentTVShow].seasons) - 1
        elif theLine[0:7] == "Episode":
            currentEPTitle = fileObj.readline()
            currentEPTitle = currentEPTitle[0:len(currentEPTitle)-1]
            currentEPIndex = fileObj.readline()
            currentEPIndex = currentEPIndex[0:len(currentEPIndex)-1]
            currentEPRuntime = fileObj.readline()
            currentEPRuntime = currentEPRuntime[0:len(currentEPRuntime)-1]
            theList[currentUser].tvShowsList[currentTVShow].seasons[currentSeason].episodes.append(userobjects.episode(currentEPTitle, currentEPIndex, currentEPRuntime))
        else:
            break
