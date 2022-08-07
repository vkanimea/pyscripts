# Install these library modules first 
# Python Youtube library
# pip install pytube 
# Python Certifi library for SSL 
# pip install certifi 

from pytube import YouTube
from sys import argv
from pytube import Playlist
import glob
import os

link = argv[1]
yt = YouTube(link)
dirstore = 'c:/temp/youtube'

print("Title: ", yt.title)
print("View: ", yt.views)

#yd = yt.streams.get_highest_resolution()
yd = yt.streams.filter(progressive=True).last()

#pl = yt.playlist.download_all()


# ADD FOLDER HERE
yd.download(dirstore)

# Print latest downloaded file
list_of_files = glob.glob(dirstore+'/*.mp4')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)