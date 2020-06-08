#!/usr/bin/env python3

import sys
import os

# testing
# sys.argv = ['asdf', '/home/chris/2020-05-11 11-40-57.mkv', '10.1:20.2', '25:28']
# sys.argv = ['asdf', '/home/chris/2020-05-11 11-40-57.mkv', ':20.2', '25:28']
# sys.argv = ['asdf', '/home/chris/b.mkv', '5:8', '10:']


def split_stamp(stamp_str):
    return map(lambda x: float(x) if not x == '' else None, stamp_str.split(':'))


if len(sys.argv) < 3:
    print('usage: ./video_cutter.py input.mp4 cut1start:cut1end [ ... cutistart:cutiend]')
    exit(1)

ffmpeg_cmd = 'ffmpeg'

in_path = sys.argv[1]
in_file = os.path.basename(in_path)
in_dir = os.path.dirname(in_path)
in_format = os.path.splitext(in_path)[1]
in_file_wo_format = in_file[:-len(in_format)]

out_suffix = 'cut'
temp_prefix = 'tmp'

segments = []

stamps_str = sys.argv[2:]
start, end = split_stamp(stamps_str[0])
if not (start == 0 or start is None):
    segments.append([0,start])
segments.append([end])

for stamp in stamps_str[1:]:
    start,end = split_stamp(stamp)
    segments[-1].append(start)
    segments.append([end])

start, end = split_stamp(stamps_str[-1])
if end is None:
    del segments[-1]
else:
    segments[-1].append(None)


print('Segments to be concatenated: %s'% (str(segments)))

segments_file = os.path.join(in_dir,temp_prefix+'_segments.txt')

with open(segments_file,'w+') as f:
    for seg_i, seg in enumerate(segments):
        seg_file = temp_prefix+'_seg_'+str(seg_i)+in_format
        f.write('file \'%s\' \n' % (seg_file))
        if seg[0] == 0: # this notation prevents loosing first keyframe of video somehow
            cmd = '%s -v 0 -y -i "%s" -c:v libx264 -c:a aac -strict experimental -b:a 128k -t %.2f "%s"' % \
                  (ffmpeg_cmd, in_path, seg[1], os.path.join(in_dir, seg_file))
        elif seg[1] is None:
            cmd = '%s -v 0 -y -i "%s" -c:v libx264 -c:a aac -strict experimental -b:a 128k -ss %.2f "%s"' % \
                  (ffmpeg_cmd, in_path, seg[0], os.path.join(in_dir, seg_file))
        else:
            cmd = '%s -v 0 -y -i "%s" -c:v libx264 -c:a aac -strict experimental -b:a 128k -ss %.2f -to %.2f "%s"' % \
                  (ffmpeg_cmd, in_path, seg[0], seg[1], os.path.join(in_dir, seg_file))
        print(cmd)
        os.system(cmd)

os.system('%s -v 0 -y -f concat -i "%s" -c copy "%s"' %
          (ffmpeg_cmd, segments_file, os.path.join(in_dir, in_file_wo_format+'_'+out_suffix+in_format)))

for seg_i, seg in enumerate(segments):
    seg_file = os.path.join(in_dir, temp_prefix + '_seg_' + str(seg_i) + in_format)
    os.system('rm '+seg_file)
os.system('rm '+segments_file)

pass