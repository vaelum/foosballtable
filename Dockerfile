FROM ubuntu:22.04
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
RUN pip install streamlit
CMD python3 -m streamlit run /foosballtable/app.py

