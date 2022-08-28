#Primary Packages
from time import time
import praw                                 #For scraping Reddit (Gets urls of posts)
import requests                             #For getting Reddit media links (For feeding RedDownloader)
from RedDownloader import RedDownloader     #For downloading Reddit media
from moviepy.editor import *                #For determining video length, making clips from iamges.
from datetime import date                   #Daily dates for naming downloads.
from lurien import organizer_general
from moviepy.config import change_settings  #Required to declare ImageMagick Binary for TextClips to work.
from time import sleep





change_settings({"IMAGEMAGICK_BINARY": r"./lurien_venv/ImageMagick-7.1.0-Q16-HDRI/ImageMagick-7.1.0-Q16-HDRI/convert.exe"})     #Setup for TextClip
reddit=praw.Reddit(
            client_id='iwEYw0KT5HXVRwWwHMCGIA',                                                                          #Setup for Reddit API, user:SV
            client_secret='RAxCEQKDmWbeHLXLek7dD5aXk7yGSw',
            username='SignoraValentine',
            password='tux9DtSBf@ZQp/p',
            user_agent='chrome:lurien_rdt:v1.0.0 (by:u/SignoraValentine)')





def text(Post, post_limit): #Remove post limit.
    for subreddit in Post.source:
        i=1
        for submission in reddit.subreddit(subreddit).top(time_filter=Post.top_filter, limit=post_limit):
            print(submission.title)    #Show the submission title as feedback.
            print(submission.selftext)
            i=i+1                      #Download respective images, gifs, videos, galleries. Increment marker for naming the file.
            print("----------------")



def video(Post):                        #Downloads top videos from the given subreddits that are cumulatively around the desired time limit.
    subreddits="+".join(Post.source)    #Create multi-reddit from selected subreddits. (All rankings below work on these multi-reddits)
    time_current=0                      #time_current holds total length of downloaded clips.
    i=1                                 #i increments by 1 after each download, is used for naming downloaded files.

    for submission in reddit.subreddit(subreddits).top(time_filter=Post.top_filter):        #In the desired multireddit, rank posts as top "weekly" or "daily" via top_filter
        if 'v.redd.it' in submission.url:                                                   #Filter the video posts:
            file = RedDownloader.Download(url=requests.get("https://www.reddit.com" + submission.permalink).url,    #Download the top videos
                output=f"{i}x",                                                                                     #Naming them as 1, 2, 3...
                destination=f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/",                   #Into this directory
                quality = 1080)                                                                                     #At this resolution
            
            video_clip=VideoFileClip(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}x.mp4")  #Taking the newly downloaded video.
            text_clip=TextClip(f"{submission.title}", font="Impact", fontsize=40, method="caption", align="North",
                                color="white", stroke_color="black", stroke_width=2, size=video_clip.size)\
                                .set_duration(organizer_general.Text_Clip_Length)           #Create post title clip to respective image clip.
            clip=CompositeVideoClip([video_clip, text_clip], size=video_clip.size)          #Overlay the text clip on to the gifclip.

            os.chdir(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}")   #Change Directory to export path. (Moviepy doesn't let you choose export path.)
            clip.write_videofile(f"{i}.mp4", codec='png')                                   #Convert composite video to video and save.
            sleep(1)                                                                        #Sleep 1 sec so saving and deleting don't overlap.
            os.remove(f"./{i}x.mp4")                                                        #Delete the raw video.
            os.chdir(f"../../../../../")                                                    #Go back to main directory.
            
            
            Post.yt_description+=f"\n{submission.author}"                                   #Add credits.
            time_current=time_current + clip.duration                                       #clip.duration gives newly downloaded video length in seconds.
            if time_current>Post.time_limit:                                                #if the cumulative length of the clips exceed the desired length, stop downloading.
                print(f"Downloaded Current Time: {time_current}")
                break
            
            i=i+1                                                                           #Increment marker for naming the videos.



def mixed(Post):                        #Downloads all images, gifs, videos (In case if used as gifs). Concatanates them into a video with a background music.
    subreddits="+".join(Post.source)    #Create multi-reddit from selected subreddits. (All rankings below work on these multi-reddits)
    time_current=0                      #time_current holds total length of downloaded clips.
    i=1                                 #i increments by 1 after each download, is used for naming downloaded files.

    for submission in reddit.subreddit(subreddits).top(time_filter=Post.top_filter):        #In the desired multireddit, rank posts as top "weekly" or "daily" via top_filter
        if 'v.redd.it' in submission.url:                                                   #Scrape the videos.

            file = RedDownloader.Download(url=requests.get("https://www.reddit.com" + submission.permalink).url,    #Download the top videos
                output=f"{i}x",                                                                                     #Naming them as 1, 2, 3...
                destination=f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/",                   #Into this directory
                quality = 1080)                                                                                     #At this resolution
            
            video_clip=VideoFileClip(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}x.mp4")  #Taking the newly downloaded video.
            text_clip=TextClip(f"{submission.title}", font="Impact", fontsize=40, method="caption", align="North",
                                color="white", stroke_color="black", stroke_width=2, size=video_clip.size)\
                                .set_duration(organizer_general.Text_Clip_Length)           #Create post title clip to respective video clip.
            clip=CompositeVideoClip([video_clip, text_clip], size=video_clip.size)          #Overlay the text clip on to the gifclip.

            os.chdir(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}")   #Change Directory to export path. (Moviepy doesn't let you choose export path.)
            clip.write_videofile(f"{i}.mp4", codec='png')                                   #Convert composite video to video and save.
            sleep(1)                                                                        #Sleep 1 sec so saving and deleting don't overlap.
            os.remove(f"./{i}x.mp4")                                                        #Delete the raw video.
            os.chdir(f"../../../../../")                                                    #Go back to main directory.

            time_current=time_current + clip.duration                                       #clip.duration gives newly downloaded video length in seconds.
            
            if time_current>=Post.time_limit:                                               #if the cumulative length of the clips exceed the desired length, stop downloading.
                print(f"Downloaded Current Time: {time_current}")
                break
            
            i=i+1                                                                           #Increment marker for naming the raw content.
        


        elif submission.url.endswith('.gif') or submission.url.endswith('.GIF') or submission.url.endswith('.gifv') or submission.url.endswith('.GIFV'):    #Scrape the gifs
            file = RedDownloader.Download(url=requests.get("https://www.reddit.com" + submission.permalink).url,    #Download the top gifs
                output=f"{i}",                                                                                      #Naming them as 1, 2, 3...
                destination=f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/",                   #Into this directory
                quality = 1080)                                                                                     #At this resolution
            
            gif_clip=VideoFileClip(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}.gif")     #Taking the newly downloaded gif.
            text_clip=TextClip(f"{submission.title}", font="Impact", fontsize=40, method="caption", align="North",
                                color="white", stroke_color="black", stroke_width=2, size=gif_clip.size)\
                                .set_duration(organizer_general.Text_Clip_Length)           #Create post title clip to respective gif clip.
            clip=CompositeVideoClip([gif_clip, text_clip], size=gif_clip.size)              #Overlay the text clip on to the gifclip.

            os.chdir(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}")   #Change Directory to export path. (Moviepy doesn't let you choose export path.)
            clip.write_videofile(f"{i}.mp4", codec='png')                                   #Convert gif to video and save.
            sleep(1)                                                                        #Sleep 1 sec so saving and deleting don't overlap.
            os.remove(f"./{i}.gif")                                                         #Delete the raw gif.
            os.chdir(f"../../../../../")                                                    #Go back to main directory.

            time_current=time_current + clip.duration                                       #clip.duration gives newly downloaded video length in seconds.
            
            if time_current>=Post.time_limit:                                               #if the cumulative length of the clips exceed the desired length, stop downloading.
                print(f"Downloaded Current Time: {time_current}")
                break
            
            i=i+1                                                                           #Increment marker for naming the raw content.



        elif 'i.redd.it' in submission.url:                                                 #Scrape the images
            file = RedDownloader.Download(url=requests.get("https://www.reddit.com" + submission.permalink).url,    #Download the top images
                output=f"{i}",                                                                                      #Naming them as 1, 2, 3...
                destination=f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/",                   #Into this directory
                quality = 1080)                                                                                     #At this resolution
            
            image_clip=ImageClip(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}.jpeg")\
                                .set_duration(organizer_general.Image_Clip_Length)          #Newly downloaded image to clip with set duration.
            text_clip=TextClip(f"{submission.title}", font="Impact", fontsize=40, method="caption", align="North",
                                color="white", stroke_color="black", stroke_width=2, size=image_clip.size)\
                                .set_duration(organizer_general.Text_Clip_Length)           #Create post title clip to respective image clip.
            clip=CompositeVideoClip([image_clip, text_clip], size=image_clip.size)          #Overlay the text clip on to the imageclip.

            os.chdir(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}")   #Change Directory to export path. (Moviepy doesn't let you choose export path.)
            clip.write_videofile(f"{i}.mp4", fps=12, codec='png')                           #Convert combined clip to mp4 and save.
            sleep(1)                                                                        #Sleep 1 sec so saving and deleting don't overlap.
            os.remove(f"./{i}.jpeg")                                                        #Delete the raw jpeg.
            os.chdir(f"../../../../../")                                                    #Go back to main directory.

            time_current=time_current + organizer_general.Image_Clip_Length                 #Updated final video length.
            
            if time_current>=Post.time_limit:                                               #if the cumulative length of the clips exceed the desired length, stop downloading.
                print(f"Downloaded Current Time: {time_current}")
                break
            
            i=i+1                                                                           #Increment marker for naming the raw content.
        


        else:                                                                               #Else if it is a gallery, skip.
            pass


        

