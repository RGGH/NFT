"""
Makes NFT Style image
ready for another image to be merged with it
"""

import os
import random
import svgwrite
import svgutils.transform as st
# from pathlib import Path
# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPM

# Constants
PATH = 'output'
IMG_H = 400
IMG_W = 400
SRC_IMG = "pi_400.svg"


class Dwg:

    """create class for a clear svg of rectangles"""

    def __init__(self, sqheight=10, sqwidth=10, fill="rgb(135,125,24)"):

        self.width = sqheight
        self.height = sqwidth

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

    def save_as(self, filename):
        self.dwg.saveas(filename)

# main


if __name__ == "__main__":

    os.chdir(PATH)

    d1 = Dwg()
    d1.draw_rectangles_tl()
    d1.save_as("first.svg")

    d2 = Dwg(sqheight=15, fill="rgb(25,25,214)")
    d2.draw_rectangles_br()
    d2.save_as("second.svg")

    d3 = Dwg(sqwidth=15, fill="rgb(25,185,214)")
    d3.draw_rectangle_tl()
    d3.save_as("third.svg")

    # The main image
    template = st.fromfile(SRC_IMG)

    # The overlays
    first_svg = st.fromfile("first.svg")
    second_svg = st.fromfile("second.svg")
    third_svg = st.fromfile("third.svg")

    template.append(first_svg)
    template.append(second_svg)
    template.append(third_svg)

    # save merged file
    template.save("merged.svg")

    '''convert svgs to png if required'''

    # drawing = svg2rlg("first.svg")
    # renderPM.drawToFile(drawing, "source_images/first.png", fmt="PNG")

    # drawing = svg2rlg("second.svg")
    # renderPM.drawToFile(drawing, "source_images/second.png", fmt="PNG")

    # drawing = svg2rlg("third.svg")
    # renderPM.drawToFile(drawing, "source_images/third.png", fmt="PNG")
