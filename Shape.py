#!/usr/bin/python3


class Shape(object):
    def __init__(self):
        self.attributes=dict()
        self.autoclosetag=True
        self.contents=""
        self.tag=""
        self.attributes["stroke"]="black"
        self.attributes["fill"]="white"
        self.attributes["stroke-width"]=1


    def add_attribute(self, attribute, value):
        self.attributes[attribute]=value
    
    def get_attributes(self):
        text=""
        for key, value in self.attributes.items():
            text+="{0}='{1}' ".format(key, value)
        return text

    def __str__(self):
        attributes=self.get_attributes()
        if self.autoclosetag:
            text="<{0} {1}/>".format(self.tag, attributes)
        else:
            text="<{0} {1}>{2}</{0}>".format(self.tag, attributes, self.contents)
        return text




class CompoundShape(Shape):
    def __init__(self):
        self.shapes=[]

    def add_shape(self, shape):
        self.shapes.append(shape)
    def __str__(self):
        shapes= "\n".join(map(str, self.shapes))
        return shapes



class SVG(CompoundShape):
    def __init__(self, width, height):
        self.shapes=[]
        self.width=width
        self.height=height
    def __str__(self):
        shapes= "\n".join(map(str, self.shapes))
        text="<svg height='{0}' width='{1}'>{2}</svg>".format(self.height, self.width, shapes)
        return text
    def as_html_page(self):
        template="""
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                {0}
            </body>
        </html>
        """
        text=self.__str__()
        return template.format(text)



    



class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.tag="circle"
        self.add_attribute("cx", x)
        self.add_attribute("cy", y)
        self.add_attribute("radius", radius)

class Text(Shape):
    def __init__(self, x, y, text):
        super().__init__()
        self.autoclosetag=False
        self.contents=text
        self.tag="text"
        self.add_attribute("x", x)
        self.add_attribute("y", y)
        self.add_attribute("fill", "black")

class Rect(Shape):
    def __init__(self, x, y, height, width):
        super().__init__()
        self.tag="rect"
        self.add_attribute("x", x)
        self.add_attribute("y", y)
        self.add_attribute("height", height)
        self.add_attribute("width", width)
        
if __name__ == "__main__":
    c=Circle(20, 40, 20)
    print(c)
    t=Text(20, 90, "Hola mundo")
    print(t)
    r=Rect(20, 20, 90, 100)
    print(r)