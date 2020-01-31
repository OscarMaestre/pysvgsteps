#!/usr/bin/python3

from Shape import *

class Packet(CompoundShape):
    def __init__(self,x, y,  src_address, src_port, dst_address, dst_port, width=250, height=30):
        super().__init__()
        self.src_address=src_address
        self.dst_address=dst_address
        
        self.src_port   =src_port
        self.dst_port   =dst_port
        
        self.x=x
        self.y=y
        
        self.diagram=CompoundShape()
        
        fig_src_address=Rect(x, y, height, width)
        self.diagram.add_shape(fig_src_address)

        fig_dst_address=Rect(x, y+height, height, width)
        self.diagram.add_shape(fig_dst_address)


        fig_src_port=Rect(x+width, y, height, width)
        self.diagram.add_shape(fig_src_port)

        fig_dst_port=Rect(x+width, y+height, height, width)
        self.diagram.add_shape(fig_dst_port)

        offset_x=9
        offset_y=18

        txt_src_address="IP Origen:  {0}".format(src_address)
        txt_dst_address="IP Destino: {0}".format(dst_address)

        txt_src_port="Puerto origen: {0}".format(src_port)
        txt_dst_port="Puerto destino:{0}".format(dst_port)

        fig_txt_src_address=Text(x+offset_x, y+offset_y, txt_src_address)
        self.diagram.add_shape(fig_txt_src_address)

        fig_txt_dest_address=Text(x+offset_x, y+height+offset_y, txt_dst_address)
        self.diagram.add_shape(fig_txt_dest_address)

        fig_txt_src_port=Text(x+offset_x+width, y+offset_y, txt_src_port)
        self.diagram.add_shape(fig_txt_src_port)

        fig_txt_dest_port=Text(x+offset_x+width, y+height+offset_y, txt_dst_port)
        self.diagram.add_shape(fig_txt_dest_port)




        self.add_shape(self.diagram)

    

if __name__ == "__main__":
    p=Packet(20, 40, "192.167.2.202", 45431, "221.91.189.90", 443)
    svg=SVG(2100, 2970)
    svg.add_shape(p)
    print(svg.as_html_page())
