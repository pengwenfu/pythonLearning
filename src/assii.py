from PIL import Image
import  argparse

parser = argparse.ArgumentParser()
parser.add_argument('file') #输入文件
parser.add_argument('-o','--output') #输出文件
parser.add_argument('--width',type = int, default= 80) #输出宽
parser.add_argument('--height',type = int,default= 80,help=' output height of pitrue')
arges = parser.parse_args()
print(arges)
print(arges.file)
print(arges.width)
print(arges.height)
print(arges.output)

imgFile = arges.file
outFile = arges.output
width = arges.width
height = arges.height

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def getchar(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256 + 1) /length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':
    txt = ""
    try:
        im = Image.open(imgFile) #type:Image.Image
        im = im.resize((width, height), Image.NEAREST)

        for i in range(height):
           for j in range(width):
             txt += getchar(*im.getpixel((j, i)))
           txt += '\n'
        print(txt)
    except IOError as e:
        print('errrrrrr')
        quit(1)

    try:
        print('ready write file retult !')
        if outFile:
            with open(outFile, 'w') as  f:
                f.write(txt)
        else:
            with open('output.txt', 'w') as f:
                f.write(txt)
    except IOError as e:
        print(e)
