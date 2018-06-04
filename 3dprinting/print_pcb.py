from PIL import Image
import numpy as np

depth = 3

im = Image.open("eagle_export.png")
imbw = im.convert('L') #convert to black and white 8bit
imbw = np.array(imbw,np.uint8) #convert it to numpy array
imbw = 1 - (imbw/255.0) #flip colors
imbw = np.flip(imbw,axis=1)

#imbw = imbw > 0

dpi = 600
dpc = dpi / 2.54
ps = 10 / dpc #pixel size


stl_content = 'solid name';

height,width = imbw.shape

for h in range(height-1):
    for w in range(width-1):
        x = w * ps
        y = h * ps
        x_s = x - 0.5 * ps
        y_s = y - 0.5 * ps

        if imbw[h,w] == 1:
            stl_content += 'facet normal ' + str(0) + ' ' + str(0) + ' ' + str(1) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x_s) + ' ' + str(y_s) + ' ' + str(depth) + '\n'
            stl_content += 'vertex ' + str(x_s) + ' ' + str(y_s+ps) + ' ' + str(depth) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y_s) + ' ' + str(depth) + '\n'
            stl_content += 'endloop\nendfacet\n'
            stl_content += 'facet normal ' + str(0) + ' ' + str(0) + ' ' + str(1) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x_s) + ' ' + str(y_s+ps) + ' ' + str(depth) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y_s) + ' ' + str(depth) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y_s+ps) + ' ' + str(depth) + '\n'
            stl_content += 'endloop\nendfacet\n'
            stl_content += 'facet normal ' + str(0) + ' ' + str(0) + ' ' + str(-1) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x_s) + ' ' + str(y_s) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x_s) + ' ' + str(y_s+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y_s) + ' ' + str(0) + '\n'
            stl_content += 'endloop\nendfacet\n'
            stl_content += 'facet normal ' + str(0) + ' ' + str(0) + ' ' + str(-1) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x_s) + ' ' + str(y_s+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y_s) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y_s+ps) + ' ' + str(0) + '\n'
            stl_content += 'endloop\nendfacet\n'


        if imbw[h,w] == 0 and imbw[h,w+1] == 1:
            stl_content += 'facet normal ' + str(-1) + ' ' + str(0) + ' ' + str(0) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y+ps) + ' ' + str(depth) + '\n'
            stl_content += 'endloop\nendfacet\n'
            stl_content += 'facet normal ' + str(-1) + ' ' + str(0) + ' ' + str(0) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y) + ' ' + str(depth) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y+ps) + ' ' + str(depth) + '\n'
            stl_content += 'endloop\nendfacet\n'
        if imbw[h,w] == 1 and imbw[h,w+1] == 0:
            stl_content += 'facet normal ' + str(1) + ' ' + str(0) + ' ' + str(0) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y+ps) + ' ' + str(depth) + '\n'
            stl_content += 'endloop\nendfacet\n'
            stl_content += 'facet normal ' + str(1) + ' ' + str(0) + ' ' + str(0) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y) + ' ' + str(depth) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x_s+ps) + ' ' + str(y+ps) + ' ' + str(depth) + '\n'
            stl_content += 'endloop\nendfacet\n'
        if imbw[h,w] == 0 and imbw[h+1,w] == 1:
            stl_content += 'facet normal ' + str(0) + ' ' + str(-1) + ' ' + str(0) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x) + ' ' + str(y_s+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x+ps) + ' ' + str(y_s+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x+ps) + ' ' + str(y_s+ps) + ' ' + str(depth) + '\n'
            stl_content += 'endloop\nendfacet\n'
            stl_content += 'facet normal ' + str(0) + ' ' + str(-1) + ' ' + str(0) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x) + ' ' + str(y_s+ps) + ' ' + str(depth) + '\n'
            stl_content += 'vertex ' + str(x+ps) + ' ' + str(y_s+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x+ps) + ' ' + str(y_s+ps) + ' ' + str(depth) + '\n'
            stl_content += 'endloop\nendfacet\n'
        if imbw[h,w] == 1 and imbw[h+1,w] == 0:
            stl_content += 'facet normal ' + str(0) + ' ' + str(1) + ' ' + str(0) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x) + ' ' + str(y_s+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x+ps) + ' ' + str(y_s+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x+ps) + ' ' + str(y_s+ps) + ' ' + str(depth) + '\n'
            stl_content += 'endloop\nendfacet\n'
            stl_content += 'facet normal ' + str(0) + ' ' + str(1) + ' ' + str(0) + '\nouter loop\n'
            stl_content += 'vertex ' + str(x) + ' ' + str(y_s+ps) + ' ' + str(depth) + '\n'
            stl_content += 'vertex ' + str(x+ps) + ' ' + str(y_s+ps) + ' ' + str(0) + '\n'
            stl_content += 'vertex ' + str(x+ps) + ' ' + str(y_s+ps) + ' ' + str(depth) + '\n'
            stl_content += 'endloop\nendfacet\n'

stl_content += 'endsolid name'





stl_file = open('pcb_output.stl','w')
stl_file.write(stl_content)
stl_file.close()