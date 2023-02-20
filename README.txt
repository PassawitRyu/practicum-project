ปฏิบัติการเกี่ยวกับวิศวกรรมคอมพิวเตอร์ (01204223)
คณะวิศวกรรมศาสตร์ สาขาคอมพิวเตอร์ มหาวิทยาลัยเกษตรศาสตร์

ชื่อโครงงาน : Forget Me Not

คณะผู้จัดทำ :
1. นายเจตนิพัทธ์   การุญบุญญานันท์    6210503501
2. นายธนพล      โอวาทวรวรัญญู     6210503594
3. นายภาสวิชญ์    สังข์ธูป           6210503764
4. นายจิรัฏฐ์       หวังมั่น           6210503764

รายละเอีดของไฟล์ :
ForgetMeNot
        - Member
                - 6210503501_เจตนิพัทธ์_การุญบุญญานันท์.jpg
                - 6210503594_ธนพล_โอวาทวรวรัญญู.jpg
                - 6210503764_ภาสวิชญ์_สังข์ธูป.jpg
                - 6210505171_จิรัฏฐ์_หวังมั่น.jpg
                - AllMember.jpg (รูปถ่ายสมาชิกทุกคน)
        - ProjectImage
                - Board.jpg (รูปถ่ายของบอร์ด MCU และ บอร์ดไข่ปลาที่บัดกรีวงจรลงไป)
                - MemWithProj.jpg (รูปถ่ายสมาชิกทุกคนกับชิ้นงาน)
                - Model.jpg (รูปถ่าย Model ห้องจำลอง)
                - Output_Line_Notify.jpg (แสดงผลการทำงานผ่าน Line Notify)
        - ProjectSchematic
                - Schematic.png (แผนผังวงจร)
                - Schematic_Draft.jpg (โครงร่างแผนผังวงจรแบบคร่าวๆ)
        - SourceCode
                - Frontend
                        - line_notify.py (รับค่าจากไฟล์ now.txt แล้วส่งข้อมูลที่ต้องการไปยัง url ของไลน์ แล้วส่งเข้าทางหน้าจอแสดงผลของผู้ใช้งาน)
                - HardWare
                        - firmware
                                - usbdrv (Directory ที่อาจารย์ให้มาเพื่อที่จะ import บาง File ไปใช้ต่อ)
                                - main.c (usbPoll() ไว้ตรวจสอบคำร้องขอจากฝั่งโฮสท์ และเรียกใช้ฟังก์ชัน usbFuntionSetup()
	                                      usbFuntionSetup() ไว้ set buzzer อ่านค่า infrared อ่านค่า light จาก ldr)
                                - Makefile 
                                - peri.c (init_peri setค่าเมื่อเริ่มต้นการทำงาน
	                                      set_buz setค่าbuzzerให้ดังหรือดับ
	                                      read_adc อ่านค่าanalog)
                                - peri.h (นิยามชื่อฟังก์ชัน จาก peri.c และนิยาม Infa_see0() Infa_see1() ให้ค่า 1 เมื่อมีของผ่าน infrared)
                                - usbconfig.h (คือ File ตั้งต้นของอาจารย์ ที่ใส่ค่า
	                                           #define USB_CFG_DEVICE_NAME     'I','D',' ','6','2','1','0','5','0','3','5','9','4'
	                                           ซึ่งเป็นรหัสนิสิตของผู้จัดทำโครงงาน)
                        - python
                                - door.py (file หลักที่เราใช้ในการทำงาน และสื่อสารกับบอร์ด mcu โดยจะทำงานตลอดเวลาที่เริ่มต้นกันทำงาน เพื่อบันทึกค่าสถานะต่างๆลงใน file now.txt)
                                - now.txt (รับค่าสถานะของอุปกรณ์ Hardware มาเก็บไว้เพื่อให้ Fronend นำไปใช้)
                                - practicum.py (class และ function ต่างๆที่ใช้ จะมีดังนี้
	                                            __init__   -> set ค่าเริ่ม
	                                            set_buz    -> setค่าbuzzerให้ดังหรือดับ
	                                            get_infa0  -> รับค่าจาก infrared ที่ต่อกับขา PC0
	                                            get_infa1  -> รับค่าจาก infrared ที่ต่อกับขา PC1
	                                            get_light  -> return arrayที่เก็บค่าไว้2ค่าคือ ค่าแสงที่รับมาจากldrที่ค่าPC3 ค่าแสงที่รับมาจากldrที่ค่าPC4)
        - License.txt
        - README.txt

อุปกรณ์ Hardware ที่นำมาใช้งาน :
1. Buzzer ขนาด 5 V 1 ตัว (ต่อกับ PC2)
2. Sensor ตรวจวัดแสง ( LDR ) 2 ตัว (ต่อกับ PC3 , PC4 ใช้เช็คที่วางของหมายเลข 1 , 2)
3. Module sensor ตรวจจับ อินฟาเรด 2 ตัว (ต่อกับ PC0 , PC1 โดย PC0 คือฝั่งใกล้ทางออกประตูห้อง)
4. LED 3 mm 1 ตัว (ต่อกับ VCC)
5. ตัวต้านทานขนาด 330 โอห์ม 1 ตัว (ต่อกับLED)
6. ตัวต้านทานขนาด 10k โอห์ม 1 ตัว (ต่อกับ)
7. Raspberry Pi 3 Model B+ พร้อม สาย Adapter Model YM-0530 1 ชุด
8. Board NodeMCU - ATmega328p (Practicum Board v3.2 CPE. KU 2020-11) 1 ชุด
9. บอร์ดไข่ปลา สำหรับบัดกรีวงจร 1 ตัว
10. สายไฟ
11. Jumper Female - Female
12. connector ขนาด 5*2 ช่อง 1 ตัว
13. connector ขนาด 2 ช่อง 3 ตัว

Library ที่ใช้งาน :
- usb
- time
- requests
- os
- usbdrv.h
- practicum import find_mcu_boards
                   McuBoard
		       
Software :
- Editor in Raspberry Pi
- Line API
