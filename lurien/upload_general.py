from os import system           #For running the upload_youtube.py script
from datetime import date       #Daily dates for naming downloads.


def youtube(Post,counter):
    system(f'python ./lurien/upload_youtube.py \
    --file="./upload/{date.today()}/youtube/{Post.tag}.mp4" \
    --title="{Post.post_title} #{counter}" \
    --description="" \
    --keywords="" --category="24" \
    --privacyStatus="public"')