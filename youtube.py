from pytube import YouTube
import sys

# Check if the user provided a valid link as an argument
if len(sys.argv) != 2:
    print("Usage: python script_name.py <youtube_link>")
    sys.exit(1)

# Get the YouTube link from the command line arguments
link = sys.argv[1]

try:
    # Create a YouTube object
    yt = YouTube(link)

    # Print video details
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the stream with the highest resolution
    yd = yt.streams.get_highest_resolution()

    # Download the video to the specified directory
    download_path = 'D:/Python'  # Change this path to your desired download location
    yd.download(download_path)

    print("Video downloaded successfully to:", download_path)

except HTTPError as e:
    if e.code == 410:
        print("The requested video is no longer available (HTTP 410: Gone).")
    else:
        print("An HTTP error occurred:", e)

except Exception as e:
    print("An error occurred:", str(e))
