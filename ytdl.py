#! /usr/bin/python
from pytube import YouTube
from pathlib import Path
from sys import argv
import os, ffmpeg

def video_audio_mux(path_audiosource, path_imagesource, out_video_path):
    video = ffmpeg.input(path_imagesource).video
    audio = ffmpeg.input(path_audiosource).audio
    ffmpeg.output(audio, video, out_video_path, vcodec='copy', acodec='copy').run()

dl_dir = Path.home() / 'Downloads'
video = YouTube(argv[1])

print("Title: ", video.title)
print("Author: ", video.author)
print("Length: ", video.length)

yd = video.streams.filter(adaptive=True).first()
ad = video.streams.get_audio_only()

vsource = yd.download(dl_dir,filename_prefix='tmp_vid_')
asource = ad.download(dl_dir,filename_prefix='tmp_audio_')
video_audio_mux(asource,vsource,f'{dl_dir}/{str(video.title)}.mkv')
os.unlink(vsource)
os.unlink(asource)
