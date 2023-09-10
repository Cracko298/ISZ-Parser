# ISZ-Parser
- Parses Ice station Z Save-Data into The *.json Human Readable Format.

# Downloads:
- Download Source [Here]().
- Download Compiled [Here]().

## Usage:
- Drag and drop Decrypted ISZ-3DS Save-Files.
- Double click the .py or compiled .exe File.
- Generates Information based on your Provided Save-Files.

## Building:
### Python Script:
```
> pyinstaller -F --strip --exclude-module numpy --exclude-module opencv --exclude-module cv2 --onefile "isz-parse.py" --icon="icon.ico"
```
### C++ Code:
```
> g++ -o ISZparse.exe -O3 -s isz-parse.cpp
```
