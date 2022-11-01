import matplotlib.pyplot as plt
from skimage import data, color
import numpy as np


class Image(object):

    def __init__(self, img, title):
        self.img = img
        self.title = title


def manage_inputs(func):
    def wrapper(*args, **kwargs):
        if isinstance(args[0], list):
            image_list = args[0]
            for image in image_list:
                img_args = (image, *args[1:])
                if kwargs['display_original_image']:
                    show_image(image.img, title=image.title)
                func(*img_args, **kwargs)

        else:
            func(*args, **kwargs)

    return wrapper


def show_image(image, title='Title not specified', cmap=None):
    """
    gray parameter is given because imshow provides a heatmap instead of classic gray values
    """
    cmap = plt.cm.gray if cmap is not None else None
    plt.figure()
    plt.imshow(image, cmap=cmap)
    plt.title(title)


@manage_inputs
def simple_image_plot(image, **kwargs):
    show_image(image.img, title=image.title)


@manage_inputs
def transform_colors(image, **kwargs):
    # original image to gray
    gray_image = color.rgb2gray(image.img)
    show_image(gray_image, title=f'gray_{image.title}', cmap='gray')


@manage_inputs
def flip_images(image, how='ud', **kwargs):
    flip_dic = {'ud': {'method': np.flipud,
                       'title': f'flipped_up_down_{image.title}'},
                'lr': {'method': np.fliplr,
                       'title': f'flipped_left_right_{image.title}'}}

    flipped_image = flip_dic[how]['method'](image.img)
    show_image(flipped_image, title=flip_dic[how]['title'], cmap='gray')


def main():
    coffee_image = Image(data.coffee(), 'Coffee')
    rocket_image = Image(data.rocket(), 'Rocket')
    images = [coffee_image, rocket_image]
    # transform_colors(images)
    # flip_images(images, how='ud', display_original_image=False)


if __name__ == '__main__':
    main()
    plt.show()
