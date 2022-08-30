#Primary Packages
from time import time                       #F
import praw                                 #For scraping Reddit (Gets urls of posts)
import requests                             #For getting Reddit media links (For feeding RedDownloader)
from RedDownloader import RedDownloader     #For downloading Reddit media
from moviepy.editor import *                #For determining video length, making clips from iamges.
from datetime import date                   #Daily dates for naming downloads.
from lurien import organizer_general        #Used for global variables.
from moviepy.config import change_settings  #Required to declare ImageMagick Binary for TextClips to work.
from time import sleep                      #Used for minor delays to prevent processing overlap.
from gtts import gTTS                       #For text to speech for the "text" type posts.
from mutagen.mp3 import MP3                 #Used for getting length of mp3.
import multiprocessing                      #For multithreading when exporting video.


change_settings({"IMAGEMAGICK_BINARY": r"./lurien_venv/ImageMagick-7.1.0-Q16-HDRI/ImageMagick-7.1.0-Q16-HDRI/convert.exe"})     #Setup for TextClip
reddit=praw.Reddit(
            client_id='iwEYw0KT5HXVRwWwHMCGIA',                                                                          #Setup for Reddit API, user:SV
            client_secret='RAxCEQKDmWbeHLXLek7dD5aXk7yGSw',
            username='SignoraValentine',
            password='tux9DtSBf@ZQp/p',
            user_agent='chrome:lurien_rdt:v1.0.0 (by:u/SignoraValentine)')





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

            #Break at desired time
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

            #Break at desired time
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

            #Break at desired time
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

            #Break at desired time
            time_current=time_current + organizer_general.Image_Clip_Length                 #Updated final video length.
            if time_current>=Post.time_limit:                                               #if the cumulative length of the clips exceed the desired length, stop downloading.
                print(f"Downloaded Current Time: {time_current}")
                break
            
            i=i+1                                                                           #Increment marker for naming the raw content.
        


        else:                                                                               #Else if it is a gallery, skip.
            pass

        

def text_with_stitching(Post):
    for submission in reddit.subreddit(Post.source).top(time_filter=Post.top_filter):       #Take just the top non-NSFW thread by breaking at the end.
        if submission.over_18:
            continue
        time_current=0                  #time_current holds total length of downloaded clips.
        i=1                             #Increment marker for naming the file.
        clip_list=[]                    #Define empty clip_list to collect all text_clips (moviepy class) into.

        Post.yt_description+=f"\n{submission.author}"                                       #Add credits.
        
        #Setup TTS and save TTS of title.
        tts=gTTS(text=submission.title, lang="en")
        tts.save(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}0.mp3")
        audio=MP3(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}0.mp3")
        time_current=time_current + audio.info.length                                       #Add tts clip length to total length.

        #Generate "screenshot" with text clip.
        text_clip=TextClip(f"{submission.title}", font="NotoSans-Bold", fontsize=40, method="caption", align="West",
                            color="white", bg_color="black", size=(1080,None))\
                            .set_duration(audio.info.length)                                #Create post title clip to respective tts length.
        tts_clip=AudioFileClip(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}0.mp3")
        clip=CompositeVideoClip([text_clip.set_position("center")], size=(1080,1920))       #Convert to video clip.
        clip=clip.set_audio(tts_clip)                                                       #Give text_clip sound
        clip_list.append(clip)                                                              #Add text with audio to clip_list.



        comments=submission.comments    #Get the comment tree
        for comment in comments:        #Get the comment

            if comment.body in ["[removed]", "[deleted]"]:                                  #Skip removed comments.
                continue
            
            i+=1                                                                            #Increment marker for naming the comments.

            Post.yt_description+=f"\n{comment.author}"                                      #Add credits.

            comment_paragraphs=comment.body.split("\n")                                     #Split long comments to paragraphs.
            while("" in comment_paragraphs):                                                #Remove empty lines
                comment_paragraphs.remove("")
            print(comment_paragraphs)
            j=0                                                                             #Increment marker for naming the paragraphs.
            for paragraph in comment_paragraphs:
                j+=1                                                                        #Increment paragraph counter for naming.

                #Setup TTS and save TTS of comments.
                tts=gTTS(text=paragraph, lang="en")
                tts.save(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}{j}.mp3")
                audio=MP3(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}{j}.mp3")
                time_current=time_current + audio.info.length                               #Add tts length to total current time.

                if j==1:
                    paragraph=f"u/{comment.author}\n" + paragraph                           #Add username to the first paragraph of split paragraph comments. (After tts is done, so it won't be read.)
                
                #Generate "screenshot" with text clip.
                text_clip=TextClip(f"{paragraph}", font="NotoSans-Medium", fontsize=40, method="caption", align="West",
                                    color="white", bg_color="black", size=(1080,None))\
                                    .set_duration(audio.info.length)                        #Create post title clip to respective tts length.
                tts_clip=AudioFileClip(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}{j}.mp3")
                clip=CompositeVideoClip([text_clip.set_position("center")], size=(1080,1920))#Convert to video clip.
                clip=clip.set_audio(tts_clip)                                               #Give text_clip sound
                clip_list.append(clip)                                                      #Add text with audio to clip_list.



            #Break if at desired time after each full comment.
            if time_current>Post.time_limit:                                                #if the cumulative length of the clips exceed the desired length, stop downloading.
                print(f"Downloaded Current Time: {time_current}")

                if Post.type == "shorts":
                    print("Removing last clip to make a short.")
                    clip_list = clip_list[: len(clip_list) - j]                             #Remove last comment if the last comment made us go overtime. (Equivalent to removing last j clips from clip list. (j is the number of paragraphs in the last comment))
                    time_current=time_current - audio.info.length
                    print(f"Final Time: {time_current}")

                break

        text_video_clip = concatenate_videoclips(clip_list,method="compose")                #Concatenate all text video clips (with audio) together.
        background_clip=VideoFileClip(f"./raw_background/exvid.mp4")                        #Taking the background video.
        final=CompositeVideoClip([background_clip.without_audio().resize( (1080,1920) ),text_video_clip])         #Overlay combined texts with audio onto background video.
        os.chdir(f"./upload/{date.today()}/compilations")                                   #Change Directory to export path. (Moviepy doesn't let you choose export path.)
        final.write_videofile(f"{Post.tag}.mp4", codec='png',
                                fps=60, preset="ultrafast",
                                threads=multiprocessing.cpu_count())                        #Export the final video
        os.chdir(f"../../../")                                                              #Go back to main directory.
        break                                                                               #Must break here so that after generating video from 1 non-NSFW post we exit.


