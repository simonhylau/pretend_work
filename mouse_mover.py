from pynput.mouse import Listener, Controller
import pyautogui
import time
from datetime import datetime

mouse_idle_sec = 20
mouse_move_duration = 1
mouse_move_waiting_sec = 20
working_hour = "09:00-12:00;13:30-6:00" 

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Calculate the positions
left_position = int(screen_width * 0.1)
right_position = int(screen_width * 0.9)
target_y = int(screen_height / 2)   # Center of the screen
move_left = True

def on_move(x, y):
    global last_move_time
    last_move_time = time.time()

def check_mouse_movement():
    global last_move_time
    while True:
        current_time = datetime.now().time()
        for time_range in working_hour.split(';'):
            start_time_str, end_time_str = time_range.split('-')
            start_time = datetime.strptime(start_time_str, "%H:%M").time()
            end_time = datetime.strptime(end_time_str, "%H:%M").time()

            if start_time <= current_time <= end_time:
                if time.time() - last_move_time > mouse_idle_sec:
                    move_mouse()
                break  # Exit the loop after finding the current time is within a working hour range
        time.sleep(1)

def move_mouse():
    global move_left
    if(move_left):
        
        # Move mouse to the left position and click
        pyautogui.moveTo(left_position, target_y,mouse_move_duration)
        pyautogui.click()

        # Wait for 20 seconds
        time.sleep(mouse_move_waiting_sec)
        move_left = False
    else:
        # Move mouse to the right position and click
        pyautogui.moveTo(right_position, target_y,mouse_move_duration)
        pyautogui.click()

        # Wait for 20 seconds
        time.sleep(mouse_move_waiting_sec)
        move_left = True

last_move_time = time.time()

mouse_listener = Listener(on_move=on_move)
mouse_listener.start()

check_mouse_movement()