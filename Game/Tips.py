'''Things to Note'''

# https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip
''' DISPLAY update vs flip'''
''pygame.display.update''
    # only updates certain portions of the whole screen
    # updates the entire display if no arguments given
    # generally faster
    # pass .blit() and build in drawing functions here
''pygame.display.flip''
    # update the contents of the entire display

'''pg.key.get_pressed() vs pg.KEYDOWN'''
#KEYDOWN
   # long as it's held down, like movement, continues
#key.get_pressed()
    #Whenever pressed, like space, shoots
    #not ideal for movement (choppy) and constantly press