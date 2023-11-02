import pyautogui
import time
pyautogui.FAILSAFE = False
pyautogui.MINIMUM_SLEEP = 0.0
delayPerSquare = 0.1225
#delayPerSquare = 0.06775


time.sleep(1)

setupActions = [["w", 1], ["a", 2], ["w", 3], ["d", 9]]
actions = [["s", 8], ["a", 0], ["w", 5], ["a", 0], ["s", 5], ["a", 0], ["w", 5], ["a", 0], ["s", 5], ["a", 0], ["w", 5], ["a", 0], ["s", 5], ["a", 0], ["w", 5], ["a", 0], ["s", 5], ["a", 0], ["w", 6], ["d", 8], ["w", 0], ["a", 8], ["w", 0], ["d", 9]]

for action in setupActions:
	pyautogui.press(action[0])
	time.sleep(delayPerSquare*action[1])

timesDone = 0

while True:
	for action in actions:
		pyautogui.press(action[0])
		time.sleep(delayPerSquare*action[1])
	time.sleep(0.05)
	timesDone +=1
	
	if timesDone == 5:
		timesDone = 0
		pyautogui.press(" ")
		
		for action in setupActions:
			pyautogui.press(action[0])
			time.sleep(delayPerSquare*action[1])


 