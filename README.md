# ISZ-Parser
- Parses Ice station Z Save-Data into The *.json Human Readable & Widely Used Data Format.
- Allows for Hundreads of Programming Languages and Game Engines to Ensure Compatibility with ISZ on The 3DS.
- Basic Functionality Available as of **09/10/2023**.

# Downloads:
- Download C++ Source [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v1/isz-parse.cpp).
- Download Python Source [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v1/isz-parse.py).
- Download Compiled Executable [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v1/isz-parse.exe).

## Usage:
- Drag and drop Decrypted ISZ-3DS Save-Files.
- Double click the .py or compiled .exe File.
- Generates Information based on your Provided Save-Files.

## Features:
- Take Save-Data & Turn it Into JSON.
- **Need Help Using It? I have a [Video on YouTube](https://youtu.be/msQ_s1OdDCo) to help!**


![2023-09-10 15-31-24](https://github.com/Cracko298/ISZ-Parser/assets/78656905/cecb0196-5454-4745-9d65-5a40461d2048)

## Planned Updates:
- Get Full Inventory Information.
- Get Coordinates, & Vehicle Coordinates.
- Convert JSON Data back into ISZ-3DS Save-Data.


## Building:
### Python Script:
```
> pyinstaller -F --strip --exclude-module numpy --exclude-module opencv --exclude-module cv2 --onefile "isz-parse.py" --icon="icon.ico"
```
### C++ Code:
```
> g++ -o ISZparse.exe -O3 -s isz-parse.cpp
```

## Example Output:
```json
[
    {
        "Data0 File Information": {
            "Game Opened": true,
            "Level Saved": true,
            "Four-Byte Time Hash": 801446425,
            "Converted Time Hash": "24/05 20:00"
        },
        "Data0 Player Information": {
            "Current Health": 52,
            "Current Hunger": 94,
            "Current Thirst": 91,
            "Current Charge": 76,
            "X Coordinates": 3301529424,
            "Y Coordinates": 1156088072,
            "Z Coordinates": 1106346423,
            "X/Y/Z Coordinates": [
                3301529424,
                1156088072,
                1106346423
            ],
            "Current Temps": 3.391648054122925,
            "Inverted Temp": -144.3486328125
        },
        "Data0 Slot #1 Information": {
            "Slot Number": 1,
            "Item Name": "Tranquilizer Gun",
            "Item Type": Weapon,
            "Durability": 28632,
            "Duplicated": 999
        },
        "Data0 Slot #2 Information": {
            "Slot Number": 2,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Duplicated": 0
        },
        "Data0 Slot #3 Information": {
            "Slot Number": 3,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Duplicated": 0
        },
        "Data0 Slot #4 Information": {
            "Slot Number": 4,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Duplicated": 0
        },
        "Data0 Slot #5 Information": {
            "Slot Number": 5,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Duplicated": 0
        }
    }
]
```
