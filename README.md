# Ascii art to Ducky script
A python script which prints ascii art .txt file to a ducky script!

<p align=center>
<img src="https://user-images.githubusercontent.com/110339660/198846157-f30d1eca-4ae7-4782-95cc-ad51720f0d49.png" width="500" />
</p>

This *cute* image was generated with [__DALL·E 2__](https://openai.com/dall-e-2/)

## WHY?
I really love these ascii arts and since I have a Flipper Zero I really like BadUSB app on this but it's really hard to paste at the begin of every line 
```
STRING ...
ENTER
```
soo I created this little Python script to make it easier.

## What it does?
Converts a **.txt** file to another **.txt** file but the new one can be read by a Ducky Script runnable device (like Flipper Zero)
First the created script will open the notepad from the *Win*+*r* Run menu
Secondly prints your ascii art to the screen
Thirdly it will save the printed file to .txt to the user's last used folder if you pressed either *"Y"* or *"y"* or typed either *"Yes"* or *"YES"* or *"yes"* when it was asked.

## Usage
Simple download and execute the ``ascii-to-badusb.py`` file from this repo and the script will say what to do.

### More advanced
1. Open a terminal
2. Type ``git clone https://github.com/ut1s/ascii-art-to-duck-script/`` then enter
3. Wait until git downloads it

((3.1 If you don't have **git** on your computer as the terminal says: ``'git' is not recognized as an internal or external command,
operable program or batch file.`` or ``git: command not found`` (although git is a must have in terminals...) then try to insall it or download it from the browser in which you are surfing the internet right now too...))

4. Type ``cd ascii-art-to-ducky-script``
5. Type ``python`` (/or ``python3``) `` ascii-to-badusb.py``
6. Type the name of that ``.txt`` file which contains and only contains the ascii art you want to convert without the **.txt** extension
7. Type then *"Y"* if you want from the script to save your ascii art to ``.txt`` to the user's computer or type *"N"* if you don't want this feature
8. Wait a little bit
9. Be happy! Your file is done! Now you'll just have to upload it to your device and run!

## For Flipper Zero
The text file's EOL (End iof line) will be on **Windows system** with *CRL* on **Linux** it will be *LF*. I can just guess why is this so but if you're using Windows not any of Linux distribution it will work perfectly. I think it's due to in Python the endings of the lines is with ``\n`` so Flipper Zero can easily handle it. Or there was a big update which I missed and can handle the CRLF EOL files 😅🙁

By the way I have an own sadly-not-always-updating [GitHub repository](https://github.com/ut1s/flipperzero-firmware) so check it out!
It has some little changes like my own animation or I added some applications and features to the [official firmware](https://github.com/flipperdevices/flipperzero-firmware) from some unofficial firmware (eg. Unleased, RogueMaster) but without any (big) graphical changes (except my little DJ animation but this is so cute...).
The link once again to check it out:
[ut1s's Flipper Zero firmware](https://github.com/ut1s/flipperzero-firmware)

## EDIT
I added a lot of debug to the code so if the *Dear user* (this is you) types something which would make an error the program handles it and asks the *User* to try again the input :)
