import pygame 

# create a window(the surface that can be drawn on) and give it dimensions by calling .display.set_mode() 
window = pygame.display.set_mode((1000, 800))

# Set color scheme variables using RGB values 
PERIWINKLE = (161, 175, 241)
PINK = (255, 179, 217)
PURPLE = (180, 151, 231)

# set the title of app using .set_caption 
pygame.display.set_caption("Tic Tac Toe")

# create clock variable to limit the speed of every cycle of of running loop
clock = pygame.time.Clock()

# Create a character panel
board_panel = pygame.Rect(50, 50, 900 , 700)
# load board assset png
board = pygame.image.load("assets/board.png")


# RUNTIME LOOP 
running = True; 
# Main while loop to control application during run time 
# while running == true
while running: 
    # loop through each event 
    for event in pygame.event.get():
        # When user clicks the close button on the window. 
        if event.type == pygame.QUIT:
            # then stop running 
            running = False

    # check for a click 
    if event.type == pygame.MOUSEBUTTONDOWN:
        selected_category = handle_customization_event(event, selected_category)
    
    # set clock frame goal to control loop 
    clock.tick(60) 
    # Use the .fill function to set window color
    window.fill(PINK)

    pygame.draw.rect(window, PERIWINKLE, panel)
    pygame.draw.rect(window, PURPLE, character_panel)
    pygame.draw.rect(window, PERIWINKLE, inner_character_panel)

    #
    window.blit(board, (100,60))

    # Update the full display surface to the screen
    pygame.display.flip()