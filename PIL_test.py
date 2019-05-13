# -*- coding: utf-8 -*-
# @Time : 2019/5/13 16:06
# @Author : Syu

import face_recognition
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import  put_chinese_text

cap = cv2.VideoCapture(0)

#设置中文字体库
ft = put_chinese_text.put_chinese_text('msyh.ttf')
while (1):
    ret, frame = cap.read()

    PILFrame = frame  #PIL窗口
    ChineseFrame = frame  #chinese窗口

    # 识别在视频帧所有的人脸
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # 在这个视频帧中循环遍历每个人脸
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        name = 'unknow'
        # 框住人脸的框
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        #CV2自带文字添加
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(cv2charimg, name, (left + 6, bottom - 6), font, 1.0,(255, 255, 255), 1)

        # 图像从OpenCV格式转换成PIL格式
        img_PIL = Image.fromarray(cv2.cvtColor(PILFrame, cv2.COLOR_BGR2RGB))
        # PIL图片上打印汉字
        draw = ImageDraw.Draw(img_PIL) # 图片上打印
        font = ImageFont.truetype("msyh.ttf", 20, encoding="utf-8") # 参数1：字体文件路径，参数2：字体大小
        draw.text((left ,bottom, top, right), '文字', (255, 255, 255), font=font) # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
        # PIL图片转cv2 图片
        PIL = cv2.cvtColor(np.array(img_PIL), cv2.COLOR_RGB2BGR)

        #使用put_chinese_text
        color_ = (0, 255, 0)
        pos = (right, bottom - 30)
        text_size = 20
        #向frame添加文字
        image = ft.draw_text(ChineseFrame, pos, name, text_size, color_)

    #pil窗口
    cv2.imshow("PIL", PIL)

    # chinese窗口
    cv2.imshow('Chinese',image)

    #在窗口内按q退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
