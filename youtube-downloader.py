from pytube import YouTube
link = input("Enter url / Donner une URL : ")
video= YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
