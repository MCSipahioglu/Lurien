#Primary Packages
from lurien import *
from datetime import datetime
import pickle                   #For interacting with counter list.



counters=pickle.load(open("./lurien/upload_counter.pickle","rb"))#Load the counters from where they were left off.
i=0                                                             #Counter index

for Post in organizer_general.Post_list:                        #Iterating through multiple post types.
    if datetime.today().strftime('%A') in Post.schedule_days:   #If today is one of the scheduled days for that post:
        organizer_general.create_folders(Post)                  #First create necessary folders to organize raw files and upload files.

        if Post.raw_material == "video":                        #Then scrape, stitch and upload such posts. (With different methods depending on raw type)
            scraper_reddit.video(Post)
            stitcher_general.video(Post)
            upload_general.youtube(Post,counters[i])
            counters[i]=counters[i]+1
        elif Post.raw_material == "Image":
            pass
        elif Post.raw_material == "Text":
            #scraper_reddit.text(Post.raw_material)
            pass
    i=i+1


pickle.dump(counters,open("./lurien/upload_counter.pickle","wb"))#Save the updated counters.


