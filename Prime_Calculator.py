#!/usr/bin/env python
##################################################
## Basic Prime Numbers Range Calculator
##################################################
## Version: 1.0
## Maintainer: Jose
## Email: jose_vila@icloud.com
##################################################

low = 261
high = 273

print("The prime numbers from", low, "and", high, "are:")

for num in range(low, high + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
