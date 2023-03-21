import subprocess, time, os, sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui', 'opencv-python', 'termcolor', 'cloudscraper'])
try:
  os.system('cls')
except:
  os.system('clear')
import pyautogui, cloudscraper; from termcolor import cprint
os.system(f'title BloxRain ^')
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
      r = cloudscraper.create_scraper().get('https://rest-bf.blox.land/chat/history').json()
      check = r['rain']
      if check['active'] == True:
        join = pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9)
        sent = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time())))
        if join:
          time.sleep(2)
          pyautogui.moveTo(join)
          time.sleep(0.5)
          pyautogui.click()
          time.sleep(2)
          pyautogui.moveTo(700, 700, 5)
          grabprize = str(check['prize'])[:-2]
          prize = (format(int(grabprize),","))
          host = check['host']
          duration = int(check['duration']/(1000*60))%60
          cprint(f"Successfully joined rain!","green")
          cprint(f"Rain amount: {prize} R$", "cyan")
          cprint(f"Expiration: {duration} minutes","red")
          cprint(f"Host: {host}","yellow")
          cprint(f"Timestamp: {sent}","magenta")
          f= open("Logs/RainLogs(BloxFlip).txt","a+")
          f.write(f"Successfully joined rain!\nRain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\nTimestamp: {sent}\n")
          f.close()
          wager = 0
        if not join:
          pyautogui.hotkey('ctrl','r')
          time.sleep(10)
          join = pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9)
          pyautogui.moveTo(join)
        waiting = ((check['duration']/(1000*60))%60*60+10)
        time.sleep(waiting)
      elif check['active'] == False:
        time.sleep(5)
    except:
      time.sleep(5)
except:
  cprint('An error has occured, please try again.',"red")
  time.sleep(5)
  cprint("Exiting...","yellow")
  time.sleep(0.3)
  quit()