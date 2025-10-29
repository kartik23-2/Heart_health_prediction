# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 01:39:51 2025

@author: karti
"""

import numpy as np
import pickle
import streamlit as st

## loading the saved model
loaded_model = pickle.load(open('C:/Users/karti/OneDrive/Model training/Heart_disease_prediction/heart_disease_model.sav', 'rb'))

# function for prediction

def heart_prediction(input_data):
    
   
    # changing the input_data to numpy array
    numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for one instance
    reshaped_data = numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(reshaped_data)
    
    print("The prediction is:", prediction)
    if (prediction[0] == 0):
        return "The person does not have a heart disease"
    else:
        return "The person has a heart disease"
    
    
def main():

   st.title('Heart Disease prediction app')
   
   
   #getting input
   

   wAge = st.number_input('Age : ', min_value=1.0, max_value=120.0, step = 1.0)
   
   st.markdown("'Male': 1, 'Female': 0")
   Sex = st.number_input('Gender : ', min_value=0, max_value=1,step = 1)
   
   st.markdown('"ASY": 0, "ATA": 1, "NAP": 2, "TA": 3')
   ChestPainType = st.number_input('chestpain type : ',step = 1)
   
   RestingBP = st.number_input('restingBP : ', min_value=0, max_value=250,step = 1)
   Cholesterol = st.number_input('Cholesterol : ', min_value=90, max_value=400,step = 1)
   FastingBS = st.number_input('Fasting Blood Sugar > 120 mg/dL', min_value=0, max_value=1,step = 1)
   
   st.markdown("'LVH': 0 , 'Normal': 1, 'ST': 2")
   RestingECG = st.number_input('RestingECG : ', min_value=0, max_value=2,step = 1)
   
   MaxHR = st.number_input('MaxHR : ', min_value=0, max_value=250,step = 1)
   
   st.markdown("'Yes': 1 , 'No': 0")
   ExerciseAngina = st.number_input('ExerciseAngina : ', min_value=0, max_value=1,step = 1)
   
   Oldpeak = st.number_input('Oldpeak : ', min_value=0.0, max_value=4.0,step = 0.1)
   
   st.markdown("'Down': 0 , 'Up': 1, 'Flat': 2")
   ST_Slope = st.number_input('ST_slope : ', min_value=0, max_value=2,step = 1)


   disease = ''
   
   #a button
   
   if st.button('disease check'):
       disease = heart_prediction([wAge, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope])


   st.success(disease)




if __name__ == '__main__':
    main()











    