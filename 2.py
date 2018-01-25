from cycler import cycler
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 2 * np.pi, 50)

default_cycler = cycler(color='r', linestyle= '-')

plt.rc('lines', linewidth=1)
plt.rc('axes', prop_cycle=default_cycler)

fig, (ax0) = plt.subplots(nrows=1)
ax0.plot(yy)
ax0.set_title('Set default color cycle to rgby')

plt.show()