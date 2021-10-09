"""
Makes NFT Style image
ready for another image to be merged with it
and adds text
"""
import random
import svgwrite
import svgutils.transform as st
from pathlib import Path

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


class Dwg:

    """create class for rectangles"""

    def __init__(self, height=10, width=10, fill="rgb(255,255,44)"):

        self.width = height
        self.height = width

        self.dwg = svgwrite.Drawing(
            "test.svg",
            size=(400, 400),
            profile="tiny",
            stroke_width=0.5,
            stroke="black",
            stroke_opacity=1.0,
            fill=fill,
        )

    def draw_rectangle(self):

        for x in range(0, self.width):
            for y in range(0, self.height):
                pos_mod_x = (random.random() - 0.5) * (x + (y * self.width))
                pos_mod_y = (random.random() - 0.5) * (x + (y * self.height))
                self.dwg.add(
                    self.dwg.rect(
                        (x * 10 + pos_mod_x, y * 10 + pos_mod_y),
                        (self.width, self.height),
                    )
                )

    def draw_text(self):

        self.dwg.add(
            self.dwg.text(
                "Dr Pi",
                insert=(55, 125),
                stroke="none",
                fill="#900",
                font_size="90px",
                font_weight="bold",
                font_family="Arial",
            )
        )

    def save_as(self, filename):
        self.dwg.saveas(filename)


# main
if __name__ == "__main__":

    path = Path("source_images/pi_400.svg")
    assert path.is_file(), "pi_400 missing"

    d1 = Dwg()
    d1.draw_rectangle()
    d1.save_as("first.svg")

    d2 = Dwg(height=15, fill="rgb(255,255,214)")
    d2.draw_rectangle()
    d2.save_as("second.svg")

    d3 = Dwg(width=15, fill="rgb(255,85,214)")
    d3.draw_rectangle()
    d3.draw_text()  # Add ome text
    d3.save_as("third.svg")

    template = st.fromfile("source_images/pi_400.svg")
    second_svg = st.fromfile("second.svg")
    third_svg = st.fromfile("third.svg")

    template.append(second_svg)
    template.append(third_svg)

    # save merged file
    template.save("merged.svg")

    # save source SVG files
    drawing = svg2rlg("first.svg")
    renderPM.drawToFile(drawing, "source_images/first.png", fmt="PNG")

    drawing = svg2rlg("second.svg")
    renderPM.drawToFile(drawing, "source_images/second.png", fmt="PNG")

    drawing = svg2rlg("third.svg")
    renderPM.drawToFile(drawing, "source_images/third.png", fmt="PNG")
