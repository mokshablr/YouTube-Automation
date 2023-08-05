import os

curr_dir=os.path.realpath(os.path.dirname(__file__))
backgrounds=curr_dir+'/backgrounds'
i=0
for file in os.listdir(backgrounds):
    i+=1
    os.rename(backgrounds+'/'+file, backgrounds+'/'+str(i)+'.mp4')