import subprocess, time, os, sys
try:
  with open("Logs/RBLXWildRequirements.txt", "r+") as rb:
    rb.read()
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui', 'opencv-python', 'termcolor'])
  haverequirements = open("Logs/RBLXWildRequirements.txt", "w+")
  haverequirements.close()
try:
  os.system('cls')
except:
  os.system('clear')
import pyautogui; from termcolor import cprint
os.system(f'title RBLXRain ^')
cprint("[CREDITS:] AutoRain made by Thwartedbrute#8188","cyan")
cprint("AutoRain Enabled! Press Ctrl + C to exit. Timestamp: " + time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time()))) + "\n","magenta")
while True:
  try:
    join = pyautogui.locateCenterOnScreen('Images/RBLXWild.png', confidence = 0.9)
    sent = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time())))
    if join:
      time.sleep(2)
      pyautogui.moveTo(join)
      time.sleep(0.5)
      pyautogui.click()
      time.sleep(2)
      pyautogui.moveTo(700, 700, 5)
      cprint(f"Successfully joined rain!","green")
      cprint(f"Timestamp: {sent}\n","yellow")
      f= open("Logs/RainLogs(RBLXWild).txt","a+")
      f.write(f"Successfully joined rain!\nTimestamp: {sent}\n")
      f.close()
      wager = 0
    if not join:
      wager += 1 
      time.sleep(1)
      if wager == 60:
        wager = 0
        pyautogui.hotkey('ctrl','r') 
  except:
    time.sleep(1)