import cv2
import time

video_input_path = '/Users/gim-yeongmin/Git-youngmin/ComputerVision/ComputerVision/#3.Opencv_video_practice/Night_Day_Chase.mp4'
video_output_path = '/Users/gim-yeongmin/Git-youngmin/ComputerVision/ComputerVision/#3.Opencv_video_practice/Night_Day_Chase_output.mp4'
cap = cv2.VideoCapture(video_input_path)

#Codec은 *'XVID'로 설정
codec = cv2.VideoWriter_fourcc(*'XVID')

#round - 소수점 제거
vid_size = (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
vid_fps = cap.get(cv2.CAP_PROP_FPS)

vid_writer = cv2.VideoWriter(video_output_path,codec,vid_fps,vid_size)


green_color = (0,255,0)
red_color = (0,0,255)

start = time.time()
index = 0

while True:
  hasFrame,img_frame = cap.read()
  if not hasFrame:
    print("더이상 처리할 프레임이 없습니다.")
    break
  index += 1
  print('frame : ',index, '처리완료')

  cv2.rectangle(img_frame, (300,100,800,400),color=green_color, thickness=2)
  caption ="frame: {}".format(index)
  cv2.putText(img_frame, caption, (300,95),cv2.FONT_HERSHEY_SIMPLEX,0.7, red_color,1)

  vid_writer.write(img_frame)

print("write 완료시간 :", round(time.time()-start,4))
vid_writer.release()
cap.release()