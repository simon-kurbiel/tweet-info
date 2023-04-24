import os
import pandas as pd
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Bidirectional, Dense, Embedding
from tensorflow.keras.layers import TextVectorization
import streamlit as st
from transformers import pipeline
from train import *





def getSent(data):
    
   
    output = clean_output(data)
    toxic = output['toxic']
    severe_toxic = output['severe_toxic']
    obscene = output['obscene']
    threat = output['threat']
    insult = output['insult']
    identity_hate = output['identity_hate']
    col1, col2,col3,col4,col5,col6 = st.columns(6)
    col1.metric("toxic",toxic,None)
    col2.metric("severe toxic",severe_toxic,None)
    col3.metric("obscene",obscene,None)
    col4.metric('threat',threat,None)
    col5.metric('insult',insult,None)
    col6.metric('Identity hate', identity_hate,None)
  
   

def rendPage():
    st.title("Twitter Toxicity")
    userText = st.text_input('User Input', "My cs482 TA is the best. May he stay blessed!")
    st.text("")
   

    if st.button('Calculate'):
        if(userText!=""):
            st.text("")
            getSent(userText)

rendPage()