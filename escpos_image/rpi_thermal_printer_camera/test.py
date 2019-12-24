import sys
import os
import datetime

img_dir = '/mnt/mmcblk0p2/own/img'
file_extension = 'jpg'
raspistill_arguments = ''
current_time_str = '{0:%Y-%m-%d_%H:%M:%S}'.format(datetime.datetime.now())


capture_cmd = 'raspistill '+raspistill_arguments+' -o '+os.path.join(img_dir,'img_'+current_time_str+'.'+file_extension)

os.system(capture_cmd)
