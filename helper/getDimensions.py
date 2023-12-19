from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video import fx


# Width of the background video to convert it into 9:16 aspect ratio
def getWidth(videoClip: VideoFileClip):
    width = videoClip.h * (9/16)
    if width % 2 != 0:
        return int(width)+1
    else:
        return int(width)

# Get the start position x1 from the video
def getX1(videoClip: VideoFileClip): 
    width = getWidth(videoClip)
    mid = int(videoClip.w/2)
    return mid-width


# Crop the background to 9:16 aspect ratio
def backgroundCrop(videoClip: VideoFileClip):
    export_background = fx.all.crop(videoClip, x1=getX1(videoClip.h), width=getWidth(videoClip.h))

    return export_background

# Generate text to place on the video
def textClipGen(videoClip: VideoFileClip, text, start):
    fgText = TextClip(txt=text, font='Impact', size=(videoClip.w/2, 0), fontsize=50, color='white', method='caption').set_position(('center', 500)).set_duration(7.5).set_start(start)

    bgText = TextClip(txt=text, font='Impact', size=(videoClip.w/2, 0), fontsize=51, color='black', method='caption').set_position(('center', 500)).set_duration(7.5).set_start(start)

    return (fgText, bgText)
