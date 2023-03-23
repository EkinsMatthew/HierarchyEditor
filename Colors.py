import typing

colors = {
    "background_dark": {
        "dark": "#002b36",
        "light": "#eee8d5",
    },
    "background_light": {
        "dark": "#073642",
        "light": "#fdf6e3",
    },
    "content_0": "#839496",
    "content_1": "#93a1a1",
    "content_00": "#657b83",
    "content_01": "#586e75",
    "Yellow": "#b58900",
    "Orange": "#cb4b16",
    "Red": "#dc322f",
    "Magenta": "#d33682",
    "Violet": "#6c71c4",
    "Blue": "#268bd2",
    "Cyan": "#2aa198",
    "Green": "#859900",
}


@staticmethod
def get_color(color_name: str, theme: typing.Optional[str] = None):
    item = colors[color_name]
    # If the item is a dict, we need the additional context of the theme
    # desired
    if type(item) == dict:
        if theme is None:
            raise ValueError("For theme based colors, a theme must be passed.")
        return item[theme]
    return item
