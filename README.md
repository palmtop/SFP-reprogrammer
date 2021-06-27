# SFP-reprogrammer

Some time ago I bought an Aruba S2500 siwtch for ~ 50 USD + 70 USD shipping cost, because in the forums I have read, that it is very silent and it is compatioble with almost any 10G SFP. After long waiting the switch arrived, and it tured out, that it is not that silent and none of my 4 SFPs available at home works with it :-(.

Aftre a lot of search and experimenting I learned that most of the SFPs can be reprogrammed and the Aruba switch only cares about the modell number, so if I change the modell number to an appropriate one, the switch will accept the SFP.

There are ready products fro SFP programming, but for my case with a few $20 SFP-s it was not worth buying a $300 programmer, even if that price is not high at all.

Finaly my starting point was this article: https://eoinpk.blogspot.com/2014/05/raspberry-pi-and-programming-eeproms-on.html

I had an Orange Pi Lite and later an Oprange Pi 3 so I had to change the programs a bit.

Here is what I did:

1. I had a Mellanox MNPA29-XTR card, where on the card there are pads for SCL and SDA connections needed for the I2C connection to the eprom.
2. I soldered cables here and connected to the orange pi I2C pins
3. Installed standard Armbian operating system
4. I enabled the i2c0 hardware using armbian-config
5. I have added the following packages sudo apt install i2c-tools python-smbus (python3-smbus) (Orange Pi 3 needed phyton3-smbus)
6. I have put the card in a computer (wich supplied power to the card) and then I could read the card.
7. sudo i2cdump -y 0 0x50 i - dumps the content of the main eeprom
8. sudo i2cset -y 0 0x50 0x34 0x20 - writes 0x20 to address 0x34
9. I did not write a program to read and save the eprom content to a binary file, instead I used https://tomeko.net/online_tools/hex_to_file.php?lang=en to convert from the hexdump to a binary file
10. If you update the ROM, you need to recalculate the checksums at position 0x3F and 0x5F, the program calculate_spf_CC_BASE.py does this.
11. The program write_i2c_file.py writes a binary file to the SFP
12. Some SFP-s are password protected, so before modifying it you have to set the password:
```
passwd = [ 0x9b, 0xb0, 0x3d, 0xfa]
import smbus
bus = smbus.SMBus(0)
bus.write_i2c_block_data(81,123,passwd)
```
13. There are some SFPs (e.g. fs.com) which can be programmed without password. There are some SFPs (e.g. Optcore) where the wendor send you the password, if you asks for it. I have seen a DAC cable, which seemd not to have an eeprom at all. And if you don't have the password, you can try to crack is, with brute force, this is what check_password.py is doing. 
14. To speed up the password cracking, you can increase the speed of the i2c bus, you can do this by creating an overlay device tree. I was sucessfull with it, and setting the clock to 1 M, I could reach 9000 test/second speed.
15. These programs are not ready for use programs, they are rather small snipletts, you have to customise to reach your goals.
16. https://sfpdb.freetime.su/ is a good place to find SFP eeproms and italso helps to decode eeprom contents
