from pyautogui import *
from random import random

msg = 'Zapraszamy do Gildii Azkaban! Wszelkie kontenty PvE i PvP, grupka zbieracka z benefitami, program pomocy nowicjuszom. Zajrzyj na naszego discorda: nN4Tsdkz'

sleep(10)

while True:
	press('enter')
	write(msg, 0)

	sleep(5)
	press('enter')

	sleep(random() * 100 + 20)

	press('i', 2, 0.5)
