# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('Models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('Models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('Models/parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open('Models/breast_cancer_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Health Diagnosis Predictor',
                          
                          ['Diabetes Predictor',
                           'Cardiac Disease Predictor',
                           'Parkinsons Disease Predictor',
                           'Breast Cancer Predictor'],
                          icons=['activity','heart','person','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Predictor'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies',value=6)
        
    with col2:
        Glucose = st.text_input('Glucose Level',value=148)
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value',value=72)
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value',value=35)
    
    with col2:
        Insulin = st.text_input('Insulin Level',value=0)
    
    with col3:
        BMI = st.text_input('BMI value',value=33.6)
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value',value=0.627)
    
    with col2:
        Age = st.text_input('Age of the Person',value=50)
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Cardiac Disease Predictor'):
    
    # page title
    st.title('Cardiac Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age',value=37)
        
    with col2:
        sex = st.text_input('Sex (1: Male and 0: Female)',value=1)
        
    with col3:
        cp = st.text_input('Chest Pain types',value=2)
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure',value=130)
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl',value=250)
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl',value=0)
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results',value=1)
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved',value=187)
        
    with col3:
        exang = st.text_input('Exercise Induced Angina',value=0)
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise',value=3.5)
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment',value=0)
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy',value=0)
        
    with col1:
        thal = st.text_input('thal( 0 = normal; 1 = fixed defect; 2 = reversable defect )',value=2)
        
        
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Cardiac Disease Test Result'):
        arr = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        heart_prediction = heart_disease_model.predict([arr])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Disease Predictor"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)',value=119.992)
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)',value=157.302)
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)',value=74.997)
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)',value=0.00784)
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)',value=0.00007)
        
    with col1:
        RAP = st.text_input('MDVP:RAP',value=0.00370)
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ',value=0.00554)
        
    with col3:
        DDP = st.text_input('Jitter:DDP',value=0.01109)
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer',value=0.04374)
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)',value=0.426)
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3',value=0.02182)
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5',value=0.0313)
        
    with col3:
        APQ = st.text_input('MDVP:APQ',value=0.02971)
        
    with col4:
        DDA = st.text_input('Shimmer:DDA',value=0.06545)
        
    with col5:
        NHR = st.text_input('NHR',value=0.02211)
        
    with col1:
        HNR = st.text_input('HNR',value=21.03300)
        
    with col2:
        RPDE = st.text_input('RPDE',value=0.414783)
        
    with col3:
        DFA = st.text_input('DFA',value=0.815285)
        
    with col4:
        spread1 = st.text_input('spread1',value=-4.81303)
        
    with col5:
        spread2 = st.text_input('spread2',value=0.266482)
        
    with col1:
        D2 = st.text_input('D2',value=2.301442)
        
    with col2:
        PPE = st.text_input('PPE',value=0.284654)
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


# Breast Cancer's Prediction Page
if (selected == "Breast Cancer Predictor"):
    
    # page title
    st.title("Breast Cancer Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        mr = st.text_input('Mean Radius',value=17.990000)
        
    with col2:
        mt = st.text_input('Mean Texture',value=10.380000)
        
    with col3:
        mp = st.text_input('Mean Perimeter',value=122.800000)
        
    with col4:
        ma = st.text_input('Mean Area',value=1001.000000)
        
    with col5:
        ms = st.text_input('Mean Smoothness',value=0.118400)
        
    with col1:
        mc = st.text_input('Mean Compactness',value=0.277600)
        
    with col2:
        mcon = st.text_input('Mean Concativity',value=0.300100)
        
    with col3:
        mcp = st.text_input('Mean Concave Points',value=0.147100)
        
    with col4:
        msym = st.text_input('Mean Symmetry',value=0.241900)
        
    with col5:
        mfd = st.text_input('Mean Fractional Dimension',value=0.078710)
        
    with col1:
        re = st.text_input('Radius Error',value=1.095000)
        
    with col2:
        te = st.text_input('Texture Error',value=0.905300)
        
    with col3:
        pe = st.text_input('Perimeter Error',value=8.589000)
        
    with col4:
        ae = st.text_input('Area Error',value=153.400000)
        
    with col5:
        se = st.text_input('Smoothness Error',value=0.006399)
        
    with col1:
        ce = st.text_input('Compactness Error',value=0.049040)
        
    with col2:
        cone = st.text_input('Concavity Error',value=0.053730)
        
    with col3:
        cpe = st.text_input('Concave Points Error',value=0.015870)
        
    with col4:
        syme = st.text_input('Symmetry Error',value=0.030030)
        
    with col5:
        fde = st.text_input('Fractal Dimension Error',value=0.006193)
        
    with col1:
        wr = st.text_input('Worst Radius',value=25.380000)
        
    with col2:
        wt = st.text_input('Worst Texture',value=17.330000)
    
    with col3:
        wp = st.text_input('Worst Perimeter',value=184.600000)
        
    with col4:
        wa = st.text_input('Worst Area',value=2019.000000)
        
    with col5:
        ws = st.text_input('Worst Smoothness',value=0.162200)

    with col1:
        wcom = st.text_input('Worst Compactness',value=0.665600)
        
    with col2:
        wcon = st.text_input('Worst Concavity',value=0.711900)
    
    with col3:
        wconp = st.text_input('Worst Concave Points',value= 0.265400)
        
    with col4:
        wsym = st.text_input('Worst Symmetry',value=0.460100)
        
    with col5:
        wfd = st.text_input('Worst Fractal Dimension',value=0.118900)

    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer's Test Result"):
        breast_cancer_prediction = breast_cancer_model.predict([[mr,mt,mp,ma,ms,mc,mcon,mcp,msym,mfd,re,te,pe,ae,se,ce,cone,cpe,syme,fde,wr,wt,wp,wa,ws,wcom,wcon,wconp,wsym,wfd]])                          
        
        if (breast_cancer_prediction[0] == 1):
          breast_cancer_diagnosis = "The Cancer is Benign"
        else:
          breast_cancer_diagnosis = "The Cancer is malignant"
        
    st.success(breast_cancer_diagnosis)
