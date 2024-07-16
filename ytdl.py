#! /usr/bin/python
"""Downloads a Youtube video in highest quality"""
import os
from sys import argv
from pathlib import Path
import ffmpeg
from pytubefix import YouTube

def video_audio_mux(path_audiosource, path_imagesource, out_video_path):
    """Download audio and video and merge with ffmpeg"""
    f_video = ffmpeg.input(path_imagesource).video
    f_audio = ffmpeg.input(path_audiosource).audio
    ffmpeg.output(f_audio, f_video, out_video_path, vcodec='copy', acodec='copy').run()

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
