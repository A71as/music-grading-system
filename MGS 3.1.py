import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="bce812a6db7e4fc9af9e23647bcc555e",
                                                           client_secret="c1bfb126244e41408115ae11b0d0b31f"))

print("***** Welcome to the Music Grading System V3.0 *****")
print("***** Created by Ahmed Alami, GitHub: A71as *****\n")
print("*** Key ***")
print("1-2 is Bad, unlistenable and truly awful.")
print("3-4 is Okay, boring and not worth revisiting.")
print("5-6 is Good, Enjoyable but can feel average or forgettable")
print("7-8 is Great, Noteworthy song with replay value and worth your time")
print("9-10 is Best, Must-hear song that leaves a lasting impression\n")

# Get the album name and artist name from the user
artist_name = input("Enter the artist name: ")
album_name = input("Enter the album name: ")

# Search for the album using the album name and artist name
results = sp.search(q='album:{} artist:{}'.format(album_name, artist_name), type='album', limit=1)
albums = results['albums']['items']

# Get the album ID
album_id = None
if len(albums) > 0:
    album = albums[0]
    album_id = album['id']

if album_id:
    results = sp.album_tracks(album_id)
    tracks = results['items']
    tracklist = []

    print("\nDRate the following songs on a Scale from 1 to 10.\n")
    for track in tracks:
        song_name = track['name']
        while True:
            user_input = int(input("'{}': ".format(song_name)))
            try:
                user_int = int(user_input)
                if user_int > 10 or user_int < 1:
                    print("Invalid input, please enter a number between 1 and 10")
                else:
                    tracklist.append([song_name, user_int])
                    break
            except ValueError:
                print("Invalid input, please enter a number between 1 and 10")
    k = int(input("How would you grade this album as a whole? (1-10) "))/2

else:
    print("No album was found with the given name and artist.")

def mgs(tllength):
    num = k
    for i in range(len(tracklist)):
        for j in range(len(tracklist[i])):
            num = num + int(tracklist[i][1])/2

    den = (10 * len(tracklist))
    score = num / den * 100
    score = min(100, round(score, 2))

    if score >= 95:
        return "\n'" + album_name + "', by " + artist_name + ", scored " + str(score) + "%, which is an A+. That's a Classic Album!"
    elif score >= 90:
        return "\n'" + album_name + "', by " + artist_name + ", scored " + str(score) + "%, which is an A. Not quite a Classic but an Honorable Mention!"
    elif score >= 85:
        return "\n'" + album_name + "', by " + artist_name + ", scored " + str(score) + "%, which is an A-. Must-hear Album that leaves a lasting impression"
    elif score >= 80:
        return "\n'" + album_name + "', by " + artist_name + ", scored " + str(score) + "%, which is a B+. This album is Noteworthy with plenty of replay value and worth your time"
    elif score >= 75:
        return "\n'" + album_name + "', by " + artist_name + ", scored " + str(score) + "%, which is a B. This is a Great album."
    elif score >= 70:
        return "\n'" + album_name + "', by " + artist_name + ", scored " + str(score) + "%, which is a C+. This album is good, but can feel average or forgettable"
    elif score >= 60:
        return "\n'" + album_name + "', by " + artist_name + ", scored " + str(score) + "%, which is a C. This album is Average"
    elif score >= 50:
        return "\n'" + album_name + "', by " + artist_name + ", scored " + str(score) + "%, which is a D. This album is boring and not worth revisiting"
    else:
        return "\n'" + album_name + "', by " + artist_name + ", scored " + str(score) + "%, or an F. This album is unlistenable and truly awful"

print(mgs(tracklist))

allgrades = open('albumgrades.txt', 'a+')
allgrades.write(mgs(tracklist) + '\n')
allgrades.close()
allgrades = open('albumgrades.txt', 'r')
ls = []
for l in allgrades.readlines():
    ls.append(l)
allgrades.close()
ls.sort()
allgrades = open('albumgrades.txt', 'w')
for i in ls:
    if '100' in i[:3]:
        allgrades.write(i)
ls.reverse()
for i in ls:
    if '100' not in i[:3]:
        allgrades.write(i)

allgrades.close()

close = input("press close to exit")