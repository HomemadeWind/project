import sys 
from Model import*
from tracker import* 
from PIL import Image
def main():
    tracker = EuclideanDistTracker()
    
 

    loaded_model = load_model()
    mixer.init()
    mixer.music.load(r"warning.mp3")
    mixer.music.set_volume(0.7)
    webcam=cv2.VideoCapture("car5.mp4")
    object_detector = cv2.createBackgroundSubtractorMOG2(history=100)
    # 1. Object Detection
    detections = []
    while True:
     ret,frame=webcam.read()
     if ret==True:
        mask = object_detector.apply(frame)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
        # Calculate area and remove small elements
         area = cv2.contourArea(cnt)
         if area > 30000:
             x, y, w, h = cv2.boundingRect(cnt)
             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
             detections.append([x, y, w, h])
             boxes_ids = tracker.update(detections)
             for box_id in boxes_ids:
              x, y, w, h, id = box_id
              
              input_image = frame[y:y+h,x:x+w]          
              img2 = cv2.resize(input_image, (228, 228))
              cv2.imshow("sub",img2)
              input_image = Image.fromarray(img2)
              feature_vector = pretrained_model.get_feature(input_image)
              prediction = loaded_model.predict([feature_vector])
              print(prediction)
              color = (0, 255, 0) 
              if prediction == 1 and (not mixer.music.get_busy()):
                color = (0, 0, 255)
                mixer.music.play(fade_ms=10)
                print("detected car")
                cv2.putText(frame, "car", (x+h+10, y-w), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
              else:
                color = (0, 255, 0)
             cv2.rectangle(frame, (x, y), (x + w, y + h),color, 3)
        cv2.imshow("cars",frame)
        key=cv2.waitKey(60) & 0xFF
   
main()
