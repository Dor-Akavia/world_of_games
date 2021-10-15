import sys
import time

sys.stdout.write(text)
time.sleep(0.7)
for x in text:
    sys.stdout.write('\b \b')

