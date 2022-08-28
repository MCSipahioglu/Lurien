import os                                       #For making directories
from datetime import date                       #Daily dates for naming downloads.



#Global Variables
compilation_time_limit=30  #Final length (s)
Image_Clip_Length=10        #Image Clip Length (s)
Text_Clip_Length=4          #Text Clip Length (s)
Youtube_Description =  "The Internet Compiler welcomes you all.\n\
This isn't your first time watching our videos? Consider subscribing.\n\
You want your voice heard? Maybe leave a comment.\n\
Are you an Extra Awesome Person? Share this video with your friends.\n\
\n\
And as always you can turn on the notification bell to be alerted for our new videos.\n\
Thank you for watching and we hope to see you in another video. Salut.\n\
\n\
\n\
For the individual content in our compilations we don't claim any ownership. We just try to make surfing through the internet more efficient.\n\
For your copyright claims please mail to theinternetcompiler+copyrightresolution@gmail.com, our team will resolve the issue within 24 hours.\n\
\n\
\n\
Credits in Order (Created/Filmed/Shared by)\n\
-------------------------------------------"
Youtube_Keywords= "funny, compilation"



#Classes
class class_post:
    def __init__(self,counter_index,schedule_days,top_filter,time_limit,raw_material,source_site,type,tag,source,post_title,audio="",
                yt_title="", yt_description="", yt_category="24", yt_keywords="", yt_privacyStatus="public", yt_link="https://www.youtube.com/watch?v="):
        self.counter_index = counter_index      #Index for external upload counter
        self.schedule_days = schedule_days      #Which days to post this content
        self.top_filter = top_filter            #Top Daily/Weekly/Yearly
        self.time_limit = time_limit            #Video Min Time Limit
        self.raw_material = raw_material        #Text/Image/Video
        self.source_site = source_site          #Source Site: Reddit/Imgur/Tumblr
        self.type = type                        #Compilation vs Short
        self.tag = tag                          #Folder Name
        self.source = source                    #Source subreddits
        self.post_title = post_title            #Youtube Post title framework
        self.audio = audio                      #Audio name for image type posts. (Empty by default, used only when necessary)
        self.yt_title = yt_title                #Youtube Title (It is assigned automatically later using Post Title)
        self.yt_description = yt_description    #Youtube Description
        self.yt_category = yt_category          #Youtube Category (Set to entertainment by default)
        self.yt_keywords = yt_keywords          #Youtube Keywords (Set above)
        self.yt_privacyStatus = yt_privacyStatus#Youtube privacy status. (Set to public by default)
        self.yt_link = yt_link                  #Youtube link (Given the start of the url, the video id is added to the end of it after posting.)





#Posts (After 50 different posts the counter list must be extended.)
Post_1=class_post(
            counter_index=  0,
            schedule_days=  ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            top_filter=     "day",
            time_limit=     compilation_time_limit,
            raw_material=   "video",
            source_site=    "reddit",
            type=           "compilations",
            tag=            "FunnyVideos",
            source=         ['funny','funnyvideos', 'holdmybeer','Unexpected'],
            post_title=     "Funny Videos Compilation",
            yt_description= Youtube_Description,
            yt_keywords=    Youtube_Keywords
            )

Post_2=class_post(
            counter_index=  1,
            schedule_days=  ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            top_filter=     "day",
            time_limit=     compilation_time_limit,
            raw_material=   "video",
            source_site=    "reddit",
            type=           "compilations",
            tag=            "WhatCouldGoWrong",
            source=         ['Whatcouldgowrong', 'instant_regret', 'holdmycosmo', 'Wellthatsucks', 'perfectlycutscreams', 'WinStupidPrizes'],
            post_title=     "Funniest Fails Compilation",
            yt_description= Youtube_Description,
            yt_keywords=    Youtube_Keywords
            )

Post_3=class_post(
            counter_index=  2,
            schedule_days=  ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            top_filter=     "day",
            time_limit=     compilation_time_limit,
            raw_material=   "image",
            source_site=    "reddit",
            type=           "compilations",
            tag=            "FunnyImages",
            source=         ['PerfectTiming', 'trippinthroughtime', 'ATBGE', 'interestingasfuck', 'mildlyinteresting', 'woahdude'],
            post_title=     "Most Viral Images Compilation",
            audio=          "Pizzatron3000",
            yt_description= Youtube_Description,
            yt_keywords=    Youtube_Keywords
            )

Post_4=class_post(
            counter_index=  3,
            schedule_days=  ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            top_filter=     "day",
            time_limit=     compilation_time_limit,
            raw_material=   "image",
            source_site=    "reddit",
            type=           "compilations",
            tag=            "Memes",
            source=         ['memes','dankmemes','meme'],
            post_title=     "Funniest Memes Compilation",
            audio=          "Pizzatron3000",
            yt_description= Youtube_Description,
            yt_keywords=    Youtube_Keywords
            )

Post_5=class_post(
            counter_index=  4,
            schedule_days=  ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            top_filter=     "day",
            time_limit=     compilation_time_limit,
            raw_material=   "video",
            source_site=    "reddit",
            type=           "compilations",
            tag=            "ViralVideos",
            source=         ['videos', 'vidid','woahdude','MadeMeSmile','Damnthatsinteresting','NatureIsFuckingLit','nextfuckinglevel', 'BeAmazed', 'holdmyredbull', 'nonononoyes'],
            post_title=     "Today's Most Viral Videos Compilation",
            yt_description= Youtube_Description,
            yt_keywords=    Youtube_Keywords
            )

Post_6=class_post(
            counter_index=  5,
            schedule_days=  ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            top_filter=     "day",
            time_limit=     compilation_time_limit,
            raw_material=   "video",
            source_site=    "reddit",
            type=           "compilations",
            tag=            "OddlySatisfying",
            source=         ['oddlysatisfying'],
            post_title=     "Oddly Satisfying Compilation",
            yt_description= Youtube_Description,
            yt_keywords=    Youtube_Keywords
            )

Post_list=[Post_1, Post_2, Post_3,Post_4,Post_5,Post_6]

#Cute/Wholesome 'Eyebleach', 'cute', 


#Methods
def create_folders(Post):
        if not os.path.isdir(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}"):
                os.makedirs(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}")        #If not existant create dated media folder

        if not os.path.isdir(f"./upload/{date.today()}/youtube"):
                os.makedirs(f"./upload/{date.today()}/youtube")                                         #and dated upload folders
        #os.makedirs(f"./upload/{date.today()}/instagram")


