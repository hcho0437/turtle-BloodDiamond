import random

def fill_half_screen(t,color,size):
    t.up()
    t.fillcolor(color)
    t.begin_fill()
    if size ==0:
        t.goto(-950,0)
        t.goto(-950,500)
        t.goto(950,500)
        t.goto(950,0)
    else :
        t.goto(-950,0)
        t.goto(-950,500)
        t.goto(950,500)
        t.goto(950,-500)
        t.goto(-950,-500)
        t.goto(-950,0)
    t.end_fill()
    

def draw_color_balls(k,size):
    count =0
    while count <100:
        k.dot(15,'blue')
        k.fd(size)
        k.dot(15,'red')
        k.lt(90)
        k.fd(size)
        k.dot(15,'blue')
        k.lt(90)
        k.fd(size)
        k.dot(15,'green')
        k.lt(90)
        k.fd(size)
        k.dot(15,'yellow')

def draw_3d_block(k):
    k.lt(35)
    k.fd(50)
    k.rt(70)
    k.fd(50)
    k.rt(105)
    k.fd(50)
    k.rt(77)
    k.fd(56)
    k.lt(127)
    k.fd(70)
    k.lt(55)
    k.fd(55)
    k.lt(125)
    k.fd(68)
    k.bk(68)
    k.rt(50)
    k.fd(51)
    k.lt(50)
    k.fd(67)

def draw_the_world_of_3d_block(k):
    k.ht();k.up();k.setpos(-960,450);k.down()
    count =0
    while count <11:
        for i in range(30):
            draw_3d_block(k)
            k.rt(90)
        k.up()
        k.bk(2529)
        k.down()
        k.lt(270)
        k.up()
        k.fd(91)
        k.down()
        k.lt(90)
        count +=1
    return
    
def draw_polygon(t,sides,distance):
    angle = 360 / sides
    for times in range(sides):
        t.forward(distance)
        t.left(angle)

def draw_star(t,size):
    count =0
    angle =144
    while count <=5:
        t.forward(size)
        t.right(angle)
        count += 1
    return

def draw_star_2(t,size):
    count =0
    angle =140
    while count <=5:
        t.forward(size)
        t.left(angle)
        count +=1
    return

def draw_diamond(t,size,sides,mode):
    count =0
    star_size =size+count
    #it makes only 19 polygon
    while count <=19:
        draw_polygon(t,sides,size)
        t.rt(90)
        t.fd(size)
        t.up()
        t.bk(size)
        t.down()
        count +=1
        draw_star(t,size) 
        #if mode equals 1, it stays on (0,0)
        if mode ==1:
            t.up()
            t.goto(0,0)
            t.down()

def draw_flower_of_diamond(k,mode,colormode,color_1,color_2):
    count =0
    #if colormode equals 1,you can decide color whatever you want
    if colormode ==1:
        k.color(color_1)
    k.up()
    k.goto(100,-200)
    #it makes only 6 'draw_diamond'
    while count <6:
        draw_diamond(k,80,5,0)
        k.up()
        k.lt(60)
        k.fd(200)
        k.down()
        count +=1
    #it goes next place to draw another one
    k.up()
    k.goto(0,0)
    k.lt(180)
    #if you decided your colormode as 1, it gives another color for next shape
    if colormode ==1:
        k.color(color_2)
    #it draws different things inside the 'draw_diamond's, you can choose 1 or 2, and 0 dose nothing
    if mode ==1:
        k.down()
        draw_6_spiral(k,35,0)
    if mode ==2:
        k.down()
        draw_wheel(k,200)
    if mode ==3:
        k.down()
        draw_web(k,50,3,4)
    if mode ==4:
        k.down()
        draw_crystallize(k)


def draw_spiral(t,size):
    count =0
    sys =0
    while count <70:
        t.fd(size+10)
        t.lt(7+sys*1.2)
        count +=1
        sys +=1
        #if sys >=40:
            #sys =40
    return

def draw_6_spiral(t,size,with_diamond):
    count =0
    while count <=5:
        t.width(1.8)
        draw_spiral(t,size)
        t.up()
        t.rt(90)
        t.bk(size*8)
        t.down()
        count +=1;
    if with_diamond ==1:
        #t.width(1)
        t.lt(90)
        t.fd(size*0.45)
        draw_diamond(t,size,5,0,1)
    return

def draw_ult_6_spiral(t,size,mode,times):
    count =0
    if mode ==0:
        t.setpos(0,0)
    while count <=times:
        draw_6_spiral(t,size,0)
        t.lt(30)
        if mode ==0:
            t.setpos(0,0)
        size +=15
        count +=1
    return

def draw_the_world_of_ult_6_spiral(t):
    count =0
    t.up()
    t.setpos(-500,0)
    t.down()
    while count <3:
        draw_ult_6_spiral(t,5,1,2)
        t.bk(50)
        t.lt(310)
        t.up()
        t.fd(500)
        t.down()
        count +=1
    return

def draw_web(t,size,sides,size_2):
    count =0
    while count <=13:
        draw_polygon(t,sides,size)
        t.lt(90)
        t.fd(size)
        t.up()
        t.bk(size*2)
        t.down()
        draw_star_2(t,size*size_2)
        count +=1
    return

def draw_crystal(k):
    for i in range (4):
        draw_3d_block(k)
        k.lt(180)

def draw_crystallize(k):
    for i in range(6):  
        draw_crystal(k)
        k.lt(60)

def draw_wheel(k,size):
    for i in range(24):
        k.fd(size)
        k.rt(135)
        k.fd(size/3)
        k.rt(135)
        k.fd(size-100)
        k.lt(135)
        k.fd(size/3)
        k.up()
        k.setpos(0,0)
        k.down()
        k.rt(120)
    return
def draw_sunflower(k,size):
    k.fillcolor('maroon')
    k.begin_fill()
    k.circle(size)
    k.end_fill()
    k.up()
    k.lt(180)
    k.fd(size/6)
    k.rt(180)
    k.down()
    for i in range(18):
        k.fillcolor('yellow')
        k.begin_fill()
        k.rt(90)
        k.fd(size)
        k.rt(30)
        k.fd(size)
        k.rt(150)
        k.fd(size)
        k.rt(10)
        k.fd(size)
        k.end_fill()
        k.rt(100)
    k.fd(size/6)
    k.fillcolor('lime')
    k.begin_fill()
    k.rt(110)
    k.fd(size*1.2)
    k.lt(20)
    k.fd(size*1.7)
    k.rt(30)
    k.fd(size*1.1)
    k.lt(120)
    k.fd(size/2.4)
    k.lt(60)
    k.fd(size)
    k.lt(30)
    k.fd(size)
    k.lt(20)
    k.fd(size/1.5)
    k.rt(40)
    k.fd(size*1.1)
    k.lt(10)
    k.fd(size/3)
    k.end_fill()

def draw_mix_1(k,color_1,color_2):
    k.up()
    k.setpos(-34,-62)
    k.down()
    draw_web(k,50,3,4)
    k.up()
    k.setpos(0,0)
    k.down()
    k.color(color_1)
    k.setpos(0,0)
    k.setpos(-400,300)
    draw_crystallize(k)
    k.setpos(0,0)
    k.setpos(400,-300)
    draw_crystallize(k)
    k.setpos(0,0)
    k.setpos(-400,-300)
    draw_crystallize(k)
    k.setpos(0,0)
    k.setpos(400,300)
    draw_crystallize(k)
    k.color(color_2)
    k.up()
    k.setpos(-34,300)
    k.down
    draw_diamond(k,60,3,0,0)
    k.up()
    k.setpos(-34,-300)
    k.down
    draw_diamond(k,60,3,0,0)
    k.up()
    k.setpos(500,0)
    k.down
    draw_diamond(k,60,3,0,0)
    k.up()
    k.setpos(-500,0)
    k.down
    draw_diamond(k,60,3,0,0)

def draw_blackhole(k,size):
    for i in range(180):
        k.fd(size*2)
        k.rt(10)
        k.fd(size/2)
        k.lt(80)
        k.fd(size)
        k.rt(30)
        k.fd(size/3)
        k.lt(70)
        k.fd(size/3.5)
        k.rt(70)
        k.fd(size*1.2)
        k.up()
        k.setpos(0, 0)
        k.down()
        k.rt(2)
    return

def draw_night_of_snow(k):
    count =0
    k.color('white')
    while count <100:
        x =random.randint(-300,300)
        y =random.randint(-200,200)
        k.up()
        k.setpos(x,y)
        k.down()
        draw_web(k,10,3,6)
        k.lt(33)
        count +=1
    return

def draw_night_of_stars(k):
    count =0
    k.color('yellow')
    while count <100:
        x =random.randint(-800,800)
        y =random.randint(-500,500)
        k.up()
        k.setpos(x,y)
        k.down()
        draw_star_2(k,30)
        k.lt(33)
        count +=1
    return

def draw_sunflower(k,size,with_leaf):
    k.fillcolor('maroon')
    k.begin_fill()
    k.circle(size)
    k.end_fill()
    k.up()
    k.lt(180)
    k.fd(size/6)
    k.rt(180)
    k.down()
    for i in range(18):
        k.fillcolor('yellow')
        k.begin_fill()
        k.rt(90)
        k.fd(size)
        k.rt(30)
        k.fd(size)
        k.rt(150)
        k.fd(size)
        k.rt(10)
        k.fd(size)
        k.end_fill()
        k.rt(100)
    k.fd(size/6)
    k.fillcolor('lime')
    k.begin_fill()
    k.rt(110)
    k.fd(size*1.2)
    k.lt(20)
    k.fd(size*1.7)
    k.rt(30)
    k.fd(size*1.1)
    k.lt(120)
    k.fd(size/2.4)
    k.lt(60)
    k.fd(size)
    k.lt(30)
    k.fd(size)
    k.lt(20)
    k.fd(size/1.5)
    k.rt(40)
    k.fd(size*1.1)
    k.lt(10)
    k.fd(size/3)
    k.end_fill()

    
def draw_sunflower_feild(k):
    k.up()
    k.setpos(800,0)
    k.down()
    k.fillcolor('skyblue')
    k.begin_fill()
    k.setpos(-800,0)
    k.setpos(-800,420)
    k.setpos(800,420)
    k.setpos(800,0)
    k.end_fill()
    for i in range(64):
        k.up()
        rsize =random.randint(5,7)
        k.setpos(-800+i*25,30)
        k.down()
        draw_sunflower(k,rsize,0)
    for i in range(34):
        k.up()
        rsize =random.randint(8,11)
        k.setpos(-800+i*50,0)
        k.down()
        draw_sunflower(k,rsize,0)
    for i in range(16):
        k.up()
        rsize =random.randint(15,27)
        k.setpos(-750+i*100,-60)
        k.down()
        draw_sunflower(k,rsize,0)
    for i in range(11):
        k.up()
        rsize =random.randint(30,50)
        k.setpos(-700+i*150,-150)
        k.down()
        draw_sunflower(k,rsize,1)
        k.rt(80)
    for i in range(10):
        k.up()
        rsize =random.randint(60,70)
        k.setpos(-750+i*200,-210)
        k.down()
        draw_sunflower(k,rsize,1)
        k.rt(80)
    for i in range(5):
        k.up()
        rsize =random.randint(65,100)
        k.setpos(-800+i*200,-300)
        k.down()
        draw_sunflower(k,rsize,1)
        k.rt(80)
