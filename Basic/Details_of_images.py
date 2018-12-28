from PIL import Image

im1 = Image.open("kajal.png")
im2 = Image.open("Kajal1.jpg")

print(im1.format, im1.size, im1.mode)
print(im2.format, im2.size, im2.mode)

#Transposing an image
out_flip_right = im1.transpose(Image.FLIP_LEFT_RIGHT)
#out_flip_right.show()


#Color transforms
'''
1 (1-bit pixels, black and white, stored with one pixel per byte)
L (8-bit pixels, black and white)
P (8-bit pixels, mapped to any other mode using a color palette)
RGB (3x8-bit pixels, true color)
RGBA (4x8-bit pixels, true color with transparency mask)
CMYK (4x8-bit pixels, color separation)
YCbCr (3x8-bit pixels, color video format)
Note that this refers to the JPEG, and not the ITU-R BT.2020, standard
LAB (3x8-bit pixels, the L*a*b color space)
HSV (3x8-bit pixels, Hue, Saturation, Value color space)
I (32-bit signed integer pixels)
F (32-bit floating point pixels)
'''
out_color_L = im1.convert("CMYK")
out_color_L.show()



