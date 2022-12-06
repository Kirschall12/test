#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.title('Erste App')

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
