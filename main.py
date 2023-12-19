from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video import fx
import os
from helper import getDimensions as gd

# Uncomment for when the executable cannot be found in windows
# from moviepy.config import change_settings
# IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe')
# change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.0-Q16-HDRI\\magick.exe"})

# Get current, background and exports directories
curr_dir = os.path.realpath(os.path.dirname(__file__))
backgrounds = curr_dir+'/backgrounds/'
exports = curr_dir+'/exports/'
facts = curr_dir+'/facts/'

# Facts that are partitioned with a certain keyword/phrase
partition_can = ['b-test.txt', 'g-test.txt']
partition_but = ['psych-test.txt']
partition_like = ['relate-test.txt']

# Iterate through all the background videos
for i in range(1, len(os.listdir(backgrounds))+1):
    # TODO: Don't hardcode the filenames
    # Checking the file name
    # for j in ['b-test.txt', 'g-test.txt', 'psych-test.txt', 'relate-test.txt']:
    for j in ['g-test.txt']:  # for testing
        i = str(i)

        # Background video, 15 second clip
        background = VideoFileClip(backgrounds + i +'.mp4').subclip(0, 15)
        export_background = fx.all.crop(background, x1=gd.getX1(background), width=gd.getWidth(background))  # Helper
        
        
        # ****************************\\ FIX LATER //*****************************
        # Header Text
        # header=TextClip(txt='Girl Fact', font='Perpetua', fontsize=50, color='white', bg_color='black').set_position(('center', 200)).set_duration(15)

        # header_w, header_h = header.size
        # header_color_clip=ColorClip(size=(100,50), color='black').set_duration(5)  
        # ****************************\\ FIX LATER //***************************** 


        # Fact Text
        lines = []

        headerText = "Undefined"
        # Header Text
        if j == 'b-test.txt':
            headerText = 'Boy Fact'
        elif j == 'g-test.txt':
            headerText = 'Girl Fact'
        elif j == 'psych-test.txt':
            headerText = 'Psychology Fact'
        elif j == 'relate-test.txt':
            headerText = 'Relateable Fact'

        # Creating the header text
        header = TextClip(txt=headerText, font='Perpetua', fontsize=50, color='white', bg_color='black')
        header = header.set_position(('center', 200)).set_duration(15)

        # Read the fact files
        with open(facts+j, 'r') as fr:

            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1
            for line in lines:
                # we want to remove 1st line
                if ptr == 1 and line != '\n':
                    if j in partition_can:
                        x = line.partition('can')
                        inp1 = x[0]+x[1]
                        inp2 = x[-1]

                    elif j in partition_but:
                        x = line.partition('but,')
                        inp1 = x[0]+x[1]
                        inp2 = x[-1]

                    elif j in partition_like:
                        x = line.partition('like')
                        inp1 = x[0]+x[1]
                        inp2 = x[-1]

                    text1, text1b = gd.textClipGen(export_background, (inp1+'...'), 0)
                    text2, text2b = gd.textClipGen(export_background, (inp2), 7.5)

                    # text1 = TextClip(txt=inp1+"...", font='Impact', size=(export_background.w/2, 0), fontsize=50,
                    #                  color='white', method='caption').set_position(('center', 500)).set_duration(7.5)
                    # text1b = TextClip(txt=inp1+'...', font='Impact', size=(export_background.w/2, 0), fontsize=51, color='black',
                    #                   method='caption').margin(top=2, right=2, opacity=0).set_position(('center', 501)).set_duration(7.5)

                    # text2 = TextClip(txt=inp2, font='Impact', size=(export_background.w/2, 0), fontsize=50,
                    #                  color='white', method='caption').set_position(('center', 500)).set_duration(7.5).set_start(7.5)
                    # text2b = TextClip(txt=inp2, font='Impact', size=(export_background.w/2, 0), fontsize=51, color='black', method='caption').margin(
                    #     top=2, right=2, opacity=0).set_position(('center', 501)).set_duration(7.5).set_start(7.5)

                    # Merging all the layers, **the order matters here**.
                    final = CompositeVideoClip([export_background, header, text1b, text1, text2b, text2])
                    os.chdir(exports)
                    print(i, j[0])
                    final.write_videofile(j+i[:-4]+'.mp4')


print('out', len([name for name in os.listdir(backgrounds) if os.path.isfile(name)]))
