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
        with open("reading.txt", "a") as file:
            file.write(f"\ntemperature:._.{temperature}℃")
            file.write(f"\nhumidity:._.{humidity}%")

        output = (
            f"{Fore.CYAN}Temperature: {Fore.YELLOW}{round(temperature, 4)} °C{Style.RESET_ALL}\t"
            f"{Fore.GREEN}Humidity: {Fore.YELLOW}{round(humidity, 4)} %{Style.RESET_ALL}"
        )
        print(f"\r{output}{' ' * 20}", end="")  # Pad with spaces to clear line

    except RuntimeError as e:
        msg = f"{Fore.RED}Sensor read failed: {e}. Retrying...{Style.RESET_ALL}"
        print(f"\r{msg}{' ' * 20}", end="")  # Pad with spaces to clear line
    except Exception as e:
        msg = f"{Fore.RED}Unexpected error: {e}. Retrying...{Style.RESET_ALL}"
        print(f"\r{msg}{' ' * 20}", end="")  # Pad with spaces to clear line
        time.sleep(2.0)

    time.sleep(1.0)  # Wait for 1 second before the next read
