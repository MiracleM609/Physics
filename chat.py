import pygame
import math

# initialize the pygame
pygame.init()
# define width of screen
width = 1000
# define height of screen
height = 600
screen_res = (width, height)

pygame.display.set_caption("GFG Elliptical orbit")
screen = pygame.display.set_mode(screen_res)

# define colors in RGB format
# These colors will be used in our game
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)

# centers of screen
X_center = width//2
Y_center = height//2

# radius of ellipse
# X_ellipse is major radius of ellipsis
X_ellipse = 400
# Y_ellipse is minor radius of ellipsis
Y_ellipse = 225

# pygame.time.Clock() will be used further
# in the game loop to control
# the speed of the planet.
clock = pygame.time.Clock()
while True:
    for degree in range(0, 360, 1):
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # fill black color on screen
        screen.fill([0, 0, 0])

        # We will find coordinates of 2 planet
        # that will rotate in same ellipse
        # calculate coordinates of planet 1
        # x_planet is x coordinate
        x_planet_1 = int(math.cos(degree * 2 * math.pi/360)
                         * X_ellipse) + X_center
        # y_planet is y coordinate
        y_planet_1 = int(math.sin(degree * 2 * math.pi/360)
                         * Y_ellipse) + Y_center

        # calculate coordinates of planet 2
        # As we want our planets to be opposite to
        # each other so we will maintain a difference
        # of 180 degrees between then
        degree_2 = degree+180
        # degree will be always between 0 and 360
        if degree > 180:
            degree_2 = degree-180

        # x_planet is x coordinate
        x_planet_2 = int(math.cos(degree_2 * 2 * math.pi/360)
                         * X_ellipse) + X_center
        # y_planet is y coordinate
        y_planet_2 = int(math.sin(degree_2 * 2 * math.pi/360)
                         * Y_ellipse) + Y_center

        # draw circle in center of screen
        pygame.draw.circle(surface=screen, color=red, center=[
                           X_center, Y_center], radius=60)

        # draw ellipse
        # Coordinate of left topmost point is (100,75)
        # width of ellipse = 2*(major radius of ellipse)
        # height of ellipse = 2*(minor radius of ellipse)
        pygame.draw.ellipse(surface=screen, color=green,
                            rect=[100, 75, 800, 450], width=1)

        # draw both planets
        # x_planet_1, y_planet_1, x_planet_2
        # and y_planet_2 are calculated above
        pygame.draw.circle(surface=screen, color=blue, center=[
                           x_planet_1, y_planet_1], radius=40)
        pygame.draw.circle(surface=screen, color=cyan, center=[
                           x_planet_2, y_planet_2], radius=40)

        # Frame Per Second /Refresh Rate
        clock.tick(60)
        # update screen
        pygame.display.flip()