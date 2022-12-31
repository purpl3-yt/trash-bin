import cv2
import telebot
import time
from datetime import datetime
import random
API_TOKEN = None
bot = telebot.TeleBot(API_TOKEN)
start_time = time.time()
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 700)
ret, frame1 = cap.read()
ret, frame2 = cap.read()
while cap.isOpened():
    ret, frame = cap.read()
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None,iterations=3)
    сontours, _ = cv2.findContours(dilated, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in сontours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 3000:
            continue
        else:
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame1, "Status: {}".format("Motion!"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3,cv2.LINE_AA)
            cv2.drawContours(frame1, сontours, -1, (0, 255, 0), 2)
            if time.time() - start_time>3:
                cv2.imwrite('Capture.png', frame1)
                ret, frame = cap.read()
                nowtime = datetime.now()
                nowdate = str(nowtime)[0:10]
                nowtime1 = str(nowtime)[10:19]
                #bot.send_message(chat_id=0, text=(nowdate+nowtime1))
                #bot.send_photo(chat_id=0,photo=open('Capture.png','rb'))
                print('Detected Motion!')
                start_time = (time.time())
    cv2.imshow("frame1", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    ret, frame = cap.read()
    if cv2.waitKey(40) == 27:
        break
cap.release()
cv2.destroyAllWindows()