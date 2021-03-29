from pytube import YouTube
from moviepy.editor import *
# from numba import jit, cuda
import sys
import argparse
import os
from os import path

# @cuda.jit
def removeFile(file):
    os.remove(file)

def func(stream, file_handle):
    video_just_audio = AudioFileClip(file_handle)
    audio = video_just_audio
    audio.write_audiofile('audio\\{0}.mp3'.format(file_handle.split('\\')[-1].split('.')[0]))

    if args.type == 'video':
        # #Set audio to video
        video = VideoFileClip(file_handle.replace('audio\\', ''))
        video_with_new_audio = video.set_audio(audio)
        video_with_new_audio.write_videofile(file_handle.replace('audio\\', 'final\\'))
        print('Done merge file!')
    else:
        os.remove(file_handle)
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--link', '-l', type=str, help='link of video')
    parser.add_argument('--type', '-t', help='Type of media: video or audio')
    parser.add_argument('--quantity', '-q', help='Quantity of media. 128kbps, 320kbps with audio and 360p, 720p with video')
    args = parser.parse_args()

    if not path.exists('audio'):
        os.mkdir('audio')
    if not path.exists('final'):
        os.mkdir('final')
    if not path.exists('video'):
        os.mkdir('video')

    if args.link is None:
        raise Exception('Not enough argument!')
    if args.type is None:
        args.type = 'audio'

    yt = YouTube(args.link) # get youtube link from stream
    # yt = yt.get('mp4', '720p')
    audioStream = yt.streams.filter(type='audio', abr='128kbps').first()
    if args.type == 'audio':
        print('Downloading audio!')
        yt.register_on_complete_callback(func)
        audioStream.download('audio')
    else:
        if args.quantity is None:
            args.quantity = '360p'
        videoStream = yt.streams.filter(file_extension='mp4', resolution=args.quantity)
        if len(videoStream) > 0:
            videoStream = videoStream.first()
            print(videoStream)
            videoStream.download('video')
            # yt = yt.order_by('resolution').desc()
            if not videoStream.is_progressive:
                yt.register_on_complete_callback(func)
                print('videoStream.is_progressive')
                audioStream.download('audio')