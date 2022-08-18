#Primary Packages
from time import time
import praw                                 #For scraping Reddit (Gets urls of posts)
import requests                             #For getting Reddit media links (For feeding RedDownloader)
from RedDownloader import RedDownloader     #For downloading Reddit media
from moviepy.editor import VideoFileClip    #For determining video length
from datetime import date                   #Daily dates for naming downloads.



reddit=praw.Reddit(client_id='Dh7zCnkmEkfg3p8FPiBdSg',
            client_secret='p2oPRnTCTPqDdShCs-nb3i17FsAf3Q',
            client_username='SignoraValentine',
            password='tux9DtSBf@ZQp/p',
            user_agent='chrome:lurien_rdt:v1.0.0 (by:u/SignoraValentine)')





def text(subreddit_list,top_filter,post_limit):
    for subreddit in subreddit_list:
        i=1
        for submission in reddit.subreddit(subreddit).top(time_filter=top_filter,limit=post_limit):
            print(submission.title)                                                         #Show the submission title as feedback.
            print(submission.selftext)
            i=i+1                                                                 #Download respective images, gifs, videos, galleries. Increment marker for naming the file.
            print("----------------")





def image():
    print("scraper_reddit_image")





def video(Post):                        #Downloads top videos from the given subreddits that are cumulatively around the desired time limit.
    
    subreddits="+".join(Post.source)    #Create multi-reddit from selected subreddits. (All rankings below work on these multi-reddits)
    time_current=0                      #time_current holds total length of downloaded clips.
    i=1                                 #i increments by 1 after each download, is used for naming downloaded files.

    for submission in reddit.subreddit(subreddits).top(time_filter=Post.top_filter):    #In the desired multireddit, rank posts as top "weekly" or "daily" via top_filter
        if 'v.redd.it' in submission.url:                                               #Filter the video posts:

            file = RedDownloader.Download(url=requests.get("https://www.reddit.com" + submission.permalink).url ,   #Download the top videos
                output=f"{i}" ,                                                                                     #Naming them as 1, 2, 3...
                destination=f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/" ,                                         #Into this directory
                quality = 720)                                                                                      #At this resolution
            
            clip=VideoFileClip(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/{i}.mp4")         #Taking the newly downloaded video.
            time_current=time_current + clip.duration                       #clip.duration gives newly downloaded video length in seconds.
            
            if time_current>Post.time_limit:                                #if the cumulative length of the clips exceed the desired length, stop downloading.
                print(f"Downloaded Current Time: {time_current}")
                break
            
            i=i+1                                                           #Increment marker for naming the videos.