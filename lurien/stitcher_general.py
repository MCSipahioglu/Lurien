import os
import glob
from moviepy.editor import *
from datetime import date               #Daily dates for naming downloads.





def text():
    print("Stitcher Text (Text Image, Background, TTS")



def mixed(Post):                                                  #Makes a video out of silent clips in a directory. (Directory name corresponds to Post class' elements)
    try:
        clip_path_list=glob.glob(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/*.mp4")    #Makes a (path string) list of all mp4 files in such directory
        clip_list=[]                                                #Define empty clip_list to collect all video_clips (moviepy class) into

        for clip_path in clip_path_list:                            #Taking one clip's path
            video_clip=VideoFileClip(clip_path)                     #Define that path as a clip
            clip_list.append(video_clip)                            #Add the video_clip to clip_list
        
        final_no_audio = concatenate_videoclips(clip_list,method="compose")                     #Concatenate all clips into an audioless video
        audio=AudioFileClip(f"./music/{Post.audio}.mp3").set_duration(final_no_audio.duration)  #Create audioclip at the video length.
        final=final_no_audio.set_audio(audio)                       #Combine video and audio.
        os.chdir(f"./upload/{date.today()}/youtube")                #Change Directory to export path. (Moviepy doesn't let you choose export path.)
        final.write_videofile(f"{Post.tag}.mp4")                    #Export the final video
        os.chdir(f"../../../")                                      #Go back to main directory.
    except:
        pass



def video(Post):                                                #Makes a video out of clips in a directory. (Directory name corresponds to Post class' elements)
    try:
        clip_path_list=glob.glob(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/*.mp4")    #Makes a (path string) list of all mp4 files in such directory
        clip_list=[]                                                #Define empty clip_list to collect all video_clips (moviepy class) into

        for clip_path in clip_path_list:                            #Taking one clip's path
            video_clip=VideoFileClip(clip_path)                     #Define that path as a clip
            clip_list.append(video_clip)                            #Add the video_clip to clip_list

        final = concatenate_videoclips(clip_list,method="compose")  #Concatenate all clips into a video
        os.chdir(f"./upload/{date.today()}/youtube")                #Change Directory to export path. (Moviepy doesn't let you choose export path.)
        final.write_videofile(f"{Post.tag}.mp4")                    #Export the final video
        os.chdir(f"../../../")                                      #Go back to main directory.
    except:
        pass



