from apscheduler.schedulers.blocking import BlockingScheduler
from rpi_temperature_logger import DHTDevice
import time
from edge_logger import SensorLog

sched = BlockingScheduler()


device = DHTDevice()


def main():
    temp = None
    humid = None

    while True:
        temp, humid = device.read()

        if(temp is not None and humid is not None):
            break

        time.sleep(1)

    # Log.
    data = {
        'temp': temp,
        'humid': humid
    }
    SensorLog().insert(data)


# if __name__ == '__main__':
#     main()


@sched.scheduled_job('cron', second=0)
def scheduled_job():
    main()


sched.start()
