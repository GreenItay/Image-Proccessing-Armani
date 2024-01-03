# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# draw_line.py

import random
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cv2
import numpy as np


def line(image_path, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    colors = ["red", "green", "blue", "yellow",
              "purple", "orange"]

    for i in range(0, 100, 20):
        draw.line((i, 0) + image.size, width=5,
                  fill=random.choice(colors))

    image.save(output_path)


def create_moving_dot(image_path, save_path):
    # Function to update the frame for animation
    # Load your image
    image_path = image_path
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    # Initial dot position
    dot_position = (50, 50)

    # Set up Matplotlib figure and axis
    fig, ax = plt.subplots()
    plt.axis("off")
    frame_counter = 1
    def update(frame):
        nonlocal dot_position, frame_counter
        img = cv2.imread(image_path)

        # Update dot position (you can modify this to move the dot in a different way)
        random_angle = random.uniform(0, 360) * (2*np.pi / 180)
        dot_position = (dot_position[0] + 2, dot_position[1])

        # Draw a white dot on the image
        cv2.circle(img, dot_position, 1, (0, 0, 0), -1)

        # Display the image using matplotlib
        ax.clear()
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_xticks([])
        ax.set_yticks([])

        if frame_counter % 50 == 0:
            cv2.imwrite(f"frame_{frame_counter // 2:03d}.jpg", img)

        frame_counter += 1

    # Create an animation
    animation = FuncAnimation(fig, update, frames=range(200), interval=50, repeat=False)

    # Show the animation
    plt.show()


if __name__ == "__main__":
    line("wall_picture.jpg", "lines.jpg")
    image = Image.open('lines.jpg')
    #image.show()
    create_moving_dot("wall_picture.jpg", '')


