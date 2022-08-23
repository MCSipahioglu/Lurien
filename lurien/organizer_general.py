import os                           #For making directories
from datetime import date           #Daily dates for naming downloads.





#Global Variables
compilation_time_limit=600  #Final length (s)
Image_Clip_Length=10        #Image Clip Length (s)
Text_Clip_Length=4          #Text Clip Length (s)





#Classes
class class_post:
    def __init__(self,counter_index,schedule_days,top_filter,time_limit,raw_material,source_site,type,tag,source,post_title,audio=""):
        self.counter_index = counter_index      #Index for external upload counter
        self.schedule_days = schedule_days      #Which days to post this content
        self.top_filter = top_filter            #Top Daily/Weekly/Yearly
        self.time_limit = time_limit            #Video Min Time Limit
        self.raw_material = raw_material        #Text/Image/Video
        self.source_site = source_site          #Source Site: Reddit/Imgur/Tumblr
        self.type = type                        #Compilation vs Short
        self.tag = tag                          #Folder Name
        self.source = source                    #Source subreddits
        self.audio = audio                      #Audio name for image type posts. (Empty by default, used only when necessary)
        self.post_title = post_title            #Youtube Post title





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
            post_title=     "Funny Videos Compilation"
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
            source=         ['Whatcouldgowrong', 'therewasanattempt', 'instant_regret', 'holdmycosmo', 'Wellthatsucks', 'perfectlycutscreams', 'instant_regret'],
            post_title=     "Funniest Fails Compilation"
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
            audio=          "Pizzatron3000"
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
            audio=          "Pizzatron3000"
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
            source=         ['videos', 'vidid','woahdude','Damnthatsinteresting','NatureIsFuckingLit','nextfuckinglevel', 'BeAmazed', 'holdmyredbull', 'nonononoyes'],
            post_title=     "Today's Most Viral Videos Compilation"
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
            post_title=     "Oddly Satisfying Compilation"
            )

Post_list=[Post_1, Post_2, Post_3,Post_4,Post_5,Post_6]



#Methods
def create_folders(Post):
        os.makedirs(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}")    #If not existant create dated media folder
        os.makedirs(f"./upload/{date.today()}/youtube")                                     #and dated upload folders
        #os.makedirs(f"./upload/{date.today()}/instagram")



