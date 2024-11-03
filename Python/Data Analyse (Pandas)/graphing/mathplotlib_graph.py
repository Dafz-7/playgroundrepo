import numpy as np
import matplotlib.pyplot as plt

#* Cosine, sine, and tangent

x = [0, 30, 90, 120, 150, 180, 210, 270]
y = np.cos(x)
print("Cosine value:", y)

#* Show the graph of cosine values
plt.title("Cosine Angle Plot")
plt.plot(x, y)
plt.xlabel("Angle Value")
plt.ylabel("Cosine Value of the Angle")
plt.grid()
plt.show()