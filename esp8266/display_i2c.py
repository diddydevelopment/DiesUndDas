from machine import Pin,I2C
import ssd1306

SCK_PIN = 2
SDA_PIN = 14

i2c = I2C(scl=Pin(SCK_PIN),sda=Pin(SDA_PIN))
i2c.scan()
lcd = ssd1306.SSD1306_I2C(128,64,i2c)
lcd.text("Geil",0,0)
lcd.text("alter",16,8)
lcd.text(":D",32,16)
lcd.show()

lcd.fill(0)
lcd.show()
