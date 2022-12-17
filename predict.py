import pandas as pd
import numpy as np
import pickle

# Load the data
loaded_model = pickle.load(open('C:/Users/Tachiii/Documents/PERMODELAN SIMULASI/lab/deploy/trained_breastcancer_model.sav', 'rb'))

# predict data
data_to_test = [[13.08,15.71,85.63,520,0.1075,0.127,0.04568,0.0311,0.1967,0.06811,0.1852,0.7477,1.383,14.67,0.004097,0.01898,0.01698,0.00649,0.01678,0.002425,14.5,20.49,96.09,630.5,0.1312,0.2776,0.189,0.07283,0.3184,0.08183]]

knn_predict = loaded_model.predict(data_to_test)
print(knn_predict)
if (knn_predict[0] == 'M'):
    print("Predicted class: Malignant")
else:
    print("Predicted class: Benign")    