# import required model
from pytube import YouTube, Playlist

# Taking link from user
print("\n")
print("**********  Welcome to Ultimate Youtube Video Downloader   *********** ")
choice= input("Press 1 to download a single  Video or Press 2 to download a playlist : ")

def get_stream():
    """
    Asks the user for the desired stream quality and returns the corresponding string value.
    """
    print("Choose stream quality:")
    print("1. 1080p")
    print("2. 720p")
    print("3. 480p")
    print("4. 360p")
    print("5. 240p")
    print("6. 144p ")

    stream_choice = input("Enter your choice (1-6): ")

    if  stream_choice == "1":
        return "1080p"
    elif stream_choice == "2":
        return "720p"
    elif stream_choice == "3":
        return "480p"
    elif stream_choice == "4":
        return "360p"
    elif stream_choice == "5":
        return "240p"
    elif stream_choice == "6":
        return "144p"
    else:
        print("Invalid choice.")
        return None

if choice=="1":
    link = input("Enter a Link to Download the single video : ")
    youtube_1=YouTube(link)
    videos = youtube_1.streams.filter(res=get_stream())
    try:
        print(f"You are Downloading {youtube_1.title}")
        print("Downloading........")
        videos.first().download()
        print(f"Succesfully Downloaded {youtube_1.title} ")
        

    except Exception as e:
        print("Some Error Occured")



else:
    try:
        link = input("Enter a Link to Download the Playlist: ")
        playlist=Playlist(link)
        stream = get_stream()
        print(f"You are Downloading {playlist.title}")
        for video in playlist.videos:
            video.streams.filter(res=stream).first().download()
            print("Downloading........")
            print(f"Succesfully Downloaded {playlist.title}")
       
    
    except Exception as e:
        print("Some Error Occured")


