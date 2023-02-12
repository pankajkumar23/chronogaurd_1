import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle

model = pickle.load(open('liver_rf.pkl','rb'))

# Department Navigation code
def dept_navigation():
    navigate = option_menu(None,
                           ["Diagnosis","Bio-Interval","Analysis","Data"],
                           icons = ["gear-fill","shield-fill-plus","bar-chart-fill","card-heading"],
                           orientation="horizontal")
    return navigate

#--------------------------------------------------------------------------
# Page - liver
def liver_page():
    st.title("Department of Gasterology")
    
    nav = dept_navigation()

    if nav =="Diagnosis":
        liver_diag()

    elif nav =="Analysis":
        liver_analysis()

    elif nav =="Data":
    	liver_data()

    elif nav == "Bio-Interval":
        liver_bio_interval()

#----------------------------------------------------------------------
def liver_diag():
    with st.form(key="Diagnose",clear_on_submit=True):
        age = st.number_input("Age",min_value=1,max_value=90)
        gender = st.selectbox("Gender",["Male","Female"])
        t_bilirubin = st.number_input("Total Bilirubin")
        d_bilirubin = st.number_input("Direct Bilirubin")
        alkphos = st.number_input("Alkaline Phosphotase",min_value=0)
        sgpt = st.number_input("SGPT - Alamine Aminotransferase",min_value=0)
        sgot = st.number_input("SGOT - Aspartate Aminotransferase",min_value=0)
        tp = st.number_input("Total Protiens")
        albumin = st.number_input("Albumin")
        a_g_ratio = st.number_input("A/G : Albumin And Globulin Ratio")

        reset_button = st.form_submit_button("Reset")
    
    if st.button("Diagnose"):
        data = [[t_bilirubin,d_bilirubin,alkphos,sgpt,sgot,albumin]]
        columns = ['t_bilirubin','d_bilirubin','alkphos','sgpt','sgot','albumin']
    
        df = pd.DataFrame(data,columns=columns)

        model.predict(df)

        if model.predict(df)==1:
            st.caption('Under Risk !!!')
        else :
            st.caption('Not Under Risk')
            st.caption("Note : To be correlated Clinically")


def liver_data():
    df = pd.read_csv('ilpd_md1.csv')
    st.dataframe(df)


def liver_bio_interval():
	col1,col2,col3 = st.columns(3)
	with col1 :
		st.write('Biological Substance')
		st.caption('Total Bilirubin')
		st.caption('Direct Bilirubin')
		st.caption('Alkaline Phosphotase')
		st.caption('SGPT - Alamine Aminotransferase')
		st.caption('SGOT - Aspartate Aminotransferase')
		st.caption('Total Protiens')
		st.caption('Albumin')
		st.caption('Albumin and Globulin Ratio')

	with col2:
		st.write('Interval Range')
		st.caption('0.30 - 1.20')
		st.caption('< 0.20')
		st.caption('30 - 120')
		st.caption('< 50')
		st.caption('< 50')
		st.caption('6.40 - 8.30')
		st.caption('3.50 - 5.20')
		st.caption('0.90 - 2.0')

	with col3:
		st.write('Units')
		st.caption('mg/dL')
		st.caption('mg/dL')
		st.caption('U/L')
		st.caption('U/L')
		st.caption('U/L')
		st.caption('g/dL')
		st.caption('g/dL')
		st.caption('None')

def liver_analysis():
    st.image('cancer.png')
    st.caption("Comparison of Accuracy Score of Multiple Algoritms")
