import streamlit as st
import pygame
import os

# Initialize pygame for sound playback
pygame.mixer.init()

# Define Animal Class
class Animal:
    def __init__(self, name, image_path, sound_path):
        self.name = name
        self.image_path = image_path
        self.sound_path = sound_path

    def get_image(self):
        return self.image_path

    def play_sound(self):
        if os.path.exists(self.sound_path):
            pygame.mixer.music.load(self.sound_path)
            pygame.mixer.music.play()
        else:
            st.error(f"Sound file not found: {self.sound_path}")

# Create Animal Objects
animals = {
    "Dog": Animal("Dog", "images/dog.jpg", "sounds/dog.mp3"),
    "Cat": Animal("Cat", "images/cat.jpg", "sounds/cat.mp3"),
    "Cow": Animal("Cow", "images/cow.jpg", "sounds/cow.mp3"),
    "Duck": Animal("Duck", "images/duck.jpg", "sounds/duck.mp3"),
    "Lion": Animal("Lion", "images/lion.jpg", "sounds/lion.mp3"),
    "Elephant": Animal("Elephant", "images/elephant.jpg", "sounds/elephant.mp3"),
    "Horse": Animal("Horse", "images/horse.jpg", "sounds/horse.mp3"),
    "Sheep": Animal("Sheep", "images/sheep.jpg", "sounds/sheep.mp3"),
    "Monkey": Animal("Monkey", "images/monkey.jpg", "sounds/monkey.mp3"),
    "Frog": Animal("Frog", "images/frog.jpg", "sounds/frog.mp3"),
}

# Streamlit UI
st.title("🐾 Animal Sound Simulator")
st.write("Click on an animal to hear its sound!")

# Display animals in a grid
cols = st.columns(3)

for idx, (animal_name, animal) in enumerate(animals.items()):
    with cols[idx % 3]:  # Arrange in 3 columns
        st.image(animal.get_image(), caption=animal.name, use_column_width=True)
        if st.button(f"🔊 Play {animal.name} Sound", key=animal_name):
            animal.play_sound()
