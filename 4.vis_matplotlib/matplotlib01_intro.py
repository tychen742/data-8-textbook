# import matplotlib
# print(matplotlib.__version__)

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 10])
# ypoints = np.array([0, 50])

# plt.plot(xpoints, ypoints)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y)
# plt.show()

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show()

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# print(random.normal(size=10))