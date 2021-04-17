flower_radius = 400
def setup():
    # runs once when the programs
    size(600, 600)
    background(0, 0, 0, 255) #RGBA, A refers to alpha, 255 refers to red
def draw():
    
    global flower_radius
    
    noFill()
    stroke(frameCount,frameCount,220,25)
    
    beginShape()
    for a in range (360):
        
        noise_factor = noise(a*0.04, frameCount * 0.01)
                             
        x = 300+flower_radius * cos(radians(a)) * noise_factor
        y = 300+flower_radius * sin(radians(a)) * noise_factor
        
        curveVertex(x,y)
        
    endShape(CLOSE)
    
    flower_radius = flower_radius -1
    
    if flower_radius <0:
        noLoop()
    
