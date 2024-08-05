# ISZ-Parser
- Parses Ice station Z Save-Data into The *.json Human Readable & Widely Used Data Format.
- Allows for Hundreads of Programming Languages and Game Engines to Ensure Compatibility with ISZ-3DS.
- Easy Edits to and From ISZ-3DS Save-Data (Planned Feature Soon **Version v10 Plan**).

# Downloads:
- Download C++ Source [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v1/isz-parse.cpp) **(Not Kept Upto-Date)**.
- Download Python Source [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v7.1/isz-parse.py).
- Download Compiled Executable [Here](https://github.com/Cracko298/ISZ-Parser/releases/download/v7.1/isz-parse.exe).

## Usage:
- Drag and drop Decrypted ISZ-3DS SaveGames.
- Double click the `*.py` or compiled `*.exe` File.
- Generates Information based on your Provided SaveGame Files.

## Features:
- Take Save-Data & Turn it Into JSON.
- Does all Conversion Needed for you to get started on Making your Next Project.
- **Need Help Using It? I have a [Video on YouTube](https://youtu.be/msQ_s1OdDCo) to help!**

![2023-09-10 15-31-24](https://github.com/Cracko298/ISZ-Parser/assets/78656905/cecb0196-5454-4745-9d65-5a40461d2048)

## Roadmap:
```
1. Convert back into ISZ-3DS SaveGames/Save-Data.
2. Decrypt and Encrypt DISA Formatted (aka Legit Current/Backup) ISZ-3DS SaveGames/Save-Data.
```

## Implimented Features:
```
Base Player Information, Fitness and Coordinates       -     75% Completed (Almost Finished).
Inventory and Apparell Information                     -    100% Completed (Finished).
Vehicle Stats, names and Coordinates/Information       -    100% Completed (Finished).
Header Information and Timestamps                      -    100% Completed (Finished).
```

## Building:
### Python Script:
```
> pyinstaller isz-parse.py --onefile  -i "favicon.ico"
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
            "Header Length": 32,
            "SaveGame Length": 17719,
            "Header + SaveGame Length": 17751,
            "Estimated File Size": "17.335kb",
            "Game Opened": true,
            "Level Saved": true,
            "Four-Byte Time Hash": 2616262327,
            "Converted Time Hash": "26/11 14:32"
        },
        "Data0 Player Information": {
            "Current Health": 100,
            "Current Hunger": 100,
            "Current Thirst": 100,
            "Current Charge": 100,
            "Days Passed": 1,
            "Current Day": 2,
            "Kilometers Traveled": 0,
            "In-Game Timestamp": 1083637915,
            "Wearing Jacket": "Defualt Jacket",
            "Wearing Backpack": "Defualt Backpack",
            "Wearing Trouser": "Defualt Trouser",
            "Wearing Outfit": [
                "Defualt Jacket",
                "Defualt Backpack",
                "Defualt Trouser"
            ],
            "Inventory Size": 14,
            "Backpack Size": 9,
            "Resistance Data-Type": "Percentage",
            "Damage Resistance": 0,
            "Weather Resistance": 0,
            "X Coordinates": 3280667608,
            "Y Coordinates": 1134250558,
            "Z Coordinates": 1101020584,
            "X/Y/Z Coordinates": [
                3280667608,
                1134250558,
                1101020584
            ],
            "Current Temps": 4.550029277801514,
            "Inverted Temp": -337698246098944.0
        },
        "Data0 Heli #1 Information": {
            "Helicopter Number": 1,
            "Vechile Name": "Greybase Helicopter",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3301796979,
            "Y Coordinates": 1155807674,
            "Z Coordinates": 1106381373,
            "X/Y/Z Coordinates": [
                3301796979,
                1155807674,
                1106381373
            ]
        },
        "Data0 Heli #2 Information": {
            "Helicopter Number": 2,
            "Vechile Name": "3-Red-Houses Helicopter",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3292726264,
            "Y Coordinates": 1144614830,
            "Z Coordinates": 1106723734,
            "X/Y/Z Coordinates": [
                3292726264,
                1144614830,
                1106723734
            ]
        },
        "Data0 Heli #3 Information": {
            "Helicopter Number": 3,
            "Vechile Name": "Oil-Rig Helicopter",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3308732535,
            "Y Coordinates": 1120378683,
            "Z Coordinates": 1105566106,
            "X/Y/Z Coordinates": [
                3308732535,
                1120378683,
                1105566106
            ]
        },
        "Data0 Snowcat #1 Information": {
            "Snowcat Number": 1,
            "Vechile Name": "Submarine Cabins Snowcat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3305821970,
            "Y Coordinates": 1140154138,
            "Z Coordinates": 1104130081,
            "X/Y/Z Coordinates": [
                3305821970,
                1140154138,
                1104130081
            ]
        },
        "Data0 Snowcat #2 Information": {
            "Snowcat Number": 2,
            "Vechile Name": "Lost Research Cabin Snowcat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3280706863,
            "Y Coordinates": 1159122731,
            "Z Coordinates": 1103330017,
            "X/Y/Z Coordinates": [
                3280706863,
                1159122731,
                1103330017
            ]
        },
        "Data0 Snowplough #1 Information": {
            "Snowplough Number": 1,
            "Vechile Name": "Church Snowplough",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": 3303117996,
            "Z Coordinates": 1074790400,
            "X/Y/Z Coordinates": [
                null,
                3303117996,
                1074790400
            ]
        },
        "Data0 Snowplough #2 Information": {
            "Snowplough Number": 2,
            "Vechile Name": "Lost Campsite Snowplough",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3307197829,
            "Y Coordinates": 1158718530,
            "Z Coordinates": 1098087662,
            "X/Y/Z Coordinates": [
                3307197829,
                1158718530,
                1098087662
            ]
        },
        "Data0 Snowmobile #1 Information": {
            "Snowmobile Number": 1,
            "Vechile Name": "Island Cabin Snowmobile",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3285276557,
            "Y Coordinates": 1131781292,
            "Z Coordinates": 1100328993,
            "X/Y/Z Coordinates": [
                3285276557,
                1131781292,
                1100328993
            ]
        },
        "Data0 Snowmobile #2 Information": {
            "Snowmobile Number": 2,
            "Vechile Name": "Lost Cabin Snowmobile",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3301764194,
            "Y Coordinates": 1155813589,
            "Z Coordinates": 1106363023,
            "X/Y/Z Coordinates": [
                3301764194,
                1155813589,
                1106363023
            ]
        },
        "Data0 Dogsled #1 Information": {
            "Dogsled Number": 1,
            "Vechile Name": "3-Lost-Cabins Dogsled",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3305453462,
            "Y Coordinates": 1160054841,
            "Z Coordinates": 1096126824,
            "X/Y/Z Coordinates": [
                3305453462,
                1160054841,
                1096126824
            ]
        },
        "Data0 Dogsled #2 Information": {
            "Dogsled Number": 2,
            "Vechile Name": "Lighthouse Dogsled",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3308362043,
            "Y Coordinates": 1149720805,
            "Z Coordinates": 1077936128,
            "X/Y/Z Coordinates": [
                3308362043,
                1149720805,
                1077936128
            ]
        },
        "Data0 Boat #1 Information": {
            "Dogsled Number": 1,
            "Vechile Name": "Lighthouse Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3308306940,
            "Y Coordinates": 1149696803,
            "Z Coordinates": 1079529964,
            "X/Y/Z Coordinates": [
                3308306940,
                1149696803,
                1079529964
            ]
        },
        "Data0 Boat #2 Information": {
            "Dogsled Number": 2,
            "Vechile Name": "Island Cabin Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3272925643,
            "Y Coordinates": 1123701490,
            "Z Coordinates": 1077936128,
            "X/Y/Z Coordinates": [
                3272925643,
                1123701490,
                1077936128
            ]
        },
        "Data0 Boat #3 Information": {
            "Dogsled Number": 3,
            "Vechile Name": "Submarine Cabin Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3304121917,
            "Y Coordinates": 1137605706,
            "Z Coordinates": 1080058446,
            "X/Y/Z Coordinates": [
                3304121917,
                1137605706,
                1080058446
            ]
        },
        "Data0 Boat #4 Information": {
            "Dogsled Number": 3,
            "Vechile Name": "Big-Red-Ship Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3307519574,
            "Y Coordinates": 1156498080,
            "Z Coordinates": 1090252702,
            "X/Y/Z Coordinates": [
                3307519574,
                1156498080,
                1090252702
            ]
        },
        "Data0 Boat #5 Information": {
            "Dogsled Number": 3,
            "Vechile Name": "Oil-Rig Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": 3308868948,
            "Y Coordinates": 1099216978,
            "Z Coordinates": 1105582359,
            "X/Y/Z Coordinates": [
                3308868948,
                1099216978,
                1105582359
            ]
        },
        "Data0 Slot #1 Information": {
            "Slot Number": 1,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #2 Information": {
            "Slot Number": 2,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #3 Information": {
            "Slot Number": 3,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #4 Information": {
            "Slot Number": 4,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #5 Information": {
            "Slot Number": 5,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #6 Information": {
            "Slot Number": 6,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #7 Information": {
            "Slot Number": 7,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #8 Information": {
            "Slot Number": 8,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #9 Information": {
            "Slot Number": 9,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #10 Information": {
            "Slot Number": 10,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #11 Information": {
            "Slot Number": 11,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #12 Information": {
            "Slot Number": 12,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #13 Information": {
            "Slot Number": 13,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data0 Slot #14 Information": {
            "Slot Number": 14,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        }
    },
    {
        "Data1 File Information": {
            "Header Length": 32,
            "SaveGame Length": 975,
            "Header + SaveGame Length": 1007,
            "Estimated File Size": "0.983kb",
            "Game Opened": false,
            "Level Saved": false,
            "Four-Byte Time Hash": 2068053687,
            "Converted Time Hash": "13/07 15:21"
        },
        "Data1 Player Information": {
            "Current Health": 0,
            "Current Hunger": 0,
            "Current Thirst": 0,
            "Current Charge": 0,
            "Days Passed": 0,
            "Current Day": 1,
            "Kilometers Traveled": 0,
            "In-Game Timestamp": 0,
            "Wearing Jacket": "Defualt Jacket",
            "Wearing Backpack": "Defualt Backpack",
            "Wearing Trouser": "Defualt Trouser",
            "Wearing Outfit": [
                "Defualt Jacket",
                "Defualt Backpack",
                "Defualt Trouser"
            ],
            "Inventory Size": 14,
            "Backpack Size": 9,
            "Resistance Data-Type": "Percentage",
            "Damage Resistance": 0,
            "Weather Resistance": 0,
            "X Coordinates": 0,
            "Y Coordinates": 0,
            "Z Coordinates": 0,
            "X/Y/Z Coordinates": [
                0,
                0,
                0
            ],
            "Current Temps": 0.0,
            "Inverted Temp": 0.0
        },
        "Data1 Heli #1 Information": {
            "Helicopter Number": 1,
            "Vechile Name": "Greybase Helicopter",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Heli #2 Information": {
            "Helicopter Number": 2,
            "Vechile Name": "3-Red-Houses Helicopter",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Heli #3 Information": {
            "Helicopter Number": 3,
            "Vechile Name": "Oil-Rig Helicopter",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Snowcat #1 Information": {
            "Snowcat Number": 1,
            "Vechile Name": "Submarine Cabins Snowcat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Snowcat #2 Information": {
            "Snowcat Number": 2,
            "Vechile Name": "Lost Research Cabin Snowcat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Snowplough #1 Information": {
            "Snowplough Number": 1,
            "Vechile Name": "Church Snowplough",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Snowplough #2 Information": {
            "Snowplough Number": 2,
            "Vechile Name": "Lost Campsite Snowplough",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Snowmobile #1 Information": {
            "Snowmobile Number": 1,
            "Vechile Name": "Island Cabin Snowmobile",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Snowmobile #2 Information": {
            "Snowmobile Number": 2,
            "Vechile Name": "Lost Cabin Snowmobile",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Dogsled #1 Information": {
            "Dogsled Number": 1,
            "Vechile Name": "3-Lost-Cabins Dogsled",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Dogsled #2 Information": {
            "Dogsled Number": 2,
            "Vechile Name": "Lighthouse Dogsled",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Boat #1 Information": {
            "Dogsled Number": 1,
            "Vechile Name": "Lighthouse Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Boat #2 Information": {
            "Dogsled Number": 2,
            "Vechile Name": "Island Cabin Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Boat #3 Information": {
            "Dogsled Number": 3,
            "Vechile Name": "Submarine Cabin Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Boat #4 Information": {
            "Dogsled Number": 3,
            "Vechile Name": "Big-Red-Ship Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Boat #5 Information": {
            "Dogsled Number": 3,
            "Vechile Name": "Oil-Rig Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data1 Slot #1 Information": {
            "Slot Number": 1,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #2 Information": {
            "Slot Number": 2,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #3 Information": {
            "Slot Number": 3,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #4 Information": {
            "Slot Number": 4,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #5 Information": {
            "Slot Number": 5,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #6 Information": {
            "Slot Number": 6,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #7 Information": {
            "Slot Number": 7,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #8 Information": {
            "Slot Number": 8,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #9 Information": {
            "Slot Number": 9,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #10 Information": {
            "Slot Number": 10,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #11 Information": {
            "Slot Number": 11,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #12 Information": {
            "Slot Number": 12,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #13 Information": {
            "Slot Number": 13,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data1 Slot #14 Information": {
            "Slot Number": 14,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        }
    },
    {
        "Data2 File Information": {
            "Header Length": 32,
            "SaveGame Length": 975,
            "Header + SaveGame Length": 1007,
            "Estimated File Size": "0.983kb",
            "Game Opened": false,
            "Level Saved": false,
            "Four-Byte Time Hash": 2353266359,
            "Converted Time Hash": "27/07 17:05"
        },
        "Data2 Player Information": {
            "Current Health": 0,
            "Current Hunger": 0,
            "Current Thirst": 0,
            "Current Charge": 0,
            "Days Passed": 0,
            "Current Day": 1,
            "Kilometers Traveled": 0,
            "In-Game Timestamp": 0,
            "Wearing Jacket": "Defualt Jacket",
            "Wearing Backpack": "Defualt Backpack",
            "Wearing Trouser": "Defualt Trouser",
            "Wearing Outfit": [
                "Defualt Jacket",
                "Defualt Backpack",
                "Defualt Trouser"
            ],
            "Inventory Size": 14,
            "Backpack Size": 9,
            "Resistance Data-Type": "Percentage",
            "Damage Resistance": 0,
            "Weather Resistance": 0,
            "X Coordinates": 0,
            "Y Coordinates": 0,
            "Z Coordinates": 0,
            "X/Y/Z Coordinates": [
                0,
                0,
                0
            ],
            "Current Temps": 0.0,
            "Inverted Temp": 0.0
        },
        "Data2 Heli #1 Information": {
            "Helicopter Number": 1,
            "Vechile Name": "Greybase Helicopter",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Heli #2 Information": {
            "Helicopter Number": 2,
            "Vechile Name": "3-Red-Houses Helicopter",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Heli #3 Information": {
            "Helicopter Number": 3,
            "Vechile Name": "Oil-Rig Helicopter",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Snowcat #1 Information": {
            "Snowcat Number": 1,
            "Vechile Name": "Submarine Cabins Snowcat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Snowcat #2 Information": {
            "Snowcat Number": 2,
            "Vechile Name": "Lost Research Cabin Snowcat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Snowplough #1 Information": {
            "Snowplough Number": 1,
            "Vechile Name": "Church Snowplough",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Snowplough #2 Information": {
            "Snowplough Number": 2,
            "Vechile Name": "Lost Campsite Snowplough",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Snowmobile #1 Information": {
            "Snowmobile Number": 1,
            "Vechile Name": "Island Cabin Snowmobile",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Snowmobile #2 Information": {
            "Snowmobile Number": 2,
            "Vechile Name": "Lost Cabin Snowmobile",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Dogsled #1 Information": {
            "Dogsled Number": 1,
            "Vechile Name": "3-Lost-Cabins Dogsled",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Dogsled #2 Information": {
            "Dogsled Number": 2,
            "Vechile Name": "Lighthouse Dogsled",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Boat #1 Information": {
            "Dogsled Number": 1,
            "Vechile Name": "Lighthouse Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Boat #2 Information": {
            "Dogsled Number": 2,
            "Vechile Name": "Island Cabin Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Boat #3 Information": {
            "Dogsled Number": 3,
            "Vechile Name": "Submarine Cabin Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Boat #4 Information": {
            "Dogsled Number": 3,
            "Vechile Name": "Big-Red-Ship Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Boat #5 Information": {
            "Dogsled Number": 3,
            "Vechile Name": "Oil-Rig Boat",
            "Vehicle Hex ID": "0x10, 0x40",
            "Vehicle Int ID": 4160,
            "X Coordinates": null,
            "Y Coordinates": null,
            "Z Coordinates": null,
            "X/Y/Z Coordinates": [
                null,
                null,
                null
            ]
        },
        "Data2 Slot #1 Information": {
            "Slot Number": 1,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #2 Information": {
            "Slot Number": 2,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #3 Information": {
            "Slot Number": 3,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #4 Information": {
            "Slot Number": 4,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #5 Information": {
            "Slot Number": 5,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #6 Information": {
            "Slot Number": 6,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #7 Information": {
            "Slot Number": 7,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #8 Information": {
            "Slot Number": 8,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #9 Information": {
            "Slot Number": 9,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #10 Information": {
            "Slot Number": 10,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #11 Information": {
            "Slot Number": 11,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #12 Information": {
            "Slot Number": 12,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #13 Information": {
            "Slot Number": 13,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        },
        "Data2 Slot #14 Information": {
            "Slot Number": 14,
            "Item Name": "Empty",
            "Item Type": null,
            "Durability": 100,
            "Amount": 0
        }
    }
]
```
