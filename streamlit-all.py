#... means this still needs to be figured out & added

import streamlit as st

# this is the sidebar
# this is section 1 of the sidebar
st.sidebar.markdown("## Parameter")
#...find out whether tooltip with markdown possible, then set collapse again
#...add text for help
dtboth = st.sidebar.slider("Lifespan", 0.1, 8.0, 1.0, help="...", label_visibility="visible")  # min, max, default
#...add info tooltip
dtboth = st.sidebar.slider("Mileage", 0.1, 8.0, 1.0, help="...", label_visibility="visible")  # min, max, default
#...add info tooltip
dtboth = st.sidebar.slider("Urban Living", 0.1, 8.0, 1.0, help="...", label_visibility="visible")  # min, max, default
#...add info tooltip
#...find out how to add functionality for consumption

# this is section 2 of the sidebar
st.sidebar.markdown("## LCI")
#...add text for production options
select_event = st.sidebar.selectbox("Production", ['Electricity Mix', '...'], help="...")
st.sidebar.markdown("#### Use Stage")
select_event = st.sidebar.selectbox("Hydrogen", ['Natural Gas Reforming', '...'], help="...")
#...add Electricity once found out
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")

st.sidebar.button('Set Parameters')


#this is the main area
st.title("Life cycle assessment mobility")
"After the energy..."


tab1, tab2 = st.tabs(["Results", "Analysis"])

#This is the results page
with tab1:
   st.header("Results")
   "The next phase..."
   "#### Climate change impact for the different life cycle stages"

   with st.expander("Production"):
    # Füge den Inhalt des Bereichs hinzu
     st.write("Hier kommt später ein Graph hin")
    #...add chart
   with st.expander("Use"):
    # Füge den Inhalt des Bereichs hinzu
     st.write("Hier kommt später ein Graph hin")
    #...add chart
   with st.expander("End"):
    # Füge den Inhalt des Bereichs hinzu
     st.write("Hier kommt später ein Graph hin")
    #...add chart
   with st.expander("Entire Life Cycle"):
    # Füge den Inhalt des Bereichs hinzu
     st.write("Hier kommt später ein Graph hin")
    #...add chart

#This is the analysis page
with tab2:
 st.header("Analysis")
 "To analyze and interpret the results in more detail..."
 with st.expander("Choose types of cars and drives to compare:"):
    #car types
    ##...see if there's a way to put them side by side
     "#### Car 1:"
     select_event = st.selectbox("Car Type:", ['None', '...'], key='car1.1')
     select_event = st.selectbox("Type of Drive Train:", ['ICEV petrol', '...'], key='car1.2')
     "#### Car 2:"
     select_event = st.selectbox("Car Type:", ['None', '...'], key='car2.1')
     select_event = st.selectbox("Type of Drive Train:", ['ICEV petrol', '...'], key='car2.2')
     "#### Car 3:"
     select_event = st.selectbox("Car Type:", ['None', '...'], key='car3.1')
     select_event = st.selectbox("Type of Drive Train:", ['ICEV petrol', '...'], key='car3.2')
     "#### Car 4:"
     select_event = st.selectbox("Car Type:", ['None', '...'], key='car4.1')
     select_event = st.selectbox("Type of Drive Train:", ['ICEV petrol', '...'], key='car4.2')
     "#### Car 5:"
     select_event = st.selectbox("Car Type:", ['None', '...'], key='car5.1')
     select_event = st.selectbox("Type of Drive Train:", ['ICEV petrol', '...'], key='car5.2')

 st.button('Start Analysis')
 #...try styling button through adding a streamlit widget key as “a class” to element classes
 #...combine with select boxes
 st.markdown("""---""")
 "Here you can see and compare the different climate change impacts..."
 #...chart
 "...Hier kommt später ein Graph hin..."






