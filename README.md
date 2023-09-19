# ISZ-Parser
- Parses Ice station Z Save-Data into The *.json Human Readable & Widely Used Data Format.
- Allows for Hundreads of Programming Languages and Game Engines to Ensure Compatibility with ISZ-3DS.
- Easy Edits to and From ISZ-3DS Save-Data (Planned Feature Soon **Version v8 Plan**).
- Basic Functionality Available as of **09/10/2023**.

# Downloads:
- Download C++ Source [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v1/isz-parse.cpp) **(Not Kept Upto-Date)**.
- Download Python Source [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v5/isz-parse.py).
- Download Compiled Executable [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v5/isz-parse.exe).

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
            "Four-Byte Time Hash": 3036311106,
            "Converted Time Hash": "19/03 07:45"
        },
        "Data0 Player Information": {
            "Current Health": 255,
            "Current Hunger": 87,
            "Current Thirst": 80,
            "Current Charge": 45,
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
            "X Coordinates": 3301280291,
            "Y Coordinates": 1155592092,
            "Z Coordinates": 1106351966,
            "X/Y/Z Coordinates": [
                3301280291,
                1155592092,
                1106351966
            ],
            "Current Temps": 2.5035226345062256,
            "Inverted Temp": -1.1034368071705103e-05
        },
        "Data0 Heli #1 Information": {
            "Helicopter Number": 1,
            "Helicopter Name": "Greybase Helicopter",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
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
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
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
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3308847120,
            "Y Coordinates": 1112039752,
            "Z Coordinates": 1105566106,
            "X/Y/Z Coordinates": [
                3308847120,
                1112039752,
                1105566106
            ]
        },
        "Data0 Snowcat #1 Information": {
            "Helicopter Number": 4,
            "Helicopter Name": "Submarine Cabins Snowcat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3305928957,
            "Y Coordinates": 1140157827,
            "Z Coordinates": 1103660472,
            "X/Y/Z Coordinates": [
                3305928957,
                1140157827,
                1103660472
            ]
        },
        "Data0 Snowcat #2 Information": {
            "Helicopter Number": 5,
            "Helicopter Name": "Lost Research Cabin Snowcat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3307160895,
            "Y Coordinates": 1158793828,
            "Z Coordinates": 1098430052,
            "X/Y/Z Coordinates": [
                3307160895,
                1158793828,
                1098430052
            ]
        },
        "Data0 Snowplough #1 Information": {
            "Helicopter Number": 6,
            "Helicopter Name": "Church Snowplough",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": 3303196623,
            "Z Coordinates": 1074790400,
            "X/Y/Z Coordinates": [
                null,
                3303196623,
                1074790400
            ]
        },
        "Data0 Snowplough #2 Information": {
            "Helicopter Number": 7,
            "Helicopter Name": "Lost Campsite Snowplough",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3300006791,
            "Y Coordinates": 1152708557,
            "Z Coordinates": 1117342299,
            "X/Y/Z Coordinates": [
                3300006791,
                1152708557,
                1117342299
            ]
        },
        "Data0 Snowmobile #1 Information": {
            "Helicopter Number": 8,
            "Helicopter Name": "Island Cabin Snowmobile",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3297255292,
            "Y Coordinates": 1152246593,
            "Z Coordinates": 1115426807,
            "X/Y/Z Coordinates": [
                3297255292,
                1152246593,
                1115426807
            ]
        },
        "Data0 Snowmobile #2 Information": {
            "Helicopter Number": 9,
            "Helicopter Name": "Lost Cabin Snowmobile",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3301280291,
            "Y Coordinates": 1155592092,
            "Z Coordinates": 1106351966,
            "X/Y/Z Coordinates": [
                3301280291,
                1155592092,
                1106351966
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
# Dictionaries for Parser (next update).
fit_dict = {
    0x45: "Kilometers Travelled",
    0x41: "Days Passed"
}

car_dict = {
    0x23AF: "Greybase Helicopter",
    0x3D47: "Oil-Rig Helicopter",
    0x1347: "3-Red-Houses Helicopter",
    0xDCF: "Submarine Cabins Snowcat",
    0x352F: "Lost Research Cabin Snowcat",
    0x1857: "Church Snowplough",
    0x192F: "Lost Campsite Snowplough",
    0x5EF: "Island Cabin Snowmobile",
    0x1FF7:"Lost Cabin Snowmbile"
}

cloth_dict = {
    0: "Defualt",
    1: "Defualt",
    2: "Defualt",
    3: "Cammo",
    4: "Military",
    5: "Kevlar",
    6: "Arctic",
    7: "Bling",
    8: "Hacked",
    9: "Hacked",
    10: "Hacked",
    11: "Hacked",
    12: "Hacked",
    13: "Hacked"
}
```
