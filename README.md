# MyExtentions

# run 
pip install -r .\requirement.txt

# get pip via
https://pip.pypa.io/en/stable/installing/

# requirement version
python >= 2.7

# usage 
usage: DownloadYoutubeList.py [-h] [--link LINK] [--type TYPE] [--quanlity QUANLITY]

optional arguments:
  -h, --help            show this help message and exit
  --link LINK, -l LINK  link of video
  --type TYPE, -t TYPE  Type of media: video or audio
  --quanlity QUANLITY, -q QUANLITY
                        Quanlity of media. 128kbps, 320kbps with audio and 360p, 720p with video

# example
python .\DownloadYoutubeList.py --link https://www.youtube.com/watch?v=BZq9FJzn1To --type audio

python .\DownloadYoutubeList.py --link https://www.youtube.com/watch?v=BZq9FJzn1To --type video --quanlity 720p

# why this repo exists
when you want to download high quality video, the default stream without its audio, you need this repo
it will automatically merge audio and video stream and bring you the high quanlity video with audio
Make sure you have time to wait when video and audio are merging! Sorry about that!

# Downloaded folder
video and audio folder will created automatically when you run download command