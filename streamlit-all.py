

#... means this still needs to be figured out & added


## Importing relevant libaries/modules
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import os
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
import ipywidgets as widgets 
from IPython.display import display, HTML, Javascript
from ipywidgets import HBox, VBox, Label, IntSlider, Dropdown, RadioButtons, Layout, Style 



st.set_page_config(
    page_title="Life Cycle Assessment",
)

# SIDEBAR
## SIDEBAR SECTION 1: PARAMETER
st.sidebar.title("Parameter")
st.sidebar.header("1. Definition of goal and scope")

# TAKE LIFESPAN INPUT
lifespan_input = st.sidebar.slider("Lifespan (a)", 5, 30, 12, help="Choose how many years will the car be used?", label_visibility="visible")  # min, max, default

# TAKE MILEAGE INPUT
mileage_year_input = st.sidebar.slider("Mileage (10.000 km)", 1, 30, 12, help="How much mileage in thousand kilometer per year should be considered?", label_visibility="visible")  # min, max, default

# TAKE URBAN LIVING INPUT
share_urban_input = st.sidebar.slider("Share of Urban Driving (%)", 0, 100, 50, step=5, help="What share is driven in urban areas? The rest is allocated to driving in the country (highway or country road)", label_visibility="visible")  # min, max, default

# TAKE CONSUMPTION INPUT
# radio button
cons_types = {
   'Manufacturer data': 0.65,
   'ADAC driving profiles': 1,
   'Or choose own percentage:': 0
}
cons_input = st.sidebar.selectbox("Hydrogen", cons_types.keys(), help="How is the driving consumption estimated? For the own percentage option: choose % more or less than manufacturer")

# select number input
cons_free_input = st.sidebar.number_input("(% more or less than manufacturer)", -60, 60, 0, 5, label_visibility="collapsed")

st.sidebar.markdown("")
st.sidebar.markdown("")


## SIDEBAR SECTION 2: LCI 
st.sidebar.header("2. Life cycle inventory")

### SIDEBAR SECTION 2.1: PRODUCTION STAGE 
# TAKE PRODUCTION INPUT
st.sidebar.subheader ("Production Stage")
cc_mat_prod_types = {
   'Electricity Mix': 'cc_normal',
   'From renewable energy sources': 'cc_ee',
   'Fossil fuel based': 'cc_worst'
}

cc_mat_prod_types_input = st.sidebar.selectbox("Production", cc_mat_prod_types.keys(), help="How is the electricity for the production processes of the batteries, fuel cells and other materials generated?")

### SIDEBAR SECTION 2.2: USE STAGE 
st.sidebar.subheader ("Use Stage")

# TAKE HYDROGEN INPUT
hydrogen_prod_types = {
   'Natural Gas Reforming': 13.3,
   'Electrolysis from electricity mix': 23.0,
   'Electrolysis renewable energy sources': 0.866
}
hydrogen_prod_input = st.sidebar.selectbox("Hydrogen", hydrogen_prod_types.keys(), help="How is the utilized hydrogen produced?")

# TAKE ELECTRICITY INPUT
# radio button
cc_el_prod_types={
   'Electricity mix':0.45128,
   'From renewable energy sources':0.056,
   'Fossil fuel based':1.018, 
   'Or choose shares [%]:': 0
   }

cc_el_prod_types_input = st.sidebar.radio('Electricity', cc_el_prod_types.keys(), help="How is the electricity used for charging produced?")
######die Werte für die Labels einsetzen mit denen gerechnet wird

# select number inputs
el_pv_input = st.sidebar.number_input("PV:", 0, 100, 0, 1)
el_wind_input = st.sidebar.number_input("Wind:", 0, 100, 0, 1)
el_water_input = st.sidebar.number_input("Water:", 0, 100, 0, 1)
el_bio_input = st.sidebar.number_input("Biomass:", 0, 100, 0, 1)
el_lignite_input = st.sidebar.number_input("Lignite:", 0, 100, 0, 1)
el_hardcoal_input = st.sidebar.number_input("Hard Coal:", 0, 100, 0, 1)
el_nuclear_input = st.sidebar.number_input("Nuclear:", 0, 100, 0, 1)
el_ngas_input = st.sidebar.number_input("Natural Gas:", 0, 100, 0, 1)


if cc_el_prod_types[cc_el_prod_types_input] == 0:
    if (el_pv_input + el_wind_input + el_water_input + el_bio_input + el_lignite_input + el_hardcoal_input + el_nuclear_input + el_ngas_input) != 100:
        st.sidebar.write('The share for the electricity generation has to equal 100%. Please adjust the numbers for "Electricity" in "Use Phase" accordingly.') 

    else: cc_el_prod = (el_pv_input*0.11+ el_wind_input*0.15 + el_water_input*0.04+ el_bio_input* 0.02+ el_lignite_input *1.227 +el_hardcoal_input*1.123 +  el_nuclear_input*0.011 + el_ngas_input*0.72)/100      
else: 
    cc_el_prod = cc_el_prod_types[cc_el_prod_types_input]

## SIDEBAR SECTION 2.3: END OF LIFE STAGE 
st.sidebar.subheader ("End of Life Stage")

# TAKE RECYCLING INPUT
# radio button
recyc_input = st.sidebar.selectbox("Recycling type", ['Pyrometallurgy', 'Hydrometallurgy', 'Reuse'], help="What recycling process is utilized for the battery?")

st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")

# SIDEBAR: SET PARAMETERS
st.sidebar.button('Set Parameters')
########add was passiert on click


# MAIN AREA
st.title("Life cycle assessment mobility")
"After the energy..."

# SELECT TAB
tab1, tab2 = st.tabs(["Results", "Analysis"])

## RESULTS TAB
with tab1:
   st.header("Results")
   "The next phase..."
   "#### Climate change impact for the different life cycle stages"
    
    # SHOW PRODUCTION OUTPUT
   with st.expander("Production"):
    # Füge den Inhalt des Bereichs hinzu
     st.write("Hier kommt später ein Graph hin")
    #...add chart
   
   # SHOW USE OUTPUT
   with st.expander("Use"):
    # Füge den Inhalt des Bereichs hinzu
     st.write("Hier kommt später ein Graph hin")
    #...add chart
   
   # SHOW END OUTPUT
   with st.expander("End"):
    # Füge den Inhalt des Bereichs hinzu
     st.write("Hier kommt später ein Graph hin")
    #...add chart
   
   # SHOW END LIFE CYCLE OUTPUT
   with st.expander("Entire Life Cycle"):
    # Füge den Inhalt des Bereichs hinzu
     st.write("Hier kommt später ein Graph hin")
    #...add chart

## ANALYSIS TAB
with tab2:
 st.header("Analysis")
 "To analyze and interpret the results in more detail..."
 
 # TAKE CAR TYPE SETTINGS
 with st.expander("Choose types of cars and drives to compare:"):
     "#### Car 1:"
     with st.container():
        col1, col2 = st.columns(2)
        with col1:
            select_cartype1 = st.selectbox("Car Type:", ['None', '...'], key='car1.1')
        with col2:
            select_drive1 = st.selectbox("Type of Drive Train:", ['ICEV petrol', '...'], key='car1.2')
     
     "#### Car 2:"
     with st.container():
        col1, col2 = st.columns(2)
        with col1:
            select_cartype2 = st.selectbox("Car Type:", ['None', '...'], key='car2.1')

        with col2:
            select_drive2 = st.selectbox("Type of Drive Train:", ['ICEV petrol', '...'], key='car2.2')
     
     "#### Car 3:"
     with st.container():
        col1, col2 = st.columns(2)
        with col1:
            select_cartype3 = st.selectbox("Car Type:", ['None', '...'], key='car3.1')
        with col2:
            select_drive3 = st.selectbox("Type of Drive Train:", ['ICEV petrol', '...'], key='car3.2')
     
     "#### Car 4:"
     with st.container():
        col1, col2 = st.columns(2)
        with col1:
            select_cartype4 = st.selectbox("Car Type:", ['None', '...'], key='car4.1')

        with col2:
            select_drive4 = st.selectbox("Type of Drive Train:", ['ICEV petrol', '...'], key='car4.2')
     
     "#### Car 5:"
     with st.container():
        col1, col2 = st.columns(2)
        with col1:
            select_cartype5 = st.selectbox("Car Type:", ['None', '...'], key='car5.1')
        with col2:
            select_drive5 = st.selectbox("Type of Drive Train:", ['ICEV petrol', '...'], key='car5.2')

# START ANALYSIS
 st.button('Start Analysis')
 st.markdown("""---""")

 # DISPLAY CHART TO COMPARE CARS
 "Here you can see and compare the different climate change impacts..."

 #...chart"
 "...Hier kommt später ein Graph hin..."

## Set variables
share_urban = share_urban_input/100
mileage_year = mileage_year_input*1000
lifespan = lifespan_input #possibly redudant
type_recycling = recyc_input #possibly redudant
hydrogen_prod_value = hydrogen_prod_types[hydrogen_prod_input]

if cons_types[cons_input]== 0:
    cons_var = (100+cons_free_input)*0.65/100
else:
    cons_var = cons_types[cons_input]

cc_mat_prod = cc_mat_prod_types[cc_mat_prod_types_input] 

#print(cc_el_prod)
