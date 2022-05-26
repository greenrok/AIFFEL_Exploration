from PIL import Image
import glob
import os


files = glob.glob('C:/Users/eofhr/OneDrive/바탕 화면/Programming/AIFFEL/TON/mountain/*.jpg')
imgDir = 'C:/Users/eofhr/OneDrive/바탕 화면/Programming/AIFFEL/TON/mountain_512/'
if not os.path.isdir(imgDir) : # 폴더가 없으면 폴더 생성
    os.mkdir(imgDir)

imageNum = 0

for i in files:
  try:
    imageNum += 1
    img = Image.open(i)
    img_resize = img.resize((512,512))
    img_resize.save(imgDir + str(imageNum).zfill(4) + '.jpg')
    print(imageNum)
  except:
    pass