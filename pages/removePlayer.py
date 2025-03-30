import streamlit as st
import os
import json

playerJsonLocation = "/foosballtable/players.json"

st.write("# Remove player")

if not os.path.isfile(playerJsonLocation):
    st.error("No players have been created.")
else:
    players = list()
    with open(playerJsonLocation, 'r') as f:
        players = json.load(f)
    
    player = st.selectbox("Choose player to remove", players)
    if st.button("Remove"):
        players.remove(player)

        with open(playerJsonLocation, 'w') as f:
            json.dump(players, f)
        st.success("Player has been removed")
