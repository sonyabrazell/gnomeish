import pygame

pygame.init()

window = pygame.display.set_mode((1200,800))

pygame.display.set_caption('gnomeish - gnomes doing gnome things')

# icon = pygame.image.load('')
# pygame.display.set_icon(icon)

#gnome
#load image
# gnome = pygame.image.load('')


running = True

while running:
    
    window.fill((255,0,45))
    
    #event loop
    for even in pygame.event.get():
        if even.type == pygame.QUIT():
            running = False
            


pygame.QUIT()