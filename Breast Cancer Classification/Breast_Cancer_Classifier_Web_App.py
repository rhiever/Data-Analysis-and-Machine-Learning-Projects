# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:59:27 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

#load the model
loaded_model = pickle.load(open("D:\Machine Learning with Python (Streamlit Deployed)\Breast Cancer Classification\Breast_Cancer_Classifier.sav",'rb'))

def breast_cancer_classifer(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'This is a Benign Tumour(Non-Cancerous)'
    else:
      return 'This is a Malignent Tumour(Cancerous)'

def main():
    
    #giving a title
    st.title('Breast Cancer Classifier Web App')
    
    #getting input from the user
    mean_radius = st.text_input("Mean Radius")
    mean_texture = st.text_input("Mean Texture")
    mean_perimeter = st.text_input("Mean Perimeter")
    mean_area = st.text_input("Mean Area")
    mean_smoothness = st.text_input("Mean Smoothness")
    
    #code for prediction
    diagnosis = ''
    
    # getting the input data from the user
    if st.button('Heart Disease Test Result : '):
        diagnosis = breast_cancer_classifer([mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness])
        
    st.success(diagnosis)

if __name__ == "__main__":
    main()