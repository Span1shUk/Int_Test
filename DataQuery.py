#!/usr/bin/env python
##################################################
## Basic Prime Numbers Range Calculator
##################################################
## Version: 1.0
## Maintainer: Jose
## Email: jose_vila@icloud.com
##################################################
temp = 'XY 77822 Capital 4343 Ltd 169'
data = [x for x in (int(x) for x in temp if x.isdigit()) if x%2 == 0] 
print (data)
