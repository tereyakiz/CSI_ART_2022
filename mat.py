import matplotlib.pyplot as plt

x = list(range(100))   # creates a list of numbers 1..99
y = [i**2 for i in x]  # creates list squaring each number from list x

plt.plot(x,y) # plots y against x

plt.show() # shows the plot