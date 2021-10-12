"""
Make NFT Style images
Based on 1 initial image
"""

import os
import random
import svgwrite
import svgutils.transform as st

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

from word_grab import two_word_name

# Constants
PATH = 'output'
IMG_H = 400
IMG_W = 400
SRC_IMG = "pi_400.svg"
NUM_IMAGES = 10
TWNAME = (two_word_name())

class Dwg:

    """create class for a clear svg of rectangles"""

    def __init__(self, sqheight=10, sqwidth=10, fill="rgb(135,125,24)"):

        self.width = sqwidth
        self.height = sqheight

        self.dwg = svgwrite.Drawing(
            "test.svg",
            size=(IMG_H, IMG_W),
            profile="tiny",
            stroke_width=0.5,
            stroke="black",
            stroke_opacity=1.0,
            fill=fill,
        )

    def draw_rectangles_tl(self):
        '''Create rectangles in top left'''

        for x in range(0, self.width):
            for y in range(0, self.height):
                pos_mod_x = (random.random() - 0.5) * (x + (x * self.width))
                pos_mod_y = (random.random() - 0.5) * (x + (y * self.height))
                self.dwg.add(
                    self.dwg.rect(
                        (x * 10 + pos_mod_x, y * 10 + pos_mod_y),
                        (self.width, self.height),
                    )
                )

    def draw_rectangles_br(self):
        '''Create rectangles in bottom rightt'''

        for x in range(0, self.width):
            for y in range(0, self.height):
                pos_mod_x = (random.random() - 0.5) * (x + (x * self.width))
                pos_mod_y = (random.random() - 0.5) * (x + (y * self.height))
                self.dwg.add(
                    self.dwg.rect(
                        (IMG_W - x * 10 + pos_mod_x, IMG_H - y * 10 + pos_mod_y),
                        (self.width, self.height)
                    )
                )

    def draw_text(self):

        self.dwg.add(
            self.dwg.text(
                TWNAME,
                insert=(70, 325),
                stroke="none",
                fill="#290",
                font_size="30px",
                font_weight="bold",
                font_family="Arial",
            )
        )

    def save_as(self, filename):
        self.dwg.saveas(filename)

# main


if __name__ == "__main__":

    os.chdir(PATH)

    for i in range(1, NUM_IMAGES):

        r1, r2, r3 = random.randint(1, 255), random.randint(
            1, 255), random.randint(1, 255)

        d1 = Dwg()
        d1.draw_rectangles_tl()
        d1.save_as("first.svg")

        d2 = Dwg(sqwidth=15, fill=f"rgb({r2},{r1},{r3})")
        d2.draw_rectangles_tl()
        d2.save_as("second.svg")

        d3 = Dwg(sqwidth=15, fill=f"rgb({r1},{r2},{r3})")
        d3.draw_rectangles_br()
        d3.draw_text()  # Add some text
        d3.save_as("third.svg")

        template = st.fromfile("pi_400.svg")
        first_svg = st.fromfile("first.svg")
        second_svg = st.fromfile("second.svg")
        third_svg = st.fromfile("third.svg")

        template.append(first_svg)
        template.append(second_svg)
        template.append(third_svg)

        # save merged file
        template.save(f"merged{i}.svg")
        drawing = svg2rlg(f"merged{i}.svg")
        renderPM.drawToFile(drawing, f"merged{i}.png", fmt="PNG")


    # # # save source SVG files
    # drawing = svg2rlg("first.svg")
    # renderPM.drawToFile(drawing, "first.png", fmt="PNG")

    # drawing = svg2rlg("second.svg")
    # renderPM.drawToFile(drawing, "second.png", fmt="PNG")

    # drawing = svg2rlg("third.svg")
    # renderPM.drawToFile(drawing, "third.png", fmt="PNG")
