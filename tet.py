import smbus
bus = smbus.SMBus(0)
address = 0x6B
data = [0xA5,0x5A]
bus.write_i2c_block_data(address, 0, data)

