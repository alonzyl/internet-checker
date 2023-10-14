from db import createSession, MyTable
import datetime
import time
import requests
import speedtest

def check_internet_connection():
    try:
        response = requests.get('https://www.google.com', timeout=5)
        return True
    except Exception as e:
        print(f"Error occurred while checking internet connection: {e}")
        return False


def check_internet_speed():
    print('starting speed test', flush=True)
    speed_test = speedtest.Speedtest(secure=True,timeout=5)

    downloadSpeedBytes = speed_test.download()
    MB = 1024 * 1024 # One MB is 1024 KB
    downloadSpeedMb = int(downloadSpeedBytes/MB)

    print("Your Download speed is", downloadSpeedMb) 
    return downloadSpeedMb

def main():
    session = createSession()
    last_speed_check_time = time.time()  # Initialize the last check time

    while True:
        download = None
        is_connected = check_internet_connection()

        if is_connected:
            current_time = time.time()
            if current_time - last_speed_check_time >= 1800:  # Check if half an hour has passed
                try:
                    download = check_internet_speed()
                    last_speed_check_time = current_time  # Update the last check time
                except Exception as e:
                    print(f"Error occurred while checking internet speed: {e}")
        else:
            print('Internet is not connected!', flush=True)


        new_record = MyTable(date=datetime.datetime.now(), isConnected=is_connected,downloadSpeed = download)
        session.add(new_record)
        session.commit()
        time.sleep(5)

if __name__ == '__main__':
    main()

