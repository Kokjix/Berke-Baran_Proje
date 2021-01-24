import matplotlib.pyplot as plt



def bar_draw(colors):
    x = ["Red", "Yellow", "Green", "Orange", "White", "Black", "Blue"]
    w = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    plt.bar(x, color, width=w)

    plt.xlabel("Car Colors")
    plt.ylabel("Car Color Numbers")

    plt.title("Analyzed Car's Color Bar Chart")
    plt.show()