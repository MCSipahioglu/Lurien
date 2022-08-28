import praw





reddit=praw.Reddit(
            client_id='iwEYw0KT5HXVRwWwHMCGIA',                                                                          #Setup for Reddit API, user:SV
            client_secret='RAxCEQKDmWbeHLXLek7dD5aXk7yGSw',
            username='SignoraValentine',
            password='tux9DtSBf@ZQp/p',
            user_agent='chrome:lurien_rdt:v1.0.0 (by:u/SignoraValentine)')





def all(Post):
    post_reddit(Post)
    upvote_reddit(Post)
    post_instagram(Post)
    post_tiktok(Post)
    post_twitch(Post)



def post_reddit(Post):
    for ad_subreddit in Post.ad_subreddits:
        reddit.subreddit(ad_subreddit).submit(title=f"{Post.yt_title} is now live!", url=Post.yt_url)



def post_instagram(Post):
    pass



def post_tiktok(Post):
    pass



def post_twitch(Post):
    pass



def upvote_reddit(Post):
    pass



