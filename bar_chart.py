import matplotlib.pyplot as plt
"""
Renkleri bar cahrta gösteren fonksiyon.
"""


def bar_draw(colors): # Grafik çizdirecek fonksiyon
    x = ["Red", "Yellow", "Green", "Orange", "White", "Black", "Blue"] # X ekseni Renklerin adları
    w = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2] # Barların kalınlığı
    plt.bar(x, colors, width=w) # x ve ye eksenini grafiklerştiricek metodu colors rank sırası x te adlandırdığım gibi olsun Berke

    plt.xlabel("Car Colors") #x'in adı
    plt.ylabel("Car Color Numbers") # y'nin adı

    plt.title("Analyzed Car's Color Bar Chart") # grafiğin başlığı
    plt.show() #grafiği gösteren metdor