from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
import serial.tools.list_ports
import time

def my_data_received_callback(xbee_message):
    address = xbee_message.remote_device.get_64bit_addr()
    data = xbee_message.data.decode("utf8")
    print(xbee_message)
    print("Received data from %s: %s" % (address, data))


port_list = serial.tools.list_ports.comports()
for port in port_list:
  print(port)

device = XBeeDevice("/dev/ttyUSB0", 9600)
device.open()
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A200403E2518"))
#device.send_data(remote_device,"test") #bytes([0x13, 0x02, 0x04]))

device.add_data_received_callback(my_data_received_callback)
