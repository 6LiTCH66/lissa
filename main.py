import numpy as np
from matplotlib.pyplot import plot, figure, show
def main():

    A = 1
    B = 1

    a = 9
    b = 8
    delta = np.pi/2
    t = np.arange(0, 4 * np.pi / 2, 0.001)
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)

    figure()
    plot(x, y)
    show()
    


if __name__ == "__main__":
    main()