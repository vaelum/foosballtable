import streamlit as st
import json
import os.path

playerJsonLocation = "/foosballtable/players.json"

st.write("# Add player")
name = st.text_input("Player name")
if st.button("Add"):
    if not os.path.isfile(playerJsonLocation):
        players = list()
        players.append(name)
        with open(playerJsonLocation, 'w') as f:
            json.dump(players, f)
        st.success("Player has been added.")
    else:
        players = list()
        with open(playerJsonLocation, 'r') as f:
            players = json.load(f)
        
        if not name in players:
            players.append(name)
            with open(playerJsonLocation, 'w') as f:
                json.dump(players, f)
            st.success("Player has been added.")
        else:
            st.warning("Player already exists.")
            

