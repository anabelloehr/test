

#... means this still needs to be figured out & added

import streamlit as st

st.set_page_config(
    page_title="Life Cycle Assessment",
)

# SIDEBAR
## SIDEBAR SECTION 1: PARAMETER
st.sidebar.title("Parameter")
st.sidebar.header("1. Definition of goal and scope")

# TAKE LIFESPAN INPUT
Lifespan = st.sidebar.slider("Lifespan (a)", 5, 30, 12, help="Choose how many years will the car be used?", label_visibility="visible")  # min, max, default

# TAKE MILEAGE INPUT
Mileage = st.sidebar.slider("Mileage (10.000 km)", 1, 30, 12, help="How much mileage in thousand kilometer per year should be considered?", label_visibility="visible")  # min, max, default

# TAKE URBAN LIVING INPUT
Urban = st.sidebar.slider("Share of Urban Driving (%)", 0, 100, 50, step=5, help="What share is driven in urban areas? The rest is allocated to driving in the country (highway or country road)", label_visibility="visible")  # min, max, default

# TAKE CONSUMPTION INPUT
# radio button
consumption = st.sidebar.radio('Consumption (basis)', ('Manufacturer data', 'ADAC driving profiles', 'Or choose own percentage:'), help="How is the driving consumption estimated? For the own percentage option: choose % more or less than manufacturer")
######die Werte für die Labels (maufacturer data 0.65, 1) einsetzen

# select number input
consumption_percentage = st.sidebar.number_input("(% more or less than manufacturer)", -60, 60, 0, 5, label_visibility="collapsed")

st.sidebar.markdown("")
st.sidebar.markdown("")


## SIDEBAR SECTION 2: LCI 
st.sidebar.header("2. Life cycle inventory")

### SIDEBAR SECTION 2.1: PRODUCTION STAGE 
# TAKE PRODUCTION INPUT
st.sidebar.subheader ("Production Stage")
select_production = st.sidebar.selectbox("Production", ['Electricity Mix', 'From renewable energy sources', 'Fossil fuel based'], help="How is the electricity for the production processes of the batteries, fuel cells and other materials generated?")

### SIDEBAR SECTION 2.2: USE STAGE 
st.sidebar.subheader ("Use Stage")

# TAKE HYDROGEN INPUT
select_hydrogen = st.sidebar.selectbox("Hydrogen", ['Natural Gas Reforming', 'Electrolysis from electricity mix', 'Electrolysis renewable energy sources'], help="How is the utilized hydrogen produced?")
######die Werte für die Labels (13.3, 23, 0.866) einsetzen mit denen gerechnet wird

# TAKE ELECTRICITY INPUT
# radio button
electricity = st.sidebar.radio('Electricity', ('Electricity mix', 'From renewable energy sources', 'Fossil fuel based', 'Or choose shares [%]:'), help="How is the electricity used for charging produced?")
######die Werte für die Labels einsetzen mit denen gerechnet wird

# select number inputs
el_pv_input = st.sidebar.number_input("PV:", 0, 100, 0, 1)
el_wind_input = st.sidebar.number_input("Wind:", 0, 100, 0, 1)
el_water_input = st.sidebar.number_input("Water:", 0, 100, 0, 1)
el_biomass_input = st.sidebar.number_input("Biomass:", 0, 100, 0, 1)
el_lignite_input = st.sidebar.number_input("Lignite:", 0, 100, 0, 1)
el_hard_coal_input = st.sidebar.number_input("Hard Coal:", 0, 100, 0, 1)
el_nuclear_input = st.sidebar.number_input("Nuclear:", 0, 100, 0, 1)
el_natural_gas_input = st.sidebar.number_input("Natural Gas:", 0, 100, 0, 1)

######rausfinden ob die number inputs verbinden kann/muss, zB als 1 variable


## SIDEBAR SECTION 2.3: END OF LIFE STAGE 
st.sidebar.subheader ("End of Life Stage")

# TAKE RECYCLING INPUT
# radio button
Recycling = st.sidebar.selectbox("Recycling type", ['Pyrometallurgy', 'Hydrometallurgy', 'Reuse'], help="What recycling process is utilized for the battery?")

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

