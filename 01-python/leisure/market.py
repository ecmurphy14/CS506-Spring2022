import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def draw_market():

    img = mpimg.imread('5760.jpg')
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    plt.savefig('market.png')