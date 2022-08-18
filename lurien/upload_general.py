from os import system           #For running the upload_youtube.py script
from datetime import date       #Daily dates for naming downloads.
import json

def youtube(Post):
    with open("./lurien/upload_counter.json","r") as fp:
        counters=json.load(fp)

    system(f'python ./lurien/upload_youtube.py \
    --file="./upload/{date.today()}/youtube/{Post.tag}.mp4" \
    --title="{Post.post_title} #{counters[Post.counter_index]}" \
    --description="" \
    --keywords="" --category="24" \
    --privacyStatus="public"')

    counters[Post.counter_index]=counters[Post.counter_index]+1

    with open("./lurien/upload_counter.json","w") as fp:
        json.dump(counters,fp)