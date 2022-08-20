import os                           #For making directories
from datetime import date           #Daily dates for naming downloads.



#Global Variables
compilation_time_limit=30





#Classes
class class_post:
    def __init__(self,counter_index,schedule_days,top_filter,time_limit,raw_material,source_site,type,tag,source,post_title):
        self.counter_index = counter_index      #Index for external upload counter
        self.schedule_days = schedule_days      #Which days to post this content
        self.top_filter = top_filter            #Top Daily/Weekly/Yearly
        self.time_limit = time_limit            #Video Min Time Limit
        self.raw_material = raw_material        #Text/Image/Video
        self.source_site = source_site          #Source Site: Reddit/Imgur/Tumblr
        self.type = type                        #Compilation vs Short
        self.tag = tag                          #Folder Name
        self.source = source                    #Source subreddits
        self.post_title = post_title            #Youtube Post title







#Posts (After 50 different posts the counter list must be extended.)
Post_1=class_post(
            0,
            ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "day",
            compilation_time_limit,
            "video",
            "reddit",
            "compilations",
            "FunnyVideos",
            ['funnyvideos','funny'],
            "Reddit Funny Videos Compilation"
            )

Post_2=class_post(
            1,
            ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "day",
            compilation_time_limit,
            "video",
            "reddit",
            "compilations",
            "WhatCouldGoWrong",
            ['Whatcouldgowrong'],
            "Reddit Fails Compilation"
            )

Post_3=class_post(
            2,
            ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "day",
            compilation_time_limit,
            "video",
            "reddit",
            "compilations",
            "FunnyAnimals",
            ['FunnyAnimals'],
            "Funny Animals Compilation"
            )

Post_4=class_post(
            3,
            ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "day",
            compilation_time_limit,
            "image",
            "reddit",
            "compilations",
            "Memes",
            ['Memes'],
            "Funniest Memes Compilation"
            )

Post_list=[Post_1, Post_2, Post_3,Post_4]



#Methods
def create_folders(Post):
    try:
        os.makedirs(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}")    #If not existant create dated media folder
    except:
        pass

    try:
        os.makedirs(f"./upload/{date.today()}/youtube")                                     #and dated upload folders
    except:
        pass
        #os.makedirs(f"./upload/{date.today()}/instagram")







