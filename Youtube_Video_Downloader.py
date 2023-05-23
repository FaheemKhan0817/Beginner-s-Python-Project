from pytube import YouTube, Playlist
import pytube.exceptions

# Taking link from user
print("\n")

welcome_emoji = '\U0001F44B'  # Unicode for the waving hand emoji

print('\t\t'+welcome_emoji +'\t\t Welcome!' + welcome_emoji)

print("**********  Welcome to Ultimate Youtube Video Downloader   *********** ")
choice= input("Press 1 to download a single Video or Press 2 to download a playlist: ")


# To get Stream from user
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
    print("6. 144p")

    stream_choice = input("Enter your choice (1-6): ")

    if stream_choice == "1":
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


if choice == "1":
    link = input("Enter a Link to Download the single video: ")
    try:
        youtube_1 = YouTube(link)
        stream = get_stream()
        print(f"You are Downloading {youtube_1.title}")
        print("Downloading........")
        selected_stream = youtube_1.streams.get_by_resolution(stream)
        if selected_stream:
            selected_stream.download()
            print(f"Successfully Downloaded {youtube_1.title}")
        else:
            print(f"No {stream} stream available for {youtube_1.title}")

    except pytube.exceptions.VideoUnavailable:
        print("The video is unavailable.")

    except Exception as e:
        print("Some Error Occurred:", str(e))

else:
    link = input("Enter a Link to Download the Playlist: ")
    try:
        playlist = Playlist(link)
        stream = get_stream()
        print(f"You are Downloading {playlist.title}")
        for video in playlist.videos:
            try:
                selected_stream = video.streams.get_by_resolution(stream)
                if selected_stream:
                    selected_stream.download()
                    print("Downloading........")
                    print(f"Successfully Downloaded {video.title}")
                else:
                    print(f"No {stream} stream available for {video.title}")

            except pytube.exceptions.VideoUnavailable:
                print(f"Video '{video.title}' is unavailable.")

    except pytube.exceptions.PlaylistError:
        print("Invalid playlist.")

    except Exception as e:
        print("Some Error Occurred:", str(e))
