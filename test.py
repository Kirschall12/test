#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
#st.title('Erste App')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#sel1 = st.selectbox('Selection', [1,2,3])

#st.write('Deine Auswahl: ', sel1)

#x = np.linspace(0, 50, 50)
#fig, ax = plt.subplots()

#ax.plot(x, x**sel1)
#st.pyplot(fig)


#df = pd.read_csv('Bastar Craton.csv')

#sel2 = st.selectbox('Selection', ['Mg', 'Si'])
#sel3 = st.selectbox('Selection2', ['Mg', 'Si'])
#ax.scatter(df[sel2], df[sel3])
#st.pyplot(fig)

df = pd.read_csv('Bastar Craton')
x = range(46)
x = np.linspace(0, 50, 50)
fig, ax = plt.subplots()
#sel2 = st.selectbox('Selection', ['Mg', 'Si'])
sel3 = st.selectbox('Selection2', ['Mg', 'Si'])
ax.scatter(x, df[sel3])
st.pyplot(fig)
