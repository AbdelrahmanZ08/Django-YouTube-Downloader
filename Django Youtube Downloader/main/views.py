# views.py
from django.shortcuts import render
from yt_dlp import YoutubeDL


def index(request):
  return render(request, "index.html")


def result(request):
  if request.method == "POST":
    url = request.POST.get("video_url")

    if url:
      ydl_opts = {
    'quiet': True,
    'writethumbnail': True, 
    'outtmpl': 'thumbnail.%(ext)s', 
  }


  with YoutubeDL(ydl_opts) as ydl:
    try:
        video_info = ydl.extract_info(url, download=False)
        thumbnail_url = video_info.get('thumbnail')
        video_title = video_info.get('title')
        channel_name = video_info.get('channel')
        download_url = video_info.get('url')

        context = {
           "thumbnail_url" : thumbnail_url,
           "video_title" : video_title,
           "channel_name" : channel_name,
           "download_url" : download_url,
        }
        return render(request, "result.html", context)
    except Exception as e:
        error_message = str(e)
        return render(request, "index.html", {"e": error_message})

  return render(request, "index.html")