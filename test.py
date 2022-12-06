#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.title('Erste App')

import matplotlib.pyplot as plt
import numpy as np

sel1 = st.selectbox('Selection', [1,2,3])

st.write('Deine Auswahl: ', sel1)

x = np.linspace(0, 50, 50)
fig = plt.plot(x, x**2)

st.pyplot(fig)
