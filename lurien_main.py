#Primary Packages
from lurien import *            #For everything else.
from datetime import datetime   #For scheduling purposes.



for Post in organizer_general.Post_list:                        #Iterating through multiple post types.
    if datetime.today().strftime('%A') in Post.schedule_days:   #If today is one of the scheduled days for that post:
        organizer_general.create_folders(Post)                  #First create necessary folders to organize raw files and upload files.

        if Post.raw_material == "video":                        #Then scrape, stitch and upload such posts. (With different methods depending on raw type)
            scraper_reddit.video(Post)
            stitcher_general.video(Post)
            uploader_general.youtube(Post)
            #pass
        elif Post.raw_material == "image":
            scraper_reddit.mixed(Post)
            stitcher_general.mixed(Post)
            uploader_general.youtube(Post)
            #pass
        elif Post.raw_material == "text":
            #scraper_reddit.text(Post.raw_material,post_limit)
            pass

        #advertiser_general.all(Post)




