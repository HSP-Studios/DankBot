import pyautogui as pygui
import pygetwindow as gw
import time
import re
import pyperclip  # For clipboard access

commands = [
    "pls beg",
    "pls dig",
    "pls hunt",
    "pls highlow",
    "pls postmemes",
    "pls dep all",
]

def main():
    # Find the Discord window and activate it
    discord_window = None
    for window in gw.getAllTitles():
        if "Discord" in window:
            discord_window = gw.getWindowsWithTitle(window)[0]
            break

    if discord_window:
        print("Focusing on the Discord app...")
        discord_window.activate()
        time.sleep(1)  # Allow time for the window to focus
        pygui.moveTo(discord_window.left + discord_window.width // 2, 
                     discord_window.top + discord_window.height // 2)
    else:
        print("Discord window not found. Please open Discord and try again.")
        return

    # Repeat the command list indefinitely
    while True:
        for command in commands:
            # Ensure the Discord app is in focus
            if not discord_window.isActive:
                print("Discord app is not in focus. Refocusing...")
                discord_window.activate()
                time.sleep(1)  # Allow time for the window to focus
                pygui.moveTo(discord_window.left + discord_window.width // 2, 
                             discord_window.top + discord_window.height // 2)
            
            print(f"Typing command: {command}")
            pygui.typewrite(command)
            print("Sending command...")
            pygui.press("enter")
            time.sleep(2)  # 2-second delay between commands

            # Check if the specific coordinate has the color #e1a91f
            pixel_color = pygui.pixel(1157, 703)
            waited_35_seconds = False
            if pixel_color == (225, 169, 31):  # RGB equivalent of #e1a91f
                print("Detected color #e1a91f at (1157, 703). Waiting 35 seconds...")
                time.sleep(35)
                waited_35_seconds = True
                # After waiting, send the command again
                print(f"Typing command: {command}")
                pygui.typewrite(command)
                print("Sending command...")
                pygui.press("enter")
                time.sleep(2)  # 2-second delay between commands

            if command == "pls highlow":
                highlow()
            
            if command == "pls postmemes":
                postmemes()

        if not waited_35_seconds:
            print("Waiting 10 seconds before repeating the commands...")
            time.sleep(10) 

def highlow(): # interact with the bot
    print("Waiting for the bot's response...")
    time.sleep(1)  # Wait for the bot's response to appear

    # Triple-click on the most recent message (using full-screen coordinates)
    print("Triple-clicking on the most recent message...")
    pygui.click(x=891, y=777, clicks=3, interval=0.2)  # Triple-click at the specified coordinates
    time.sleep(0.5)  # Allow time for the selection to complete

    # Copy the selected text
    print("Copying selected text...")
    pygui.hotkey("ctrl", "c")  # Perform Ctrl+C to copy the selected text
    time.sleep(1)  # Allow time for the clipboard to update

    # Get the copied text from the clipboard
    text = pyperclip.paste()
    print(f"Copied text: {text}")

    # Extract the hint from the bot's response
    match = re.search(r"Is the secret number higher or lower than (\d+)\?", text, re.IGNORECASE)
    if match:
        hint = int(match.group(1))
        print(f"Hint received: {hint}")

        # Click the appropriate button based on the hint
        if hint > 50:
            print("Clicking 'lower' button...")
            pygui.click(x=563, y=876)  # Replace with actual coordinates of the "lower" button
        else:
            print("Clicking 'higher' button...")
            pygui.click(x=794, y=876)  # Replace with actual coordinates of the "higher" button
    else:
        print("Failed to extract hint from the bot's response. Text might not match the expected format.") # 10-second delay before repeating the commands

def postmemes(): # interect with the bot 
    print("Checking color at position (598, 864) for 'pls postmemes'...")
    pixel_color = pygui.pixel(592, 861)
    red, green, blue = pixel_color

    # Check if the color falls within the specified ranges
    if 0 <= red <= 10 and 120 <= green <= 140 and 50 <= blue <= 60:
        print("Color matched. Clicking at position (598, 864)...")
        pygui.click(x=592, y=861)
    else:
        print("Color did not match. Skipping 'pls postmemes'...")

main()