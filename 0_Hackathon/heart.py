import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
import pickle

# Model
model = pickle.load(open('rf_model.pkl','rb'))

# Heart page
def heart_page():
    st.title("Department of Cardiology")

    nav = dept_navigation()
    if nav =="Diagnosis":
        heart_diag()

    elif nav =="Analysis":
        heart_analysis()

    elif nav =="Data":
        heart_data()
    
    elif nav == "Bio-Interval":
        heart_bio_interval()

# Department Navigation code
def dept_navigation():
    navigate = option_menu(None,
                           ["Diagnosis","Bio-Interval","Analysis","Data"],
                           icons = ["gear-fill","shield-fill-plus","bar-chart-fill","card-heading"],
                           orientation="horizontal")
    return navigate

# -------------------------------------------------------------------------------------------

# Heart disease Diagnosis
def heart_diag():
    with st.form(key="Diagnose",clear_on_submit=True):
        age = st.number_input("Age",min_value=1,max_value=90)

        gender =st.selectbox("Gender",["Male","Female"])
        if gender=="Male":
            gender=1
        else:
            gender=0
        

        chest_pain_type=st.selectbox("Chest Pain Type",
                                    ["None","Typical Angina","Atypical Angina","Non Anginal Pain","Asymotomatic Pain"])
        if chest_pain_type=='Atypical Angina':
            cpt_Ata = 1 
        else :
            cpt_Ata = 0

        if chest_pain_type=='Non Anginal Pain':
            cpt_nap = 1
        else :
            cpt_nap = 0

        if chest_pain_type=='Typical Angina':
            cpt_ta = 1
        else :
            cpt_ta = 0 


        resting_bp =st.number_input("Resting BP")


        cholesterol = st.number_input("Cholesterol")
        
        fasting_bs = st.selectbox("Fasting Blood Sugar",
                                 ["Fasting Blood Sugar > 120 mg/dl","Fasting Blood Sugar < 120 mg/dl"])
        if fasting_bs=="Fasting Blood Sugar > 120 mg/dl":
            fasting_bs = 1 
        else :
            fasting_bs = 0
        

        resting_ecg =st.selectbox("Resting ECG",["Normal","ST","LVH"])
        if resting_ecg == "Normal":
            resting_ecg_n = 1 
        else :
            resting_ecg_n = 0

        if resting_ecg == "ST":
            resting_ecg_st = 1 
        else :
            resting_ecg_st = 0

        max_hr =st.number_input("Max Heart Rate")
        
        exercise_angina = st.selectbox("Exercise Angina",["Yes","No"])
        if exercise_angina=='Yes':
            exercise_angina = 1 
        else :
            exercise_angina = 0
        
        oldpeak =st.number_input("Old Peak")
        
        St_slop = st.selectbox("ST Slope",["Up","Flat","Down"])
        if St_slop=='Flat':
            St_slop_flat=1
        else :
            St_slop_flat=0

        if St_slop=='Up':
            St_slop_up=1
        else :
            St_slop_up=0

            
        reset_button = st.form_submit_button("Reset")

    if st.button("Diagnose"):
        data = [[gender,cpt_Ata,cpt_nap,cpt_ta,resting_ecg_n,resting_ecg_st,exercise_angina,St_slop_flat,St_slop_up,fasting_bs,age,resting_bp,cholesterol,max_hr,oldpeak]]
        columns = ['Sex','cpt_Ata','cpt_nap','cpt_ta','resting_ecg_n','resting_ecg_st','ExerciseAngina','St_slope_flat','St_slope_up','fasting_bs','Age','RestingBP','Cholesterol','MaxHR','Oldpeak']
        
        df = pd.DataFrame(data,columns=columns)

        model.predict(df)

        if model.predict(df)==1:
            st.caption('Under Risk !!!')
        else :
            st.caption('Not Under Risk')
            st.caption("Note : To be correlated Clinically")

# Result analysis
def heart_analysis():
    st.image('heart.png')
    st.caption("Comparison of Accuracy Score of Multiple Algoritms")

# Heart Data
def heart_data():
    df = pd.read_csv('heart.csv')
    string = '''This dataset was created by combining different datasets already available independently but not combined before. In this dataset, 5 heart datasets are combined over 11 common features which makes it the largest heart disease dataset available so far for research purposes. The five datasets used for its curation are:

Cleveland: 303 observations
Hungarian: 294 observations
Switzerland: 123 observations
Long Beach VA: 200 observations
Stalog (Heart) Data Set: 270 observations
Total: 1190 observations
Duplicated: 272 observations

Final dataset: 918 observations

Every dataset used can be found under the Index of heart disease datasets from UCI Machine Learning Repository on the following link: https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/'''
    st.caption(string)
    st.dataframe(df)

# Biological Interval ref
def heart_bio_interval():
    col1,col2,col3 = st.columns(3)
    with col1 :
        st.write("Biological Substance")
        st.caption("Chest Pain Type")
        st.caption("Resting BP")
        st.caption("Cholesterol")
        st.caption("Fasting BS")
        st.caption("Resting ECG")
        st.caption("Max Heart Rate")
        st.caption("Exercise Angina")
        st.caption("Old Peak")
        st.caption("ST Slope")

    with col2 :
        st.write("Interval Range")
        st.caption("None")
        st.caption("< 120/80")
        st.caption("< 200")
        st.caption("< 99")
        st.caption("Normal")
        st.caption("50 - 80")
        st.caption("No")
        st.caption("< 2")
        st.caption("Flat")
    
    with col3 :
        st.write("Units")
        st.caption("None")
        st.caption("mm Hg")
        st.caption("mg/dL")
        st.caption("mmol/L")
        st.caption("ms")
        st.caption("beats/minute")
        st.caption("None")
        st.caption("units")
        st.caption("None")
        st.caption("")







