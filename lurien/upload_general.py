from os import system           #For running the upload_youtube.py script
from datetime import date       #Daily dates for naming downloads.
import json                     #For storing the counters. Because we take the counter in first we can't use an expanding list without defining a "1" counter for the new Posts first.
from PIL import Image           #Image Library for creating thumbnail with compilation counter.
from PIL import ImageDraw
from lurien import upload_youtube

def youtube(Post):
    with open("./lurien/upload_counter.json","r") as fp:                    #Import counters.
        counters=json.load(fp)

    #Create Thumbnail
    Post.yt_title = f"{Post.post_title} #{counters[Post.counter_index]}"    #Create Youtube Title with the Addition of the counter.
    upload_youtube.main(Post)
    
    #Upload Thumbnail inside



    counters[Post.counter_index]=counters[Post.counter_index]+1             #Increase the Post counter by 1.
    with open("./lurien/upload_counter.json","w") as fp:                    #Export counters.
        json.dump(counters,fp)


