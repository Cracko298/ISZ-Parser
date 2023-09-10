# ISZ-Parser
- Parses Ice station Z Save-Data into The *.json Human Readable Format.

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

![2023-09-10 15-31-24](https://github.com/Cracko298/ISZ-Parser/assets/78656905/cecb0196-5454-4745-9d65-5a40461d2048)

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
            "Four-Byte Time Hash": 1302141361,
            "Converted Time Hash": "05/04 21:56"
        },
        "Data0 Player Information": {
            "Current Health": 255,
            "Current Hunger": 254,
            "Current Thirst": 253,
            "Current Charge": 250,
            "Current Temps": 9999.0,
            "Inverted Temp": 5.520272367764256e-39
        },
        "Data0 Slot #1 Information": {
            "Slot Number": 1,
            "Item Name": null,
            "Item Type": "Invalid Item ID.",
            "Durability": 490,
            "Duplicated": 1
        },
        "Data0 Slot #2 Information": {
            "Slot Number": 2,
            "Item Name": "Tent",
            "Item Type": "Miscellaneous",
            "Durability": 50,
            "Duplicated": 1
        },
        "Data0 Slot #3 Information": {
            "Slot Number": 3,
            "Item Name": "Tranquilizer Ammo",
            "Item Type": "Ammunition",
            "Durability": 100,
            "Duplicated": 1
        },
        "Data0 Slot #4 Information": {
            "Slot Number": 4,
            "Item Name": "Tranquilizer Gun",
            "Item Type": "Weapon",
            "Durability": 96,
            "Duplicated": 9
        },
        "Data0 Slot #5 Information": {
            "Slot Number": 5,
            "Item Name": "Arctic Handgun",
            "Item Type": "Weapon",
            "Durability": 200,
            "Duplicated": 1
        }
    }
]
```
