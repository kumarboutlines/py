# import pyautogui
# import requests

# pyautogui.sleep(3)

# def pc_sr_fun():
#     pyautogui.moveTo(293, 17, 1)
#     pyautogui.sleep(2)
#     pyautogui.click()
#     pyautogui.moveTo(254, 19, 1)
#     pyautogui.sleep(2)
#     pyautogui.click()
#     pyautogui.moveTo(624, 495, 1,pyautogui.easeInOutBounce)
#     pyautogui.sleep(2)
#     pyautogui.click()

#     res = requests.get('https://api.quotable.io/quotes/random?minLength=15&maxLength=25')
#     resp = res.json()
#     sr_str_pc = resp[0]['content']

#     pyautogui.sleep(3)
#     pyautogui.write(sr_str_pc,0.25)
#     pyautogui.sleep(5)
#     pyautogui.press('enter')
#     pyautogui.sleep(2)
#     pyautogui.moveTo(523, 132, 1)
#     pyautogui.click()
#     pyautogui.sleep(4)
#     for i in range(15):
#         pyautogui.press('backspace')
#         pyautogui.sleep(2)
#         pyautogui.press('enter')
#         pyautogui.sleep(2)
#         pyautogui.click()
#         pyautogui.sleep(3)    

# def open_cr_pc(x,y):
#     pyautogui.moveTo(36, 293, 5, pyautogui.easeInOutBounce) #select chrome
#     pyautogui.sleep(1)
#     pyautogui.doubleClick()
#     pyautogui.sleep(2)
#     pyautogui.moveTo(x, y, 2, pyautogui.easeInOutBounce) #open chrome
#     pyautogui.sleep(2)
#     pyautogui.click()
#     pyautogui.sleep(2)
#     pc_sr_fun()
#     pyautogui.sleep(1)
#     pyautogui.moveTo(1340, 16, 2)
#     pyautogui.sleep(2)
#     pyautogui.click()
# open_cr_pc(411,317)
# pyautogui.sleep(5)

# open_cr_pc(595,317)
# pyautogui.sleep(5)
# open_cr_pc(772,318)
# pyautogui.sleep(5)
# open_cr_pc(947,315)
# pyautogui.sleep(5)
# open_cr_pc(414,506)
# pyautogui.sleep(5)
# open_cr_pc(594,507)
# pyautogui.sleep(5)
# open_cr_pc(769,508)
# pyautogui.sleep(5)
# open_cr_pc(949,509)

import pyautogui

print(pyautogui.position())