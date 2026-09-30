   import smbus

   class ImuReader:
       """MPU6050 기울기 읽기 (테스트용)"""
       def __init__(self):
           self.bus = smbus.SMBus(1)

       def read(self):
           return self.bus.read_byte_data(0x68, 0x3B)
