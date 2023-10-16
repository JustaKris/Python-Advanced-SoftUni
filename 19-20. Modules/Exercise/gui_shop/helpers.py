import os
from canvas import app

base_path = os.path.dirname(__file__)


def clean_screen():
    for el in app.grid_slaves():
        el.destroy()
