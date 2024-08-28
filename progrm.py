import pygame
from pygame.locals import *
import sys
import time

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CAR_TOLL = 50
BUS_TOLL = 100
TRUCK_TOLL = 150

# Vehicle constants
CAR_WIDTH = 60
CAR_HEIGHT = 40
BUS_WIDTH = 100
BUS_HEIGHT = 50
TRUCK_WIDTH = 120
TRUCK_HEIGHT = 60

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Toll Booth Simulator')

# Clock for controlling the traffic light timer
clock = pygame.time.Clock()

# Load background image
background_image = pygame.image.load(r"C:\Users\91916\Desktop\New folder (2)\background.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize variables for tracking
total_vehicles = 0
total_toll_collected = 0
light_color = RED  # Starting with red light
light_timer = 0

pygame.mixer.init()
beep_sound = pygame.mixer.Sound(r"C:\Users\91916\Downloads\collect-ring-15982.mp3") 

# Function to draw the toll booth
def draw_toll_booth():
    pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 4, 100, 200))
    pygame.draw.rect(screen, light_color, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 4, 100, 50))  # Red light
    pygame.draw.rect(screen, YELLOW, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 4 + 75, 100, 50))  # Yellow light
    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 4 + 150, 100, 50))  # Green light

# Function to draw a vehicle
def draw_vehicle(color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))

# Function to simulate vehicle passing through toll booth
def pass_through_booth(vehicle_type):
    global total_vehicles, total_toll_collected

    x = -120
    y = SCREEN_HEIGHT // 2 - 50
    vehicle_width = CAR_WIDTH if vehicle_type == 'CAR' else BUS_WIDTH if vehicle_type == 'BUS' else TRUCK_WIDTH
    vehicle_height = CAR_HEIGHT if vehicle_type == 'CAR' else BUS_HEIGHT if vehicle_type == 'BUS' else TRUCK_HEIGHT
    vehicle_color = BLUE if vehicle_type == 'CAR' else GREEN if vehicle_type == 'BUS' else RED

    while x < SCREEN_WIDTH + vehicle_width:
        screen.blit(background_image, (0, 0))
        draw_toll_booth()
        draw_vehicle(vehicle_color, x, y, vehicle_width, vehicle_height)
        pygame.display.flip()
        pygame.time.delay(30)  # Adjust speed of vehicle
        
        x += 5  # Move vehicle to the right

    toll_collected = CAR_TOLL if vehicle_type == 'CAR' else BUS_TOLL if vehicle_type == 'BUS' else TRUCK_TOLL
    total_vehicles += 1
    total_toll_collected += toll_collected
    font = pygame.font.Font(None, 36)
    text = font.render(f"Toll collected Rs.{toll_collected}", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()
    time.sleep(2)  # Display toll collected for 2 seconds

    beep_sound.play()

# Function to update traffic light
def update_traffic_light():
    global light_color, light_timer

    light_timer += clock.get_time()  # Increase timer by the time since last tick
    if light_timer >= 5000:  # Change light every 5 seconds
        if light_color == RED:
            light_color = GREEN
        elif light_color == GREEN:
            light_color = YELLOW
        elif light_color == YELLOW:
            light_color = RED
        light_timer = 0  # Reset timer

# Main function to run the toll booth simulation
def main():
    running = True
    while running:
        screen.blit(background_image, (0, 0))
        draw_toll_booth()
        update_traffic_light()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and light_color == GREEN:
                    pass_through_booth('CAR')
                elif event.key == pygame.K_b and light_color == GREEN:
                    pass_through_booth('BUS')
                elif event.key == pygame.K_t and light_color == GREEN:
                    pass_through_booth('TRUCK')
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # Display total count and toll collected
        font = pygame.font.Font(None, 36)
        text = font.render(f"Total vehicles: {total_vehicles}, Total toll: Rs.{total_toll_collected}", True, WHITE)
        screen.blit(text, (10, 10))
        pygame.display.flip()
        clock.tick(30)  # Limit the loop to 30 frames per second

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
