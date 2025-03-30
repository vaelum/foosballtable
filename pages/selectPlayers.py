import streamlit as st
import os
import json
import random

playerJsonLocation = "/foosballtable/players.json"

st.write("# Select players")

if not os.path.isfile(playerJsonLocation):
    st.error("No players have been created.")
else:
    players = list()
    with open(playerJsonLocation, 'r') as f:
        players = json.load(f)
    
    playersToSelectFrom = st.multiselect("Choose players to build teams", players)

    if st.button("Shuffle teams"):
        if len(playersToSelectFrom) < 2:
            st.warning("You need to select at least 2 players")
        elif len(playersToSelectFrom) < 4:
            team1player1 = random.choice(playersToSelectFrom)
            playersToSelectFrom.remove(team1player1)
            team2player1 = random.choice(playersToSelectFrom)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("## Black team")
                st.write("### " + team1player1)

            with col2:
                st.write("## White team")
                st.write("### " + team2player1)
        else:
            team1player1 = random.choice(playersToSelectFrom)
            playersToSelectFrom.remove(team1player1)
            team1player2 = random.choice(playersToSelectFrom)
            playersToSelectFrom.remove(team1player2)            
            team2player1 = random.choice(playersToSelectFrom)
            playersToSelectFrom.remove(team2player1)            
            team2player2 = random.choice(playersToSelectFrom)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("## Black team")
                st.metric(label="Player offense", value=team1player1)
                st.metric(label="Player defense", value=team1player2)

            with col2:
                st.write("## White team")
                st.metric(label="Player offense", value=team2player1)
                st.metric(label="Player defense", value=team2player2)


            