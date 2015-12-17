# anly_image.py
#!/usr/bin/env python
#encoding=utf-8
 
import image,imageEnhance,imageFilter
import sys
 
image_name = "./images/81.jpeg"
im = Image.open(image_name)
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')