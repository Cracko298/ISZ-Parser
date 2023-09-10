from os import getcwd, makedirs
from os.path import basename, join, exists
from time import sleep
import struct
import datetime

if exists('Data0') != False:
    with open('Data0','rb+') as data0:
        data0.seek(0)
        open_byte = data0.read(1)
        data0.seek(16)
        save_byte = data0.read(1)
        data0.seek(20)
        y = data0.read(4)
        data0.seek(24)
        z = data0.read(4)
        data0.seek(28)
        x = data0.read(4)
        data0.seek(32)
        health = data0.read(4)
        data0.seek(36)
        food = data0.read(4)
        data0.seek(40)
        water = data0.read(4)
        data0.seek(48)
        battery = data0.read(4)
        data0.seek(44)
        temp = data0.read(4)

        invert_y = y[::-1]
        invert_z = z[::-1]
        invert_x = x[::-1]
        int_y = int.from_bytes(invert_y, byteorder='big')
        int_z = int.from_bytes(invert_z, byteorder='big')
        int_x = int.from_bytes(invert_x, byteorder='big')

        invert_health = health[::-1]
        invert_food = food[::-1]
        invert_water = water[::-1]
        invert_battery = battery[::-1]

        invert_temp = temp[::-1]

        int_h = int.from_bytes(invert_health, byteorder='big')
        int_f = int.from_bytes(invert_food, byteorder='big')
        int_w = int.from_bytes(invert_water, byteorder='big')
        int_b = int.from_bytes(invert_battery, byteorder='big')

        temperature = struct.unpack('f', temp)[0]
        calc_temp = struct.unpack('f', invert_temp)[0]

        print("==== File Information ====")
        file0 = open('_ISZ-Save-Info.txt','a')
        file0.write(f"==== File Information ====\n")
        
        if open_byte == b'\x01':
            print(f"Game Opened: True")
            file0 = open('_ISZ-Save-Info.txt','a')
            file0.write(f"Game Opened: True\n")
        else:
            print(f"Game Opened: False")
            file0 = open('_ISZ-Save-Info.txt','a')
            file0.write(f"Game Opened: True\n")
        
        if save_byte >= b'\x01' and save_byte <= b'\xFF':
            print("Level Saved: True")
            file0 = open('_ISZ-Save-Info.txt','a')
            file0.write(f"Level Saved: True\n")
        else:
            print("Level Saved: False")
            file0 = open('_ISZ-Save-Info.txt','a')
            file0.write(f"Level Saved: False\n")

        with open("Data0", "rb") as file:
            file.seek(7)
            timestamp_bytes = file.read(5)

        reversed_bytes = timestamp_bytes[::-1]
        timestamp = int.from_bytes(reversed_bytes, byteorder='little')
        nintendo_epoch = datetime.datetime(2000, 1, 1)
        nintendo_timestamp = nintendo_epoch + datetime.timedelta(seconds=timestamp)
        unix_timestamp = int((nintendo_timestamp - datetime.datetime(1970, 1, 1)).total_seconds())
        date_time = datetime.datetime.fromtimestamp(unix_timestamp)

        formatted_date_time = date_time.strftime("%d/%m %H:%M")
        print(" ")
        print("Four-Byte Time Hash:", timestamp)
        print("Converted Time Hash:", formatted_date_time)

        file0 = open('_ISZ-Save-Info.txt','a')
        file0.write(f"Four-Byte Time Hash: {timestamp}.\n")
        file0.write(f"Converted Time Hash: {formatted_date_time}.\n")
        file0.write(f"\n")

        print(" ")
        print("==== Player Information ====")
        print(f"Current Health: {int_h}.")
        print(f"Current Hunger: {int_f}.")
        print(f"Current Thirst: {int_w}.")
        print(f"Current Charge: {int_b}.")
        print(f"Current Temps:  {temperature}.")
        print(f"Inverted Temp:  {calc_temp}.")
        print(" ")

        file0.write(f"==== Player Information ====\n")
        file0.write(f"Current Health: {int_h}.\n")
        file0.write(f"Current Hunger: {int_f}.\n")
        file0.write(f"Current Thirst: {int_w}.\n")
        file0.write(f"Current Health: {int_b}.\n")
        file0.write(f"Current Temps:  {temperature}.\n")
        file0.write(f"Inverted Temp:  {calc_temp}.\n")
        file0.write(f"\n")
        file0.write(f"==== Slots Information ====\n")





        print("==== Slot Information ====")
        data_dict = {
        0x01: "Basic Handgun",
        0x02: "Arctic Handgun",
        0x03: "Arctic Eagle Handgun",
        0x04: "Double Barrel Shotgun",
        0x05: "Hunting Shotgun",
        0x06: "Arctic Hunting Shotgun",
        0x07: "Hunting Rifle",
        0x08: "Scout Hunting Rifle",
        0x09: "Arctic Hunting Rifle",
        0x0A: "Crossbow",
        0x0B: "Hunting Crossbow",
        0x0C: "Arctic Hunting Crossbow",
        0x0D: "Tranquilizer Gun",
        0x0E: "Hunting Knife",
        0x0F: "Pistol Ammo",
        0x10: "Shotgun Ammo",
        0x11: "Rifle Ammo",
        0x12: "Crossbow Bolts",
        0x13: "Tranquilizer Ammo",
        0x14: "Matches",
        0x15: "Fuel",
        0x16: "Binoculars",
        0x17: "Cooking Stove",
        0x18: "Bear Trap",
        0x19: "Fishing Rod",
        0x1A: "Field Binoculars",
        0x1B: "Professional Fishing Rod",
        0x1C: "Metal Detector",
        0x1D: "Water Bottle",
        0x1E: "Snackbar",
        0x1F: "Tuna",
        0x20: "Beans",
        0x21: "Corned Beef",
        0x22: "Large Water Bottle",
        0x23: "Mint Cake",
        0x24: "Antiseptic",
        0x25: "Antibiotics",
        0x26: "Bandage",
        0x27: "Dressing",
        0x28: "Large Bandage",
        0x29: "Large Dressing",
        0x2A: "Jacket",
        0x2B: "Trousers",
        0x2C: "Backpack",
        0x2D: "Cammo Jacket",
        0x2E: "Cammo Trousers",
        0x2F: "Cammo Backpack",
        0x30: "Military Jacket",
        0x31: "Military Trousers",
        0x32: "Military Backpack",
        0x33: "Kevlar Jacket",
        0x34: "Kevlar Trousers",
        0x35: "Kevlar Backpack",
        0x36: "Arctic Jacket",
        0x37: "Arctic Trousers",
        0x38: "Arctic Backpack",
        0x39: "Bling Jacket",
        0x3A: "Bling Trousers",
        0x3B: "Bling Backpack",
        0x3C: "Tent",
        0x3D: "Logs",
        0x3E: "Goose",
        0x3F: "Cooked Goose",
        0x40: "Minnow",
        0x41: "Large Fish",
        0x42: "Cooked Fish",
        0x43: "Engine Part",
        0x44: "Snowboard",
        0x45: "Flamethrower",
        0x46: "Ray Gun",
        0x47: "Flare Gun"}


        with open("Data0", "rb") as file:
            for i in range(1, 6):
                num = 90 + (15*i)

                file.seek(num)
                byte = file.read(1)

                durability = num + 1
                duplicity = num + 9
                item_type = num - 1

                file.seek(durability)
                num1 = file.read(4)

                file.seek(duplicity)
                num2 = file.read(4)

                file.seek(item_type)
                num3 = file.read(1)
        
                inv_dur = num1[::-1]
                inv_dup = num2[::-1]
                inv_typ = num3[::-1]

                int_dur = int.from_bytes(inv_dur, byteorder='big')
                int_dup = int.from_bytes(inv_dup, byteorder='big')
                int_typ = int.from_bytes(inv_typ, byteorder='big')

                if int_typ == 3:
                    if "Shotgun" in data_dict[ord(byte)] or "Handgun" in data_dict[ord(byte)] or "Flame" in data_dict[ord(byte)] or "Trap" in data_dict[ord(byte)] or "Rifle" in data_dict[ord(byte)] or "Hunting" in data_dict[ord(byte)] or "Gun" in data_dict[ord(byte)] and "Ammo" not in data_dict[ord(byte)]:
                        int_typ = "Weapon"

                    if "Bandage" in data_dict[ord(byte)] or "Dressing" in data_dict[ord(byte)] or "Antibiotics" in data_dict[ord(byte)] or "Water" in data_dict[ord(byte)] or "Cake" in data_dict[ord(byte)] or "Cooked" in data_dict[ord(byte)] or "Beans" in data_dict[ord(byte)] or "Tuna" in data_dict[ord(byte)] or "Beef" in data_dict[ord(byte)] or "Antiseptic" in data_dict[ord(byte)] or "Snackbar" in data_dict[ord(byte)]:
                        int_typ = "Consumable"
            
                    if "Tent" in data_dict[ord(byte)] or "Stove" in data_dict[ord(byte)] or "Part" in data_dict[ord(byte)] or "Fuel" in data_dict[ord(byte)] or "Logs" in data_dict[ord(byte)]:
                        int_typ = "Miscellaneous"

                    if "Snowboard" in data_dict[ord(byte)]:
                        int_typ = "Vehicle"


                if int_typ == 4:
                    if "Jacket" in data_dict[ord(byte)] or "Trousers" in data_dict[ord(byte)] or "Backpack" in data_dict[ord(byte)]:
                        int_typ = "Clothing"
            
                    if "Shotgun" in data_dict[ord(byte)] or "Handgun" in data_dict[ord(byte)] or "Flame" in data_dict[ord(byte)] or "Trap" in data_dict[ord(byte)] or "Rifle" in data_dict[ord(byte)] or "Hunting" in data_dict[ord(byte)] or "Crossbow" in data_dict[ord(byte)] and "Ammo" not in data_dict[ord(byte)]:
                        int_typ = "Weapon"
            
                    if "Ammo" in data_dict[ord(byte)] or "Bolt" in data_dict[ord(byte)]:
                        int_typ = "Ammunition"

                    if "Tent" in data_dict[ord(byte)] or "Stove" in data_dict[ord(byte)] or "Part" in data_dict[ord(byte)] or "Fuel" in data_dict[ord(byte)] or "Logs" in data_dict[ord(byte)]:
                        int_typ = "Miscellaneous"

                    if "Snowboard" in data_dict[ord(byte)]:
                        int_typ = "Vehicle"



                if ord(byte) in data_dict:
                    print(f'Slot #{i}:   ',data_dict[ord(byte)])
                    print(f"Item Types: {int_typ}.")
                    print(f"Durability: {int_dur}.")
                    print(f"Duplicated: {int_dup}.")
                    file0 = open('_ISZ-Save-Info.txt','a')
                    file0.write(f"Slot #{i}:    {data_dict[ord(byte)]}.\n")
                    file0.write(f"Item Types: {int_typ}.\n")
                    file0.write(f"Durability: {int_dur}.\n")
                    file0.write(f"Duplicated: {int_dup}.\n")
                    file0.write(f"\n")
                    print(" ")
                    print(" ")
                  
                else:
                    int_typ = "None"
                    print(f"Slot #{i}:    Empty")
                    print(f"Item Types: {int_typ}.")
                    print(f"Durability: {int_dur}.")
                    print(f"Duplicated: {int_dup}.")
                    file0 = open('_ISZ-Save-Info.txt','a')
                    file0.write(f"Slot #{i}:    Empty.\n")
                    file0.write(f"Item Types: {int_typ}.\n")
                    file0.write(f"Durability: {int_dur}.\n")
                    file0.write(f"Duplicated: {int_dup}.\n")
                    file0.write(f"\n")
                    print(" ")
                    print(" ")

                byte = file.read(1)



if exists('Data1') != False:
    with open('Data1','rb+') as data0:
        data0.seek(0)
        open_byte = data0.read(1)
        data0.seek(16)
        save_byte = data0.read(1)
        data0.seek(20)
        y = data0.read(4)
        data0.seek(24)
        z = data0.read(4)
        data0.seek(28)
        x = data0.read(4)
        data0.seek(32)
        health = data0.read(4)
        data0.seek(36)
        food = data0.read(4)
        data0.seek(40)
        water = data0.read(4)
        data0.seek(48)
        battery = data0.read(4)
        data0.seek(44)
        temp = data0.read(4)

        invert_y = y[::-1]
        invert_z = z[::-1]
        invert_x = x[::-1]
        int_y = int.from_bytes(invert_y, byteorder='big')
        int_z = int.from_bytes(invert_z, byteorder='big')
        int_x = int.from_bytes(invert_x, byteorder='big')

        invert_health = health[::-1]
        invert_food = food[::-1]
        invert_water = water[::-1]
        invert_battery = battery[::-1]

        invert_temp = temp[::-1]

        int_h = int.from_bytes(invert_health, byteorder='big')
        int_f = int.from_bytes(invert_food, byteorder='big')
        int_w = int.from_bytes(invert_water, byteorder='big')
        int_b = int.from_bytes(invert_battery, byteorder='big')

        temperature = struct.unpack('f', temp)[0]
        calc_temp = struct.unpack('f', invert_temp)[0]

        print("==== File Information ====")
        file0 = open('_ISZ-Save-Info1.txt','a')
        file0.write(f"==== File Information ====\n")
        
        if open_byte == b'\x01':
            print(f"Game Opened: True")
            file0 = open('_ISZ-Save-Info1.txt','a')
            file0.write(f"Game Opened: True\n")
        else:
            print(f"Game Opened: False")
            file0 = open('_ISZ-Save-Info1.txt','a')
            file0.write(f"Game Opened: True\n")
        
        if save_byte >= b'\x01' and save_byte <= b'\xFF':
            print("Level Saved: True")
            file0 = open('_ISZ-Save-Info1.txt','a')
            file0.write(f"Level Saved: True\n")
        else:
            print("Level Saved: False")
            file0 = open('_ISZ-Save-Info1.txt','a')
            file0.write(f"Level Saved: False\n")

        with open("Data1", "rb") as file:
            file.seek(7)
            timestamp_bytes = file.read(5)

        reversed_bytes = timestamp_bytes[::-1]
        timestamp = int.from_bytes(reversed_bytes, byteorder='little')
        nintendo_epoch = datetime.datetime(2000, 1, 1)
        nintendo_timestamp = nintendo_epoch + datetime.timedelta(seconds=timestamp)
        unix_timestamp = int((nintendo_timestamp - datetime.datetime(1970, 1, 1)).total_seconds())
        date_time = datetime.datetime.fromtimestamp(unix_timestamp)

        formatted_date_time = date_time.strftime("%d/%m %H:%M")
        print(" ")
        print("Four-Byte Time Hash:", timestamp)
        print("Converted Time Hash:", formatted_date_time)

        file0 = open('_ISZ-Save-Info1.txt','a')
        file0.write(f"Four-Byte Time Hash: {timestamp}.\n")
        file0.write(f"Converted Time Hash: {formatted_date_time}.\n")
        file0.write(f"\n")

        print(" ")
        print("==== Player Information ====")
        print(f"Current Health: {int_h}.")
        print(f"Current Hunger: {int_f}.")
        print(f"Current Thirst: {int_w}.")
        print(f"Current Charge: {int_b}.")
        print(f"Current Temps:  {temperature}.")
        print(f"Inverted Temp:  {calc_temp}.")
        print(" ")

        file0.write(f"==== Player Information ====\n")
        file0.write(f"Current Health: {int_h}.\n")
        file0.write(f"Current Hunger: {int_f}.\n")
        file0.write(f"Current Thirst: {int_w}.\n")
        file0.write(f"Current Health: {int_b}.\n")
        file0.write(f"Current Temps:  {temperature}.\n")
        file0.write(f"Inverted Temp:  {calc_temp}.\n")
        file0.write(f"\n")
        file0.write(f"==== Slots Information ====\n")





        print("==== Slot Information ====")
        data_dict = {
        0x01: "Basic Handgun",
        0x02: "Arctic Handgun",
        0x03: "Arctic Eagle Handgun",
        0x04: "Double Barrel Shotgun",
        0x05: "Hunting Shotgun",
        0x06: "Arctic Hunting Shotgun",
        0x07: "Hunting Rifle",
        0x08: "Scout Hunting Rifle",
        0x09: "Arctic Hunting Rifle",
        0x0A: "Crossbow",
        0x0B: "Hunting Crossbow",
        0x0C: "Arctic Hunting Crossbow",
        0x0D: "Tranquilizer Gun",
        0x0E: "Hunting Knife",
        0x0F: "Pistol Ammo",
        0x10: "Shotgun Ammo",
        0x11: "Rifle Ammo",
        0x12: "Crossbow Bolts",
        0x13: "Tranquilizer Ammo",
        0x14: "Matches",
        0x15: "Fuel",
        0x16: "Binoculars",
        0x17: "Cooking Stove",
        0x18: "Bear Trap",
        0x19: "Fishing Rod",
        0x1A: "Field Binoculars",
        0x1B: "Professional Fishing Rod",
        0x1C: "Metal Detector",
        0x1D: "Water Bottle",
        0x1E: "Snackbar",
        0x1F: "Tuna",
        0x20: "Beans",
        0x21: "Corned Beef",
        0x22: "Large Water Bottle",
        0x23: "Mint Cake",
        0x24: "Antiseptic",
        0x25: "Antibiotics",
        0x26: "Bandage",
        0x27: "Dressing",
        0x28: "Large Bandage",
        0x29: "Large Dressing",
        0x2A: "Jacket",
        0x2B: "Trousers",
        0x2C: "Backpack",
        0x2D: "Cammo Jacket",
        0x2E: "Cammo Trousers",
        0x2F: "Cammo Backpack",
        0x30: "Military Jacket",
        0x31: "Military Trousers",
        0x32: "Military Backpack",
        0x33: "Kevlar Jacket",
        0x34: "Kevlar Trousers",
        0x35: "Kevlar Backpack",
        0x36: "Arctic Jacket",
        0x37: "Arctic Trousers",
        0x38: "Arctic Backpack",
        0x39: "Bling Jacket",
        0x3A: "Bling Trousers",
        0x3B: "Bling Backpack",
        0x3C: "Tent",
        0x3D: "Logs",
        0x3E: "Goose",
        0x3F: "Cooked Goose",
        0x40: "Minnow",
        0x41: "Large Fish",
        0x42: "Cooked Fish",
        0x43: "Engine Part",
        0x44: "Snowboard",
        0x45: "Flamethrower",
        0x46: "Ray Gun",
        0x47: "Flare Gun"}


        with open("Data1", "rb") as file:
            for i in range(1, 6):
                num = 90 + (15*i)

                file.seek(num)
                byte = file.read(1)

                durability = num + 1
                duplicity = num + 9
                item_type = num - 1

                file.seek(durability)
                num1 = file.read(4)

                file.seek(duplicity)
                num2 = file.read(4)

                file.seek(item_type)
                num3 = file.read(1)
        
                inv_dur = num1[::-1]
                inv_dup = num2[::-1]
                inv_typ = num3[::-1]

                int_dur = int.from_bytes(inv_dur, byteorder='big')
                int_dup = int.from_bytes(inv_dup, byteorder='big')
                int_typ = int.from_bytes(inv_typ, byteorder='big')

                if int_typ == 3:
                    if "Shotgun" in data_dict[ord(byte)] or "Handgun" in data_dict[ord(byte)] or "Flame" in data_dict[ord(byte)] or "Trap" in data_dict[ord(byte)] or "Rifle" in data_dict[ord(byte)] or "Hunting" in data_dict[ord(byte)] or "Gun" in data_dict[ord(byte)] and "Ammo" not in data_dict[ord(byte)]:
                        int_typ = "Weapon"

                    if "Bandage" in data_dict[ord(byte)] or "Dressing" in data_dict[ord(byte)] or "Antibiotics" in data_dict[ord(byte)] or "Water" in data_dict[ord(byte)] or "Cake" in data_dict[ord(byte)] or "Cooked" in data_dict[ord(byte)] or "Beans" in data_dict[ord(byte)] or "Tuna" in data_dict[ord(byte)] or "Beef" in data_dict[ord(byte)] or "Antiseptic" in data_dict[ord(byte)] or "Snackbar" in data_dict[ord(byte)]:
                        int_typ = "Consumable"
            
                    if "Tent" in data_dict[ord(byte)] or "Stove" in data_dict[ord(byte)] or "Part" in data_dict[ord(byte)] or "Fuel" in data_dict[ord(byte)] or "Logs" in data_dict[ord(byte)]:
                        int_typ = "Miscellaneous"

                    if "Snowboard" in data_dict[ord(byte)]:
                        int_typ = "Vehicle"


                if int_typ == 4:
                    if "Jacket" in data_dict[ord(byte)] or "Trousers" in data_dict[ord(byte)] or "Backpack" in data_dict[ord(byte)]:
                        int_typ = "Clothing"
            
                    if "Shotgun" in data_dict[ord(byte)] or "Handgun" in data_dict[ord(byte)] or "Flame" in data_dict[ord(byte)] or "Trap" in data_dict[ord(byte)] or "Rifle" in data_dict[ord(byte)] or "Hunting" in data_dict[ord(byte)] or "Crossbow" in data_dict[ord(byte)] and "Ammo" not in data_dict[ord(byte)]:
                        int_typ = "Weapon"
            
                    if "Ammo" in data_dict[ord(byte)] or "Bolt" in data_dict[ord(byte)]:
                        int_typ = "Ammunition"

                    if "Tent" in data_dict[ord(byte)] or "Stove" in data_dict[ord(byte)] or "Part" in data_dict[ord(byte)] or "Fuel" in data_dict[ord(byte)] or "Logs" in data_dict[ord(byte)]:
                        int_typ = "Miscellaneous"

                    if "Snowboard" in data_dict[ord(byte)]:
                        int_typ = "Vehicle"



                if ord(byte) in data_dict:
                    print(f'Slot #{i}:   ',data_dict[ord(byte)])
                    print(f"Item Types: {int_typ}.")
                    print(f"Durability: {int_dur}.")
                    print(f"Duplicated: {int_dup}.")
                    file0 = open('_ISZ-Save-Info1.txt','a')
                    file0.write(f"Slot #{i}:    {data_dict[ord(byte)]}.\n")
                    file0.write(f"Item Types: {int_typ}.\n")
                    file0.write(f"Durability: {int_dur}.\n")
                    file0.write(f"Duplicated: {int_dup}.\n")
                    file0.write(f"\n")
                    print(" ")
                    print(" ")
                  
                else:
                    int_typ = "None"
                    print(f"Slot #{i}:    Empty")
                    print(f"Item Types: {int_typ}.")
                    print(f"Durability: {int_dur}.")
                    print(f"Duplicated: {int_dup}.")
                    file0 = open('_ISZ-Save-Info1.txt','a')
                    file0.write(f"Slot #{i}:    Empty.\n")
                    file0.write(f"Item Types: {int_typ}.\n")
                    file0.write(f"Durability: {int_dur}.\n")
                    file0.write(f"Duplicated: {int_dup}.\n")
                    file0.write(f"\n")
                    print(" ")
                    print(" ")

                byte = file.read(1)


if exists('Data2') != False:
    with open('Data2','rb+') as data0:
        data0.seek(0)
        open_byte = data0.read(1)
        data0.seek(16)
        save_byte = data0.read(1)
        data0.seek(20)
        y = data0.read(4)
        data0.seek(24)
        z = data0.read(4)
        data0.seek(28)
        x = data0.read(4)
        data0.seek(32)
        health = data0.read(4)
        data0.seek(36)
        food = data0.read(4)
        data0.seek(40)
        water = data0.read(4)
        data0.seek(48)
        battery = data0.read(4)
        data0.seek(44)
        temp = data0.read(4)

        invert_y = y[::-1]
        invert_z = z[::-1]
        invert_x = x[::-1]
        int_y = int.from_bytes(invert_y, byteorder='big')
        int_z = int.from_bytes(invert_z, byteorder='big')
        int_x = int.from_bytes(invert_x, byteorder='big')

        invert_health = health[::-1]
        invert_food = food[::-1]
        invert_water = water[::-1]
        invert_battery = battery[::-1]

        invert_temp = temp[::-1]

        int_h = int.from_bytes(invert_health, byteorder='big')
        int_f = int.from_bytes(invert_food, byteorder='big')
        int_w = int.from_bytes(invert_water, byteorder='big')
        int_b = int.from_bytes(invert_battery, byteorder='big')

        temperature = struct.unpack('f', temp)[0]
        calc_temp = struct.unpack('f', invert_temp)[0]

        print("==== File Information ====")
        file0 = open('_ISZ-Save-Info2.txt','a')
        file0.write(f"==== File Information ====\n")
        
        if open_byte == b'\x01':
            print(f"Game Opened: True")
            file0 = open('_ISZ-Save-Info2.txt','a')
            file0.write(f"Game Opened: True\n")
        else:
            print(f"Game Opened: False")
            file0 = open('_ISZ-Save-Info2.txt','a')
            file0.write(f"Game Opened: True\n")
        
        if save_byte >= b'\x01' and save_byte <= b'\xFF':
            print("Level Saved: True")
            file0 = open('_ISZ-Save-Info2.txt','a')
            file0.write(f"Level Saved: True\n")
        else:
            print("Level Saved: False")
            file0 = open('_ISZ-Save-Info2.txt','a')
            file0.write(f"Level Saved: False\n")

        with open("Data2", "rb") as file:
            file.seek(7)
            timestamp_bytes = file.read(5)

        reversed_bytes = timestamp_bytes[::-1]
        timestamp = int.from_bytes(reversed_bytes, byteorder='little')
        nintendo_epoch = datetime.datetime(2000, 1, 1)
        nintendo_timestamp = nintendo_epoch + datetime.timedelta(seconds=timestamp)
        unix_timestamp = int((nintendo_timestamp - datetime.datetime(1970, 1, 1)).total_seconds())
        date_time = datetime.datetime.fromtimestamp(unix_timestamp)

        formatted_date_time = date_time.strftime("%d/%m %H:%M")
        print(" ")
        print("Four-Byte Time Hash:", timestamp)
        print("Converted Time Hash:", formatted_date_time)

        file0 = open('_ISZ-Save-Info2.txt','a')
        file0.write(f"Four-Byte Time Hash: {timestamp}.\n")
        file0.write(f"Converted Time Hash: {formatted_date_time}.\n")
        file0.write(f"\n")

        print(" ")
        print("==== Player Information ====")
        print(f"Current Health: {int_h}.")
        print(f"Current Hunger: {int_f}.")
        print(f"Current Thirst: {int_w}.")
        print(f"Current Charge: {int_b}.")
        print(f"Current Temps:  {temperature}.")
        print(f"Inverted Temp:  {calc_temp}.")
        print(" ")

        file0.write(f"==== Player Information ====\n")
        file0.write(f"Current Health: {int_h}.\n")
        file0.write(f"Current Hunger: {int_f}.\n")
        file0.write(f"Current Thirst: {int_w}.\n")
        file0.write(f"Current Health: {int_b}.\n")
        file0.write(f"Current Temps:  {temperature}.\n")
        file0.write(f"Inverted Temp:  {calc_temp}.\n")
        file0.write(f"\n")
        file0.write(f"==== Slots Information ====\n")





        print("==== Slot Information ====")
        data_dict = {
        0x01: "Basic Handgun",
        0x02: "Arctic Handgun",
        0x03: "Arctic Eagle Handgun",
        0x04: "Double Barrel Shotgun",
        0x05: "Hunting Shotgun",
        0x06: "Arctic Hunting Shotgun",
        0x07: "Hunting Rifle",
        0x08: "Scout Hunting Rifle",
        0x09: "Arctic Hunting Rifle",
        0x0A: "Crossbow",
        0x0B: "Hunting Crossbow",
        0x0C: "Arctic Hunting Crossbow",
        0x0D: "Tranquilizer Gun",
        0x0E: "Hunting Knife",
        0x0F: "Pistol Ammo",
        0x10: "Shotgun Ammo",
        0x11: "Rifle Ammo",
        0x12: "Crossbow Bolts",
        0x13: "Tranquilizer Ammo",
        0x14: "Matches",
        0x15: "Fuel",
        0x16: "Binoculars",
        0x17: "Cooking Stove",
        0x18: "Bear Trap",
        0x19: "Fishing Rod",
        0x1A: "Field Binoculars",
        0x1B: "Professional Fishing Rod",
        0x1C: "Metal Detector",
        0x1D: "Water Bottle",
        0x1E: "Snackbar",
        0x1F: "Tuna",
        0x20: "Beans",
        0x21: "Corned Beef",
        0x22: "Large Water Bottle",
        0x23: "Mint Cake",
        0x24: "Antiseptic",
        0x25: "Antibiotics",
        0x26: "Bandage",
        0x27: "Dressing",
        0x28: "Large Bandage",
        0x29: "Large Dressing",
        0x2A: "Jacket",
        0x2B: "Trousers",
        0x2C: "Backpack",
        0x2D: "Cammo Jacket",
        0x2E: "Cammo Trousers",
        0x2F: "Cammo Backpack",
        0x30: "Military Jacket",
        0x31: "Military Trousers",
        0x32: "Military Backpack",
        0x33: "Kevlar Jacket",
        0x34: "Kevlar Trousers",
        0x35: "Kevlar Backpack",
        0x36: "Arctic Jacket",
        0x37: "Arctic Trousers",
        0x38: "Arctic Backpack",
        0x39: "Bling Jacket",
        0x3A: "Bling Trousers",
        0x3B: "Bling Backpack",
        0x3C: "Tent",
        0x3D: "Logs",
        0x3E: "Goose",
        0x3F: "Cooked Goose",
        0x40: "Minnow",
        0x41: "Large Fish",
        0x42: "Cooked Fish",
        0x43: "Engine Part",
        0x44: "Snowboard",
        0x45: "Flamethrower",
        0x46: "Ray Gun",
        0x47: "Flare Gun"}


        with open("Data2", "rb") as file:
            for i in range(1, 6):
                num = 90 + (15*i)

                file.seek(num)
                byte = file.read(1)

                durability = num + 1
                duplicity = num + 9
                item_type = num - 1

                file.seek(durability)
                num1 = file.read(4)

                file.seek(duplicity)
                num2 = file.read(4)

                file.seek(item_type)
                num3 = file.read(1)
        
                inv_dur = num1[::-1]
                inv_dup = num2[::-1]
                inv_typ = num3[::-1]

                int_dur = int.from_bytes(inv_dur, byteorder='big')
                int_dup = int.from_bytes(inv_dup, byteorder='big')
                int_typ = int.from_bytes(inv_typ, byteorder='big')

                if int_typ == 3:
                    if "Shotgun" in data_dict[ord(byte)] or "Handgun" in data_dict[ord(byte)] or "Flame" in data_dict[ord(byte)] or "Trap" in data_dict[ord(byte)] or "Rifle" in data_dict[ord(byte)] or "Hunting" in data_dict[ord(byte)] or "Gun" in data_dict[ord(byte)] and "Ammo" not in data_dict[ord(byte)]:
                        int_typ = "Weapon"

                    if "Bandage" in data_dict[ord(byte)] or "Dressing" in data_dict[ord(byte)] or "Antibiotics" in data_dict[ord(byte)] or "Water" in data_dict[ord(byte)] or "Cake" in data_dict[ord(byte)] or "Cooked" in data_dict[ord(byte)] or "Beans" in data_dict[ord(byte)] or "Tuna" in data_dict[ord(byte)] or "Beef" in data_dict[ord(byte)] or "Antiseptic" in data_dict[ord(byte)] or "Snackbar" in data_dict[ord(byte)]:
                        int_typ = "Consumable"
            
                    if "Tent" in data_dict[ord(byte)] or "Stove" in data_dict[ord(byte)] or "Part" in data_dict[ord(byte)] or "Fuel" in data_dict[ord(byte)] or "Logs" in data_dict[ord(byte)]:
                        int_typ = "Miscellaneous"

                    if "Snowboard" in data_dict[ord(byte)]:
                        int_typ = "Vehicle"


                if int_typ == 4:
                    if "Jacket" in data_dict[ord(byte)] or "Trousers" in data_dict[ord(byte)] or "Backpack" in data_dict[ord(byte)]:
                        int_typ = "Clothing"
            
                    if "Shotgun" in data_dict[ord(byte)] or "Handgun" in data_dict[ord(byte)] or "Flame" in data_dict[ord(byte)] or "Trap" in data_dict[ord(byte)] or "Rifle" in data_dict[ord(byte)] or "Hunting" in data_dict[ord(byte)] or "Crossbow" in data_dict[ord(byte)] and "Ammo" not in data_dict[ord(byte)]:
                        int_typ = "Weapon"
            
                    if "Ammo" in data_dict[ord(byte)] or "Bolt" in data_dict[ord(byte)]:
                        int_typ = "Ammunition"

                    if "Tent" in data_dict[ord(byte)] or "Stove" in data_dict[ord(byte)] or "Part" in data_dict[ord(byte)] or "Fuel" in data_dict[ord(byte)] or "Logs" in data_dict[ord(byte)]:
                        int_typ = "Miscellaneous"

                    if "Snowboard" in data_dict[ord(byte)]:
                        int_typ = "Vehicle"



                if ord(byte) in data_dict:
                    print(f'Slot #{i}:   ',data_dict[ord(byte)])
                    print(f"Item Types: {int_typ}.")
                    print(f"Durability: {int_dur}.")
                    print(f"Duplicated: {int_dup}.")
                    file0 = open('_ISZ-Save-Info2.txt','a')
                    file0.write(f"Slot #{i}:    {data_dict[ord(byte)]}.\n")
                    file0.write(f"Item Types: {int_typ}.\n")
                    file0.write(f"Durability: {int_dur}.\n")
                    file0.write(f"Duplicated: {int_dup}.\n")
                    file0.write(f"\n")
                    print(" ")
                    print(" ")
                  
                else:
                    int_typ = "None"
                    print(f"Slot #{i}:    Empty")
                    print(f"Item Types: {int_typ}.")
                    print(f"Durability: {int_dur}.")
                    print(f"Duplicated: {int_dup}.")
                    file0 = open('_ISZ-Save-Info2.txt','a')
                    file0.write(f"Slot #{i}:    Empty.\n")
                    file0.write(f"Item Types: {int_typ}.\n")
                    file0.write(f"Durability: {int_dur}.\n")
                    file0.write(f"Duplicated: {int_dup}.\n")
                    file0.write(f"\n")
                    print(" ")
                    print(" ")

                byte = file.read(1)