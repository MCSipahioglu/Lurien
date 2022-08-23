#Full Tutorial from: https://www.youtube.com/watch?v=aFwZgth790Q&ab_channel=TonyTeachesTech
#Also fixed "apiclient" module (outdated) as googleapiclient in the import section.
#Modified for use as a function instead of a script with help from: https://github.com/SteBurz/youtube-uploader
#For being able to upload custom thumbnails, you MUST verify your phone number from: YoutubeStudio->Settings->Channel->FeatureEligibility->IntermediateFeatures

import httplib2
import os
import random
import sys
import time
from datetime import date

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow



httplib2.RETRIES = 1
MAX_RETRIES = 10
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError)
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")

CLIENT_SECRETS_FILE = "./lurien/client_secrets.json"    #Use the client secrets file from this path.



def get_authenticated_service():                        #args passing has been removed.
  storage = Storage(f"./lurien/client-oauth2.json")     #Save and use the oauth file from this path.
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_UPLOAD_SCOPE)
    credentials = run_flow(flow, storage)

  return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=credentials)



def initialize_upload(youtube, Post):
  tags = None
  if Post.yt_keywords:
    tags = Post.yt_keywords.split(",")

  body=dict(
    snippet=dict(
      title=Post.yt_title,
      description=Post.yt_description,
      tags=tags,
      categoryId=Post.yt_category
    ),
    status=dict(
      privacyStatus=Post.yt_privacyStatus
    )
  )

  # Call the API's videos.insert method to create and upload the video.
  insert_request = youtube.videos().insert(
    part=",".join(body.keys()),
    body=body,
    media_body=MediaFileUpload(f"./upload/{date.today()}/youtube/{Post.tag}.mp4", chunksize=-1, resumable=True)
  )


  videoId=resumable_upload(insert_request)      #Upload the video and fetch back its ID.

  thumbnail_request=youtube.thumbnails().set(
  videoId = videoId,
  media_body=MediaFileUpload(f"./media/{date.today()}/{Post.source_site}/{Post.type}/{Post.tag}/thumbnail.png")
  )                                             #Create thumbnail upload request.
  thumbnail_request.execute()                   #Upload thumbnail


# This method implements an exponential backoff strategy to resume a failed upload.
def resumable_upload(insert_request):
  response = None
  error = None
  retry = 0
  while response is None:
    try:
      print("Uploading Video...")
      status, response = insert_request.next_chunk()
      if response is not None:
        if 'id' in response:
          print(f"Video id '{response['id']}' was successfully uploaded.")
          return response['id']
        else:
          exit(f"The upload failed with an unexpected response: {response}")
    except HttpError as e:
      if e.resp.status in RETRIABLE_STATUS_CODES:
        error = f"A retriable HTTP error {e.resp.status} occurred:\n{e.content}"
      else:
        raise
    except RETRIABLE_EXCEPTIONS as e:
      error = f"A retriable error occurred: {e}"

    if error is not None:
      print(error)
      retry += 1
      if retry > MAX_RETRIES:
        exit("No longer attempting to retry.")

      max_sleep = 2 ** retry
      sleep_seconds = random.random() * max_sleep
      print(f"Sleeping {sleep_seconds} seconds and then retrying...")
      time.sleep(sleep_seconds)



def main(Post):
  
  youtube = get_authenticated_service()          #Get the youtube object.

  try:
    initialize_upload(youtube, Post)
  except HttpError as e:
    print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")