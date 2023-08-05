from moviepy.editor import * #VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video import fx
from moviepy.config import change_settings
import os
IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe')
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.0-Q16-HDRI\\magick.exe"})


curr_dir=os.path.realpath(os.path.dirname(__file__))
backgrounds=curr_dir+'/backgrounds'
exports=curr_dir+'/exports'
i=0
# for file in os.listdir(backgrounds):
def get_w(height):
    width=height*(9/16)
    if width%2!=0:
        return int(width)+1
    else:
        return int(width)

def get_x1_bg(height):
    width=get_w(height)
    mid=int(background.w/2)
    return mid-width

partition_can = ['b-test.txt', 'g-test.txt']
partition_but = ['psych-test.txt']
partition_like= ['relate-test.txt']

for i in range(1, len(os.listdir(backgrounds))+1):
    for j in ['b-test.txt', 'g-test.txt', 'psych-test.txt', 'relate-test.txt']:
        i=str(i)
        #background video
        background = VideoFileClip(backgrounds+ '/'+i+'.mp4').subclip(0,15)
        export_background= fx.all.crop(background, x1=get_x1_bg(background.h), width= get_w(background.h))

        #Header Text
        # header=TextClip(txt='Girl Fact', font='Perpetua', fontsize=50, color='white', bg_color='black').set_position(('center', 200)).set_duration(15)

        # header_w, header_h = header.size
        # header_color_clip=ColorClip(size=(100,50), color='black').set_duration(5)  ****************************\\ FIX LATER //*****************************

        #Fact Text
        lines=[]
        
        #Header Text
        if j=='b-test.txt':
            header=TextClip(txt='Boy Fact', font='Perpetua', fontsize=50, color='white', bg_color='black').set_position(('center', 200)).set_duration(15)
        elif j=='g-test.txt':
            header=TextClip(txt='Girl Fact', font='Perpetua', fontsize=50, color='white', bg_color='black').set_position(('center', 200)).set_duration(15)
        elif j=='psych-test.txt':
            header=TextClip(txt='Psychology Fact', font='Perpetua', fontsize=50, color='white', bg_color='black').set_position(('center', 200)).set_duration(15)
        elif j=='relate-test.txt':
            header=TextClip(txt='Relateable Facts', font='Perpetua', fontsize=50, color='white', bg_color='black').set_position(('center', 200)).set_duration(15)


        with open(curr_dir+'/Facts/'+j, 'r') as fr:
            # reading line by line
            lines = fr.readlines()
            # pointer for position
            ptr = 1
            # opening in writing mode
            with open(curr_dir+'/Facts/'+j, 'w') as fw:
                for line in lines:
                    # we want to remove 1st line
                    if ptr==1 and line !='\n':
                        if j in partition_can:
                            x=line.partition('can')
                            inp1=x[0]+x[1]
                            inp2=x[-1]
                            
                        elif j in partition_but:
                            x=line.partition('but,')
                            inp1=x[0]+x[1]
                            inp2=x[-1]

                        elif j in partition_like:
                            x=line.partition('like')
                            inp1=x[0]+x[1]
                            inp2=x[-1]
                            
                        text1=TextClip(txt=inp1+'...', font='Impact', size = (export_background.w/2,0),fontsize=50, color='white', method = 'caption').set_position(('center', 500)).set_duration(7.5)
                        text1b=TextClip(txt=inp1+'...', font='Impact', size = (export_background.w/2,0),fontsize=51, color='black', method = 'caption').margin(top=2, right=2,opacity=0).set_position(('center', 501)).set_duration(7.5)
                        
                        text2=TextClip(txt=inp2, font='Impact', size = (export_background.w/2,0),fontsize=50, color='white', method = 'caption').set_position(('center', 500)).set_duration(7.5).set_start(7.5)
                        text2b=TextClip(txt=inp2, font='Impact', size = (export_background.w/2,0),fontsize=51, color='black', method = 'caption').margin(top=2, right=2,opacity=0).set_position(('center', 501)).set_duration(7.5).set_start(7.5)
                        
                        final= CompositeVideoClip([export_background, header, text1b, text1, text2b, text2])
                        os.chdir(exports)
                        print(i,j[0])
                        final.write_videofile(j+i+'.mp4')

                    if ptr != 1 and line!='\n':
                        fw.write(line)
                    ptr += 1


        

print('out',len([name for name in os.listdir(backgrounds) if os.path.isfile(name)]))