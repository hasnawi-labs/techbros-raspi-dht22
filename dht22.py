import time
import adafruit_dht
import board
from colorama import init, Fore, Style

# Initialize colorama
init()

dht_device = adafruit_dht.DHT22(board.D17)  # GPIO17 (BCM) -> board.D17

while True:
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity

        print(
            f"{Fore.CYAN}Temperature: {Fore.YELLOW}{round(temperature, 2)} °C{Style.RESET_ALL}\t"
            f"{Fore.GREEN}Humidity: {Fore.YELLOW}{round(humidity, 2)} %{Style.RESET_ALL}",
            end="\r",
        )

    except RuntimeError as e:
        print(
            f"{Fore.RED}Sensor read failed: {e}. Retrying...{Style.RESET_ALL}", end="\r"
        )
    except Exception as e:
        print(
            f"{Fore.RED}Unexpected error: {e}. Retrying...{Style.RESET_ALL}", end="\r"
        )
        time.sleep(2.0)

    time.sleep(1.0)
