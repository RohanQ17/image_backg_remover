from rembg import remove
from PIL import Image

input_path = 'Timothee.png'
output_path = 'Timothee.png'

img = Image.open(input_path)
output = remove(img)
output.save(output_path)
Image.open(output_path)