import streamlit as st
import os
import json
import random

seasonsFile = "/foosballtable/seasons.json"

st.write("# Manage Seasons")

seasons = dict()
if not os.path.isfile(seasonsFile):
    seasons["active"] = "none"
    seasons["seasons"] = dict()
    with open(seasonsFile, 'w') as f:
        json.dump(seasons, f)

with open(seasonsFile, 'r') as f:
    seasons = json.load(f)

col1, col2 = st.columns(2)


with col1:
    st.write("#### Create Season")
    season = st.text_input("Season name")
    if st.button("Create"):
        if season == "none":
            st.error("none is reserved as season name")
        elif not season in seasons["seasons"]:
            seasons["seasons"][season] = dict()
            with open(seasonsFile, 'w') as f:
                json.dump(seasons, f)
            st.success("Season has been created")
        else:
            st.error("Season name already exists")

with col2:
    st.write("#### Set active Season")
    season = st.selectbox("Select active Season", seasons["seasons"])
    if st.button("Confirm"):
        seasons["active"] = season
        with open(seasonsFile, 'w') as f:
            json.dump(seasons, f)
        st.success("Active season set to " + season)
    
    