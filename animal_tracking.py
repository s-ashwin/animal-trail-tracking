from keras.models import load_model
import numpy as np
import cv2
from helper import getPredictionResult

model = load_model('keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

cap = cv2.VideoCapture(0)

while(True):
            ret, frame = cap.read()
            cv2.imshow('frame',frame)
    
            frame1 = cv2.resize(frame,(224, 224))
            image_array = np.asarray(frame1)

            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            data[0] = normalized_image_array

            prediction = model.predict(data)
            predictionArray =list(prediction[0])
            predictionResult = getPredictionResult(predictionArray)
            print(predictionResult)
            
            if cv2.waitKey(700) & 0xFF == ord('q'):
                break
    
cap.release()
cv2.destroyAllWindows()