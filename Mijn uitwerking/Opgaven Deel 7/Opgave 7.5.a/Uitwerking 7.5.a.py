# -*-coding:utf-8 -*-
'''
@File    :   Uitwerking 7.5.a.py
@Time    :   2022/11/07 10:09:21
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

#a
file = open('Klas.txt')
lines = file.readlines()

for line in lines:
    print(line)
    
file.close


# Output:
"""
Naam	Geslacht	Leeftijd	Lengte	Gewicht	Cijfer

Sarah	meisje	18	160	78	8

Lucas	jongen	17	171	67	10

Anne	meisje	21	167	70	8

Noah	jongen	19	172	63	6

Selin	meisje	19	185	79	10

Zayn	jongen	19	194	71	8

Iris	meisje	21	161	51	7

Marilyn	jongen	17	165	99	8

Mohammed	jongen	21	167	96	8

Julia	meisje	21	185	54	6

Jayden	jongen	20	183	65	4

Tamaz	jongen	20	176	61	8

Femke	meisje	21	157	45	7

Rosa	meisje	18	158	72	6

Mulan	meisje	18	176	58	8

Adam	jongen	18	198	81	5

Remon	jongen	19	178	68	7

Emma	meisje	17	167	55	4

Sepp	jongen	18	195	75	5

Lieke	meisje	20	181	73	7

Nova	meisje	18	171	59	6

Olivier	jongen	20	186	74	10

Floor	meisje	20	173	65	6

Fatima	meisje	21	176	59	4

Daan	jongen	21	175	96	7

Dunya	meisje	20	161	70	4

Fahid	jongen	17	170	98	9

Fleur	meisje	21	169	51	10

Jurre	jongen	20	175	54	5

Niek	jongen	21	167	99	7

Romy	meisje	18	177	60	10

DaniÃ«l	jongen	20	169	70	6

Noa	meisje	21	179	56	5

Nathan	jongen	17	169	84	10

Jasmijn	meisje	21	156	52	5

Terry	jongen	18	200	83	7

Michelle	meisje	20	182	55	4

<function TextIOWrapper.close()>
"""