#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[5]:


import pandas as pd


# In[10]:


fname = r"C:\Users\e.howick\gits\ls_RA2200\flick_stds_2020-05\data\raw\verrification\20200513T1511_FS.txt"


# In[11]:


r = lambda x: (float(x.replace('\xb5m', ''))) # µm
d = lambda x: (float(x.replace('\xb0', '')))  # °
converters = {
    **dict.fromkeys(['Roundness(RONt)', 'DX', 'DY', 'DL', 'Peak(RONp)', 'Valley(RONv)', 'Mean Roundness'], r),
    **dict.fromkeys(['DA'], d)
}

df = pd.read_csv(fname, skiprows=13, nrows=1, encoding='latin-1', converters=converters)
df


# In[12]:


# refactor above into functions in roundness.processing.read_roundpak
from roundness.processing.read_roundpak import read_result, read_result_list

read_result(fname)


# In[13]:


import glob
import os
import config


# In[14]:


path = os.path.join(config.DATA_RAW, "verrification")
fns = glob.glob(os.path.join(path, '*_FS.txt'))
fns


# In[15]:


ids = [pd.to_datetime(os.path.split(fname)[1][:13]) for fname in fns]


# In[16]:


df = read_result_list(fns, ids)
df


# Now move to 01-efh-analysis-flick-std.ipynb
# 
# 

# In[1]:


import config
config.DATA_RAW


# In[ ]:


# Does this save as python? at all and again? and a third time? Yep!
# Now for html and then from within vscode OK

