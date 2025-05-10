import pyautogui
import time
import winsound

print("Move your mouse to the desired position. You have 5 seconds... uwu")
winsound.Beep(500, 500)  
time.sleep(1)  # Wait for 5 seconds
winsound.Beep(2000, 100)  
time.sleep(1)  # Wait for 5 seconds
winsound.Beep(2000, 100)  
time.sleep(1)  # Wait for 5 seconds
winsound.Beep(2000, 100)  
time.sleep(1)  # Wait for 5 seconds
winsound.Beep(2000, 100)  
time.sleep(1)  # Wait for 5 seconds
position = pyautogui.position()  # Get the current mouse position
print(f"Mouse position: {position}")
# Play a generic beep sound
winsound.Beep(1000, 500) 