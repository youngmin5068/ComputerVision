# pascal-voc2012를 미리 다운받아놓습니다.
from ast import increment_lineno
import cv2
import matplotlib.pyplot as plt
import os
import xml.etree.ElementTree as ET

#default_dir = '/Users/gim-yeongmin/Git-youngmin/ComputerVision/ComputerVision/#2 Pascal_VOC_2012'
# img = cv2.imread(os.path.join(default_dir,'VOCdevkit/VOC2012/JPEGImages/2007_000032.jpg'))
# img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# print(img_rgb.shape)
# plt.figure(figsize=(8,8))
# plt.imshow(img_rgb)
# plt.show()

#VOC 저장된 로컬 내 위치
VOC_ROOT_DIR = "/Users/gim-yeongmin/Desktop/VOCdevkit/VOC2012/"

ANNO_DIR = os.path.join(VOC_ROOT_DIR,"Annotations")
IMAGE_DIR = os.path.join(VOC_ROOT_DIR,"JPEGImages")

xml_file = os.path.join(ANNO_DIR,"2007_000032.xml")

#XML파일을 파싱하여 element 생성
tree = ET.parse(xml_file)
root = tree.getroot()

#image 관련 정보는 root의 자식으로 존재
image_name = root.find('filename').text
full_image_name = os.path.join(IMAGE_DIR, image_name)

img = cv2.imread(full_image_name)
draw_image = img.copy()

green_color = (0,255,0)
red_color = (0,0,255)

#파일 내의 모든 object Element 찾기
object_list = []

for obj in root.findall('object'):
    xmlbox = obj.find('bndbox')

    left = int(xmlbox.find('xmin').text)
    top = int(xmlbox.find('ymin').text)
    right = int(xmlbox.find('xmax').text)
    bottom = int(xmlbox.find('ymax').text)

    class_name = obj.find('name').text

    cv2.rectangle(draw_image, (left,top),(right,bottom),color=green_color,thickness=1)
    cv2.putText(draw_image,class_name,(left,top-5),cv2.FONT_HERSHEY_SIMPLEX,0.4, red_color, thickness=1)

img_rgb = cv2.cvtColor(draw_image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8,8))
plt.imshow(img_rgb)
plt.show()

 