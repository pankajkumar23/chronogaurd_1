import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Department Navigation code
def dept_navigation():
    navigate = option_menu(None,
                           ["Diagnosis","Bio-Interval","Analysis","Data"],
                           icons = ["gear-fill","shield-fill-plus","bar-chart-fill","card-heading"],
                           orientation="horizontal")
    return navigate

# kidney page
def kidney_page():
    st.title("Department of Nephrology")
    nav = dept_navigation()
    if nav =="Diagnosis":
        kidney_diag()

    elif nav =="Analysis":
        kidney_analysis()

    elif nav =="Data":
        kidney_data()

    elif nav == "Bio-Interval":
        kidney_bio_interval()

# Kidney Daignosis
def kidney_diag():
    with st.form("kidney_diagnosis",clear_on_submit=True):
        # Data input
        age = st.number_input("Age",min_value=1,max_value=90)
        bp = st.number_input("Blood Pressure")
        sg = st.selectbox("Specific Gravity",['1.005','1.010','1.015','1.020','1.025'])
        alb = st.selectbox("Albumin",[0,1,2,3,4,5])
        sugar = st.selectbox("Sugar",[0,1,2,3,4,5])
        rbc = st.selectbox("RBC's",['Normal','Abnormal'])
        pus_cell = st.selectbox("Pus Cell",['Normal','Abnormal'])
        pus_cell_clumps = st.selectbox("Pus Cell Clumps",['Present','Not Present'])
        bacteria = st.selectbox("Bacteria",['Present','Not Present'])
        blood_glucose_random = st.number_input("Blood Glucose Random")
        blood_urea = st.number_input("Blood Urea")
        serum_c = st.number_input("Serum Creatinine")
        sodium = st.number_input("Sodium")
        potassium = st.number_input("Potassium")
        hemo = st.number_input("Hemoglobin")
        pcv = st.number_input("Packed Cell Volume")
        wbc = st.number_input("White Blood Cell")
        rbc = st.number_input("Red Blood Cell")
        hyper = st.selectbox("Hypertension",['Yes','No'])
        diabetes_melitus = st.selectbox("Daibetes Mellitus",['Yes','No'])
        ca_disease = st.selectbox("Coronary Artery Disease",['Yes','No'])
        appetite = st.selectbox("Appetite",['Good','Poor'])
        pedal_e = st.selectbox("Pedal Edema",['Yes','No'])
        anemia = st.selectbox("Anemia",['Yes','No'])

        reset_button = st.form_submit_button("Reset")

    if st.button("Diagnose"):
        kidney_model()

# Result analysis
def kidney_analysis():
    st.image('kidney.png')
    st.caption("Comparison of Accuracy Score of Multiple Algoritms")

# Heart Data
def kidney_data():
    df = pd.read_csv('kidney_disease.csv')
    st.dataframe(df)

# Biological Interval ref
def kidney_bio_interval():
    col1,col2,col3 = st.columns(3)
    with col1 :
        st.write("Biological Substance")
        st.caption("Blood Pressure")
        st.caption("Specific Gravity")
        st.caption("Albumin")
        st.caption("Sugar")
        st.caption("Red Blod Cell Shape")
        st.caption("Pus Cell Shape")
        st.caption("Pus Cell Clumps")
        st.caption("Bacteria")
        st.caption("Blood Glucose Random")
        st.caption("Blood Urea")
        st.caption("Serum Creatinine")
        st.caption("Sodium")
        st.caption("Potassium")
        st.caption("Hemoglobin")
        st.caption("Packed Cell Volume")
        st.caption("White Blood Cell Count")
        st.caption("Red Blood Cell Count")
        st.caption("Hypertension")
        st.caption("Diabetes")
        st.caption("Coronary Artery Disease")
        st.caption("Appetite")
        st.caption("Pedal Edema")
        st.caption("Anemia")


    with col2 :
        st.write("Interval Range")
        st.caption("90/60 - 120/80")
        st.caption("1.005 - 1.030")
        st.caption("3.50 - 5")
        st.caption("< 140")
        st.caption("Normal")
        st.caption("Normal")
        st.caption("Not Present")
        st.caption("Not Present")
        st.caption("< 99")
        st.caption("6 - 24")
        st.caption("0.6 - 1.0")
        st.caption("136.0 - 145.0")
        st.caption("3.50 - 5.10")
        st.caption("11.6 - 15.0")
        st.caption("(36 - 46)")
        st.caption("(4.5 - 11.0) X 10^9")
        st.caption("(3.8 - 5.20) X 10^12")
        st.caption("No")
        st.caption("No")
        st.caption("No")
        st.caption("Good")
        st.caption("No")
        st.caption("No")
    
    with col3 :
        st.write("Units")
        st.caption("mm/Hg")
        st.caption("none")
        st.caption("g/dL")
        st.caption("m mol/L")
        st.caption("none")
        st.caption("none")
        st.caption("none")
        st.caption("none")
        st.caption("mg/dL")
        st.caption("mg/dL")
        st.caption("mg/dL")
        st.caption("mEq/L")
        st.caption("mEq/L")
        st.caption("gms")
        st.caption("%")
        st.caption("cells/cmm")
        st.caption("cells/cmm")
        st.caption("none")
        st.caption("none")
        st.caption("none")
        st.caption("none")
        st.caption("none")
        st.caption("none")

def kidney_model():
    pass
