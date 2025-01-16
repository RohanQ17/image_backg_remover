from rembg import remove
from PIL import Image

input_path = 'TimotheeChamalet.png'
output_path = 'TimotheeChamalet.png'

img = Image.open(input_path)
output = remove(img)
output.save(output_path)
Image.open(output_path)