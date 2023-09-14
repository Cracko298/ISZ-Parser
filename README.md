# ISZ-Parser
- Parses Ice station Z Save-Data into The *.json Human Readable & Widely Used Data Format.
- Allows for Hundreads of Programming Languages and Game Engines to Ensure Compatibility with ISZ-3DS.
- Easy Edits to and From ISZ-3DS Save-Data (Planned Feature Soon **Version v8 Plan**).
- Basic Functionality Available as of **09/10/2023**.

# Downloads:
- Download C++ Source [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v4/isz-parse.cpp) **(Not Kept Upto-Date)**.
- Download Python Source [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v4/isz-parse.py).
- Download Compiled Executable [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v4/isz-parse.exe).

## Usage:
- Drag and drop Decrypted ISZ-3DS Save-Files.
- Double click the .py or compiled .exe File.
- Generates Information based on your Provided Save-Files.

## Features:
- Take Save-Data & Turn it Into JSON.
- **Need Help Using It? I have a [Video on YouTube](https://youtu.be/msQ_s1OdDCo) to help!**


![2023-09-10 15-31-24](https://github.com/Cracko298/ISZ-Parser/assets/78656905/cecb0196-5454-4745-9d65-5a40461d2048)

## Planned Updates:
- Get Full Inventory Information. - **0% Completed.**
- Get Vehicle Stats & Coordinates. - **15% Completed.**
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
            "Four-Byte Time Hash": 56039210,
            "Converted Time Hash": "10/10 10:26"
        },
        "Data0 Player Information": {
            "Current Health": 48,
            "Current Hunger": 37,
            "Current Thirst": 5,
            "Current Charge": 0,
            "Days Passed": "NaN",
            "Kilometers Traveled": "NaN",
            "Wearing Jacket": "Defualt Jacket",
            "Wearing Backpack": "Defualt Backpack",
            "Wearing Trouser": "Defualt Trouser",
            "Wearing Outfit": [
                "Defualt Jacket",
                "Defualt Backpack",
                "Defualt Trouser"
            ],
            "X Coordinates": 3280667608,
            "Y Coordinates": 1134250558,
            "Z Coordinates": 1101020584,
            "X/Y/Z Coordinates": [
                3280667608,
                1134250558,
                1101020584
            ],
            "Current Temps": -1.791548728942871,
            "Inverted Temp": 1.7028903872063366e+34
        },
        "Data0 Heli #1 Information": {
            "Helicopter Number": 1,
            "Helicopter Name": "Greybase Helicopter",
            "Helicopter Hex ID": "0x10, 0x40",
            "Helicopter Int ID": 4160,
            "X Coordinates": 3301800903,
            "Y Coordinates": 1155716407,
            "Z Coordinates": 1106754142,
            "X/Y/Z Coordinates": [
                3301800903,
                1155716407,
                1106754142
            ]
        },
        "Data0 Heli #2 Information": {
            "Helicopter Number": 2,
            "Helicopter Name": "3-Red-Houses Helicopter",
            "Helicopter Hex ID": "0x10, 0x40",
            "Helicopter Int ID": 4160,
            "X Coordinates": 3293505470,
            "Y Coordinates": 1145064653,
            "Z Coordinates": 1106782978,
            "X/Y/Z Coordinates": [
                3293505470,
                1145064653,
                1106782978
            ]
        },
        "Data0 Heli #3 Information": {
            "Helicopter Number": 3,
            "Helicopter Name": "Oil-Rig Helicopter",
            "Helicopter Hex ID": "0x10, 0x40",
            "Helicopter Int ID": 4160,
            "X Coordinates": 3308847120,
            "Y Coordinates": 1112039752,
            "Z Coordinates": 1105566106,
            "X/Y/Z Coordinates": [
                3308847120,
                1112039752,
                1105566106
            ]
        },
        "Data0 Slot #1 Information": {
            "Slot Number": 1,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Duplicated": 0
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
```py
# Dictionary for Python (next update).
car_dict = {
    0x23AF: "Greybase Helicopter",
    0x3D47: "Oil-Rig Helicopter",
    0x1347: "3 Red Houses"
}
```
