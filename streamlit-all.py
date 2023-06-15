

#... means this still needs to be figured out & added


##1: Importing relevant libaries/modules
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

#4: material impact climate change, could be expanded to all impact categories
cc_impact_prod=pd.read_excel('assets/excel/Input_LCA_TESA.xlsx', sheet_name = 'cc_impact_prod', index_col=[0], header=[0], usecols=[0,1,2,3,4], engine ='openpyxl')
cc_impact_use=pd.read_excel('assets/excel/Input_LCA_TESA.xlsx', sheet_name = 'cc_impact_use', index_col=[0], header=[0], usecols=[0,1,2,3], engine ='openpyxl')

#5: materials and car specifications
amount_mat_ct1=pd.read_excel('assets/excel/Input_LCA_TESA.xlsx',sheet_name = 'mat_ct1', index_col=[0], header=[0], usecols=[0,2,3,4,5,6], engine ='openpyxl')
car_specs_ct1=pd.read_excel('assets/excel/Input_LCA_TESA.xlsx',sheet_name = 'car_specs_ct1', index_col=[0], header=[0], usecols=[0,2,3,4,5,6], engine ='openpyxl')

amount_mat_ct2=pd.read_excel('assets/excel/Input_LCA_TESA.xlsx',sheet_name = 'mat_ct2', index_col=[0], header=[0], usecols=[0,2,3,4,5,6], engine ='openpyxl')
car_specs_ct2=pd.read_excel('assets/excel/Input_LCA_TESA.xlsx',sheet_name = 'car_specs_ct2', index_col=[0], header=[0], usecols=[0,2,3,4,5,6], engine ='openpyxl')

amount_mat_ct3=pd.read_excel('assets/excel/Input_LCA_TESA.xlsx',sheet_name = 'mat_ct3', index_col=[0], header=[0], usecols=[0,2,3,4,5,6], engine ='openpyxl')
car_specs_ct3=pd.read_excel('assets/excel/Input_LCA_TESA.xlsx',sheet_name = 'car_specs_ct3', index_col=[0], header=[0], usecols=[0,2,3,4,5,6], engine ='openpyxl')

amount_mat_ct4=pd.read_excel('assets/excel/Input_LCA_TESA.xlsx',sheet_name = 'mat_ct4', index_col=[0], header=[0], usecols=[0,2,3,4,5,6], engine ='openpyxl')
car_specs_ct4=pd.read_excel('assets/excel/Input_LCA_TESA.xlsx',sheet_name = 'car_specs_ct4', index_col=[0], header=[0], usecols=[0,2,3,4,5,6], engine ='openpyxl')

#6
amount_mat = [amount_mat_ct1, amount_mat_ct2,amount_mat_ct3,amount_mat_ct4]
car_specs = [car_specs_ct1, car_specs_ct2,car_specs_ct3,car_specs_ct4]

#13: drivetrain types and car types
dt_ar = ['ICEV_petrol', 'ICEV_diesel','PHEV' ,'BEV', 'FCEV'] 
ct_ar = ['small car', 'small family car', 'large family car', 'executive car']

#define figures for the results graphs. the values are set through clicking the 'set parameters' button
fig1=None
fig2=None
fig3=None
fig4=None
fig5=None

#definition funktion für button
def results_LCA(cc_impact_prod, cc_mat_prod, cc_el_prod, hydrogen_prod, cons_var, type_recycling, mileage_year, lifespan): #write down same as when call function
    #alle berechnungen
   
    #14: Production process
    data_prod = np.array([np.arange(len(ct_ar))]*len(dt_ar)).T

    for ct_key in ct_ar:
        i=ct_ar.index(ct_key) #cartype

        for items, col in amount_mat[i].iteritems():
        
            lcascore_mat = (cc_impact_prod[cc_mat_prod]*((amount_mat[i][items])*car_specs[i][items]['weight'])).sum() #einfach

            lcascore_bat_fc = (cc_impact_prod[cc_mat_prod]*car_specs[i][items]).sum() #battery, fuel cell and electricity for production

            lcascore = lcascore_mat + lcascore_bat_fc

            data_prod[i][dt_ar.index(items)] = lcascore

    h_prod_cc = pd.DataFrame(data_prod,index=ct_ar,columns=dt_ar) 
    

    #15: Use phase (per 100 km)

    data_use = np.array([np.arange(len(ct_ar))]*len(dt_ar)).T
    losses_el = (0.95*0.95*0.94)
    cc_petrol = cc_impact_use['climate change']['petrol'] #cc pro 1 liter
    cc_diesel = cc_impact_use['climate change']['diesel'] #cc pro 1 liter
    cc_el = cc_el_prod #cc per 1 kWh
    cc_hy = hydrogen_prod
    #cc_hy = cc_impact_use['climate change']['hydrogen'] #cc per 1 kWh        

    for dt_key in dt_ar:

    #petrol:
        
        if dt_key == 'ICEV_petrol':
            
            for ct_key in ct_ar:
                i=ct_ar.index(ct_key)
                cons_urban = car_specs[i][dt_key]['cons_urban']*cons_var
                cons_land = car_specs[i][dt_key]['cons_land']*cons_var
                
                lcascore_use_km =(cons_urban * share_urban + cons_land* (1-share_urban)) * cc_petrol
                data_use [ct_ar.index(ct_key)][dt_ar.index(dt_key)] = lcascore_use_km
                
        
    #diesel:
        if dt_key == 'ICEV_diesel':
            
            for ct_key in ct_ar:
                i=ct_ar.index(ct_key)
                cons_urban = car_specs[i][dt_key]['cons_urban']*cons_var
                cons_land = car_specs[i][dt_key]['cons_land']*cons_var

                lcascore_use_km =(cons_urban * share_urban + cons_land* (1-share_urban)) * cc_diesel
                data_use [ct_ar.index(ct_key)][dt_ar.index(dt_key)] = lcascore_use_km
                
    #PHEV:
        
        if dt_key == 'PHEV':

            for ct_key in ct_ar:
                
                i=ct_ar.index(ct_key)
                cons_urban_l = car_specs[i][dt_key]['cons_urban']*cons_var
                cons_land_l = car_specs[i][dt_key]['cons_land']*cons_var
                cons_urban_el = car_specs[i][dt_key]['cons_urban_PHEV_el']*cons_var
                cons_land_el = car_specs[i][dt_key]['cons_land_PHEV_el']*cons_var
                
                lcascore_use_km =(((cons_urban_l * share_urban + cons_land_l* (1-share_urban)) * cc_petrol) + ((cons_urban_el * share_urban + cons_land_el* (1-share_urban)) * cc_el/losses_el))
                data_use [ct_ar.index(ct_key)][dt_ar.index(dt_key)] = lcascore_use_km             
                
    #BEV:
        
        if dt_key == 'BEV':
            
            for ct_key in ct_ar:            
                
                i=ct_ar.index(ct_key)
                cons_urban = car_specs[i][dt_key]['cons_urban']*cons_var
                cons_land = car_specs[i][dt_key]['cons_land']*cons_var
                
                lcascore_use_km =(cons_urban * share_urban + cons_land* (1-share_urban)) * cc_el/losses_el
                data_use [ct_ar.index(ct_key)][dt_ar.index(dt_key)] = lcascore_use_km        
                
                
    #FCEV:
        
        if dt_key == 'FCEV':
            
            for ct_key in ct_ar:
                
                i=ct_ar.index(ct_key)
                cons_urban = car_specs[i][dt_key]['cons_urban']*cons_var
                cons_land = car_specs[i][dt_key]['cons_land']*cons_var        
                
                lcascore_use_km =(cons_urban * share_urban + cons_land* (1-share_urban)) * cc_hy
                data_use [ct_ar.index(ct_key)][dt_ar.index(dt_key)] = lcascore_use_km

    #co2-eq per 100 km    
    h_use_cc = pd.DataFrame(data_use/100,index=ct_ar,columns=dt_ar)

    #16: End of life
    data_eol = np.array([np.arange(len(ct_ar))]*len(dt_ar)).T

    e_density_bat = 0.135 #kWh/kg battery pack

    if type_recycling == 'Pyrometallurgy':
        cc_recycling = 1.554/e_density_bat
    if type_recycling == 'Hydrometallurgy':
        cc_recycling = 0.914/e_density_bat
    if type_recycling == 'Reuse':
        cc_recycling = -3.551/e_density_bat

    for dt_key in dt_ar:
        
        for ct_key in ct_ar:
            i=ct_ar.index(ct_key)
            lcascore_eof = cc_recycling*car_specs[i][dt_key]['battery_base'] #*GrößeBatterie
            
            data_eol[ct_ar.index(ct_key)][dt_ar.index(dt_key)] = lcascore_eof     
            
            
            
    h_eol_cc = pd.DataFrame(data_eol,index=ct_ar,columns=dt_ar)  

    
    #17: Total:
    total_cc = (h_prod_cc + h_use_cc * (mileage_year*lifespan) + h_eol_cc)       
    # print(lifespan)
    # print(cc_impact_prod)
    # print(cc_mat_prod)
    # print(cc_el_prod)
    # print(hydrogen_prod)
    # print(cons_var)
    # print(type_recycling)
    # print(mileage_year)
    # print(h_use_cc)
    # print(h_prod_cc)
    # print(h_eol_cc)
    # print(total_cc)

    return (h_prod_cc, h_use_cc, h_eol_cc, total_cc)



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
mileage_year_input = st.sidebar.slider("Mileage (1000 km)", 1, 30, 12, help="How much mileage in thousand kilometer per year should be considered?", label_visibility="visible")  # min, max, default

# TAKE URBAN LIVING INPUT
share_urban_input = st.sidebar.slider("Share of urban driving (%)", 0, 100, 50, step=5, help="What share is driven in urban areas? The rest is allocated to driving in the country (highway or country road)", label_visibility="visible")  # min, max, default

# TAKE CONSUMPTION INPUT
# radio button
cons_types = {
   'Manufacturer data': 0.65,
   'ADAC driving profiles': 1,
   'Or choose own percentage:': 0
}
cons_input = st.sidebar.selectbox("Consumption", cons_types.keys(), help="How is the driving consumption estimated? For the own percentage option: choose % more or less than manufacturer")

# select number input
cons_free_input = st.sidebar.number_input("(% more or less than manufacturer)", -60, 60, 0, 5, label_visibility="collapsed")

st.sidebar.markdown("")
st.sidebar.markdown("")


## SIDEBAR SECTION 2: LCI 
st.sidebar.header("2. Life cycle inventory")

### SIDEBAR SECTION 2.1: PRODUCTION STAGE 
# TAKE PRODUCTION INPUT
st.sidebar.subheader ("Production stage")
cc_mat_prod_types = {
   'Electricity mix': 'cc_normal',
   'From renewable energy sources': 'cc_ee',
   'Fossil fuel based': 'cc_worst'
}

cc_mat_prod_types_input = st.sidebar.selectbox("Production", cc_mat_prod_types.keys(), help="How is the electricity for the production processes of the batteries, fuel cells and other materials generated?")

### SIDEBAR SECTION 2.2: USE STAGE 
st.sidebar.subheader ("Use stage")

# TAKE HYDROGEN INPUT
hydrogen_prod_types = {
   'Natural gas reforming': 13.3,
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


# with st.sidebar.expander("Shares"):
#     # select number inputs
#     el_pv_input = st.number_input("PV:", 0, 100, 0, 1)
#     el_wind_input = st.number_input("Wind:", 0, 100, 0, 1)
#     el_water_input = st.number_input("Water:", 0, 100, 0, 1)
#     el_bio_input = st.number_input("Biomass:", 0, 100, 0, 1)
#     el_lignite_input = st.number_input("Lignite:", 0, 100, 0, 1)
#     el_hardcoal_input = st.number_input("Hard coal:", 0, 100, 0, 1)
#     el_nuclear_input = st.number_input("Nuclear:", 0, 100, 0, 1)
#     el_ngas_input = st.number_input("Natural gas:", 0, 100, 0, 1)

with st.expander("Summary of intercepts"):
    # select number inputs
    el_pv_input = st.sidebar.number_input("PV:", 0, 100, 0, 1)
    el_wind_input = st.sidebar.number_input("Wind:", 0, 100, 0, 1)
    el_water_input = st.sidebar.number_input("Water:", 0, 100, 0, 1)
    el_bio_input = st.sidebar.number_input("Biomass:", 0, 100, 0, 1)
    el_lignite_input = st.sidebar.number_input("Lignite:", 0, 100, 0, 1)
    el_hardcoal_input = st.sidebar.number_input("Hard coal:", 0, 100, 0, 1)
    el_nuclear_input = st.sidebar.number_input("Nuclear:", 0, 100, 0, 1)
    el_ngas_input = st.sidebar.number_input("Natural gas:", 0, 100, 0, 1)

# define variable
if cc_el_prod_types[cc_el_prod_types_input] == 0:
    if (el_pv_input + el_wind_input + el_water_input + el_bio_input + el_lignite_input + el_hardcoal_input + el_nuclear_input + el_ngas_input) != 100:
        st.sidebar.write('The share for the electricity generation has to equal 100%. Please adjust the numbers for "Electricity" in "Use Phase" accordingly.') 

    else: cc_el_prod = (el_pv_input*0.11+ el_wind_input*0.15 + el_water_input*0.04+ el_bio_input* 0.02+ el_lignite_input *1.227 +el_hardcoal_input*1.123 +  el_nuclear_input*0.011 + el_ngas_input*0.72)/100      
else: 
    cc_el_prod = cc_el_prod_types[cc_el_prod_types_input]

## SIDEBAR SECTION 2.3: END OF LIFE STAGE 
st.sidebar.subheader ("End of life stage")


# TAKE RECYCLING INPUT
# radio button
recyc_input = st.sidebar.selectbox("Recycling type", ['Pyrometallurgy', 'Hydrometallurgy', 'Reuse'], help="What recycling process is utilized for the battery?")

st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")

## Set variables
share_urban = share_urban_input/100
mileage_year = mileage_year_input*1000
lifespan = lifespan_input #possibly redudant
type_recycling = recyc_input #possibly redudant
hydrogen_prod = hydrogen_prod_types[hydrogen_prod_input]

if cons_types[cons_input]== 0:
    cons_var = (100+cons_free_input)*0.65/100
else:
    cons_var = cons_types[cons_input]

cc_mat_prod = cc_mat_prod_types[cc_mat_prod_types_input] 

# SIDEBAR: SET PARAMETERS
if st.sidebar.button('Set parameters'):
    #funktion results_LCA wird getriggert die die parameter als variablen nimmt und die berechnungen als tables/arrays(?) outputtet 
    #diese resultate werden in Array arr_results gespeichert
    #h_prod_cc, h_use_cc, h_eol_cc, total_cc = results_LCA(cc_impact_prod, cc_mat_prod, cc_el_prod, hydrogen_prod, cons_var, type_recycling, mileage_year, lifespan)
    arr_results = results_LCA(cc_impact_prod, cc_mat_prod, cc_el_prod, hydrogen_prod, cons_var, type_recycling, mileage_year, lifespan)

    #18:
    #resultate an stellen im array werden dann in variablen, die für die graphen genutzt werden gespeichert
    data1=arr_results[0]/1000 #h_prod_cc
    data2=arr_results[1] #h_use_cc
    data3=arr_results[2] #h_eol_cc
    data4=arr_results[3]/1000 #total_cc

    
    #DEFINITION GRAPH PRODUCTION PHASE
    #die resultate werden als graphen dargestellt
    # Streamlit chart object erstellen
    fig1, ax1 = plt.subplots()

    # an die matplotlib funktion plot() übergeben um barchart zu erstellen
    ax1 = data1.plot(kind='bar', ax=ax1)

    # chart properties definieren mit set_*() funktion
    ax1.set_title('Climate change impact for production stage')
    ax1.set_xlabel('Type of car', color='#1C2833')
    ax1.set_ylabel('Climate change per kilometer [t CO2-eq]', color='#1C2833')
    ax1.legend(loc='upper left')
    ax1.grid()

    #DEFINITION GRAPH USE PHASE
    fig2, ax2 = plt.subplots()
    ax2 = data2.plot(kind='bar', ax=ax2)

    ax2.set_title('Climate change impact for use stage')
    ax2.set_xlabel('Type of car', color='#1C2833')
    ax2.set_ylabel('Climate change per kilometer [kg CO2-eq/km]', color='#1C2833')
    ax2.legend(loc='upper left')
    ax2.grid()

    #DEFINITION GRAPH END PHASE
    fig3, ax3 = plt.subplots()
    ax3 = data3.plot(kind='bar', ax=ax3)

    ax3.set_title('Climate change impact for end of life stage')
    ax3.set_xlabel('Type of car', color='#1C2833')
    ax3.set_ylabel('Climate change per kilometer [kg CO2-eq]', color='#1C2833')
    ax3.legend(loc='upper left')
    ax3.grid()

    #DEFINITION GRAPH ENTIRE LIFE CYCLE
    fig4, ax4 = plt.subplots()
    ax4 = data4.plot(kind='bar', ax=ax4)

    ax4.set_title('Climate change impact for entire life cycle')
    ax4.set_xlabel('Type of car', color='#1C2833')
    ax4.set_ylabel('Climate change per kilometer [t CO2-eq]', color='#1C2833')
    ax4.legend(loc='upper left')
    ax4.grid()

st.sidebar.markdown("---")

st.sidebar.markdown("Chair for Energy System Economics")
st.sidebar.markdown("(FCN-ESE)")
st.sidebar.markdown("Prof. Dr.-Ing. Aaron Praktiknjo")
st.sidebar.markdown("post_fcn-ese@eonerc.rwth-aachen.de")
st.sidebar.image("/Users/admin/Documents/Lavoro/basic/rwth_eerc_logo_rgb.png")

# MAIN AREA
st.header("JERICHO")
st.title("Life cycle assessment mobility tool")
st.write("Analyse which factors have an influence on the results of greenhouse gas emissions for different vehicle classes and powertrains over their **whole life cycle**.")
with st.expander("Learn more"):
    st.write("After the energy and industrial sectors, the transport sector in Germany emits the most greenhouse gas emissions (GHG) in Germany, thus promoting anthropogenic climate change. One approach to reducing greenhouse gas emissions can be the electrification of the powertrain.  However, when comparing different powertrain technologies, not only the CO2 emissions during the use phase should be considered, but also **all greenhouse gas emissions (CO2-eq.) over the entire life cycle**. Many factors can play a role in this analysis. That is why many scientific life cycle assessment (LCA) studies have obtained differing results in the past few years.   \n  \nFor this, you have first the possibility to set the **parameters for the scenario setting (1.1)** and the **life cycle inventory (1.2)**. After you can see the **results for the different life cycle stages** and summed up **(2)** or to choose which type of cars with which power trains to **compare** directly **(3)**.\n\nHere only the climate change impact measured in CO2-eq is evaluated as an example. In a comprehensive analyses, the other impact categories should to be taken into account as well.")

# SELECT TAB
tab1, tab2 = st.tabs(["Results", "Analysis"])

## RESULTS TAB
with tab1:
   st.header("Results")
   st.write("The next phase would be the life cycle impact assessment (LCIA). \n\nHere you can see the results for the different car types and the different drive types. First divided into the individual life cycle stages and then in total.")

   with st.expander("Explanation of terms"):
       "**The different drive types are:**" 
       "**ICEV** = internal combustion engine vehicle (used with petrol or diesel)"
       "**BEV** = battery electric vehicle"
       "**PHEV** = plug-in hybrid electric vehicle"
       "**FCEV** = fuel cell electric vehicle"
       ""
       "**The different types of cars and their German translation are:**"
       "**small car** – Kleinwagen"
       "**small family car** – Kompaktwagen"
       "**large family car** – Mittelklasse"    
       "**executive car** – Oberklasse"
    


   "#### Climate change impact for the different life cycle stages"
    
    # SHOW PRODUCTION OUTPUT
   with st.expander("Production Phase"):
    if fig1:
        # if parameters have been set, display production phase chart
        st.pyplot(fig1)
    else:
        st.write("To display the chart of the climate change impact for the production phase please set the parameters in the side bar.")

   # SHOW USE OUTPUT
   with st.expander("Use Phase"):
    if fig2:
        # if parameters have been set, display use phase chart
        st.pyplot(fig2)
    else:
        st.write("To display the chart of the climate change impact for the use phase please set the parameters in the side bar.")
   
   # SHOW END OUTPUT
   with st.expander("End Phase"):
    if fig3:
        # if parameters have been set, display end of life phase chart
        st.pyplot(fig3)
    else:
        st.write("To display the chart of the climate change impact for the end of life phase please set the parameters in the side bar.")
   
   # SHOW END LIFE CYCLE OUTPUT
   with st.expander("Entire Life Cycle"):
    if fig4:
        # if parameters have been set, display entire life cycle chart
        st.pyplot(fig4)
    else:
        st.write("To display the chart of the climate change impact for the entire life cycle please set the parameters in the side bar.")

## ANALYSIS TAB
with tab2:
 st.header("Analysis")
 "To analyze and interpret the results in more detail, you have the possibility to **compare the different vehicles** with each other.   \nHere you can select up to five cars with different drive trains and vehicle classes and compare their climate change impact in relation to the driven mileage."

 # TAKE CAR TYPE SETTINGS
 with st.expander("Choose types of cars and drives to compare:"):
     "#### Car 1:"
     with st.container():
        col1, col2 = st.columns(2)
        with col1:
            car1_ct_input = st.selectbox("Car Type:", ['none', ct_ar[0],ct_ar[1], ct_ar[2], ct_ar[3]], key='car1.1')
        with col2:
            car1_dt_input = st.selectbox("Type of Drive Train:", [dt_ar[0],dt_ar[1], dt_ar[2], dt_ar[3], dt_ar[4]], key='car1.2')
     
     "#### Car 2:"
     with st.container():
        col1, col2 = st.columns(2)
        with col1:
            car2_ct_input = st.selectbox("Car Type:", ['none', ct_ar[0],ct_ar[1], ct_ar[2], ct_ar[3]], key='car2.1')

        with col2:
            car2_dt_input = st.selectbox("Type of Drive Train:", [dt_ar[0],dt_ar[1], dt_ar[2], dt_ar[3], dt_ar[4]], key='car2.2')
     
     "#### Car 3:"
     with st.container():
        col1, col2 = st.columns(2)
        with col1:
            car3_ct_input = st.selectbox("Car Type:", ['none', ct_ar[0],ct_ar[1], ct_ar[2], ct_ar[3]], key='car3.1')
        with col2:
            car3_dt_input = st.selectbox("Type of Drive Train:", [dt_ar[0],dt_ar[1], dt_ar[2], dt_ar[3], dt_ar[4]], key='car3.2')
     
     "#### Car 4:"
     with st.container():
        col1, col2 = st.columns(2)
        with col1:
            car4_ct_input = st.selectbox("Car Type:", ['none', ct_ar[0],ct_ar[1], ct_ar[2], ct_ar[3]], key='car4.1')

        with col2:
            car4_dt_input = st.selectbox("Type of Drive Train:", [dt_ar[0],dt_ar[1], dt_ar[2], dt_ar[3], dt_ar[4]], key='car4.2')
     
     "#### Car 5:"
     with st.container():
        col1, col2 = st.columns(2)
        with col1:
            car5_ct_input = st.selectbox("Car Type:", ['none', ct_ar[0],ct_ar[1], ct_ar[2], ct_ar[3]], key='car5.1')
        with col2:
            car5_dt_input = st.selectbox("Type of Drive Train:", [dt_ar[0],dt_ar[1], dt_ar[2], dt_ar[3], dt_ar[4]], key='car5.2')

# START ANALYSIS


 st.markdown("""---""")

 st.write("Here you can see and compare the different climate change impacts the choose cars have over their life time in dependence of their driven kilometers.  \nThe y-axis represents the emissions during the production and end of life stage, while the slope stands for the CO2-eq. emitted during the use phase per driven kilometer.")

 if st.button('Start Analysis'):    
    #assign the return values of results to variable
    result = results_LCA(cc_impact_prod, cc_mat_prod, cc_el_prod, hydrogen_prod, cons_var, type_recycling, mileage_year, lifespan)

    #unpack the return values into separate variables
    h_prod_cc, h_use_cc, h_eol_cc, total_cc = result

    total_km = lifespan*mileage_year
    #print(lifespan)
    #print(mileage_year)
    #print(total_km)
    
    #put input from car selection into variables 
    # create empty graph array for that
    ct_1 = car1_ct_input
    dt_1 = car1_dt_input
    graph_car1 = []

    ct_2 = car2_ct_input
    dt_2 = car2_dt_input
    graph_car2 = []


    ct_3 = car3_ct_input
    dt_3 = car3_dt_input
    graph_car3 = []

    ct_4 = car4_ct_input
    dt_4 = car4_dt_input
    graph_car4 = []


    ct_5 = car5_ct_input
    dt_5 = car5_dt_input
    graph_car5 = []

    #set visual parameters for the graphs
    plt.rcParams['figure.figsize'] = [45, 30]
    plt.rcParams['figure.dpi'] = 95
    plt.rcParams['font.size'] = 50

    plt.rcParams['figure.subplot.bottom'] = 0.14
    linewidth=10

    #create new figure
    fig5, ax5 = plt.subplots(constrained_layout=True)

    #create x-axis settings
    x = np.linspace(0,total_km,num=int(total_km/1000))

    #wenn car type angegeben:
    if ct_1 !='none':
        #fülle den graphen mit diesen werten & einstellungen
        graph_car1 = h_prod_cc[dt_1][ct_1] + h_use_cc[dt_1][ct_1] *x + h_eol_cc[dt_1][ct_1]
        # plot a line graph on the ax5 subplot, showing the relationship between the values of x and graph_car1 with a red line.
        ax5.plot(x/1000, graph_car1/1000, '-r', label='car 1: '+ct_1+ ' '+ dt_1, linewidth=linewidth)

    if ct_2 !='none':   
        graph_car2 = h_prod_cc[dt_2][ct_2] + h_use_cc[dt_2][ct_2] *x + h_eol_cc[dt_2][ct_2]
        ax5.plot(x/1000, graph_car2/1000, '-b', label='car 2: '+ct_2+ ' '+ dt_2, linewidth=linewidth)
        
    if ct_3 !='none': 
        
        graph_car3 = h_prod_cc[dt_3][ct_3] + h_use_cc[dt_3][ct_3] *x + h_eol_cc[dt_3][ct_3]
        ax5.plot(x/1000, graph_car3/1000, '-c', label='car 3: '+ct_3+ ' '+ dt_3, linewidth=linewidth)
        
    if ct_4 !='none': 
        graph_car4 = h_prod_cc[dt_4][ct_4] + h_use_cc[dt_4][ct_4] *x + h_eol_cc[dt_4][ct_4]
        ax5.plot(x/1000, graph_car4/1000, '-y', label='car 4: '+ct_4+ ' '+ dt_4, linewidth=linewidth)
            
    if ct_5 !='none': 
        graph_car5 = h_prod_cc[dt_5][ct_5] + h_use_cc[dt_5][ct_5] *x + h_eol_cc[dt_5][ct_5]
        ax5.plot(x/1000, graph_car5/1000, '-g', label='car 5: '+ct_5+ ' '+ dt_5, linewidth=linewidth)

    def one_over(x):
        return x*1000 / mileage_year
    inverse = one_over
    
    # Set the title and axis labels for the graph
    #ax5.set_title('Comparison climate change impact over life time')
    ax5.set_xlabel('Mileage [1000 km]')
    ax5.set_ylabel('Climate change [t CO2-eq]')

    # Add a legend to the graph
    ax5.legend(loc='upper left')

    ax5.set_ylim(ymin=0)
    ax5.set_xlim(xmin=0, xmax= total_km/1000 )

    secax = ax5.secondary_xaxis('top', functions=(one_over, inverse) )
    secax.set_xlabel('Years [a]')

    ax5.grid()

    #a = y-axis intercept
    #b = slope 

    car_ar= (graph_car1,graph_car2, graph_car3, graph_car4, graph_car5)
    car_ar_name = ['Car 1','Car 2', 'Car 3','Car 4','Car 5']

    x1=[0,1,2,3,4]

# DISPLAY CHART TO COMPARE CARS
 if fig5:
    # if parameters have been set, display analysis chart
    st.pyplot(fig5)

    with st.expander("Summary of intercepts"):
        #a = y-axis intercept
        #b = slope 

        car_ar= (graph_car1,graph_car2, graph_car3, graph_car4, graph_car5)
        car_ar_name = ['Car 1','Car 2', 'Car 3','Car 4','Car 5']

        x1=[0,1,2,3,4]

        for i in x1: #loop
            if car_ar[i] != []: #wenn nicht leer
                a_i = car_ar[i][0] #y-achsen abschnitt
                b_i = car_ar[i][1]-car_ar[i][0] #steigung

                for j in x1: #i ausgangsgraph, j vergleichsgraph
                    if car_ar[j] != []:
                        if j>i: #wenn noch nicht verglichen hat
                            a_j = car_ar[j][0] 
                            b_j = car_ar[j][1]-car_ar[j][0]
                            
                            #wo sich auf x treffen
                            if b_j!=b_i:
                                xij =(a_i-a_j)/(b_j-b_i) #intersection

                                xij_int = xij.astype(int) #integer

                                #wo sich auf y treffen
                                yij = a_j+xij*b_j
                                yij_int = round(yij)

                                if xij_int < 0:
                                    st.write(car_ar_name[i]+ ' and ' +car_ar_name[j] + ' have no intercept.')
                                else:
                                    st.write(car_ar_name[i] + ' and '+  car_ar_name[j] + ' intercept at', xij_int*1000, 'kilometer and climate change impact of',yij_int ,'kg CO2-eq.')              
                                st.write(' ')
                            else:
                                st.write(car_ar_name[i]+ ' and ' +car_ar_name[j] + ' have no intercept.')
                                st.write(' ')


                
 else:
    st.write("")
