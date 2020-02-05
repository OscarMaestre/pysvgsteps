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


        fig_txt_src_address=Text(x+offset_x, y+offset_y, txt_src_address)
        self.diagram.add_shape(fig_txt_src_address)
        self.add_shape(self.diagram)


class Router(CompoundShape):
    def __init__(self,x, y,  address_left, address_right, width=150, height=40):
        self.x=x
        self.y=y
        self.height=height
        self.width=width

        self.diagram=CompoundShape()
        super().__init__()
        fig_src_address=Rect(x, y, height, width)
        self.diagram.add_shape(fig_src_address)

        radius=height/9
        
        fig_card_1=Circle(x-radius, y+(height/2), radius)
        fig_card_1.set_fill()
        self.diagram.add_shape(fig_card_1)

        fig_card_2=Circle(width+x+radius, y+(height/2), radius)
        fig_card_2.set_fill()
        self.diagram.add_shape(fig_card_2)

        offset_x=140
        offset_y=20+(height/2)
        
        fig_txt_left_address=Text(x-offset_x, y+offset_y, address_left)
        self.diagram.add_shape(fig_txt_left_address)

        fig_txt_right_address=Text(x+offset_x+20, y+offset_y, address_right)
        self.diagram.add_shape(fig_txt_right_address)

        self.add_shape(self.diagram)

        

    def get_left_card_coordinates(self):
        x=self.x
        y=self.y+(self.height/2)
        return (x, y)

    def get_right_card_coordinates(self):
        x=self.x+self.width
        y=self.y+(self.height/2)
        return (x, y)


class PCRightCard(CompoundShape):
    def __init__(self,x, y,  address_right, name, gw, width=180, height=100):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        
        self.diagram=CompoundShape()
        super().__init__()
        
        fig_src_address=Rect(x, y, height, width)
        self.diagram.add_shape(fig_src_address)

        radius=5
        
        
        fig_card_2=Circle(width+x+radius, y+(height/2), radius)
        fig_card_2.set_fill()
        self.diagram.add_shape(fig_card_2)

        offset_x=5
        offset_y=height/2
        
        
        fig_txt_right_address=Text(x+offset_x+3, y+offset_y, "IP:"+address_right)
        self.diagram.add_shape(fig_txt_right_address)

        txt_name=Text(x+20, y+20, name)
        txt_name.add_attribute("fill", "blue")
        self.diagram.add_shape(txt_name)
        
        
        txt_gw=Text(x+offset_x, y+70, "GW;"+gw)
        txt_gw.add_attribute("fill", "blue")
        self.diagram.add_shape(txt_gw)

        self.add_shape(self.diagram)



    
    def get_right_card_coordinates(self):
        x=self.x+self.width
        y=self.y+(self.height/2)
        return (x, y)



class PCLeftCard(CompoundShape):
    def __init__(self,x, y,  address_right, name, gw, width=180, height=100):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        
        self.diagram=CompoundShape()
        super().__init__()
        
        fig_src_address=Rect(x, y, height, width)
        self.diagram.add_shape(fig_src_address)

        radius=5
        
        
        fig_card_1=Circle(x-radius, y+(height/2), radius)
        fig_card_1.set_fill()
        self.diagram.add_shape(fig_card_1)

        offset_x=5
        offset_y=height/2
        
        
        fig_txt_right_address=Text(x+offset_x+3, y+offset_y, "IP:"+address_right)
        self.diagram.add_shape(fig_txt_right_address)

        txt_name=Text(x+20, y+20, name)
        txt_name.add_attribute("fill", "blue")
        self.diagram.add_shape(txt_name)
        
        
        txt_gw=Text(x+offset_x, y+70, "GW;"+gw)
        txt_gw.add_attribute("fill", "blue")
        self.diagram.add_shape(txt_gw)

        self.add_shape(self.diagram)

    def get_left_card_coordinates(self):
        x=self.x
        y=self.y+(self.height/2)
        return (x, y)

    
    
class PCStack(CompoundShape):
    def __init__(self,x, y, ip_prefix, mask, gw, num_first_pc, total_pcs=2, right=True):
        self.x=x
        self.y=y    
        self.total_pcs=total_pcs   
        self.diagram=CompoundShape()
        self.right=right
        super().__init__()

        self.pcs=[]
        current_y=y
        self.offset_pcs=20
        pc_number=num_first_pc
        for i in range(0, total_pcs):
            ip="{0}.{1}/{2}".format(ip_prefix,str(pc_number),  str(mask))
            pc_name="PC {0}".format(str(i))
            pc=None
            if right:
                pc=PCRightCard(x, current_y, ip , pc_name, gw)
            else:
                pc=PCLeftCard(x, current_y, ip , pc_name, gw)
            self.pcs.append(pc)
            self.diagram.add_shape(pc)
            current_y=current_y+pc.height+self.offset_pcs
            pc_number=pc_number+1

    def get_pc(self, num):
        return self.pcs[num]

    def get_total_pcs(self):
        return self.total_pcs

    def join_to_router(self, router):
        x_card=0
        y_card=0
        if self.right:
            (x,y)=router.get_left_card_coordinates()
        else:
            (x,y)=router.get_right_card_coordinates()
        for i in range(0, self.total_pcs):
            pc=self.pcs[i]
            if self.right:
                (x_pc, y_pc)=pc.get_right_card_coordinates()
            else:
                (x_pc, y_pc)=pc.get_left_card_coordinates()
            line=Line(x,y, x_pc, y_pc)
            self.diagram.add_shape(line)

    def get_diagram(self):
        return self.diagram



if __name__ == "__main__":
    p=Packet(20, 40, "192.167.2.202", 45431, "221.91.189.90", 443)
    r=Router(520, 240, "192.168.1.1/24", "10.0.2.2/8")
    pc_1=PCRightCard(130, 300, "192.168.1.10/24", "PC 1", "192.168.1.1")
    pc_2=PCLeftCard(730, 300, "192.168.1.11/24", "PC 2", "192.168.1.1")
    svg=SVG(2100, 2970)
    (x1, y1)=pc_1.get_right_card_coordinates()
    (x2, y2)=r.get_left_card_coordinates();
    linea=Line(x1,y1,x2,y2);
    svg.add_shape(p)
    svg.add_shape(r)
    svg.add_shape(pc_1)
    svg.add_shape(pc_2)
    svg.add_shape(linea)

    pila_pcs=PCStack(640, 40, "192.168.1", 24, "192.168.1.1", 10, 3, right=False)
    r=Router(220, 240, "192.168.1.1/24", "10.0.2.2/8")
    pila_pcs.join_to_router(r)
    svg2=SVG(2100, 2970)
    svg2.add_shape(pila_pcs.get_diagram())
    svg2.add_shape(r)
    print(svg2.as_html_page())
