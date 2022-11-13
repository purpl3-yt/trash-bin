from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import tempfile
def create_image(filepath,name):
    img = Image.open(tempfile.gettempdir()+'temp.png')
    font = ImageFont.truetype('./assets/Latin_Font.ttf', size=20)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0),name,(255,255,255),font=font)
    done_savepath = str(name).rfind('.')
    img.save('./assets/'+name[:done_savepath]+'1'+'.png')

def convert_image(filepath):
    im = Image.open(filepath).convert('RGB')
    im.resize((500,500))
    im.save(tempfile.gettempdir()+'temp.png')