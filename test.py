import os
from PIL import Image

path = "E:/study/chat-gpt/example1/"
for file in os.listdir(path):
    if file.endswith(".bmp"):
        img = Image.open(os.path.join(path, file))
        img.show()
        
a = 1
