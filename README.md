# techbros-raspi-dht22

## Setup
```bash
# Install Python virtual environment
sudo apt-get update
sudo apt-get install python3-venv

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
sudo apt-get install python3-pip
pip3 install -r requirements.txt
```

## Run
```bash
python3 dht22.py
```
