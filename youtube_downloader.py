
from pytube import YouTube
from sys import argv

link = argv[1] # argv[1] first command line argument which we give when we run this program
youtube = YouTube(link)

print("Title: ", youtube.title)
print("Views: ", youtube.views)
print("Channel URL: ", youtube.channel_url)
print("Author: ", youtube.author)

youtube_download = youtube.streams.get_highest_resolution()

try:
    youtube_download.download('C:/Users/Marius/Desktop/download')
except:
    print("An error has occurred")
print("Download successfully")

