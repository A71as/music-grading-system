print("***** Welcome to the Music Grading System 1.0 *****")
print("***** Created by Ahmed Alami, GitHub: A71as *****")

songs = input("How many songs are on the album? ")
songs = int(songs)

interlude = input("How many songs are interludes or skits? ")
interlude = int(interlude)

songs = (songs - interlude)

ten = input("How many songs on the album are a 10/10? ")
ten = int(ten)

if ten > songs:
    print("Error: Value larger than track list. ")
    end


nine = input("How many songs on the album are a 9/10? ")
nine = int(nine)
if nine > (songs - ten):
    print("Error: Value larger than track list. ")
    end

eight = input("How many songs on the album are a 8/10? ")
eight = int(eight)
if eight > (songs - ten - nine):
    print("Error: Value larger than track list. ")
    end

seven = input("How many songs on the album are a 7/10? ")
seven = int(seven)
if seven > (songs - ten - nine - eight):
    print("Error: Value larger than track list. ")
    end

six = input("How many songs on the album are a 6/10? ")
six = int(six)
if six > (songs - ten - nine - eight - seven):
    print("Error: Value larger than track list. ")
    end

five = input("How many songs on the album are a 5/10? ")
five = int(five)
if five > (songs - ten - nine - eight - seven - six):
    print("Error: Value larger than track list.")
    end

four = input("How many songs on the album are a 4/10? ")
four = int(four)
if four > (songs - ten - nine - eight - seven - six - five):
    print("Error: Value larger than track list.")
    end

three = input("How many songs on the album are a 3/10? ")
three = int(three)
if three > (songs - ten - nine - eight - seven - six - five - four):
    print("Error: Value larger than track list.")
    end

two = input("How many songs on the album are a 2/10? ")
two = int(two)
if two > (songs - ten - nine - eight - seven - six - five - four - three):
    print("Error: Value larger than track list.")
    end


one = input("How many songs on the album are a 1/10? ")
one = int(one)
if one > (songs - ten - nine - eight - seven - six - five - four - three - two):
    print("Error: Value larger than track list.")
    end

k = input("How would you grade this album as a whole from 1-10? ")
k = int(k)

ten *= 10
nine *= 9
eight *= 8
seven *= 7
six *= 6
five *= 5
four *= 4
three *= 3
two *= 2
k = ((1/2) * k)

num = (ten + nine + eight + seven + six + five + four + three + two + one + k)
den = (10 * songs)

score = ((num/den)*100)


if score >= 95:
    print("Your album scored a " + str(score) + " which is an A+. That's a Classic Album!")
elif score >= 90:
    print("Your album scored a " + str(score) + " which is an A. Not quite a Classic but an Honorable Mention!")
elif score >= 85:
    print("Your album scored a " + str(score) + " which is an A-. You Loved this album.")
elif score >= 80:
    print("Your album scored a " + str(score) + " which is a B+. This is a Great album.")
elif score >= 76:
    print("Your album scored a " + str(score) + " which is a B. This is a Good album.")
elif score >= 70:
    print("Your album scored a " + str(score) + " which is a B-. You Liked this Album.")
elif score >= 65:
    print("Your album scored a " + str(score) + " which is a C. This album is average.")
elif score >= 61:
    print("Your album scored a " + str(score) + " which is a C-. This album is VERY average  ._.")
elif score >= 60:
    print("Your album scored a " + str(score) + " which is a D. It's just bad.")
else:
    score = str(score)
    print("Your album scored a " + score + " or an F. This album sucks.")
end
