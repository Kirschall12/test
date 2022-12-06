#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.title('Erste App')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sel1 = st.selectbox('Selection', [1,2,3])

st.write('Deine Auswahl: ', sel1)

x = np.linspace(0, 50, 50)
fig, ax = plt.subplots()

ax.plot(x, x**sel1)
st.pyplot(fig)
