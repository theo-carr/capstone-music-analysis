# What distinct features make up popular music today, and do these features differs from past generations of popular music?
## Table of Contents
* [Inspiration](#inspiration)
* [Methodology](#methodology)
* [The-Code](#introduction-to-notebook)
* [Results](#results)
* [Technologies-Used](#technologies-used)

## Inspiration
I am a lifelong musician and music lover. I have played piano since I was ten years old, and picked up guitar when I was sixteen. Due to this, I have always been drawn to older, more instrumental music. This got me thinking, are popular songs today really less instrumental? In comes the spotify API; an extensive, free resource that tracks "audio features" for each song they have available on their platform. These "audio features" consist of stats such as *energy*, *danceability*, *speechiness*, *instrumentalness*, and many more.

## Methodology
The question I set out to answer was whether or not the popular music of today differed from the popular music of the past, and if there was a way to quanitatively describe the difference. In comes the spotify API, which does put a number on features of music that they use to recommend their users music they might like. The second piece of the puzzle was deciding what/how many songs to look at. For this I turned to the billboard 100 charts, as they are usally an agreed on authority for popular music. I found a pre-curated dataset on kaggle which can be found [here](https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs), and had billboard hot 100 songs going back to 1958. From there I fed these songs into the SpotifyAPI to get the audio feature statistics for each of the tracks. After cleaning the resulting datasets, I brought them into tableau to begin my analysis. Further, I brought in a curated dataset of music industry sales data from the RIAA (recording industry of america) to get a sense of how music has been digested the past 50 years. That dataset can be found [here](https://www.kaggle.com/datasets/andrewmvd/music-sales), and more details about the dataset [here](https://www.riaa.com/u-s-sales-database/)

## Introduction to notebook 
### The drivers behind the whole project
> the two most important documents in this repo are "spotifyAPI.py" and "data_collection_functions.py". These two python scripts were the fundamental drivers for collecting the data necessary for this project.
### SpotifyAPI.py
> SpotifyAPI.py is a custom module I wrote to help me interact with Spotify's API service. It includes functions that interact with each endpoint and return the response from that endpoint. This is a usable module for anyone interested in playing with the SpotifyAPI, all you would need to do is substitute in your API key into the get_token() function. 
### data_collection_functions.py
> data_collection_functions.py is a python script I wrote that worked in conjunction with spotifyAPI.py to quickly build ready to work with datasets from the massive list of songs I wanted to track. This was a neccessary step for the project as getting information from any given song required working with multiple endpoints such as "Search" and "Get Audio Features". Plus, I had to stay within my API request limits so I could not collect all the data at once, so it was important to have a predefined method of collecting and building the datasets so I could consistently collect the same information day to day. 
### Misc
> There are many misc. notebooks throughout this repository, as with tackling such a big projcet, there was a lot of trial and error. I had to test methods of collecting data before I could confidently write a module that did the work for me, and there were also a lot of trial angles I tried to bring into the project that did not make the final cut. I thought it was important to include these in the final repository to get a sense of the journey I took in making this project happen. 

## Results
> Popular music has changed a lot with time (duh). But working on this project, I found it has changed in interesting ways. To start, popular music on average is less positive and happy than it was in the past. Perhaps signifing a general shift in what we as a culture expect and want from music. However, the largest takeaway I have after working with this data is an appreciation for how much computers and electronics have shaped the music we listen to today. Out of all the audio features I looked at, "acousticness" and loudness saw that most drastic changes; both of these are directly tied to the equipment used to create music. Further, the largest shifts in these areas were in line with the music industries shifts away from analog towards digital formats, namely, the Compact Disk (CD). Electronics have even changed the keys that are used to create music, allowing artists to stray away from keys that are friendliest to play on popular instruments such as guitar and piano. Overall popular music has changed significantly over time, enabled by different factors such as the tools used to create music and general cultural expectations of what is expected of music, and music will continue to change into the future. I had a lot of working with this data and I am eager to check back on the state of music years from now. 

## Technologies Used
* Python
* REST API (spotify)
* Jupyter Notebooks
* Tableau

