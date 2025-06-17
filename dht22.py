import time
import Adafruit_DHT
from colorama import init, Fore, Style

# Initialize colorama
init()

SENSOR = Adafruit_DHT.AM2302  # or Adafruit_DHT.DHT22
SENSOR_PIN = 12  # BCM pin number (GPIO12)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, SENSOR_PIN)

    if humidity is not None and temperature is not None:
        print(f"{Fore.CYAN}Temperature: {Fore.YELLOW}{round(temperature, 2)} °C{Style.RESET_ALL}\t{Fore.GREEN}Humidity: {Fore.YELLOW}{round(humidity, 2)} %{Style.RESET_ALL}", end='\r')
    else:
        print(f"{Fore.RED}Sensor read failed. Retrying...{Style.RESET_ALL}", end='\r')

    time.sleep(1)
