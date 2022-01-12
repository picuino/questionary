EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 8268 11693 portrait
encoding utf-8
Sheet 1 1
Title "Circuitos digitales para Questionary"
Date "16/02/2021"
Rev ""
Comp "www.picuino.com"
Comment1 "Copyright (c) 2021 by Carlos Pardo"
Comment2 "License CC BY-SA 4.0"
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L simbolos:CopyRight CP?
U 1 1 602E50E7
P 3775 11500
AR Path="/602E50E7" Ref="CP?"  Part="1" 
AR Path="/5C6CFC33/602E50E7" Ref="CP?"  Part="1" 
F 0 "CP?" H 4200 11825 40  0001 C CNN
F 1 "CopyRight" H 3950 11825 40  0001 C CNN
F 2 "" H 3675 11850 50  0001 C CNN
F 3 "" H 3775 11700 50  0001 C CNN
F 4 "CC BY-SA 4.0" H 3775 11450 50  0000 C CNN "License"
F 5 "" H 4350 11425 50  0000 C CNN "Author"
F 6 "" H 3875 11425 50  0000 C CNN "Date"
F 7 "www.picuino.com" H 4525 11450 50  0000 C CNN "Web"
	1    3775 11500
	1    0    0    -1  
$EndComp
Wire Notes Line
	4150 200  4150 11450
Wire Notes Line
	200  200  8100 200 
Wire Notes Line
	200  2075 8100 2075
Wire Notes Line
	8100 3950 200  3950
Wire Notes Line
	200  5825 8100 5825
Wire Notes Line
	8100 7700 200  7700
Wire Notes Line
	200  9575 8100 9575
Wire Notes Line
	8100 11450 200  11450
Wire Notes Line
	200  11450 200  200 
Wire Notes Line
	8100 200  8100 11450
Text Notes -650 1150 0    300  ~ 0
1\n
Text Notes -650 3175 0    300  ~ 0
2\n
Text Notes 8525 1275 0    300  ~ 0
7\n
Text Notes 8500 3000 0    300  ~ 0
8\n
$Comp
L simbolos:NPN Q?
U 1 1 6031030F
P 2000 950
F 0 "Q?" H 2354 750 100 0001 L CNN
F 1 "NPN" H 1925 650 50  0001 C CNN
F 2 "" H 2100 750 50  0001 C CNN
F 3 "" H 2100 750 50  0001 C CNN
	1    2000 950 
	1    0    0    -1  
$EndComp
$Comp
L simbolos:NPN Q?
U 1 1 60310CDD
P 2000 550
F 0 "Q?" H 2354 350 100 0001 L CNN
F 1 "NPN" H 1925 250 50  0001 C CNN
F 2 "" H 2100 350 50  0001 C CNN
F 3 "" H 2100 350 50  0001 C CNN
	1    2000 550 
	1    0    0    -1  
$EndComp
$Comp
L simbolos:resistencia R?
U 1 1 603113AE
P 1900 750
F 0 "R?" V 1734 550 100 0001 C CNN
F 1 "10k" V 1734 550 100 0000 C CNN
F 2 "" H 2000 650 50  0001 C CNN
F 3 "" H 2000 650 50  0001 C CNN
	1    1900 750 
	0    1    1    0   
$EndComp
$Comp
L simbolos:conector o?
U 1 1 60312126
P 2250 450
F 0 "o?" H 2400 300 100 0001 C CNN
F 1 "5V" V 2312 382 100 0000 R CNN
F 2 "" H 2375 450 50  0001 C CNN
F 3 "" H 2375 450 50  0001 C CNN
	1    2250 450 
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2250 450  2250 550 
$Comp
L simbolos:resistencia R?
U 1 1 6031341D
P 1900 1150
F 0 "R?" V 1734 950 100 0001 C CNN
F 1 "10k" V 1734 950 100 0000 C CNN
F 2 "" H 2000 1050 50  0001 C CNN
F 3 "" H 2000 1050 50  0001 C CNN
	1    1900 1150
	0    1    1    0   
$EndComp
Wire Wire Line
	1900 750  2000 750 
Wire Wire Line
	1900 1150 2000 1150
$Comp
L simbolos:conector o?
U 1 1 60313CED
P 1400 750
F 0 "o?" H 1550 600 100 0001 C CNN
F 1 "A" H 1625 750 100 0000 C CNN
F 2 "" H 1525 750 50  0001 C CNN
F 3 "" H 1525 750 50  0001 C CNN
	1    1400 750 
	-1   0    0    1   
$EndComp
Wire Wire Line
	1400 750  1500 750 
$Comp
L simbolos:conector o?
U 1 1 60314334
P 1400 1150
F 0 "o?" H 1550 1000 100 0001 C CNN
F 1 "B" H 1625 1150 100 0000 C CNN
F 2 "" H 1525 1150 50  0001 C CNN
F 3 "" H 1525 1150 50  0001 C CNN
	1    1400 1150
	-1   0    0    1   
$EndComp
Wire Wire Line
	1400 1150 1500 1150
$Comp
L simbolos:resistencia R?
U 1 1 60314734
P 2250 1750
F 0 "R?" V 2084 1550 100 0001 C CNN
F 1 "2k" H 2168 1550 100 0000 R CNN
F 2 "" H 2350 1650 50  0001 C CNN
F 3 "" H 2350 1650 50  0001 C CNN
	1    2250 1750
	-1   0    0    1   
$EndComp
$Comp
L simbolos:tierra V?
U 1 1 60314F8B
P 2250 1750
F 0 "V?" H 2275 1725 100 0001 L CNN
F 1 "tierra" H 2125 1725 50  0001 C CNN
F 2 "" H 2550 1600 50  0001 C CNN
F 3 "" H 2550 1600 50  0001 C CNN
	1    2250 1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	2250 1350 2875 1350
Connection ~ 2250 1350
$Comp
L simbolos:conector o?
U 1 1 60317036
P 2875 1350
F 0 "o?" H 3025 1200 100 0001 C CNN
F 1 "Salida" H 3275 1350 100 0000 C CNN
F 2 "" H 3000 1350 50  0001 C CNN
F 3 "" H 3000 1350 50  0001 C CNN
	1    2875 1350
	1    0    0    -1  
$EndComp
$Comp
L simbolos:NPN Q?
U 1 1 6031B29B
P 2500 2650
F 0 "Q?" H 2854 2450 100 0001 L CNN
F 1 "NPN" H 2425 2350 50  0001 C CNN
F 2 "" H 2600 2450 50  0001 C CNN
F 3 "" H 2600 2450 50  0001 C CNN
	1    2500 2650
	1    0    0    -1  
$EndComp
$Comp
L simbolos:NPN Q?
U 1 1 6031B2A1
P 1250 2625
F 0 "Q?" H 1604 2425 100 0001 L CNN
F 1 "NPN" H 1175 2325 50  0001 C CNN
F 2 "" H 1350 2425 50  0001 C CNN
F 3 "" H 1350 2425 50  0001 C CNN
	1    1250 2625
	1    0    0    -1  
$EndComp
$Comp
L simbolos:resistencia R?
U 1 1 6031B2A7
P 1150 2825
F 0 "R?" V 984 2625 100 0001 C CNN
F 1 "10k" V 984 2625 100 0000 C CNN
F 2 "" H 1250 2725 50  0001 C CNN
F 3 "" H 1250 2725 50  0001 C CNN
	1    1150 2825
	0    1    1    0   
$EndComp
$Comp
L simbolos:conector o?
U 1 1 6031B2AD
P 2750 2375
F 0 "o?" H 2900 2225 100 0001 C CNN
F 1 "5V" V 2812 2307 100 0000 R CNN
F 2 "" H 2875 2375 50  0001 C CNN
F 3 "" H 2875 2375 50  0001 C CNN
	1    2750 2375
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1500 2475 1500 2625
$Comp
L simbolos:resistencia R?
U 1 1 6031B2B4
P 2400 2850
F 0 "R?" V 2234 2650 100 0001 C CNN
F 1 "10k" V 2234 2650 100 0000 C CNN
F 2 "" H 2500 2750 50  0001 C CNN
F 3 "" H 2500 2750 50  0001 C CNN
	1    2400 2850
	0    1    1    0   
$EndComp
Wire Wire Line
	1150 2825 1250 2825
Wire Wire Line
	2400 2850 2500 2850
$Comp
L simbolos:conector o?
U 1 1 6031B2BC
P 675 2825
F 0 "o?" H 825 2675 100 0001 C CNN
F 1 "A" H 900 2825 100 0000 C CNN
F 2 "" H 800 2825 50  0001 C CNN
F 3 "" H 800 2825 50  0001 C CNN
	1    675  2825
	-1   0    0    1   
$EndComp
Wire Wire Line
	675  2825 750  2825
$Comp
L simbolos:conector o?
U 1 1 6031B2C3
P 1900 2850
F 0 "o?" H 2050 2700 100 0001 C CNN
F 1 "B" H 2125 2850 100 0000 C CNN
F 2 "" H 2025 2850 50  0001 C CNN
F 3 "" H 2025 2850 50  0001 C CNN
	1    1900 2850
	-1   0    0    1   
$EndComp
Wire Wire Line
	1900 2850 2000 2850
$Comp
L simbolos:resistencia R?
U 1 1 6031B2CA
P 2750 3675
F 0 "R?" V 2584 3475 100 0001 C CNN
F 1 "2k" H 2668 3475 100 0000 R CNN
F 2 "" H 2850 3575 50  0001 C CNN
F 3 "" H 2850 3575 50  0001 C CNN
	1    2750 3675
	-1   0    0    1   
$EndComp
$Comp
L simbolos:tierra V?
U 1 1 6031B2D0
P 2750 3675
F 0 "V?" H 2775 3650 100 0001 L CNN
F 1 "tierra" H 2625 3650 50  0001 C CNN
F 2 "" H 3050 3525 50  0001 C CNN
F 3 "" H 3050 3525 50  0001 C CNN
	1    2750 3675
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 3275 3375 3275
Connection ~ 2750 3275
$Comp
L simbolos:conector o?
U 1 1 6031B2D8
P 3375 3275
F 0 "o?" H 3525 3125 100 0001 C CNN
F 1 "Salida" H 3775 3275 100 0000 C CNN
F 2 "" H 3500 3275 50  0001 C CNN
F 3 "" H 3500 3275 50  0001 C CNN
	1    3375 3275
	1    0    0    -1  
$EndComp
Wire Wire Line
	1500 3275 2750 3275
Wire Wire Line
	1500 3025 1500 3275
Wire Wire Line
	2750 3050 2750 3275
Wire Wire Line
	1500 2475 2750 2475
Wire Wire Line
	2750 2475 2750 2650
Wire Wire Line
	2750 2375 2750 2475
Connection ~ 2750 2475
$Comp
L simbolos:NPN Q?
U 1 1 603235C8
P 2000 5150
F 0 "Q?" H 2354 4950 100 0001 L CNN
F 1 "NPN" H 1925 4850 50  0001 C CNN
F 2 "" H 2100 4950 50  0001 C CNN
F 3 "" H 2100 4950 50  0001 C CNN
	1    2000 5150
	1    0    0    -1  
$EndComp
$Comp
L simbolos:NPN Q?
U 1 1 6032371A
P 2000 4750
F 0 "Q?" H 2354 4550 100 0001 L CNN
F 1 "NPN" H 1925 4450 50  0001 C CNN
F 2 "" H 2100 4550 50  0001 C CNN
F 3 "" H 2100 4550 50  0001 C CNN
	1    2000 4750
	1    0    0    -1  
$EndComp
$Comp
L simbolos:resistencia R?
U 1 1 60323724
P 1900 4950
F 0 "R?" V 1734 4750 100 0001 C CNN
F 1 "10k" V 1734 4750 100 0000 C CNN
F 2 "" H 2000 4850 50  0001 C CNN
F 3 "" H 2000 4850 50  0001 C CNN
	1    1900 4950
	0    1    1    0   
$EndComp
$Comp
L simbolos:conector o?
U 1 1 6032372E
P 2250 4250
F 0 "o?" H 2400 4100 100 0001 C CNN
F 1 "5V" V 2312 4182 100 0000 R CNN
F 2 "" H 2375 4250 50  0001 C CNN
F 3 "" H 2375 4250 50  0001 C CNN
	1    2250 4250
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2250 4250 2250 4350
$Comp
L simbolos:resistencia R?
U 1 1 60323739
P 1900 5350
F 0 "R?" V 1734 5150 100 0001 C CNN
F 1 "10k" V 1734 5150 100 0000 C CNN
F 2 "" H 2000 5250 50  0001 C CNN
F 3 "" H 2000 5250 50  0001 C CNN
	1    1900 5350
	0    1    1    0   
$EndComp
Wire Wire Line
	1900 4950 2000 4950
Wire Wire Line
	1900 5350 2000 5350
$Comp
L simbolos:conector o?
U 1 1 60323745
P 1400 4950
F 0 "o?" H 1550 4800 100 0001 C CNN
F 1 "A" H 1625 4950 100 0000 C CNN
F 2 "" H 1525 4950 50  0001 C CNN
F 3 "" H 1525 4950 50  0001 C CNN
	1    1400 4950
	-1   0    0    1   
$EndComp
Wire Wire Line
	1400 4950 1500 4950
$Comp
L simbolos:conector o?
U 1 1 60323750
P 1400 5350
F 0 "o?" H 1550 5200 100 0001 C CNN
F 1 "B" H 1625 5350 100 0000 C CNN
F 2 "" H 1525 5350 50  0001 C CNN
F 3 "" H 1525 5350 50  0001 C CNN
	1    1400 5350
	-1   0    0    1   
$EndComp
Wire Wire Line
	1400 5350 1500 5350
$Comp
L simbolos:resistencia R?
U 1 1 6032375B
P 2250 4750
F 0 "R?" V 2084 4550 100 0001 C CNN
F 1 "2k" H 2168 4550 100 0000 R CNN
F 2 "" H 2350 4650 50  0001 C CNN
F 3 "" H 2350 4650 50  0001 C CNN
	1    2250 4750
	-1   0    0    1   
$EndComp
$Comp
L simbolos:tierra V?
U 1 1 60323765
P 2250 5550
F 0 "V?" H 2275 5525 100 0001 L CNN
F 1 "tierra" H 2125 5525 50  0001 C CNN
F 2 "" H 2550 5400 50  0001 C CNN
F 3 "" H 2550 5400 50  0001 C CNN
	1    2250 5550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2250 4750 2875 4750
$Comp
L simbolos:conector o?
U 1 1 60323771
P 2875 4750
F 0 "o?" H 3025 4600 100 0001 C CNN
F 1 "Salida" H 3275 4750 100 0000 C CNN
F 2 "" H 3000 4750 50  0001 C CNN
F 3 "" H 3000 4750 50  0001 C CNN
	1    2875 4750
	1    0    0    -1  
$EndComp
Connection ~ 2250 4750
$Comp
L simbolos:NPN Q?
U 1 1 6033219A
P 2475 6825
F 0 "Q?" H 2829 6625 100 0001 L CNN
F 1 "NPN" H 2400 6525 50  0001 C CNN
F 2 "" H 2575 6625 50  0001 C CNN
F 3 "" H 2575 6625 50  0001 C CNN
	1    2475 6825
	1    0    0    -1  
$EndComp
$Comp
L simbolos:NPN Q?
U 1 1 603321A0
P 1225 6800
F 0 "Q?" H 1579 6600 100 0001 L CNN
F 1 "NPN" H 1150 6500 50  0001 C CNN
F 2 "" H 1325 6600 50  0001 C CNN
F 3 "" H 1325 6600 50  0001 C CNN
	1    1225 6800
	1    0    0    -1  
$EndComp
$Comp
L simbolos:resistencia R?
U 1 1 603321A6
P 1125 7000
F 0 "R?" V 959 6800 100 0001 C CNN
F 1 "10k" V 959 6800 100 0000 C CNN
F 2 "" H 1225 6900 50  0001 C CNN
F 3 "" H 1225 6900 50  0001 C CNN
	1    1125 7000
	0    1    1    0   
$EndComp
$Comp
L simbolos:conector o?
U 1 1 603321AC
P 2725 6100
F 0 "o?" H 2875 5950 100 0001 C CNN
F 1 "5V" V 2787 6032 100 0000 R CNN
F 2 "" H 2850 6100 50  0001 C CNN
F 3 "" H 2850 6100 50  0001 C CNN
	1    2725 6100
	0    -1   -1   0   
$EndComp
$Comp
L simbolos:resistencia R?
U 1 1 603321B3
P 2375 7025
F 0 "R?" V 2209 6825 100 0001 C CNN
F 1 "10k" V 2209 6825 100 0000 C CNN
F 2 "" H 2475 6925 50  0001 C CNN
F 3 "" H 2475 6925 50  0001 C CNN
	1    2375 7025
	0    1    1    0   
$EndComp
Wire Wire Line
	1125 7000 1225 7000
Wire Wire Line
	2375 7025 2475 7025
$Comp
L simbolos:conector o?
U 1 1 603321BB
P 650 7000
F 0 "o?" H 800 6850 100 0001 C CNN
F 1 "A" H 875 7000 100 0000 C CNN
F 2 "" H 775 7000 50  0001 C CNN
F 3 "" H 775 7000 50  0001 C CNN
	1    650  7000
	-1   0    0    1   
$EndComp
Wire Wire Line
	650  7000 725  7000
$Comp
L simbolos:conector o?
U 1 1 603321C2
P 1875 7025
F 0 "o?" H 2025 6875 100 0001 C CNN
F 1 "B" H 2100 7025 100 0000 C CNN
F 2 "" H 2000 7025 50  0001 C CNN
F 3 "" H 2000 7025 50  0001 C CNN
	1    1875 7025
	-1   0    0    1   
$EndComp
Wire Wire Line
	1875 7025 1975 7025
$Comp
L simbolos:resistencia R?
U 1 1 603321C9
P 2725 6600
F 0 "R?" V 2559 6400 100 0001 C CNN
F 1 "2k" H 2643 6400 100 0000 R CNN
F 2 "" H 2825 6500 50  0001 C CNN
F 3 "" H 2825 6500 50  0001 C CNN
	1    2725 6600
	-1   0    0    1   
$EndComp
$Comp
L simbolos:tierra V?
U 1 1 603321CF
P 2725 7400
F 0 "V?" H 2750 7375 100 0001 L CNN
F 1 "tierra" H 2600 7375 50  0001 C CNN
F 2 "" H 3025 7250 50  0001 C CNN
F 3 "" H 3025 7250 50  0001 C CNN
	1    2725 7400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2725 6700 3350 6700
$Comp
L simbolos:conector o?
U 1 1 603321D7
P 3350 6700
F 0 "o?" H 3500 6550 100 0001 C CNN
F 1 "Salida" H 3750 6700 100 0000 C CNN
F 2 "" H 3475 6700 50  0001 C CNN
F 3 "" H 3475 6700 50  0001 C CNN
	1    3350 6700
	1    0    0    -1  
$EndComp
Wire Wire Line
	1475 7300 2725 7300
Wire Wire Line
	1475 7200 1475 7300
Wire Wire Line
	2725 7225 2725 7300
Wire Wire Line
	2725 7300 2725 7400
Connection ~ 2725 7300
Wire Wire Line
	2725 6700 2725 6825
Wire Wire Line
	2725 6700 1475 6700
Wire Wire Line
	1475 6700 1475 6800
Wire Wire Line
	2725 6100 2725 6200
Wire Wire Line
	2725 6700 2725 6600
Connection ~ 2725 6700
$Comp
L simbolos:NPN Q?
U 1 1 603407C4
P 2500 8700
F 0 "Q?" H 2854 8500 100 0001 L CNN
F 1 "NPN" H 2425 8400 50  0001 C CNN
F 2 "" H 2600 8500 50  0001 C CNN
F 3 "" H 2600 8500 50  0001 C CNN
	1    2500 8700
	1    0    0    -1  
$EndComp
$Comp
L simbolos:conector o?
U 1 1 603407D0
P 2750 7975
F 0 "o?" H 2900 7825 100 0001 C CNN
F 1 "5V" V 2812 7907 100 0000 R CNN
F 2 "" H 2875 7975 50  0001 C CNN
F 3 "" H 2875 7975 50  0001 C CNN
	1    2750 7975
	0    -1   -1   0   
$EndComp
$Comp
L simbolos:resistencia R?
U 1 1 603407D6
P 2400 8900
F 0 "R?" V 2234 8700 100 0001 C CNN
F 1 "10k" V 2234 8700 100 0000 C CNN
F 2 "" H 2500 8800 50  0001 C CNN
F 3 "" H 2500 8800 50  0001 C CNN
	1    2400 8900
	0    1    1    0   
$EndComp
Wire Wire Line
	2400 8900 2500 8900
$Comp
L simbolos:conector o?
U 1 1 603407DD
P 1900 8900
F 0 "o?" H 2050 8750 100 0001 C CNN
F 1 "A" H 2125 8900 100 0000 C CNN
F 2 "" H 2025 8900 50  0001 C CNN
F 3 "" H 2025 8900 50  0001 C CNN
	1    1900 8900
	-1   0    0    1   
$EndComp
Wire Wire Line
	1900 8900 2000 8900
$Comp
L simbolos:resistencia R?
U 1 1 603407E4
P 2750 8475
F 0 "R?" V 2584 8275 100 0001 C CNN
F 1 "2k" H 2668 8275 100 0000 R CNN
F 2 "" H 2850 8375 50  0001 C CNN
F 3 "" H 2850 8375 50  0001 C CNN
	1    2750 8475
	-1   0    0    1   
$EndComp
$Comp
L simbolos:tierra V?
U 1 1 603407EA
P 2750 9275
F 0 "V?" H 2775 9250 100 0001 L CNN
F 1 "tierra" H 2625 9250 50  0001 C CNN
F 2 "" H 3050 9125 50  0001 C CNN
F 3 "" H 3050 9125 50  0001 C CNN
	1    2750 9275
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 8575 3375 8575
$Comp
L simbolos:conector o?
U 1 1 603407F1
P 3375 8575
F 0 "o?" H 3525 8425 100 0001 C CNN
F 1 "Salida" H 3775 8575 100 0000 C CNN
F 2 "" H 3500 8575 50  0001 C CNN
F 3 "" H 3500 8575 50  0001 C CNN
	1    3375 8575
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 8575 2750 8700
Wire Wire Line
	2750 7975 2750 8075
Wire Wire Line
	2750 8575 2750 8475
Connection ~ 2750 8575
Wire Wire Line
	2750 9100 2750 9275
$Comp
L simbolos:logic_nand U?
U 1 1 6034196B
P 1500 10400
F 0 "U?" H 1800 10577 100 0001 C CNN
F 1 "logic_nand" H 1800 10500 50  0001 C CNN
F 2 "" V 1600 10225 50  0001 C CNN
F 3 "" V 1600 10225 50  0001 C CNN
	1    1500 10400
	1    0    0    -1  
$EndComp
$Comp
L simbolos:logic_nand U?
U 1 1 6034281D
P 2500 10400
F 0 "U?" H 2800 10577 100 0001 C CNN
F 1 "logic_nand" H 2800 10500 50  0001 C CNN
F 2 "" V 2600 10225 50  0001 C CNN
F 3 "" V 2600 10225 50  0001 C CNN
	1    2500 10400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 10400 2375 10400
Wire Wire Line
	2375 10400 2375 10500
Wire Wire Line
	2375 10600 2500 10600
Wire Wire Line
	2375 10500 2100 10500
Connection ~ 2375 10500
Wire Wire Line
	2375 10500 2375 10600
$Comp
L simbolos:logic_nand U?
U 1 1 6034541C
P 5850 1025
F 0 "U?" H 6150 1202 100 0001 C CNN
F 1 "logic_nand" H 6150 1125 50  0001 C CNN
F 2 "" V 5950 850 50  0001 C CNN
F 3 "" V 5950 850 50  0001 C CNN
	1    5850 1025
	1    0    0    -1  
$EndComp
Wire Wire Line
	5850 1025 5725 1025
Wire Wire Line
	5725 1025 5725 1125
Wire Wire Line
	5725 1225 5850 1225
Wire Wire Line
	5725 1125 5450 1125
Connection ~ 5725 1125
Wire Wire Line
	5725 1125 5725 1225
$Comp
L simbolos:logic_nand U?
U 1 1 6034828A
P 6450 2950
F 0 "U?" H 6750 3127 100 0001 C CNN
F 1 "logic_nand" H 6750 3050 50  0001 C CNN
F 2 "" V 6550 2775 50  0001 C CNN
F 3 "" V 6550 2775 50  0001 C CNN
	1    6450 2950
	1    0    0    -1  
$EndComp
$Comp
L simbolos:logic_nand U?
U 1 1 6034B4D5
P 5475 2650
F 0 "U?" H 5775 2827 100 0001 C CNN
F 1 "logic_nand" H 5775 2750 50  0001 C CNN
F 2 "" V 5575 2475 50  0001 C CNN
F 3 "" V 5575 2475 50  0001 C CNN
	1    5475 2650
	1    0    0    -1  
$EndComp
$Comp
L simbolos:logic_nand U?
U 1 1 6034BD08
P 5475 3250
F 0 "U?" H 5775 3427 100 0001 C CNN
F 1 "logic_nand" H 5775 3350 50  0001 C CNN
F 2 "" V 5575 3075 50  0001 C CNN
F 3 "" V 5575 3075 50  0001 C CNN
	1    5475 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	6075 2750 6250 2750
Wire Wire Line
	6250 2750 6250 2950
Wire Wire Line
	6250 2950 6450 2950
Wire Wire Line
	6450 3150 6250 3150
Wire Wire Line
	6250 3150 6250 3350
Wire Wire Line
	6250 3350 6075 3350
Wire Wire Line
	5475 2650 5325 2650
Wire Wire Line
	5325 2650 5325 2750
Wire Wire Line
	5325 2850 5475 2850
Wire Wire Line
	5325 2750 5150 2750
Connection ~ 5325 2750
Wire Wire Line
	5325 2750 5325 2850
Wire Wire Line
	5475 3250 5325 3250
Wire Wire Line
	5325 3250 5325 3350
Wire Wire Line
	5325 3450 5475 3450
Wire Wire Line
	5325 3350 5150 3350
Connection ~ 5325 3350
Wire Wire Line
	5325 3350 5325 3450
Text Notes 7075 3100 0    100  ~ 0
Salida
Text Notes 4975 2800 0    100  ~ 0
A\n
Text Notes 4975 3400 0    100  ~ 0
B
Text Notes 5275 1200 0    100  ~ 0
A\n
Text Notes 6500 1200 0    100  ~ 0
Salida
Text Notes 3150 10575 0    100  ~ 0
Salida
Text Notes 1325 10450 0    100  ~ 0
A\n
Text Notes 1325 10675 0    100  ~ 0
B\n
$Comp
L simbolos:logic_nand U?
U 1 1 60358D27
P 5150 4750
F 0 "U?" H 5450 4927 100 0001 C CNN
F 1 "logic_nand" H 5450 4850 50  0001 C CNN
F 2 "" V 5250 4575 50  0001 C CNN
F 3 "" V 5250 4575 50  0001 C CNN
	1    5150 4750
	1    0    0    -1  
$EndComp
$Comp
L simbolos:logic_nand U?
U 1 1 60359C21
P 6000 4450
F 0 "U?" H 6300 4627 100 0001 C CNN
F 1 "logic_nand" H 6300 4550 50  0001 C CNN
F 2 "" V 6100 4275 50  0001 C CNN
F 3 "" V 6100 4275 50  0001 C CNN
	1    6000 4450
	1    0    0    -1  
$EndComp
$Comp
L simbolos:logic_nand U?
U 1 1 6035AB2F
P 6000 5050
F 0 "U?" H 6300 5227 100 0001 C CNN
F 1 "logic_nand" H 6300 5150 50  0001 C CNN
F 2 "" V 6100 4875 50  0001 C CNN
F 3 "" V 6100 4875 50  0001 C CNN
	1    6000 5050
	1    0    0    -1  
$EndComp
Wire Wire Line
	5750 4850 5875 4850
Wire Wire Line
	5875 4850 5875 4650
Wire Wire Line
	5875 4650 6000 4650
Wire Wire Line
	5875 4850 5875 5050
Wire Wire Line
	5875 5050 6000 5050
Connection ~ 5875 4850
Wire Wire Line
	6000 5250 5150 5250
Wire Wire Line
	5150 4950 5150 5250
Connection ~ 5150 5250
Wire Wire Line
	5150 5250 4875 5250
Wire Wire Line
	5150 4750 5150 4450
Wire Wire Line
	5150 4450 6000 4450
Wire Wire Line
	5150 4450 4900 4450
Connection ~ 5150 4450
$Comp
L simbolos:logic_nand U?
U 1 1 60366B83
P 6600 4750
F 0 "U?" H 6900 4927 100 0001 C CNN
F 1 "logic_nand" H 6900 4850 50  0001 C CNN
F 2 "" V 6700 4575 50  0001 C CNN
F 3 "" V 6700 4575 50  0001 C CNN
	1    6600 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	6600 4550 6600 4750
Wire Wire Line
	6600 4950 6600 5150
Text Notes 7225 4900 0    100  ~ 0
Salida
Text Notes 4725 4500 0    100  ~ 0
A\n
Text Notes 4700 5300 0    100  ~ 0
B
$Comp
L simbolos:logic_nand U?
U 1 1 6036F1DF
P 4750 6700
F 0 "U?" H 5050 6877 100 0001 C CNN
F 1 "logic_nand" H 5050 6800 50  0001 C CNN
F 2 "" V 4850 6525 50  0001 C CNN
F 3 "" V 4850 6525 50  0001 C CNN
	1    4750 6700
	1    0    0    -1  
$EndComp
$Comp
L simbolos:logic_nand U?
U 1 1 6036F639
P 5475 6400
F 0 "U?" H 5775 6577 100 0001 C CNN
F 1 "logic_nand" H 5775 6500 50  0001 C CNN
F 2 "" V 5575 6225 50  0001 C CNN
F 3 "" V 5575 6225 50  0001 C CNN
	1    5475 6400
	1    0    0    -1  
$EndComp
$Comp
L simbolos:logic_nand U?
U 1 1 6036F643
P 5475 7000
F 0 "U?" H 5775 7177 100 0001 C CNN
F 1 "logic_nand" H 5775 7100 50  0001 C CNN
F 2 "" V 5575 6825 50  0001 C CNN
F 3 "" V 5575 6825 50  0001 C CNN
	1    5475 7000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 6800 5350 6600
Wire Wire Line
	5350 6600 5475 6600
Wire Wire Line
	5350 6800 5350 7000
Wire Wire Line
	5350 7000 5475 7000
Connection ~ 5350 6800
Wire Wire Line
	5475 7200 4750 7200
Wire Wire Line
	4750 6900 4750 7200
Wire Wire Line
	4750 6700 4750 6400
$Comp
L simbolos:logic_nand U?
U 1 1 6036F65B
P 6075 6700
F 0 "U?" H 6375 6877 100 0001 C CNN
F 1 "logic_nand" H 6375 6800 50  0001 C CNN
F 2 "" V 6175 6525 50  0001 C CNN
F 3 "" V 6175 6525 50  0001 C CNN
	1    6075 6700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6075 6500 6075 6700
Wire Wire Line
	6075 6900 6075 7100
Text Notes 7425 6850 0    100  ~ 0
Salida
Text Notes 4350 6450 0    100  ~ 0
A\n
Text Notes 4350 7250 0    100  ~ 0
B
$Comp
L simbolos:logic_nand U?
U 1 1 60374CFF
P 6775 6700
F 0 "U?" H 7075 6877 100 0001 C CNN
F 1 "logic_nand" H 7075 6800 50  0001 C CNN
F 2 "" V 6875 6525 50  0001 C CNN
F 3 "" V 6875 6525 50  0001 C CNN
	1    6775 6700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6675 6800 6675 6700
Wire Wire Line
	6675 6700 6775 6700
Wire Wire Line
	6675 6800 6675 6900
Wire Wire Line
	6675 6900 6775 6900
Connection ~ 6675 6800
Connection ~ 4750 6400
Wire Wire Line
	4750 6400 5475 6400
Connection ~ 4750 7200
Wire Wire Line
	4525 6400 4750 6400
Wire Wire Line
	4525 7200 4750 7200
$Comp
L simbolos:logic_nand U?
U 1 1 60392F7A
P 5775 8575
F 0 "U?" H 6075 8752 100 0001 C CNN
F 1 "logic_nand" H 6075 8675 50  0001 C CNN
F 2 "" V 5875 8400 50  0001 C CNN
F 3 "" V 5875 8400 50  0001 C CNN
	1    5775 8575
	1    0    0    -1  
$EndComp
$Comp
L simbolos:logic_nand U?
U 1 1 60392F80
P 5000 8275
F 0 "U?" H 5300 8452 100 0001 C CNN
F 1 "logic_nand" H 5300 8375 50  0001 C CNN
F 2 "" V 5100 8100 50  0001 C CNN
F 3 "" V 5100 8100 50  0001 C CNN
	1    5000 8275
	1    0    0    -1  
$EndComp
$Comp
L simbolos:logic_nand U?
U 1 1 60392F86
P 5000 8875
F 0 "U?" H 5300 9052 100 0001 C CNN
F 1 "logic_nand" H 5300 8975 50  0001 C CNN
F 2 "" V 5100 8700 50  0001 C CNN
F 3 "" V 5100 8700 50  0001 C CNN
	1    5000 8875
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 8375 5775 8375
Wire Wire Line
	5775 8375 5775 8575
Wire Wire Line
	5775 8775 5775 8975
Wire Wire Line
	5775 8975 5600 8975
Wire Wire Line
	5000 8275 4850 8275
Wire Wire Line
	4850 8275 4850 8375
Wire Wire Line
	4850 8475 5000 8475
Wire Wire Line
	4850 8375 4675 8375
Connection ~ 4850 8375
Wire Wire Line
	4850 8375 4850 8475
Wire Wire Line
	5000 8875 4850 8875
Wire Wire Line
	4850 8875 4850 8975
Wire Wire Line
	4850 9075 5000 9075
Wire Wire Line
	4850 8975 4675 8975
Connection ~ 4850 8975
Wire Wire Line
	4850 8975 4850 9075
Text Notes 7200 8725 0    100  ~ 0
Salida
Text Notes 4500 8425 0    100  ~ 0
A\n
Text Notes 4500 9025 0    100  ~ 0
B
$Comp
L simbolos:logic_nand U?
U 1 1 60399A14
P 6550 8575
F 0 "U?" H 6850 8752 100 0001 C CNN
F 1 "logic_nand" H 6850 8675 50  0001 C CNN
F 2 "" V 6650 8400 50  0001 C CNN
F 3 "" V 6650 8400 50  0001 C CNN
	1    6550 8575
	1    0    0    -1  
$EndComp
Wire Wire Line
	6375 8675 6475 8675
Wire Wire Line
	6475 8675 6475 8575
Wire Wire Line
	6475 8575 6550 8575
Wire Wire Line
	6475 8675 6475 8775
Wire Wire Line
	6475 8775 6550 8775
Connection ~ 6475 8675
$EndSCHEMATC