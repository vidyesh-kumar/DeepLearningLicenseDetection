from algorithm.object_detector import YOLOv7
from utils.detections import draw
from tqdm import tqdm
import cv2,json

yolov7 = YOLOv7()
ocr_classes=['plate']
yolov7.set(ocr_classes=ocr_classes)
yolov7.load('best.weights', classes='best.yaml', device='cpu') # use 'gpu' for CUDA GPU inference

video = cv2.VideoCapture(0)


if video.isOpened() == False:
	print('[!] error opening the video')

texts = {}

try:
    while video.isOpened():
        ret, frame = video.read()
        if ret == True:
            detections = yolov7.detect(frame, track=True)
            
            for detection in detections:
                if detection['class'] in ocr_classes:
                    detection_id = detection['id']
                    text = detection['text']
                    if len(text) > 0:
                        if detection_id not in texts:
                            texts[detection_id] = {
                                'most_frequent':{
                                    'value':'', 
                                    'count':0
                                }, 
                                'all':{}
                            }
                        
                        if text not in texts[detection_id]['all']:
                            texts[detection_id]['all'][text] = 0
                        
                        texts[detection_id]['all'][text] += 1

                        if texts[detection_id]['all'][text] > texts[detection_id]['most_frequent']['count']:
                            texts[detection_id]['most_frequent']['value'] = text
                            texts[detection_id]['most_frequent']['count'] = texts[detection_id]['all'][text]
                
                    if detection_id in texts:
                        detection['text'] = texts[detection_id]['most_frequent']['value']

            detected_frame = draw(frame, detections)
            print(json.dumps(detections, indent=4))
            cv2.imshow('webcam', detected_frame)
            cv2.waitKey(1)

except KeyboardInterrupt:
    pass

video.release()
yolov7.unload()