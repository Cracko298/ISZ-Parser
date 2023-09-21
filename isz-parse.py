from os.path import exists
from struct import unpack
import datetime
from json import dump

save_data_list = []
number0 = 0

fit_dict = {
    0x48: "Kilometers Travelled",
    0x44: "Days Passed"
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
    0x1FF7: "Lost Cabin Snowmbile",
    0x2F47: "3-Lost-Cabins Dogsled",
    0x1CAF: "Lighthouse Dogsled",
    0x1CE7: "Lighthouse Boat",
    0xB67: "Submarine Cabins Boat",
    0x3F7: "Island Cabin Boat"

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
    13: "Hacked", 
}

data_dict = {
        0x00: "Empty",
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
        0x47: "Flare Gun"
}

for file_index in range(3):
    file_name = f'Data{file_index}'
    save_data = {}

    if exists(file_name):
        with open(file_name, 'rb+') as data_file:
            data_file.seek(0)
            open_byte = data_file.read(1)
            data_file.seek(16)
            save_byte = data_file.read(1)
            data_file.seek(20)
            y = data_file.read(4)
            data_file.seek(24)
            z = data_file.read(4)
            data_file.seek(28)
            x = data_file.read(4)
            data_file.seek(32)
            health = data_file.read(4)
            data_file.seek(36)
            food = data_file.read(4)
            data_file.seek(40)
            water = data_file.read(4)
            data_file.seek(48)
            battery = data_file.read(4)
            data_file.seek(44)
            temp = data_file.read(4)
            data_file.seek(0x34)
            jack0 = data_file.read(1)
            data_file.seek(0x38)
            trou0 = data_file.read(1)
            data_file.seek(0x3C)
            back0 = data_file.read(1)
            data_file.seek(0x44)
            day0 = data_file.read(4)
            data_file.seek(0x48)
            km_trav = data_file.read(4)

            int_jack = int.from_bytes(jack0, byteorder="big")
            int_trou = int.from_bytes(trou0, byteorder="big")
            int_back = int.from_bytes(back0, byteorder="big")

            invert_day = day0[::-1]
            invert_km = km_trav[::-1]

            int_day = int.from_bytes(invert_day, byteorder="big")
            int_km = int.from_bytes(invert_km, byteorder="big")

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

            temperature = unpack('f', temp)[0]
            calc_temp = unpack('f', invert_temp)[0]

            with open(file_name, "rb") as file:
                file.seek(7)
                timestamp_bytes = file.read(5)

            reversed_bytes = timestamp_bytes[::-1]
            timestamp = int.from_bytes(reversed_bytes, byteorder='little')
            nintendo_epoch = datetime.datetime(2000, 1, 1)
            nintendo_timestamp = nintendo_epoch + datetime.timedelta(seconds=timestamp)
            unix_timestamp = int((nintendo_timestamp - datetime.datetime(1970, 1, 1)).total_seconds())
            date_time = datetime.datetime.fromtimestamp(unix_timestamp)

            formatted_date_time = date_time.strftime("%d/%m %H:%M")

            xyz_coord = [int_x, int_y, int_z]

            if cloth_dict[int(int_back)]:
                backpacks = f"{cloth_dict[int(int_back)]} Backpack"
            else:
                backpacks = "Corrupted Backpack"
            
            if cloth_dict[int(int_trou)]:
                trousers = f"{cloth_dict[int(int_trou)]} Trouser"
            else:
                trousers = "Corrupted Trouser"

            if cloth_dict[int(int_jack)]:
                jackets = f"{cloth_dict[int(int_jack)]} Jacket"
            else:
                jackets = "Corrupted Jacket"

            clothes = [jackets, backpacks, trousers]

            save_data[f"Data{file_index} File Information"] = {
                "Game Opened": open_byte == b'\x01',
                "Level Saved": save_byte >= b'\x01' and save_byte <= b'\xFF',
                "Four-Byte Time Hash": timestamp,
                "Converted Time Hash": formatted_date_time
            }

            save_data[f"Data{file_index} Player Information"] = {
                "Current Health": int_h,
                "Current Hunger": int_f,
                "Current Thirst": int_w,
                "Current Charge": int_b,
                "Days Passed": int_day,
                "Kilometers Traveled": int_km,
                "Wearing Jacket": jackets,
                "Wearing Backpack": backpacks,
                "Wearing Trouser": trousers,
                "Wearing Outfit": clothes,
                "X Coordinates": int_x,
                "Y Coordinates": int_y,
                "Z Coordinates": int_z,
                "X/Y/Z Coordinates": xyz_coord,
                "Current Temps": temperature,
                "Inverted Temp": calc_temp
            }

            for a in range(14):
                if a == 0:
                    offset = 0x23AF
                elif a == 1:
                    offset = 0x1347
                elif a == 2:
                    offset = 0x3D47
                elif a == 3:
                    offset = 0xDCF
                elif a == 4:
                    offset = 0x352F
                elif a == 5:
                    offset = 0x1857
                elif a == 6:
                    offset = 0x192F
                elif a == 7:
                    offset = 0x5EF
                elif a == 8:
                    offset = 0x1FF7
                elif a == 9:
                    offset = 0x2F47
                elif a == 10:
                    offset = 0x1CAF
                elif a == 11:
                    offset = 0x1CE7
                elif a == 12:
                    offset = 0x3F7
                elif a == 13:
                    offset = 0xB67


                data_file.seek(offset)
                heli0_y = data_file.read(4)
                data_file.seek(offset+0x04)
                heli0_z = data_file.read(4)
                data_file.seek(offset+0x08)
                heli0_x = data_file.read(4)

                invert_h0y = heli0_y[::-1]
                invert_h0z = heli0_z[::-1]
                invert_h0x = heli0_x[::-1]
                int_h0y = int.from_bytes(invert_h0y, byteorder='big')
                int_h0z = int.from_bytes(invert_h0z, byteorder='big')
                int_h0x = int.from_bytes(invert_h0x, byteorder='big')

                if int_h0y == 0:
                    int_h0y = None
                if int_h0z == 0:
                    int_h0z = None
                if int_h0x == 0:
                    int_h0x = None

                h0_lst = [int_h0x, int_h0y, int_h0z]
                
                heli_id = b'\x10\x40'

                HELI_INT = int.from_bytes(heli_id, byteorder='big')

                HELI_ID = '0x10, 0x40'

                if a == 0:
                    heli_name = f"Greybase Helicopter"

                if a == 1:
                    heli_name = f"3-Red-Houses Helicopter"

                if a == 2:
                    heli_name = f"Oil-Rig Helicopter"

                if a == 3:
                    heli_name = f"Submarine Cabins Snowcat"
                     
                if a == 4:
                    heli_name = f"Lost Research Cabin Snowcat"
                     
                if a == 5:
                    heli_name = f"Church Snowplough"
                     
                if a == 6:
                    heli_name = f"Lost Campsite Snowplough"
                     
                if a == 7:
                    heli_name = f"Island Cabin Snowmobile"
                     
                if a == 8:
                    heli_name = f"Lost Cabin Snowmobile"

                if a == 9:
                    heli_name = f"3-Lost-Cabins Dogsled"

                if a == 10:
                    heli_name = f"Lighthouse Dogsled"
                
                if a == 11:
                    heli_name = f"Lighthouse Boat"
                
                if a == 12:
                    heli_name = f"Island Cabin Boat"

                if a == 13:
                    heli_name = f"Submarine Cabin Boat"

                if a == 0:
                    save_data[f"Data{file_index} Heli #1 Information"] = {
                        "Helicopter Number": 1,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }

                if a == 1:
                    save_data[f"Data{file_index} Heli #2 Information"] = {
                        "Helicopter Number": 2,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }

                if a == 2:
                    save_data[f"Data{file_index} Heli #3 Information"] = {
                        "Helicopter Number": 3,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }
                
                if a == 3:
                    save_data[f"Data{file_index} Snowcat #1 Information"] = {
                        "Snowcat Number": 1,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }

                if a == 4:
                    save_data[f"Data{file_index} Snowcat #2 Information"] = {
                        "Snowcat Number": 2,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }

                if a == 5:
                    save_data[f"Data{file_index} Snowplough #1 Information"] = {
                        "Snowplough Number": 1,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }
                
                if a == 6:
                    save_data[f"Data{file_index} Snowplough #2 Information"] = {
                        "Snowplough Number": 2,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }

                if a == 7:
                    save_data[f"Data{file_index} Snowmobile #1 Information"] = {
                        "Snowmobile Number": 1,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }

                if a == 8:
                    save_data[f"Data{file_index} Snowmobile #2 Information"] = {
                        "Snowmobile Number": 2,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }
                if a == 9:
                    save_data[f"Data{file_index} Dogsled #1 Information"] = {
                        "Dogsled Number": 1,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }

                if a == 10:
                    save_data[f"Data{file_index} Dogsled #2 Information"] = {
                        "Dogsled Number": 2,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }
                
                if a == 11:
                    save_data[f"Data{file_index} Boat #1 Information"] = {
                        "Dogsled Number": 1,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }

                if a == 12:
                    save_data[f"Data{file_index} Boat #2 Information"] = {
                        "Dogsled Number": 2,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }
                
                if a == 13:
                    save_data[f"Data{file_index} Boat #3 Information"] = {
                        "Dogsled Number": 3,
                        "Vechile Name": heli_name,
                        "Vehicle Hex ID": HELI_ID,
                        "Vehicle Int ID": HELI_INT,
                        "X Coordinates": int_h0x,
                        "Y Coordinates": int_h0y,
                        "Z Coordinates": int_h0z,
                        "X/Y/Z Coordinates": h0_lst
                    }

            with open(file_name, "rb") as file:
                slot_info = []
                for i in range(1, 6):
                    num = 90 + (15 * i)

                    file.seek(num)
                    byte = file.read(1)

                    if byte >= b'\x48':
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
                        int_typ = 0xFF

                    else:
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

                    if int_typ == 0xFF:
                        int_typ = f"Invalid Item ID."


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
                        
                        if "Bandage" in data_dict[ord(byte)] or "Dressing" in data_dict[ord(byte)] or "Antibiotics" in data_dict[ord(byte)] or "Water" in data_dict[ord(byte)] or "Cake" in data_dict[ord(byte)] or "Cooked" in data_dict[ord(byte)] or "Beans" in data_dict[ord(byte)] or "Tuna" in data_dict[ord(byte)] or "Beef" in data_dict[ord(byte)] or "Antiseptic" in data_dict[ord(byte)] or "Snackbar" in data_dict[ord(byte)]:
                            int_typ = "Consumable"

                        if "Ammo" in data_dict[ord(byte)] or "Bolt" in data_dict[ord(byte)]:
                            int_typ = "Ammunition"

                        if "Tent" in data_dict[ord(byte)] or "Stove" in data_dict[ord(byte)] or "Part" in data_dict[ord(byte)] or "Fuel" in data_dict[ord(byte)] or "Logs" in data_dict[ord(byte)]:
                            int_typ = "Miscellaneous"

                        if "Snowboard" in data_dict[ord(byte)]:
                            int_typ = "Vehicle"

                    if int_typ == 1:
                        if "Shotgun" in data_dict[ord(byte)] or "Handgun" in data_dict[ord(byte)] or "Flame" in data_dict[ord(byte)] or "Trap" in data_dict[ord(byte)] or "Rifle" in data_dict[ord(byte)] or "Hunting" in data_dict[ord(byte)] or "Gun" in data_dict[ord(byte)] and "Ammo" not in data_dict[ord(byte)]:
                            int_typ = "Weapon"

                        if "Bandage" in data_dict[ord(byte)] or "Dressing" in data_dict[ord(byte)] or "Antibiotics" in data_dict[ord(byte)] or "Water" in data_dict[ord(byte)] or "Cake" in data_dict[ord(byte)] or "Cooked" in data_dict[ord(byte)] or "Beans" in data_dict[ord(byte)] or "Tuna" in data_dict[ord(byte)] or "Beef" in data_dict[ord(byte)] or "Antiseptic" in data_dict[ord(byte)] or "Snackbar" in data_dict[ord(byte)]:
                            int_typ = "Consumable"

                        if "Tent" in data_dict[ord(byte)] or "Stove" in data_dict[ord(byte)] or "Part" in data_dict[ord(byte)] or "Fuel" in data_dict[ord(byte)] or "Logs" in data_dict[ord(byte)]:
                            int_typ = "Miscellaneous"

                        if "Snowboard" in data_dict[ord(byte)]:
                            int_typ = "Vehicle"

                    if int_typ == 2:
                        if "Jacket" in data_dict[ord(byte)] or "Trousers" in data_dict[ord(byte)] or "Backpack" in data_dict[ord(byte)]:
                            int_typ = "Clothing"

                        if "Shotgun" in data_dict[ord(byte)] or "Handgun" in data_dict[ord(byte)] or "Flame" in data_dict[ord(byte)] or "Trap" in data_dict[ord(byte)] or "Rifle" in data_dict[ord(byte)] or "Hunting" in data_dict[ord(byte)] or "Crossbow" in data_dict[ord(byte)] and "Ammo" not in data_dict[ord(byte)]:
                            int_typ = "Weapon"
                        
                        if "Bandage" in data_dict[ord(byte)] or "Dressing" in data_dict[ord(byte)] or "Antibiotics" in data_dict[ord(byte)] or "Water" in data_dict[ord(byte)] or "Cake" in data_dict[ord(byte)] or "Cooked" in data_dict[ord(byte)] or "Beans" in data_dict[ord(byte)] or "Tuna" in data_dict[ord(byte)] or "Beef" in data_dict[ord(byte)] or "Antiseptic" in data_dict[ord(byte)] or "Snackbar" in data_dict[ord(byte)]:
                            int_typ = "Consumable"

                        if "Ammo" in data_dict[ord(byte)] or "Bolt" in data_dict[ord(byte)]:
                            int_typ = "Ammunition"

                        if "Tent" in data_dict[ord(byte)] or "Stove" in data_dict[ord(byte)] or "Part" in data_dict[ord(byte)] or "Fuel" in data_dict[ord(byte)] or "Logs" in data_dict[ord(byte)]:
                            int_typ = "Miscellaneous"

                        if "Snowboard" in data_dict[ord(byte)]:
                            int_typ = "Vehicle"
                    
                    if isinstance(int_typ, int):
                        int_typ = None
                    
                    save_data[f"Data{file_index} Slot #{i} Information"] = {
                        "Slot Number": i,
                        "Item Name": data_dict.get(ord(byte), None),
                        "Item Type": int_typ,
                        "Durability": int_dur,
                        "Duplicated": int_dup
                    }

        save_data_list.append(save_data)

    else:
        print(f"Save File: '{file_name}' does NOT exist.")
        print("Ignoring Error...\n")

with open('_ISZ-Save-Info.json', 'w') as json_file:
    dump(save_data_list, json_file, indent=4)

print("Data saved to '_ISZ-Save-Info.json'.")