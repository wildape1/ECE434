# Homework 4

## Memory Mapping

|                |Start Address                  |End Address                  |
|----------------|-------------------------------|-----------------------------|
|EMIF0   |0x4C00_0000 |0x4CFF_FFFF|
|SDRAM   |0x420F_0400 |0x402F_FFFF|
|GPIO_0  |0x44E0_7000 |0x44E0_7FFF|
|GPIO_1  |0x4804_C000 |0x481A_CFFF|
|GPIO_2  |0x481A_C000 |0x481A_CFFF|
|GPIO_3  |0x481A_E000 |0x481A_EFFF|


## Mmap gpio

mmap_buttons.c is my c file for controlling two LEDs on the bone with 2 buttons using mmap.  The file was complied with a headerfile beaglebone_gpio.h to make the file mmap_buttons 

## Images

 - The rotated image of boris is called boris90.png
 - The image with text overlayed is called boris90withtext.png

## Toggle gpio

0.55ms delay in toggling the LED.  This is much less delay/overhead than the methods in homework 2 assignment
Removing usleep call, the delay dropped to ~23 microseconds, however program would not stop anymore.

## Prof. Yoder's comments

Need to start

Grade:  0/10
