import numpy as np
import scipy
import matplotlib.pyplot as plt
from math import pi, sqrt
from cmath import phase

y = scipy.fromfile(open("signal-source-out.bin"), dtype=scipy.float32, count = 64)

plt.plot(y, 'bx')
plt.xlabel("Sample Number")
plt.axis("on")
plt.show()
