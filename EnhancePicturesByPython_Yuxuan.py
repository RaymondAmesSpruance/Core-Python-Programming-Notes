import PIL
import os
from PIL import ImageEnhance
from PIL import Image
A=Image.open('3.png')
enhancer = ImageEnhance.Sharpness(A)
B=enhancer.enhance(2)
enhancer = ImageEnhance.Brightness(B)
B=enhancer.enhance(2)
enhancer = ImageEnhance.Color(B)
B=enhancer.enhance(2)
Now_dir=os.getcwd()
outfile=os.path.join(Now_dir,'Afterenhance.png')
B.save(outfile,'png')