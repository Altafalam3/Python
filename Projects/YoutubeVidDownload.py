from pytube import YouTube

link = "https://www.youtube.com/watch?v=GxaDVOpcX5Y&list=RDGxaDVOpcX5Y&start_radio=1"

yt=YouTube(link)
yt.streams.first().download()