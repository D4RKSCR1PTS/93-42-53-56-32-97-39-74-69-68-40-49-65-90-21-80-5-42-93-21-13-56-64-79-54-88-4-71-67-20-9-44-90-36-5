import subprocess, time, os, sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui', 'opencv-python', 'termcolor'])
try:
  os.system('cls')
except:
  os.system('clear')
import pyautogui; from termcolor import cprint
os.system(f'title RBLXRain ^')
cprint("[CREDITS:] AutoRain made by Thwartedbrute#8188","cyan")
time.sleep(1)
try:
  os.system('cls')
except:
  os.system('clear')
starttime = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time())))
try:
  cprint(f"AutoRain Enabled! Press Ctrl + C to exit. Timestamp: {starttime}\n","magenta")
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
    except Exception:
      time.sleep(1)
except:
  cprint('An error has occured, please try again.',"red")
  time.sleep(5)
  cprint("Exiting...","yellow")
  time.sleep(0.3)
  quit()