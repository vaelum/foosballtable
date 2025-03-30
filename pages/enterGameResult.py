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

st.write("# Enter game result")

activeSeason = seasons["active"]
seasonList = list(seasons["seasons"].keys())
activeIndex = seasonList.index(activeSeason)
season = st.selectbox("Select season", seasonList, activeIndex)


players = list()
with open(playerJsonLocation, 'r') as f:
    players = json.load(f)

def clear_multi():
    st.session_state.winningPlayers = []
    st.session_state.loosingPlayers = []
    return

st.write("### Players in winning team")
winningPlayers = st.multiselect("Select winning players", players, key="winningPlayers")
loosingPlayers = st.multiselect("Select loosing players", players, key="loosingPlayers")
gameResult = st.radio("Game result", ["2:0", "2:1"])
change = 2
if gameResult == "2:1":
    change = 1
if len(winningPlayers) > 2 or len(winningPlayers) < 1 or len(loosingPlayers) > 2 or len(loosingPlayers) < 1:
    st.info("select betweenn 1 and 2 players for each team")
elif set(winningPlayers) & set(loosingPlayers):
    st.error("player can not be both on winning and loosing team")
else:
    if st.button("Enter result"):
        for player in loosingPlayers:
            if player in seasons["seasons"][season]:
                seasons["seasons"][season][player] -= change
            else:
                seasons["seasons"][season][player] = -change
        for player in winningPlayers:
            if player in seasons["seasons"][season]:
                seasons["seasons"][season][player] += change
            else:
                seasons["seasons"][season][player] = change
        
        with st.spinner("Saving results...", show_time=True):
            with open(seasonsFile, 'w') as f:
                json.dump(seasons, f)
            time.sleep(2)
        st.switch_page("pages/standings.py")

    