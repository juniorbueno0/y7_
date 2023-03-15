from pathlib import Path
from subprocess import call
import os

def pathToText(path):
    vid=[]
    for i in range(len(str(path))):
        if(i>=48):
            vid.append(str(path)[i])
    vid=str(vid).replace(", ",""); vid = vid.replace("''","");vid = vid.replace("['","");vid = vid.replace("']","")
    return vid

def videoSelect(rawvid):

    if len(os.listdir(rawvid)) != 0:
        directory = rawvid
        pendinglist = Path(directory).glob('*.mp4')
    
        for path in pendinglist:
            vid=pathToText(path)
            #print(path)
            print("raw_videos:",vid)
            call('python youtubeDetect.py --weights yolov7-tiny.pt --conf 0.4 --img-size 640 --source /home/ubuntu/scripts/py3.9.12/y7/youtube/videos/{}'.format(vid))
            #os.remove(path)
    else:
        print('video directory is empty')

if __name__ == '__main__':
    rawvid = Path('/home/ubuntu/scripts/py3.9.12/y7/youtube/videos/')
    print(rawvid)
    videoSelect(rawvid)