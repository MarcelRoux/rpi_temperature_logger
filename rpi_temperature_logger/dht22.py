import board
import adafruit_dht


class DHTDevice:

    def __init__(self, pin=board.D4):
        self.device = adafruit_dht.DHT22(pin)

    def read(self):
        '''
        Fetches readings from DHT device.
        '''
        temp = None
        humid = None
        try:
            temp = self.device.temperature
            humid = self.device.humidity

        except RuntimeError as error:
            print(error)
            pass

        except Exception as error:
            self.device.exit()
            raise error

        return temp, humid
