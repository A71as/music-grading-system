import tkinter as tk
print("***** Welcome to the Music Grading System V2.5 *****")
print("***** Created by Ahmed Alami, GitHub: A71as *****")

album = input("What is the name of the album? ")
artist = input("What is the name of the artist ")
numsongs = int(input("How many total songs are on the album? "))

def mgs(songs):
    album = [0] * 10
    i = 1
    while i <= numsongs:

        score = int(input(f'Song {i}: What do you rate this song from 1 to 10?'))
        if score <= 10 and score >= 1:
            album[score - 1] += 1
            i += 1
        else:
             print("Invalid rating entered, please try again")

    num = int(input("How would you rate this album as a whole out of 10? ")) / 2

    for i in range(len(album)):
        num += album[i] * (i + 1)
        
    den = (10 * songs)
    s = num / den * 100
    return min(100, round(s, 2))


score = mgs(numsongs)


def mgsscore(score):

    if score >= 95:
        return "'" + album + "', by " + artist + ", scored " + str(score) + "%, which is an A+. That's a Classic Album!"
    elif score >= 90:
        return "'" + album + "', by " + artist + ", scored " + str(score) + "%, which is an A. Not quite a Classic but an Honorable Mention!"
    elif score >= 85:
        return "'" + album + "', by " + artist + ", scored " + str(score) + "%, which is an A-. You Loved this album."
    elif score >= 80:
        return "'" + album + "', by " + artist + ", scored " + str(score) + "%, which is a B+. This is a Great album."
    elif score >= 76:
        return "'" + album + "', by " + artist + ", scored " + str(score) + "%, which is a B. This is a Good album."
    elif score >= 70:
        return "'" + album + "', by " + artist + ", scored " + str(score) + "%, which is a B-. You Liked this Album."
    elif score >= 65:
        return "'" + album + "', by " + artist + ", scored " + str(score) + "%, which is a C. This album is average."
    elif score >= 61:
        return "'" + album + "', by " + artist + ", scored " + str(score) + "%, which is a C-. This album is below Average"
    elif score >= 60:
        return "'" + album + "', by " + artist + ", scored " + str(score) + "%, which is a D. This album is not good."
    else:
        return "'" + album + "', by " + artist + ", scored " + str(score) + "%, or an F. This album is bad."


grade = mgsscore(score)

print(grade)

allgrades = open('albumgrades.txt', 'a+')
allgrades.write(str(score) + "% " + album + " " + artist + '\n')
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

def run_music_grading_system():
    album = entry_album.get()
    artist = entry_artist.get()
    numsongs = int(entry_numsongs.get())
    
    score = mgs(numsongs)
    grade = mgsscore(score)
    
    label_grade.config(text=grade)

root = tk.Tk()
root.title("Music Grading System V2.5")

label_album = tk.Label(root, text="Album Name:")
entry_album = tk.Entry(root)

label_artist = tk.Label(root, text="Artist Name:")
entry_artist = tk.Entry(root)

label_numsongs = tk.Label(root, text="Number of Songs:")
entry_numsongs = tk.Entry(root)

label_grade = tk.Label(root, text="")

button = tk.Button(root, text="Submit", command=run_music_grading_system)

label_album.grid(row=0, column=0)
entry_album.grid(row=0, column=1)

label_artist.grid(row=1, column=0)
entry_artist.grid(row=1, column=1)

label_numsongs.grid(row=2, column=0)
entry_numsongs.grid(row=2, column=1)

label_grade.grid(row=3, column=0, columnspan=2)

button.grid(row=4, column=0, columnspan=2)

root.mainloop()

