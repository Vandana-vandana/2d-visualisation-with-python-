# Topic : Visualisation in 2D
# Team Members :-

# 1.Shubhanshu Mohan
# 4.Vandana

#####################  SHUBHANSHU MOHAN  ######################


#*********** 1st Graph  ************#

#Pie - Chart
# Import libraries
from matplotlib import pyplot as plt
import numpy as np


# Creating dataset
students = ['Group A', 'Group B', 'Group C','Group D']

data = [23, 17, 35, 29]

# Creating plot
plt.pie(data, labels =students)

# show plot
plt.show()

#*********** 2nd Graph  ************#

#Pie - Chart
 
# defining labels
students = ['Group A', 'Group B', 'Group C','Group D']
 
# portion covered by each label
data = [3, 7, 8, 6]
 
# color for each label
colors = ['r', 'y', 'g', 'b']
 
# plotting the pie chart
plt.pie(data, labels = students, colors=colors,startangle=90, shadow = True, explode = (0, 0, 0.1, 0.1),
        radius = 1.2, autopct = '%1.1f%%')
 
# plotting legend
plt.legend(loc='lower left')
 
# showing the plot
plt.show()

#*********** 1st Graph  ************#
 
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
 
# plotting the points
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Simple line graph')
 
# function to show the plot
plt.show()



#*********** 2nd Graph  ************#

# line 1 points
x1 = [1,2,3]
y1 = [2,4,1]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")
 
# line 2 points
x2 = [1,2,3]
y2 = [4,1,3]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2")
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to  graph
plt.title('Two lines on same graph!')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()



#*********** 3rd Graph  ************#

# Get x values of the sin and cos wave
x= np.arange(0.,10,0.1)

# implementing cos wave
a=np.cos(x)
# implementing sine wave
b=np.sin(x)

#plot sin wave with blue colour
plt.plot(x,a,'b',label = "cos(x)")

#plot cos wave with dashed line of red colour 
plt.plot(x,b,'r',linestyle='dashed' ,label = "sin(x)" )

#title of the graph
plt.title('Line graph for sin(x) and cos(x)')

# show a legend on the plot
plt.legend()

#function to show the plot
plt.show()



#*********** 4th Graph  ************#
 
# x axis values
x = [1,2,3,4,5,6]
# corresponding y axis values
y = [2,4,1,5,2,6]
 
# plotting the points
plt.plot(x, y, color='b', linestyle='dashed', linewidth = 2,marker='*', markerfacecolor='black', markersize=12)
 
# setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to  graph
plt.title('Line graph with some customization')
 
# function to show the plot
plt.show()



#*********** 1st Graph  ************#

 
# Creating dataset
a = np.array([22, 87, 5, 43, 56,73, 55, 54, 11,20, 51, 5, 79, 31,27])
 
# Creating histogram
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(a, bins = [0, 25, 50, 75, 100])
 
# Show plot
plt.show()


#*********** 2nd Graph  ************#


from matplotlib.ticker import PercentFormatter

# Creating dataset
np.random.seed(23685752)
N_points = 10000
n_bins = 20

# Creating distribution
x = np.random.randn(N_points)
y = .8 ** x + np.random.randn(10000) + 25

# Creating histogram
fig, axs = plt.subplots(1, 1,figsize =(10, 7),tight_layout = True)

axs.hist(x, bins = n_bins )

# Show plot
plt.show()


####################  VANDANA   ######################


#*********** 1st Graph  ************#

#Creating a Dataset
X = ['Group A','Group B','Group C','Group D']
Ygirls = [10,20,20,40]


#Creating an array
X_axis = np.arange(len(X))

plt.bar(X_axis, Ygirls, 0.4, label = 'Girls',color =['red','cyan','yellow','blue'])

plt.xticks(X_axis, X)
plt.xlabel("Groups")
plt.ylabel("Number_of_Students")
plt.title("Number of Students in each group")
plt.legend()

plt.show()


#*********** 2nd Graph  ************#

#Creating a Dataset
X = ['Group A','Group B','Group C','Group D']
Ygirls = [10,20,20,40]


#Creating an array
X_axis = np.arange(len(X))

plt.barh (X_axis, Ygirls, 0.4, label = 'Girls',color = 'magenta')

plt.xticks(X_axis, X)
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Horizontal bar graph")
plt.legend()

plt.show()


#*********** 3rd Graph  ************#


#Multiple bar-graph
#import libraries

import numpy as np
import matplotlib.pyplot as plt

#Dataset
X = ['Group A','Group B','Group C','Group D']
Ygirls = [10,20,20,40]
Zboys = [20,30,25,30]

#Creating an array
X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys')

plt.xticks(X_axis, X)
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Number of Students in each group")
plt.legend()

plt.show()

#*********** 4th Graph  ************#


#Dataset
X = ['Group A','Group B','Group C','Group D']
data = [[10,20,20,40],[20,30,25,30],[10,8,15,13]]

#Creating an array
X_axis = np.arange(len(X))

plt.bar(X_axis + 0.00, data[0], label = 'Girls', color = 'cyan',width = 0.25)
plt.bar(X_axis + 0.25, data[1], label = 'Boys', color = 'black',width = 0.25)
plt.bar(X_axis + 0.50, data[2], label = 'Teachers', color = 'red' ,width = 0.25)

plt.xticks(X_axis + 0.27, X)
plt.xlabel("Groups")
plt.ylabel("Number of Students and Teachers")
plt.title("Number of Students and Teachers in each group")
plt.legend()

plt.show()

#*********** 5th Graph  ************#

#Dataset
X = ['Group A','Group B','Group C','Group D']
Ygirls = [10,20,20,40]
Zboys = [20,30,25,30]

#Creating an array
X_axis = np.arange(len(X))

plt.barh(X_axis - 0.2, Ygirls, 0.4, label = 'Girls' )
plt.barh(X_axis + 0.2, Zboys, 0.4, label = 'Boys')

plt.xticks(X_axis, X)
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Horizontal bar graph")
plt.legend()

plt.show()