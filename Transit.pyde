
###########################
# Created by Eric Davidson
# 7/9/19
###########################
grid_width = 20
grid_height = 20
square_size = 50

w = (grid_width+10) * square_size 
h = (grid_height+10) * square_size

stations = 6
station_size = 10

paths = 200
path_size = 20

#colors = [(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)]
colors = [(213, 180, 147)]
def grid_to_pixel(c):
    return (c[0]*square_size+square_size/2 + square_size*4, c[1]*square_size+square_size/2 + square_size*5)

def distance_by_pixel(g1, g2):
    p1 = grid_to_pixel(g1)
    p2 = grid_to_pixel(g2)
    
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))

def setup():
    # Set up the image
    size(w, h)
    global img
    img = createImage(w, h, ARGB)
    
    r = int(random(255))
    g = int(random(255))   
    b = int(random(255))   
    background(35, 35, 35)
    
    # Color of the line
    stroke(0, 168, 175)
    
    # Thicker
    strokeWeight(path_size)
    fill(255)
    
    grid = []
    for i in range(grid_height):
        grid.append([])
        for j in range(grid_width):
            grid[i].append((i, j))
    
    # Take advantage of retina display
    pixelDensity(2)
    
    station_list = []
    for i in range(stations):
        s = ((int(random(grid_height)), int(random(grid_width))))
        too_close = True
        while(too_close):
            too_close = False
            for st in station_list:
                if distance_by_pixel(s, st) < 300:
                    too_close = True
                    s = ((int(random(grid_height)), int(random(grid_width))))
        station_list.append(s)
        print(s)
 
    for p in range(paths):
        r = int(random(255))
        g = int(random(255))   
        b = int(random(255))  
        stroke(r, g, b, 10)
        start_station = station_list[int(random(stations))]
        end_station = station_list[int(random(stations))]
        while (end_station is start_station):
            end_station = station_list[int(random(stations))]
        current_position = start_station
        noFill()
        # beginShape()
        # c = grid_to_pixel(current_position)
        # curveVertex(c[1], c[0])
        travel_state = "none"
        while(current_position != end_station):
            # Above
            
            previous_position = current_position
            
            x_delta = 0
            y_delta = 0
            if current_position[0] < end_station[0]:
                x_delta = 1
            elif current_position[0] > end_station[0]:
                x_delta = -1
            if current_position[1] < end_station[1]:
                y_delta = 1
            elif current_position[1] > end_station[1]:
                y_delta = -1
                
            if travel_state is "none":
                chance = random(1)
                if chance < .5:
                    travel_state = "vertical"
                else:
                    travel_state = "horizontal"
            
            current_position = (current_position[0] + x_delta, current_position[1] + y_delta)
            
            p = grid_to_pixel(previous_position)
            c = grid_to_pixel(current_position)
            #curveVertex(c[1], c[0])
            line(p[1], p[0], c[1], c[0])
            print("hellow")
    
    fill(r, g, b, 10)
    strokeWeight(path_size)
    for st in station_list:
        stroke(r, g, b, 10)
        c = grid_to_pixel(st)
        print(c)
        circle(c[1], c[0], station_size)
    
    

    # beginShape()
    # curveVertex()
    
    # # Draw the curvy line
    # endShape()
    
    # textAlign(CENTER);
    # textSize(200)
    # letters = ['B', 'H', 'F', 'A', 'T', 'E', 'Z', 'G', 'R', 'O', 'C', 'S']
    seed = int(random(1500))
    # name = str(letters[int(random(len(letters)))]) + str(letters[int(random(len(letters)))]) + '-' + str(seed)
    # text(name, w/2, h-(square_size*8))
    
    # Save the image with line count and 'seed'
    save("Examples/" + str(seed) + ".png")
    
#     # Only need to draw once
#     noLoop()
    
# def draw():
#     image(img, 0, 0)
    
    
    
