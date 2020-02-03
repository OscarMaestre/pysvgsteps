from Shape import *
from math import sin, cos


def as_html_page(cloud):
        template="""
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                <svg height="1000" width="1000">{0}</svg>
            </body>
        </html>
        """
        text=cloud.__str__()
        return template.format(text)

class Cloud(Shape):
    def __init__(self, cx, cy, radius, total_points=8):
        super().__init__()
        self.points=[]
        self.cx=cx
        self.cy=cy
        self.radius=radius
        self.tag="polygon"
        self.total_points=total_points
        self.generate_points()
    def __str__(self):
        attributes=self.get_attributes()
        if self.autoclosetag:
            text="<{0} {1}/>".format(self.tag, attributes)
        else:
            text="<{0} {1}>{2}</{0}>".format(self.tag, attributes, self.contents)
        return text

    def generate_points(self):
        start=0
        end=3.15415926*2
        rads=0
        delta=end/self.total_points
        while rads<end:
            x=int(self.radius*sin(rads)) + self.cx 
            y=int(self.radius*cos(rads)) + self.cy
            self.points.append( (x, y))
            rads=rads+delta

        
        tuples_format="{0},{1}"
        tuples=[tuples_format.format(t[0], t[1]) for t in self.points]
        tuples_string=" ".join(tuples)
        self.add_attribute("points", tuples_string)
            


if __name__ == "__main__":
    c=Cloud(100, 100, 80, total_points=5)
    print(as_html_page(c))