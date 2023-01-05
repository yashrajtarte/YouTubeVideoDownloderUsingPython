from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Error Downloading your video !!!")
    print("Downloading is been completed !")

link = input("Youtube URL:")
Download(link)
