from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
import serial.tools.list_ports
import time, json

port_list = serial.tools.list_ports.comports()
for port in port_list:
  print(port)

device = XBeeDevice("/dev/ttyUSB0", 9600)
time_stamps = {}
device.open()
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A200403A8AB5"))
for i in range (100):
    time.sleep(0.1)
    print('sending')
    start = time.time()
    device.send_data(remote_device, bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF3]))
    end = time.time()
    time_stamps[str(start)] = (end - start)

json_samples = json.dumps(time_stamps, sort_keys=True)
with open('sender.json', 'w') as f:
    f.write(json_samples)

#device.send_data(remote_device, "Hello XBee!")
#network = device.get_network()
#network.start_discovery_process()
#while(network.is_discovery_running()):
#    time.sleep(0.5)
#print(network.get_device_by_node_id('ROUTER'))
device.close()
