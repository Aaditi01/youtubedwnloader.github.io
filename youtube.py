from pytube import YouTube
link=("https://youtu.be/DmsOinqrPvQ")
youtube_1= YouTube(link)
videos=youtube_1.streams.all()
#videos=youtube_1.streams.filter(only_audio=True)
vid= list(enumerate(videos))
for i in vid:
    print(i)
print()
strm=int(input("enter:"))
videos[strm].download()
print("successfully")
#************ Playlist*********************
from pytube import Playlist

py= Playlist("https://youtube.com/playlist?list=PLgwJf8NK-2e7ocyYBq-Tv3tb2lR154p2H")
print(f'downloading :{py.title}')
for video in py.videos:
    video.streams.first().download()
 