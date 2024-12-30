import time
import sys

text = "Merry Christmas"
delay = 0.5  # seconds

for letter in text:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(delay)

print()  # Move to the next line after the animation
