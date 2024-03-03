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
                        tvName.seasons.append(userobjects.season())
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
    w = 1
    for user in userList:
        fileObject.write("User " + str(w) + ": " + user.username + "\n")
        x = 1
        for tvShows in user.tvShowsList:
            fileObject.write("TV-Show " + str(x) + ": " + tvShows.tvShowName + ": " + str(tvShows.haveWatched) + ": " + tvShows.genre + "\n")
            y = 1
            for aSeason in tvShows.seasons:
                fileObject.write("Season " + str(y) + ":" + "\n")
                z = 1
                for aEpisode in aSeason.episodes:
                    fileObject.write("Episode " + str(z) + ": " + aEpisode.Title + ": " + str(aEpisode.Index) + ": " + aEpisode.Time + "\n")
                    z += 1
                y += 1
            x += 1
        w += 1

