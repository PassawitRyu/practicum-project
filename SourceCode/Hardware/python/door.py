from practicum import find_mcu_boards, McuBoard ,PeriBoard
from time import sleep
import os

devs = find_mcu_boards()

if len(devs) == 0:
    print("*** No practicum board found.")
    exit(1)

mcu = McuBoard(devs[0])
print("*** Practicum board found")
print("*** Manufacturer: %s" % \
        mcu.handle.getString(mcu.device.iManufacturer, 256))
print("*** Product: %s" % \
        mcu.handle.getString(mcu.device.iProduct, 256))
peri = PeriBoard(mcu)


peri.set_buz(2,0)
while True:
    infa0 = peri.get_infa0()
    infa1 = peri.get_infa1()
    state = 0
    if(infa0):
        for i in range(0,300):
            infa1 = peri.get_infa1()
            if(infa1):
                state = 1
                light3,light4 = peri.get_light()
                if ((light3 < 300) and (light4 < 500)):
                    ldr3 = 1
                    ldr4 = 1
                elif (light3 < 300):
                    ldr3 = 1
                    ldr4 = 0
                    peri.set_buz(2,1)
                elif (light4 < 500):
                    ldr3 = 0
                    ldr4 = 1
                    peri.set_buz(2,1)
                else:
                    ldr3 = 0
                    ldr4 = 0
                    peri.set_buz(2,1)
                tx = open("tmp.txt","w")
                tx.write("%d %d %d"%(state,ldr3,ldr4))
                tx.close()
                os.rename("tmp.txt","now.txt")
                print(state,ldr3,ldr4)
                sleep(2)
                peri.set_buz(2,0)
                break
            sleep(0.01)
    elif(infa1):
        for i in range(0,300):
            infa0 = peri.get_infa0()
            if(infa0):
                state = 2
                light3,light4 = peri.get_light()
                if ((light3 < 300) and (light4 < 500)):
                    ldr3 = 1
                    ldr4 = 1
                    peri.set_buz(2,1)
                elif (light3 < 300):
                    ldr3 = 1
                    ldr4 = 0
                    peri.set_buz(2,1)
                elif (light4 < 500):
                    ldr3 = 0
                    ldr4 = 1
                    peri.set_buz(2,1)
                else:
                    ldr3 = 0
                    ldr4 = 0
                tx = open("tmp.txt","w")
                tx.write("%d %d %d"%(state,ldr3,ldr4))
                tx.close()
                os.rename("tmp.txt","now.txt")
                sleep(2)
                print(state,ldr3,ldr4)
                peri.set_buz(2,0)
                break
            sleep(0.01)
    else:
        tx = open("tmp.txt","w")
        tx.write("0 0 0")
        tx.close()
        os.rename("tmp.txt","now.txt")
       #print("0")
    sleep(0.1)
