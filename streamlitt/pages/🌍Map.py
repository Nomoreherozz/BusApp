import streamlit as st
import leafmap.f as leafmap
from funcs.getPath import getRoute, addMarkers
from funcs.buses_info import AllBusesInfo

bus_list = AllBusesInfo()

st.set_page_config(layout="wide")
markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


st.title("Interactive Map")

col1, col2 = st.columns([1, 0.15])
options = list(leafmap.basemaps.keys())[0:5]
buses = [bus for bus in AllBusesInfo()]

with col2:
    basemap = st.selectbox("Select a basemap:", options, 1)
    number = st.selectbox("Select a bus number: ", buses, 1)

with col1:
    m = leafmap.Map()
    m.add_basemap(basemap)
    m.add_geojson(getRoute(number), style={'opacity': 1, 'fillOpacity': 0.1, 'weight': 5, 'color': "green"}, info_mode="on_hover")
    addMarkers(m, number)
    m.to_streamlit(height=720)