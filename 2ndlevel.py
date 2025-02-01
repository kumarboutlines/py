import pyautogui
import json


pyautogui.FAILSAFE = False

pyautogui.sleep(2)
                
sr_str_pc_list = []
sr_str_mob_list = []

with open('list_pc.json', 'r') as file:
    pc_list = json.load(file)
sr_str_pc_list = pc_list

with open('list_mob.json', 'r') as file:
    pc_mob = json.load(file)
sr_str_mob_list = pc_mob

def pc_sr_fun(b,e):
    pyautogui.moveTo(293, 17, 1)
    pyautogui.sleep(3)
    pyautogui.click()
    pyautogui.moveTo(254, 19, 1)
    pyautogui.sleep(3)
    pyautogui.click()
    pyautogui.moveTo(624, 495, 1,pyautogui.easeInOutBounce)
    pyautogui.sleep(3)
    pyautogui.click()
    pyautogui.sleep(2)
    pyautogui.write(sr_str_pc_list[e],0.25)
    pyautogui.sleep(5) 
    print('pc b',b)
    for i in range(b*5):
        pyautogui.sleep(1) 
        pyautogui.press('backspace')
    pyautogui.sleep(5)
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.moveTo(680, 132, 1)
    pyautogui.click()
    pyautogui.sleep(2)
    for i in range(5):
        pyautogui.press('backspace')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.sleep(3)

def mob_sr_fun(b,e):
    pyautogui.moveTo(293, 17, 1)
    pyautogui.sleep(3)
    pyautogui.click()
    pyautogui.moveTo(254, 19, 1)
    pyautogui.sleep(3)
    pyautogui.click()
    pyautogui.sleep(3)
    pyautogui.press('F12')
    pyautogui.sleep(2)
    pyautogui.moveTo(659, 326, 2,pyautogui.easeInOutBounce)
    pyautogui.sleep(2)
    pyautogui.click()
    pyautogui.sleep(5)
    pyautogui.write(sr_str_mob_list[e],0.25)
    pyautogui.sleep(3)
    print('mob b',b)
    for i in range(b*5):
        pyautogui.sleep(1) 
        pyautogui.press('backspace')
    pyautogui.sleep(5)
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.moveTo(766, 212, 2,pyautogui.easeInOutBounce)
    pyautogui.sleep(2)
    pyautogui.click()
    pyautogui.sleep(2)
    for i in range(5):
        pyautogui.press('backspace')
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(4)
        pyautogui.click()
        pyautogui.sleep(2)


def open_cr_pc(x,y,z,e):
    pyautogui.moveTo(36, 293, 5, pyautogui.easeInOutBounce) #select chrome
    pyautogui.sleep(2)
    pyautogui.doubleClick()
    pyautogui.sleep(5)
    pyautogui.moveTo(x, y, 2, pyautogui.easeInOutBounce) #open chrome
    pyautogui.sleep(5)
    pyautogui.click()
    pyautogui.sleep(2)
    pc_sr_fun(z,e)
    print('pc z',z,'pc e',e)
    pyautogui.sleep(1)
    pyautogui.moveTo(1340, 16, 2)
    pyautogui.sleep(2)
    pyautogui.click()

def open_cr_mob(x,y,z,e):
    pyautogui.moveTo(36, 293, 5, pyautogui.easeInOutBounce) #select chrome
    pyautogui.sleep(2)
    pyautogui.doubleClick()
    pyautogui.sleep(5)
    pyautogui.moveTo(x, y, 2, pyautogui.easeInOutBounce) #open chrome
    pyautogui.sleep(5)
    pyautogui.click()
    pyautogui.sleep(2)
    mob_sr_fun(z,e)
    print('mob z',z ,'mob e',e)
    pyautogui.sleep(1)
    pyautogui.moveTo(1340, 16, 2)
    pyautogui.sleep(2)
    pyautogui.click()

pyautogui.sleep(10)

for i in range(8):
    open_cr_pc(414,317,i,0)
    pyautogui.sleep(5)
    open_cr_pc(595,317,i,1)
    pyautogui.sleep(5)
    open_cr_pc(772,318,i,2)
    pyautogui.sleep(5)
    open_cr_pc(947,315,i,3)
    pyautogui.sleep(5)
    open_cr_pc(414,506,i,4)
    pyautogui.sleep(5)
    open_cr_pc(594,507,i,5)
    pyautogui.sleep(5)
    open_cr_pc(769,508,i,6)
    pyautogui.sleep(5)
    open_cr_pc(949,509,i,7)
    pyautogui.sleep(200)

pyautogui.sleep(5)

for i in range(5):
    open_cr_mob(414,317,i,0)
    pyautogui.sleep(5)
    open_cr_mob(595,317,i,1)
    pyautogui.sleep(5)
    open_cr_mob(772,318,i,2)
    pyautogui.sleep(5)
    open_cr_mob(947,315,i,3)
    pyautogui.sleep(5)
    open_cr_mob(414,506,i,4)
    pyautogui.sleep(5)
    open_cr_mob(594,507,i,5)
    pyautogui.sleep(5)
    open_cr_mob(769,508,i,6)
    pyautogui.sleep(5)
    open_cr_mob(949,509,i,7)
    pyautogui.sleep(200)