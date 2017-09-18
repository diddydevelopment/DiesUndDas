from PIL import Image
import numpy as np

width = 100
height = 100
img_depth = 10
depth = 20

min_depth = depth-img_depth
step_depth = img_depth / 255.0


im = Image.open("portrait.jpg")
im = im.resize((width,height))
imbw = im.convert('L') #convert to black and white 8bit
imbw = np.array(imbw,np.uint8) #convert it to numpy array

#imbw = 255 - imbw

stl_content = 'solid name';

for h in list(range(height-1))[::-1]:
    for w in range(width-1):
        u = imbw[h,w+1] * step_depth - imbw[h, w] * step_depth
        v = imbw[h+1,w] * step_depth - imbw[h, w] * step_depth
        nx = u
        ny = v
        nz = 1

        stl_content += 'facet normal '+str(nx)+' '+str(ny)+' '+str(nz)+'\nouter loop\n'
        stl_content += 'vertex '+str(w)+' '+str(h)+' '+str(imbw[h,w]*step_depth)+'\n'
        stl_content += 'vertex '+str(w+1)+' '+str(h)+' '+str(imbw[h,w+1]*step_depth)+'\n'
        stl_content += 'vertex '+str(w)+' '+str(h+1)+' '+str(imbw[h+1,w]*step_depth)+'\n'
        stl_content += 'endloop\nendfacet\n'

        u = imbw[h,w+1] * step_depth - imbw[h+1, w] * step_depth
        v = imbw[h+1,w+1] * step_depth - imbw[h+1, w] * step_depth
        nx = u
        ny = v
        nz = 1

        stl_content += 'facet normal '+str(nx)+' '+str(ny)+' '+str(nz)+'\nouter loop\n'
        stl_content += 'vertex '+str(w)+' '+str(h+1)+' '+str(imbw[h+1,w]*step_depth)+'\n'
        stl_content += 'vertex '+str(w+1)+' '+str(h)+' '+str(imbw[h,w+1]*step_depth)+'\n'
        stl_content += 'vertex '+str(w+1)+' '+str(h+1)+' '+str(imbw[h+1,w+1]*step_depth)+'\n'
        stl_content += 'endloop\nendfacet\n'

stl_content += 'endsolid name'





stl_file = open('output.stl','w')
stl_file.write(stl_content)
stl_file.close()