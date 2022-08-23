from os import system           #For running the upload_youtube.py script
from datetime import date       #Daily dates for naming downloads.
import json                     #For storing the counters. Because we take the counter in first we can't use an expanding list without defining a "1" counter for the new Posts first.
from lurien import upload_youtube
from PIL import Image, ImageDraw,ImageFont      #Image Library for creating thumbnail with compilation counter.


def youtube(Post):
    with open("./lurien/upload_counter.json","r") as fp:                    #Import counters.
        counters=json.load(fp)

    #Create Thumbnail
    image=Image.open(f"./raw_thumbnails/thumbnail_{Post.tag}.png")          #Open raw thumbnail (No counter)
    draw=ImageDraw.Draw(image)                                              #Import raw thumbnail
    font=ImageFont.truetype('./lurien_env/impact.ttf',size=100)             #Choose font and point
    draw.text((60, 575), f"#{counters[Post.counter_index]}", font=font, fill ="white", stroke_fill="black", stroke_width=3) #Add text
    image.save(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/thumbnail.png")                           #Save the thumbnail.
    

    Post.yt_title = f"{Post.post_title} #{counters[Post.counter_index]}"    #Create Youtube Title with the addition of the counter.
    upload_youtube.main(Post)                                               #Upload the video and thumbnail. (Thumbnail is fetched automatically from above directory)
    

    counters[Post.counter_index]=counters[Post.counter_index]+1             #Increase the Post counter by 1.
    with open("./lurien/upload_counter.json","w") as fp:                    #Export counters.
        json.dump(counters,fp)


