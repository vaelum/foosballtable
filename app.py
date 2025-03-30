import streamlit as st

pages = {
    "Season":[
        st.Page("pages/standings.py", title = "Standings"),
        st.Page("pages/manageSeason.py", title = "Mange season")
    ],
    "Play": [
        st.Page("pages/selectPlayers.py", title="Select players"),
        st.Page("pages/enterGameResult.py", title="Enter game result")
    ],
    "Users": [
        st.Page("pages/addPlayer.py", title="Add Player"),
        st.Page("pages/removePlayer.py", title="Remove Player"),
    ]
}

pg = st.navigation(pages)
pg.run()