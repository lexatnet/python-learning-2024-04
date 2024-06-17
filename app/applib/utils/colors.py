import random


def generate_random_colors_rgb(number_of_colors):
    return [
        "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
        for i in range(number_of_colors)
    ]


def get_random_colors_from_palette(number_of_colors):
    palette = [
        "#21a055",
        "#00702e",
        "#c53117",
        "#c51785",
        "#4f17c5",
        "#c5b517",
        "#179ec5",
        "#544828",
        "#285451",
        "#502854",
        "#3b2854",
        "#0ad0e3",
        "#0ae324",
        "#e30ab3",
        "#e30f0a",
        "#e3710a",
        "#0ac4e3",
    ]
    return [random.choice(palette) for j in range(number_of_colors)]
