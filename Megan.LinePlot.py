#on Jupyter notebook
#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as lineplot
import numpy as np
import pandas as pd
#have to run each box


# In[12]:
#line plot based on: https://www.youtube.com/watch?v=DAQNHzOcO5A&list=PLXCw5VdOQb7gCT0gC5jg66carWh48JcOy&index=8
#Purpose of this program: To practice applying pytohn in presenting data in various modes, one being line graphs. I hope to utilize this when presenting data from my chemistry experiments related to drug discovery for my honors thesis at USF.

#resizing graph for viewability
lineplot.figure(figsize= (5,3),dpi=500)

#line number one

#these act like coordinate points
y = [20,60,85,90,100]
x = [1,2,3,5,6]


#displays the lineplot
lineplot.plot(x,y)

#displays the legend for chart
# lineplot.plot(x,y, label = "No Drugs", color="blue", marker="d", markersize = "10")
lineplot.plot(x,y,"b^",label="Without Drugs")

#Line number 2
x2=np.arange(0,10,1)
#(starting number, ending number, increments of)
# print(x2)
lineplot.plot(x2,x2*.5,"r^-", label="With Drugs")
#adding points on the line as marker

#change the font of the title requires us to include it in "lineplot.title"


#adding title to the line plot
lineplot.title("Correlation between Studying Time and Score on Exam",fontdict={"fontname": "Times New Roman","fontsize":16})

#adding titles for x and y axis
lineplot.xlabel("Studying Time (Hours)",fontdict={"fontname": "Times New Roman","fontsize":12})
lineplot.ylabel("Score on Exam (Points out of 100)", fontdict={"fontname": "Times New Roman","fontsize":12})


#how to edit the tick marks on the x and y axis 
lineplot.xticks([0,1,2,3,4,5,6,7,8,9,10])
lineplot.yticks([0,10,20,30,40,50,60,70,80,90,100])
lineplot.legend()

lineplot.show()

