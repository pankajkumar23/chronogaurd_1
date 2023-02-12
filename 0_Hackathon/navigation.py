import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from heart import heart_page
from cancer import cancer_page
from liver import liver_page
from kidney import kidney_page
from home import home_page

def sidebar():
    with st.sidebar:
        option = navigation()
    if option=="heart":
        heart_page()

    elif option=="kidney":
        kidney_page()

    elif option=="cancer":
        cancer_page()

    elif option=="Liver":
        liver_page()

    # else :
    #     home_page()

# Main Navigation code
def navigation():
    navigate = option_menu("ChronoGaurd 1.0",
                            ["heart","kidney","cancer","Liver"],
                            icons=["activity","activity","activity","activity"],menu_icon='shield-fill-plus',
                            default_index=0)

    return navigate

