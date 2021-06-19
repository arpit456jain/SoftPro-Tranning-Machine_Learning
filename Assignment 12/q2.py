from matplotlib import pyplot as plt

# Data to plot
labels =  'Java' , 'Python', 'Php', 'JavaScript' , 'C#', 'C++'
sizes = [17.6,22.2,8.8,8,.7,6.7]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red' , 'blue']
explode = (0.1, 0, 0, 0 , 0 ,0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()