# Lurien
Automated Youtube

## Composition
- lurien (Master Internal Package)
  - organizer_general
    - Holds the "Post" Class used throughout the code
    - Holds daily directory creation functions
  - scraper_reddit (Praw + Reddownloader)
    - .text
    - .image
    - .video(Post,top_filter,time_limit)
      -Downloads videos from Post.source that are cumulatively around the time_limit given.
  - scraper_tumblr
  - scraper_twitter
  - stitcher_general
    - Stitches clips at Post Directory and puts the final render into the upload directory.
  - upload_general
    - Calls upload youtube script 
  - upload_youtube
    - Script for uploading to youtube.
  
- lurien_venv (Holds External Packages, Increases Modularity)
- media (Holds Raw Data/Clips)
- music  (Holds Background Music)
- upload (Holds Final Renders Ready for Upload)
- lurien_main.py (Main Script to Run)


## Capabilities
-  



## DevLog
- Gmail account created
- Youtube channel created
- Reddit account created
- Reddit API registered
- scraper_reddit.video() created
  - Reddownloader can't choose "Top This Week" etc.
  - So posts are filtered using praw ("Top Daily" or "Top Weekly")
  - Checks if post is video (v.reddit.)
  - Download using Reddownloader if so.
  - Stop downloading when time_limit is exceeded.
- Built crude filing system
- Got access to Youtube API
- upload_general created
  - youtube (Uploads youtube post using upload_youtube.py) (6 video limit per day)

## To Do
- Added dated directorie to filing system



