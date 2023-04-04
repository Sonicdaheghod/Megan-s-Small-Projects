#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as lineplot
import numpy as np
import pandas as pd
#have to run each box


# In[12]:


#these act like coordinate points
y = [20,20,30]
x = [1,3,5]

#displays the lineplot
lineplot.plot(x,y)

#adding title to the line plot
lineplot.title("Correlation between Studying Time and Score on Exam")

#adding titles for x and y axis
lineplot.xlabel("Studying Time (Hours)")
lineplot.ylabel("Score on Exam (Points out of 100)")


lineplot.show()


# In[ ]:




