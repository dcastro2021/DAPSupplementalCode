import matplotlib.pyplot as plt
import numpy as np
# make a silly array
x = np.arange(1, 15)
# for our demo, y can be anything (in this case, we will end up with a straight line)
y = (x - 2) * 5

# give the chart a title
plt.title("Melissa's Chart")

#text(0.5, 1.0, "Melissa's Chart")
# label our x and y axis
plt.xlabel("donuts")
#text(0.5, 0, 'donuts')
plt.ylabel("dollar")

#text(0, 0.5, 'dollar')
# tell it to plot
plt.plot(x, y)
# tell it to display
plt.show()