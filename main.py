import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 1024, 600
WHITE = (255, 255, 255)
BLUE = (0, 121, 245)
GREEN = (0, 255, 0)

BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 32)
FONT_SMALL = pygame.font.Font(None, 18)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3X+1")


# Define X and Y axes
x_axis = pygame.Rect(50, HEIGHT // 2, WIDTH - 100, 2)
y_axis = pygame.Rect(WIDTH // 2, 50, 2, HEIGHT - 100)

# Labels for X and Y axes
x_label = FONT_SMALL.render("X-axis", True, GREEN)
y_label = FONT_SMALL.render("Y-axis", True, GREEN)


data = []

# Tick marks and labels for positive integers on the axes
x_ticks = [(i, i * 50) for i in range(1, (WIDTH - 100) // 50)]
y_ticks = [(i, i * 50) for i in range(1, (HEIGHT - 100) // 50)]

# Text Field Class
class TextField:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = False
        self.color = (200, 200, 200)  # Default color

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = (255, 255, 255) if self.active else (200, 200, 200)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = FONT.render(self.text, True, BLACK)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

# Button Class
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, self.rect)
        text_surface = FONT.render(self.text, True, BLACK)
        surface.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

# Function to perform an action when the button is clicked
def button_action():
    data.clear()
    WIN.fill(BLACK)
    #print("Button clicked with text:", text_field.text)
    text = text_field.text
    while True:
        
        if text.isdigit() and text != "1":  # Check if the input is a positive integer
            num = int(text)
            if num % 2 != 0:
                num = num * 3 + 1
            else:
                num = num // 2  # Use integer division for even numbers
            print("Button clicked with text:", num)
            text = str(num)  # Update the text field with the new value
            data.append((len(data) * 50, num))  # X-coordinates increment by 100 for each data point

        else:
            data.append((len(data) * 50, 1))
            break

    # Calculate scaling factors based on the screen size and the number of data points
    x_scale = (WIDTH - 100) / max(1, len(data) * 50)
    y_scale = (HEIGHT - 100) / max(1, max(data, key=lambda x: x[1])[1])


    # Plot data points and connect them with lines
    for i in range(len(data) - 1):
        x1, y1 = data[i]
        x2, y2 = data[i + 1]
        # Scale and offset the coordinates to fit the screen
        x1_scaled = int(x1 * x_scale) + 50
        y1_scaled = int(HEIGHT - y1 * y_scale) - 50
        x2_scaled = int(x2 * x_scale) + 50
        y2_scaled = int(HEIGHT - y2 * y_scale) - 50

        pygame.draw.circle(WIN, BLUE, (x1_scaled, y1_scaled), 5)

        # Create a label to display the number on the circle
        label = FONT_SMALL.render(str(y1), True, WHITE)
        WIN.blit(label, (x1_scaled - 15, y1_scaled - 25))

        if i < len(data) - 2:  # Check if there is a next data point
            pygame.draw.line(WIN, WHITE, (x1_scaled, y1_scaled), (x2_scaled, y2_scaled), 2)

# Function to perform an action when the button is clicked
def button_action2():
    data.clear()
    text_field.text = ""
    WIN.fill(BLACK)


# Create text field and button
text_field = TextField(850, 50, 150, 30)
button = Button(850, 100, 150, 40, "DO MATH", button_action)
button2 = Button(850, 150, 150, 40, "CLEAR", button_action2)

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            text_field.handle_event(event)
            button.handle_event(event)
            button2.handle_event(event)

        text_field.draw(WIN)
        button.draw(WIN)
        button2.draw(WIN)

        # Display axis labels
        WIN.blit(x_label, (WIDTH - 80, HEIGHT - 30))
        WIN.blit(y_label, (20, 20))

        # Draw X and Y axes
        pygame.draw.line(WIN, WHITE, (50, HEIGHT - 50), (WIDTH - 50, HEIGHT - 50), 2)
        pygame.draw.line(WIN, WHITE, (50, 50), (50, HEIGHT - 50), 2)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
main()