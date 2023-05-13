# Following program takes a folder as an input and adds a footer to the each supported image file
# Scaling is done by streching the footer to the width of the original image
# Footer is applied under the image, not on top of in the bottom of the image

from PIL import Image
import os
os.system("")

# Only following file formats can be converted using this program
# Change as your need
allowed = ['.bmp','.dds','.exif','.gif','jpg','.jpeg','.jp2','.jpx','.pcx','.png','.pnm','.ras','.tga','.tif','.tiff','.xbm','.xpm']

print('\n--------------- AddFooter.py ---------------')
print('This program adds a footer to all the images in a file\n')

directory   = input('Enter the directory          : ')
footer_path = input('Enter the path of the footer : ')
# footer_path = '<add your path here>'  # Uncomment if you're working only using one footer
                                        # Comment the line 2 lines before if you're uncommenting

os.chdir(directory)
dir_list  = os.listdir(directory)
work_list = []
os.mkdir('Done')                        # Creating a new folder 

# Sorting the image files
for i in dir_list:
    for j in allowed:
        if j in i:
            work_list.append(i)
work_items = len(work_list)
print('\n%d image files detected' %work_items)

i = 1
for k in work_list:
    # the Header
    footer = Image.open(footer_path)
    footer_width  = footer.size[0]
    footer_height = footer.size[1]

    appImage = Image.open(k)            # appImage stands for the image which the footer is applied to
    appImage_width  = appImage.size[0]
    appImage_height = appImage.size[1]

    # Resizing
    footer_newheight = int(footer_height*appImage_width/footer_width)
    footer_newwidth  = appImage_width
    footer = footer.resize((footer_newwidth,footer_newheight))

    # Canvas
    canvas = Image.new('RGB',(appImage_width,(appImage_height+footer_newheight)),(250,250,250))
    canvas.paste(appImage,(0,0))
    canvas.paste(footer,(0,appImage_height))

    # Saving the canvas
    os.chdir('Done')                    # Now in the new folder
    canvas_name = k[0:len(k)-4] + '.png' 
    canvas.save(canvas_name,'png')
    #canvas.show()                      # Uncomment if needed to show each image after done
    os.chdir('../')

    print(' %d of %s processed   ' %(i,work_items), end='\r')
    i+=1

print('\n\nDone!\n')