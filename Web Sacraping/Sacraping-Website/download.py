import yt_dlp

video_url = 'https://www.youtube.com/watch?v=3vsC05rxZ8c&list=PLzMcBGfZo4-l5kVSNVKGO60V6RkXAVtp-'  # Example video

ydl_opts = {
    'outtmpl': 'Python-MySQL-Tutorial_v .mp4',  # Path and filename
    'format': 'best',  # Get the best quality audio and video
#  bestaudio
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print('Download completed.')
except Exception as e:
    print(f'Error: {e}')
