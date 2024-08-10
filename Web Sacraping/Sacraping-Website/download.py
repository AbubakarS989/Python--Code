import yt_dlp

video_url = 'https://www.youtube.com/watch?v=JR9NX2y7Ow8&t'  # Example video

ydl_opts = {
    'outtmpl': 'Sacraping-Website/end-to-end portfolio.mp4',  # Path and filename
    'format': 'bestaudio/best',  # Get the best quality audio and video
 
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print('Download completed.')
except Exception as e:
    print(f'Error: {e}')
