import cv2
import time
import os
import mediapipe as mp

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=1, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
 
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
 
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
 
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img
 
    def findPosition(self, img, handNo=0, draw=True):
 
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
 
        return lmList
    
def Gesture(lmList):
    if len(lmList) != 0:
    #fingers = []
    
    # 手勢判別
        if (lmList[5][1] < lmList[17][1]):#手掌正反判別
            if (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] 
                and lmList[tipIds[1]][2] > lmList[tipIds[1]-2][2]
                and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2]
                and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                print(0)
                h, w, c = overlayList[0].shape
                img[0:h, 0:w] = overlayList[0]
            elif (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(1)
                  h, w, c = overlayList[1].shape
                  img[0:h, 0:w] = overlayList[1]
            elif (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(2)
                  h, w, c = overlayList[2].shape
                  img[0:h, 0:w] = overlayList[2]
            elif (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(3)
                  h, w, c = overlayList[3].shape
                  img[0:h, 0:w] = overlayList[3]
            elif (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2]):
                  print(4)
                  h, w, c = overlayList[4].shape
                  img[0:h, 0:w] = overlayList[4]
            elif (lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2]):
                  print(5)
                  h, w, c = overlayList[5].shape
                  img[0:h, 0:w] = overlayList[5]
            elif (lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] > lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2]):
                  print(6)
                  h, w, c = overlayList[6].shape
                  img[0:h, 0:w] = overlayList[6]
            elif (lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(7)
                  h, w, c = overlayList[7].shape
                  img[0:h, 0:w] = overlayList[7]
            elif (lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(8)
                  h, w, c = overlayList[8].shape
                  img[0:h, 0:w] = overlayList[8]
            elif (lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(9)
                  h, w, c = overlayList[9].shape
                  img[0:h, 0:w] = overlayList[9]
        
        elif (lmList[5][1] > lmList[17][1]):#手掌正反判別
            if (lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] 
                and lmList[tipIds[1]][2] > lmList[tipIds[1]-2][2]
                and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2]
                and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                print(0)
                h, w, c = overlayList[0].shape
                img[0:h, 0:w] = overlayList[0]
            elif (lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(1)
                  h, w, c = overlayList[1].shape
                  img[0:h, 0:w] = overlayList[1]
            elif (lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(2)
                  h, w, c = overlayList[2].shape
                  img[0:h, 0:w] = overlayList[2]
            elif (lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(3)
                  h, w, c = overlayList[3].shape
                  img[0:h, 0:w] = overlayList[3]
            elif (lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2]):
                  print(4)
                  h, w, c = overlayList[4].shape
                  img[0:h, 0:w] = overlayList[4]
            elif (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2]):
                  print(5)
                  h, w, c = overlayList[5].shape
                  img[0:h, 0:w] = overlayList[5]
            elif (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] > lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2]):
                  print(6)
                  h, w, c = overlayList[6].shape
                  img[0:h, 0:w] = overlayList[6]
            elif (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(7)
                  h, w, c = overlayList[7].shape
                  img[0:h, 0:w] = overlayList[7]
            elif (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(8)
                  h, w, c = overlayList[8].shape
                  img[0:h, 0:w] = overlayList[8]
            elif (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] 
                  and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]
                  and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]
                  and lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]
                  and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2]):
                  print(9)
                  h, w, c = overlayList[9].shape
                  img[0:h, 0:w] = overlayList[9]

    return img

#開啟鏡頭
cap = cv2.VideoCapture(0)
detector = handDetector()

folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)

#覆蓋
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image) 
print(len(overlayList))



#指尖ID:4=拇指、8=食指、12=中指、16=無名指、20=小指
tipIds = [4, 8, 12, 16, 20]

while(True):
  # 從攝影機擷取一張影像
  success, img = cap.read()
  #翻轉
  img = cv2.flip(img, 1)
  
  #偵測手部
  img = detector.findHands(img)
  #讀取手部關鍵點編號
  lmList = detector.findPosition(img)
  
  img = Gesture(lmList)

  # 顯示圖片
  cv2.imshow('frame', img)

  # 若按下 esc 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == 27:
    break

# 釋放攝影機
cap.release()
# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
    
    
    
    
    
