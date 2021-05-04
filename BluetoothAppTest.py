#please run discovery program when you flash the microcontroller bluetooth program
#onto the microcontrikker. Target MAC address will have changed
import bluetooth
import kivy
import time

"""
First is ssid name
Second is ssid pass
Third is Channel ID
Fourth is Channel Write Key
"""

class Bluetooth():
    def __init__():
        target_address = "FC:F5:C4:01:19:3A"
        target_name = "UpRight Device"

        nearby_devices = bluetooth.discover_devices()

        print("addresses found: \n")
        for bdaddr in nearby_devices:
            if bdaddr.decode('utf-8') == target_address:
                print("found {}".format(target_name))
                break

        if bdaddr.decode('utf-8') == target_address:
            client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            port = 1
            client_sock.connect((target_address, port))
            print("Accepted connection from: {}".format(target_address))

            phrase = ["NETGEAR21","sillyink605", "1070498", "IEMLBJ5IFJ657VZD"]
            for i in range(4):
                print("Sending phrase message: {}\n".format(phrase[i]))
                encoded_message = phrase[i].encode('utf-8')
                client_sock.send(encoded_message)
                time.sleep(2)

            client_sock.close()
        else:
            print("could not find target bluetooth device nearby")


if __name__ == '__main__':
    Bluetooth.__init__()
