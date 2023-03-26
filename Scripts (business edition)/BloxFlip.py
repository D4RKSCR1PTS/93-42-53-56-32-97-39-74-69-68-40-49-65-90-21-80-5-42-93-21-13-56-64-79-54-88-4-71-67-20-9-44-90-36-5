import subprocess, time, os, sys
try:
  with open("Logs/BloxFlipRequirements.txt", "r+") as rb:
    rb.read()
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui', 'opencv-python', 'termcolor', 'cloudscraper'])
  haverequirements = open("Logs/BloxFlipRequirements.txt", "w+")
  haverequirements.close()
try:
  os.system('cls')
except:
  os.system('clear')
import pyautogui, cloudscraper; from termcolor import cprint
os.system(f'title BloxRain ^')
cprint("[CREDITS:] AutoRain made by Thwartedbrute#8188","cyan")
cprint("AutoRain Enabled! Press Ctrl + C to exit. Timestamp: " + time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time()))) + "\n","magenta")
while True:
  try:
    check = cloudscraper.create_scraper().get('http://rest-bf.blox.land/chat/history').json()['rain']
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
        waiting = ((check['duration']/(1000*60))%60*60+10)
        cprint(f"Successfully joined rain!","green")
        cprint(f"Rain amount: {prize} R$", "cyan")
        cprint(f"Expiration: {duration} minutes","red")
        cprint(f"Host: {host}","yellow")
        cprint(f"Timestamp: {sent}","magenta")
        f= open("Logs/RainLogs(BloxFlip).txt","a+")
        f.write(f"Successfully joined rain!\nRain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\nTimestamp: {sent}\n")
        f.close()
        time.sleep(waiting)
      if not join:
        pyautogui.hotkey('ctrl','r')
        time.sleep(10)
    elif check['active'] == False:
      time.sleep(1)
  except:
    time.sleep(1)