import matplotlib.pyplot as plt
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("2LINE PLOTTED GRAPH")
x=[1,2,6,18]
y=[3,10,12,20]
x1=[1,8,5,10]
y1=[4,6,11,22]
plt.plot(x,y,marker='o',linestyle='dotted',color='red',mec='green',mfc='green')
plt.plot(x1,y1,marker='o',linestyle='solid',color='black',mec='yellow',mfc='yellow')
plt.legend(["first","second"],loc="lower right")
plt.show()
