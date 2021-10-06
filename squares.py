
import svgwrite
import svgutils.transform as st
import random


class Dwg():

    def __init__(self,height=10, width=10, fill = "rgb(255,255,44)"):

        self.width = height
        self.height = width
        
        self.dwg = svgwrite.Drawing(
        'test.svg', 
        size=(400, 400), 
        profile='tiny', 
        stroke_width=0.5,
        stroke='black',
        stroke_opacity=1.0,
        fill = fill
        )

    def draw_rectangle(self):
        
        for x in range(0, self.width):
            for y in range(0, self.height):
                position_modifier_x = (random.random() - 0.5) * (x + (y * self.width))
                position_modifier_y = (random.random() - 0.5) * (x + (y * self.height))
                self.dwg.add(self.dwg.rect(
                    (
                        x * 10 + position_modifier_x,
                        y * 10 + position_modifier_y
                    ),
                    (self.width,self.height)
                ))

    def save_as(self,filename):
        self.dwg.saveas(filename)

# main
if __name__ == "__main__":

    d1 = Dwg()
    d1.draw_rectangle()
    d1.save_as("first.svg")

    d2 = Dwg(height=15, fill = "rgb(255,255,214)")
    d2.draw_rectangle()
    d2.save_as("second.svg")

    d3 = Dwg(width=15, fill = "rgb(255,85,214)")
    d3.draw_rectangle()
    d3.save_as("third.svg")

    template = st.fromfile('first.svg')
    second_svg = st.fromfile('second.svg')
    third_svg = st.fromfile('third.svg')

    template.append(second_svg)

    template.append(third_svg)
    template.save('merged.svg')

    # https://stackoverflow.com/a/23482756/12670189


 
