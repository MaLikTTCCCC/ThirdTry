#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:22:47 2024

@author: malikcarpanin
"""

import streamlit as st
#import numpy as np
import pandas as pd
import yfinance as yf
#import matplotlib.pyplot as plt
#import matplotlib as mpl
#import matplotlib.dates as mdates
#from datetime import datetime
import altair as alt
import vega_datasets as vd


msft = yf.download("msft", start="2020-01-01", end="2024-01-01")
dates=msft.index

chart=alt.Chart(msft)
c=chart.mark_point()

st.altair_chart(c)