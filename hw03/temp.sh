#!/bin/sh
temp=$(i2cget -y 2 0x48 0)
temp=$(($temp * 1))
temp2=$(($temp * 2 + 32))
echo "Celcius: " $temp
echo "Farhenheit : " $temp2
i2cset -y 2 0x48 2 70
i2cset -y 2 0x48 3 85
Tlow=$(i2cget -y 2 0x48 2)
Thigh=$(i2cget -y 2 0x48 3)
Tlow=$((Tlow))
Thigh=$((Thigh))
echo $Tlow
echo $Thigh
