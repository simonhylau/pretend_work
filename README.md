# README

## MOUSE MOVER

### Overview
The Mouse Mover program is designed to automatically move the mouse cursor during specified working hours to keep the computer from going into sleep mode or showing the user as inactive. This script is particularly useful for users who need to keep their computer active while doing tasks that do not require constant interaction, such as reading documents or attending online meetings.

### Features
- **Automatic Mouse Movement**: Moves the mouse cursor automatically when the system is idle for a specified duration.
- **Working Hours Configuration**: Allows users to define working hours during which the mouse movement should occur.
- **Customizable Idle Time**: Users can set the duration of inactivity before the mouse is moved.

### Prerequisites
Before running the Mouse Mover script, ensure you have Python installed on your system. This script has been tested with Python 3.8 and above.

### Dependencies
The script relies on the [`pyautogui`] library for controlling the mouse and [`datetime`] for managing time-related functions.

To install the required dependencies, run the following command in your terminal:
```bash
pip install -r requirements.txt
```

### Configuration
Before running the script, you may need to adjust several variables within the mouse_mover.py file to suit your needs:

- ```working_hour```: The hours during which the mouse should move, formatted as ```start_time-end_time``` and separated by semicolons for multiple intervals (e.g., ```09:00-12:00;13:00-17:00```).
- ```mouse_idle_sec```: The number of seconds the system should be idle before the mouse moves.
- ```left_position```, ```target_y```: The screen coordinates to which the mouse will move.
- ```mouse_move_duration```, ```mouse_move_waiting_sec```: How quickly the mouse moves and how long it waits afterward.

### Running the Script
To run the Mouse Mover script, open a terminal or command prompt, navigate to the directory containing the script, and execute:
```bash
python mouse_mover.py
```
### Stopping the Script
To stop the Mouse Mover script, simply interrupt its execution by pressing Ctrl+C in the terminal or command prompt where it's running.

## License
This script is provided "as is", without warranty of any kind. You are free to modify and distribute it as needed.
