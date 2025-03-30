import streamlit as st
import os
import json
import random
import time

seasonsFile = "/foosballtable/seasons.json"
playerJsonLocation = "/foosballtable/players.json"

seasons = dict()
if not os.path.isfile(seasonsFile):
    seasons["active"] = "none"
    seasons["seasons"] = dict()
    with open(seasonsFile, 'w') as f:
        json.dump(seasons, f)

with open(seasonsFile, 'r') as f:
    seasons = json.load(f)

st.write("# Standings")

activeSeason = seasons["active"]
seasonList = list(seasons["seasons"].keys())
activeIndex = seasonList.index(activeSeason)
season = st.selectbox("Select season", seasonList, activeIndex)

st.write("Results Table")
st.bar_chart(seasons["seasons"][season])