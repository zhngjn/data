import matplotlib.pyplot as plt
import numpy as np

def test1():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.random.randn(100)

    plt.plot(x, y1, ls="-", lw=2, c="g", label="test1 1")
    plt.plot(x, y2, "*", c="b", label="test1 2")
    plt.legend(loc="upper left")
    plt.show()

if __name__ == '__main__':
    test1()