from keras.models import load_model
import numpy as np
import cv2, mysql.connector
from helper import getPredictionResult

model = load_model('keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

cap = cv2.VideoCapture(0)

insertStatement = "INSERT INTO classification_data (id,image,prediction_result,location) VALUES (%s,%s,%s,%s)"

try:
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="AnimalTrailTracking",
        )
    mycursor = mydb.cursor()
    print("CONNECTED")
except Exception as e: 
    print("Connection - Failed ", e)

def insertData(image,prediction_result):
    try:
        val = (None,image,prediction_result,"Camera 1")
        mycursor.execute(insertStatement, val)
        mydb.commit()
        print("Data Uploaded")
        
    except Exception as e: 
        print("Data Upload - Failed ", e)
      

while(True):
            ret, frame = cap.read()
            cv2.imshow('frame',frame)
    
            resized_image = cv2.resize(frame,(224, 224))
            image_array = np.asarray(resized_image)

            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            data[0] = normalized_image_array

            prediction = model.predict(data)
            predictionArray =list(prediction[0])
            predictionResult = getPredictionResult(predictionArray)
            print(predictionResult)
            insertData((cv2.imencode('.jpg',resized_image))[1].tobytes(),predictionResult)
            
            if cv2.waitKey(700) & 0xFF == ord('q'):
                break
    
cap.release()
cv2.destroyAllWindows()
mycursor.close()
mydb.close()