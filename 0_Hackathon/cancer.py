import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle

model = pickle.load(open('Logbc.pkl','rb'))

# Department Navigation code
def dept_navigation():
    navigate = option_menu(None,
                           ["Diagnosis","Analysis","Data"],
                           icons = ["gear-fill","bar-chart-fill","card-heading"],
                           orientation="horizontal")
    return navigate

# Cancer page
def cancer_page():
    st.title("Department of Oncology")

    nav = dept_navigation()
    if nav =="Diagnosis":
        cancer_diag()


    elif nav =="Analysis":
        cancer_analysis()

    elif nav =="Data":
        cancer_data()

    elif nav == "Bio-Interval":
        st.write("Bio-Interval")


# cancer diag function
def cancer_diag():
    with st.form(key="Diagnose",clear_on_submit=True):
        clump_thickness = st.number_input("Clump Thikness",min_value=1,max_value=10)
        cell_size = st.number_input("Cell Size",min_value=1,max_value=10)
        cell_shape = st.number_input("Cell Shape",min_value=1,max_value=10)
        marginal_adhesion = st.number_input("Marginal Adhesion",min_value=1,max_value=10)
        single_epithelial_cell_size = st.number_input("Single Epithelial Cell Size",min_value=1,max_value=10)
        bn_median = st.number_input("Bare Nuclei",min_value=1,max_value=10)
        bland_chromatin = st.number_input("Bland Chromatin",min_value=1,max_value=10)
        normal_nucleoli = st.number_input("Normal Nucleoi",min_value=1,max_value=10)
        mitosis = st.number_input("Motosis",min_value=1,max_value=10)
        reset_button = st.form_submit_button("Reset")
        
    if st.button("Diagnose"):
        data = [[clump_thickness, cell_size, cell_shape, marginal_adhesion,
        single_epithelial_cell_size, bland_chromatin, normal_nucleoli,
        mitosis, bn_median]]
        columns = ['clump_thickness', 'cell_size', 'cell_shape', 'marginal_adhesion',
        'single_epithelial_cell_size', 'bland_chromatin', 'normal_nucleoli',
        'mitosis', 'bn_median']
        
        df = pd.DataFrame(data,columns=columns)

        model.predict(df)

        if model.predict(df)==1:
            st.caption('Under Risk !!!')
        else :
            st.caption('Not Under Risk')
            st.caption("Note : To be correlated Clinically")

def cancer_data():
    df = pd.read_csv('breast_cancer_wisconsin.data')
    df.to_csv('breast_cancer_wisconsin.data',index=False)
    # st.caption(string)
    st.dataframe(df.drop(['id'],axis=1))

def cancer_analysis():
    st.image('cancer.png')
    st.caption("Comparison of Accuracy Score of Multiple Algoritms")
