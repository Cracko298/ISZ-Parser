#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <chrono>
#include <ctime>
#include <iomanip>

using namespace std;

map<uint8_t, string> data_dict = {
    {0x01, "Basic Handgun"},
    {0x02, "Arctic Handgun"},
    {0x03, "Arctic Eagle Handgun"},
    {0x04, "Double Barrel Shotgun"},
    {0x05, "Hunting Shotgun"},
    {0x06, "Arctic Hunting Shotgun"},
    {0x07, "Hunting Rifle"},
    {0x08, "Scout Hunting Rifle"},
    {0x09, "Arctic Hunting Rifle"},
    {0x0A, "Crossbow"},
    {0x0B, "Hunting Crossbow"},
    {0x0C, "Arctic Hunting Crossbow"},
    {0x0D, "Tranquilizer Gun"},
    {0x0E, "Hunting Knife"},
    {0x0F, "Pistol Ammo"},
    {0x10, "Shotgun Ammo"},
    {0x11, "Rifle Ammo"},
    {0x12, "Crossbow Bolts"},
    {0x13, "Tranquilizer Ammo"},
    {0x14, "Matches"},
    {0x15, "Fuel"},
    {0x16, "Binoculars"},
    {0x17, "Cooking Stove"},
    {0x18, "Bear Trap"},
    {0x19, "Fishing Rod"},
    {0x1A, "Field Binoculars"},
    {0x1B, "Professional Fishing Rod"},
    {0x1C, "Metal Detector"},
    {0x1D, "Water Bottle"},
    {0x1E, "Snackbar"},
    {0x1F, "Tuna"},
    {0x20, "Beans"},
    {0x21, "Corned Beef"},
    {0x22, "Large Water Bottle"},
    {0x23, "Mint Cake"},
    {0x24, "Antiseptic"},
    {0x25, "Antibiotics"},
    {0x26, "Bandage"},
    {0x27, "Dressing"},
    {0x28, "Large Bandage"},
    {0x29, "Large Dressing"},
    {0x2A, "Jacket"},
    {0x2B, "Trousers"},
    {0x2C, "Backpack"},
    {0x2D, "Cammo Jacket"},
    {0x2E, "Cammo Trousers"},
    {0x2F, "Cammo Backpack"},
    {0x30, "Military Jacket"},
    {0x31, "Military Trousers"},
    {0x32, "Military Backpack"},
    {0x33, "Kevlar Jacket"},
    {0x34, "Kevlar Trousers"},
    {0x35, "Kevlar Backpack"},
    {0x36, "Arctic Jacket"},
    {0x37, "Arctic Trousers"},
    {0x38, "Arctic Backpack"},
    {0x39, "Bling Jacket"},
    {0x3A, "Bling Trousers"},
    {0x3B, "Bling Backpack"},
    {0x3C, "Tent"},
    {0x3D, "Logs"},
    {0x3E, "Goose"},
    {0x3F, "Cooked Goose"},
    {0x40, "Minnow"},
    {0x41, "Large Fish"},
    {0x42, "Cooked Fish"},
    {0x43, "Engine Part"},
    {0x44, "Snowboard"},
    {0x45, "Flamethrower"},
    {0x46, "Ray Gun"},
    {0x47, "Flare Gun"}
};

template <typename T>
T reverse_bytes(const T& bytes) {
    T reversed_bytes = bytes;
    reverse(reversed_bytes.begin(), reversed_bytes.end());
    return reversed_bytes;
}

string formatted_time(uint32_t timestamp) {
    auto nintendo_epoch = chrono::system_clock::from_time_t(946684800); // Nintendo epoch (2000-01-01)
    auto nintendo_timestamp = nintendo_epoch + chrono::seconds(timestamp);
    auto unix_timestamp = chrono::system_clock::to_time_t(nintendo_timestamp);
    tm* time_info = gmtime(&unix_timestamp);
    stringstream ss;
    ss << setfill('0') << setw(2) << time_info->tm_mday << "/" << setw(2) << time_info->tm_mon + 1 << " " << setw(2) << time_info->tm_hour << ":" << setw(2) << time_info->tm_min;
    return ss.str();
}

int main() {
    vector<map<string, map<string, string>>> save_data_list;

    for (int file_index = 0; file_index < 3; ++file_index) {
        string file_name = "Data" + to_string(file_index);
        map<string, map<string, string>> save_data;

        ifstream data_file(file_name, ios::binary);

        if (data_file.good()) {
            uint8_t open_byte;
            data_file.seekg(0);
            data_file.read(reinterpret_cast<char*>(&open_byte), sizeof(open_byte));

            uint8_t save_byte;
            data_file.seekg(16);
            data_file.read(reinterpret_cast<char*>(&save_byte), sizeof(save_byte));

            uint32_t y, z, x, health, food, water, battery;
            data_file.seekg(20);
            data_file.read(reinterpret_cast<char*>(&y), sizeof(y));
            data_file.seekg(24);
            data_file.read(reinterpret_cast<char*>(&z), sizeof(z));
            data_file.seekg(28);
            data_file.read(reinterpret_cast<char*>(&x), sizeof(x));
            data_file.seekg(32);
            data_file.read(reinterpret_cast<char*>(&health), sizeof(health));
            data_file.seekg(36);
            data_file.read(reinterpret_cast<char*>(&food), sizeof(food));
            data_file.seekg(40);
            data_file.read(reinterpret_cast<char*>(&water), sizeof(water));
            data_file.seekg(48);
            data_file.read(reinterpret_cast<char*>(&battery), sizeof(battery));

            uint32_t int_y = reverse_bytes(y);
            uint32_t int_z = reverse_bytes(z);
            uint32_t int_x = reverse_bytes(x);

            uint32_t int_h = reverse_bytes(health);
            uint32_t int_f = reverse_bytes(food);
            uint32_t int_w = reverse_bytes(water);
            uint32_t int_b = reverse_bytes(battery);

            float temperature, calc_temp;
            data_file.seekg(44);
            data_file.read(reinterpret_cast<char*>(&temperature), sizeof(temperature));
            calc_temp = reverse_bytes(temperature);

            uint8_t timestamp_bytes[5];
            data_file.seekg(7);
            data_file.read(reinterpret_cast<char*>(timestamp_bytes), sizeof(timestamp_bytes));

            uint32_t timestamp = 0;
            for (int i = 0; i < 5; ++i) {
                timestamp |= (static_cast<uint32_t>(timestamp_bytes[i]) << (i * 8));
            }

            string formatted_date_time = formatted_time(timestamp);

            save_data["Data" + to_string(file_index) + " File Information"] = {
                {"Game Opened", open_byte == 0x01},
                {"Level Saved", (save_byte >= 0x01 && save_byte <= 0xFF)},
                {"Four-Byte Time Hash", to_string(timestamp)},
                {"Converted Time Hash", formatted_date_time}
            };

            map<string, string> player_info = {
                {"Current Health", to_string(int_h)},
                {"Current Hunger", to_string(int_f)},
                {"Current Thirst", to_string(int_w)},
                {"Current Charge", to_string(int_b)},
                {"Current Temps", to_string(temperature)},
                {"Inverted Temp", to_string(calc_temp)}
            };

            save_data["Data" + to_string(file_index) + " Player Information"] = player_info;

            map<string, map<string, string>> slot_info;
            for (int i = 1; i <= 5; ++i) {
                uint8_t byte;
                int num = 90 + (15 * i);
                data_file.seekg(num);
                data_file.read(reinterpret_cast<char*>(&byte), sizeof(byte));

                int durability = num + 1;
                int duplicity = num + 9;
                int item_type = num - 1;

                uint32_t num1, num2;
                data_file.seekg(durability);
                data_file.read(reinterpret_cast<char*>(&num1), sizeof(num1));
                data_file.seekg(duplicity);
                data_file.read(reinterpret_cast<char*>(&num2), sizeof(num2));

                uint8_t num3;
                data_file.seekg(item_type);
                data_file.read(reinterpret_cast<char*>(&num3), sizeof(num3));

                uint32_t int_dur = reverse_bytes(num1);
                uint32_t int_dup = reverse_bytes(num2);
                uint8_t int_typ = reverse_bytes(num3);

                string int_typ_str;
                if (int_typ == 3) {
                    if (data_dict[byte].find("Shotgun") != string::npos || data_dict[byte].find("Handgun") != string::npos ||
                        data_dict[byte].find("Flame") != string::npos || data_dict[byte].find("Trap") != string::npos ||
                        data_dict[byte].find("Rifle") != string::npos || data_dict[byte].find("Hunting") != string::npos ||
                        data_dict[byte].find("Gun") != string::npos) {
                        int_typ_str = "Weapon";
                    } else if (data_dict[byte].find("Bandage") != string::npos || data_dict[byte].find("Dressing") != string::npos ||
                               data_dict[byte].find("Antibiotics") != string::npos || data_dict[byte].find("Water") != string::npos ||
                               data_dict[byte].find("Cake") != string::npos || data_dict[byte].find("Cooked") != string::npos ||
                               data_dict[byte].find("Beans") != string::npos || data_dict[byte].find("Tuna") != string::npos ||
                               data_dict[byte].find("Beef") != string::npos || data_dict[byte].find("Antiseptic") != string::npos ||
                               data_dict[byte].find("Snackbar") != string::npos) {
                        int_typ_str = "Consumable";
                    } else if (data_dict[byte].find("Tent") != string::npos || data_dict[byte].find("Stove") != string::npos ||
                               data_dict[byte].find("Part") != string::npos || data_dict[byte].find("Fuel") != string::npos ||
                               data_dict[byte].find("Logs") != string::npos) {
                        int_typ_str = "Miscellaneous";
                    } else if (data_dict[byte] == "Snowboard") {
                        int_typ_str = "Vehicle";
                    }
                } else if (int_typ == 4) {
                    if (data_dict[byte].find("Jacket") != string::npos || data_dict[byte].find("Trousers") != string::npos ||
                        data_dict[byte].find("Backpack") != string::npos) {
                        int_typ_str = "Clothing";
                    } else if (data_dict[byte].find("Shotgun") != string::npos || data_dict[byte].find("Handgun") != string::npos ||
                               data_dict[byte].find("Flame") != string::npos || data_dict[byte].find("Trap") != string::npos ||
                               data_dict[byte].find("Rifle") != string::npos || data_dict[byte].find("Hunting") != string::npos ||
                               data_dict[byte].find("Crossbow") != string::npos) {
                        int_typ_str = "Weapon";
                    } else if (data_dict[byte].find("Ammo") != string::npos || data_dict[byte].find("Bolt") != string::npos) {
                        int_typ_str = "Ammunition";
                    } else if (data_dict[byte].find("Tent") != string::npos || data_dict[byte].find("Stove") != string::npos ||
                               data_dict[byte].find("Part") != string::npos || data_dict[byte].find("Fuel") != string::npos ||
                               data_dict[byte].find("Logs") != string::npos) {
                        int_typ_str = "Miscellaneous";
                    } else if (data_dict[byte] == "Snowboard") {
                        int_typ_str = "Vehicle";
                    }
                }

                map<string, string> slot_data = {
                    {"Slot Number", to_string(i)},
                    {"Item Name", data_dict.find(byte) != data_dict.end() ? data_dict[byte] : "Unknown Item (" + to_string(byte) + ")"},
                    {"Item Type", int_typ_str},
                    {"Durability", to_string(int_dur)},
                    {"Duplicated", to_string(int_dup)}
                };

                slot_info["Data" + to_string(file_index) + " Slot" + to_string(i) + " Information"] = slot_data;
            }

            save_data["Data" + to_string(file_index) + " Slot Information"] = slot_info;
            save_data_list.push_back(save_data);
        }

        data_file.close();
    }

    ofstream json_file("_ISZ-Save-Info.json");
    json_file << "{\n";
    for (size_t i = 0; i < save_data_list.size(); ++i) {
        json_file << "  \"Save" << i << "\": {\n";
        for (auto it = save_data_list[i].begin(); it != save_data_list[i].end(); ++it) {
            json_file << "    \"" << it->first << "\": {\n";
            for (auto inner_it = it->second.begin(); inner_it != it->second.end(); ++inner_it) {
                json_file << "      \"" << inner_it->first << "\": \"" << inner_it->second << "\"";
                if (next(inner_it) != it->second.end()) {
                    json_file << ",";
                }
                json_file << "\n";
            }
            json_file << "    }";
            if (next(it) != save_data_list[i].end()) {
                json_file << ",";
            }
            json_file << "\n";
        }
        json_file << "  }";
        if (i != save_data_list.size() - 1) {
            json_file << ",";
        }
        json_file << "\n";
    }
    json_file << "}\n";
    json_file.close();

    cout << "Data saved to '_ISZ-Save-Info.json'." << endl;

    return 0;
}
