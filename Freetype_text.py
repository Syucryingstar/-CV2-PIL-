# -*- coding: utf-8 -*-
# @Time : 2019/5/14 1:15
# @Author : Syu
# tttttt

import face_recognition
import cv2
import  put_chinese_text

cap = cv2.VideoCapture(0)

#设置中文字体库
ft = put_chinese_text.put_chinese_text('msyh.ttf')

while (1):
    ret, frame = cap.read()

    ChineseFrame = frame  #Chinese窗口

    # 识别在视频帧所有的人脸
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # 在这个视频帧中循环遍历每个人脸
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = '文字'

        # 框住人脸的框
        cv2.rectangle(ChineseFrame, (left, top), (right, bottom), (0, 0, 255), 2)

        #CV2自带文字添加
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(cv2charimg, name, (left + 6, bottom - 6), font, 1.0,(255, 255, 255), 1)

        # 使用put_chinese_text向frame添加文字
        ChineseFrame = ft.draw_text(ChineseFrame, (right, bottom - 30), name, 20, (0, 255, 0))

    # Chinese窗口
    cv2.imshow('Chinese', ChineseFrame)

    #在窗口内按q退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
