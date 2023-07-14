import pygame  
import random 
pygame.init()  
white = (255, 255, 255)  # screen color 
height = 400  # y
width = 400  # x
  
display_surface = pygame.display.set_mode((height, width))  
  
ran_v_1 =random.randrange(300) # random position at the first 
ran_v_2 =random.randrange(300)  # random position at the first 

pygame.display.set_caption('PRESS UP_KEY')  # title
image = pygame.image.load(r'pp.png') # load the $0.0000000000000000001 image

while True:  
    display_surface.fill(white)  #fill screen
    display_surface.blit(image, (ran_v_1, ran_v_2)) #postion the imge
    def pygame_press():
            ran_v_1 =random.randrange(300) #  random position after the K_UP is preesed (x-axis) 
            ran_v_2 =random.randrange(300) # random position after the K_UP is preesed (y-axis)
            display_surface.blit(image, (ran_v_1, ran_v_2)) # currently the image disapper as the ram of the computer runs out
        
    pressed = pygame.key.get_pressed() # listen the keyboard
    if pressed[pygame.K_UP]:pygame_press() # check if the key is preesed up
    for event in pygame.event.get():  # goes to events
        if event.type == pygame.QUIT:  # is events is close (when clossing the window) 
            pygame.quit()  # then close         
            quit()  # kill

        pygame.display.update() #update for the loop

# iknow that this code is $HIt.
# the performance is garbage
# but a noob game