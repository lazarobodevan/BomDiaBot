
from PIL import Image, ImageDraw, ImageFont

import textwrap
import io

class ImageHandling:

    def __init__(self):
        pass

    def writeImage(self,random_comment):
        lines = textwrap.wrap(random_comment, width=20)
        y_text = 150
        image = Image.open("fundo.png")
        font_type = ImageFont.truetype("arial.ttf",36)
        draw = ImageDraw.Draw(image)
        for line in lines:
            width, height = font_type.getsize(line)
            draw.text((580, y_text), line, font=font_type, fill="black")
            y_text += height
        file_like_object = io.BytesIO()
        image.save(file_like_object, 'png')
        file_like_object.seek(0)  # move to the beginning of file
        return file_like_object
        #image.show()
