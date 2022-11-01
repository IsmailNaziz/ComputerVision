import matplotlib.pyplot as plt
from skimage import data

def show_image(image, title, cmap_type='gray'):
    plt.figure()
    plt.imshow(image, cmap_type=cmap_type)
    plt.title(title)

def show_image_std(image, title):
    plt.figure()
    plt.imshow(image)
    plt.title(title)


def main():
    coffee_image = data.coffee()
    coins_image = data.coins()
    show_image_std(coffee_image, title=coffee_image)
    show_image_std(coins_image, title=coffee_image)
    return

if __name__ == '__main__':
    main()
    plt.show()


