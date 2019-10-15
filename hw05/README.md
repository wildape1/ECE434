# Homework 5

## Project

Leela and I are planning on doing Object Recognition.  We are going to use tensorflow and OpenCV to detect and track items using a camera.


## Make
1. Target = app.o
2. Dependency = app.c 
3. Command =  gcc

-c creates -o file without invoking the linker

Makefile made by following exercise 15 in ./Makefile/

## Installing Kernel Source
Installed the 4.18 version of the kernel due to continual errors while trying with the 4.19 version

## Cross-Compiling
Output on host: 

    Hello, World! Main is executing at 0x56215b9ce6aa 
    This address (0x7ffc19762c50) is in our stack frame 
    This address (0x56215bbcf018) is in our bss section 
    This address (0x56215bbcf010) is in our data section 

Output on bone: 

    Hello, World! Main is executing at 0x4545ad 
    This address (0xbe903c48) is in our stack frame 
    This address (0x465010) is in our bss section 
    This address (0x465008) is in our data section
