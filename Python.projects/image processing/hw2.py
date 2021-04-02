from PIL import Image,ImageFilter
import os
# display and open
'''
image1=Image.open('cat.jpg')
image1.show()
'''

# save
'''
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i=Image.open(f)
        fn,text=os.path.splitext(f)
        i.save('pngs/{}.png'.format(fn))


'''

# resize
'''
size_200=(200,200)
size_500=(500,500)
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i=Image.open(f)
        fn,text=os.path.splitext(f)
        i.thumbnail(size_500)
        i.save('500/{}_500{}'.format(fn, text))

        i.thumbnail(size_200)
        i.save('200/{}_200{}'.format(fn,text))
'''

# filter images
'''
image1=Image.open('cat.jpg')
image1.filter(ImageFilter.GaussianBlur(10)).save('cat.mod.jpg')
'''