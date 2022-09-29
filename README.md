# music-grading-system
Python based album grader based on User Input



// MGS DEVELOPMENT NOTES 1.0

This program is being developed with the intention of reviewing any musical album that the user chooses. A grade is determined by how many songs are on the album, and how many of those songs have a specific score. For example, how many songs score a 10 out of 10, how many songs score a 9 out of 10 etc. 

-Formula developed for determining score
  - Letter Grade Range not finalized
- Edge case covered for inputted # of songs greater than songs on the album for songs with n score using if statements
- ELIF Print statements created for the possible letter grades to display to the user

//MGS DEVELOPMENT NOTES 2.0

- IMPORT SPOTIPY
  - Import SPOTIPY API to access Spotify database to pull data of Artist, Album, Tracklist, and Number of songs from Spotify to prevent large amounts of user inputs as seen in 1.0
  - Score Formula Unchanged

