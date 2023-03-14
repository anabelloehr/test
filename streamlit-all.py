

#... means this still needs to be figured out & added

import streamlit as st

st.set_page_config(
    page_title="Life Cycle Assessment",
)

# SIDEBAR
## SIDEBAR SECTION 1: PARAMETER
st.sidebar.header("Parameter")
#...find out whether tooltip with markdown possible, then set collapse again

# TAKE LIFESPAN INPUT
Lifespan = st.sidebar.slider("Lifespan", 0.1, 8.0, 1.0, help="...", label_visibility="visible")  # min, max, default

# TAKE MILEAGE INPUT
Mileage = st.sidebar.slider("Mileage", 0.1, 8.0, 1.0, help="...", label_visibility="visible")  # min, max, default

# TAKE URBAN LIVING INPUT
Urban = st.sidebar.slider("Urban Living", 0.1, 8.0, 1.0, help="...", label_visibility="visible")  # min, max, default

# TAKE CONSUMPTION INPUT
# radio button
consumption = st.sidebar.radio('Consumption',
                  ('Manufacturer data', 'ADAC driving profiles', 'Or choose own percentage:'), help="... For the own percentage option: choose % more or less than manufacturer")
# select number input
consumption_percentage = st.sidebar.number_input("(% more or less than manufacturer)", label_visibility="collapsed")


## SIDEBAR SECTION 2: LCI 
st.sidebar.header("LCI")
### SIDEBAR SECTION 2.1: PRODUCTION STAGE 
# TAKE PRODUCTION INPUT
st.sidebar.subheader ("Production Stage")
select_production = st.sidebar.selectbox("Production", ['Electricity Mix', '...'], help="...")

### SIDEBAR SECTION 2.2: USE STAGE 
st.sidebar.subheader ("Use Stage")

# TAKE HYDROGEN INPUT
select_hydrogen = st.sidebar.selectbox("Hydrogen", ['Natural Gas Reforming', '...'], help="...")

# TAKE ELECTRICITY INPUT
# radio button
electricity = st.sidebar.radio('Electricity',
                  ('Electricity mix', 'From renewable energy sources', 'Fossil fuel based', 'Or choose shares [%]:'), help="...")
# select number inputs
electricity_shares_pv = st.sidebar.number_input("PV:")
electricity_shares_wind = st.sidebar.number_input("Wind:")
electricity_shares_water = st.sidebar.number_input("Water:")
electricity_shares_biomass = st.sidebar.number_input("Biomass:")
electricity_shares_lignite = st.sidebar.number_input("Lignite:")
electricity_shares_hard_coal = st.sidebar.number_input("Hard Coal:")
electricity_shares_nuclear = st.sidebar.number_input("Nuclear:")
electricity_shares_natural_gas = st.sidebar.number_input("Natural Gas:")


## SIDEBAR SECTION 2.3: END OF LIFE STAGE 
st.sidebar.subheader ("End of Life Stage")
# TAKE RECYCLING INPUT
# radio button
Recycling = st.sidebar.selectbox("Recycling type", ['Pyrometallurgy', 'Hydrometallurgy', 'Reuse'], help="...")

st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")

# SIDEBAR: SET PARAMETERS
st.sidebar.button('Set Parameters')



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

