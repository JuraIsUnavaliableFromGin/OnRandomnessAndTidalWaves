#!/usr/bin/env python
# coding: utf-8

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

gap_s_1 = np.arange(10,21,1)
gap_s_2 = np.arange(20,31,1)
gap_s_3 = np.arange(30,41,1)
gap_s_4 = np.arange(40,51,1)
gap_s_5 = np.arange(50,61,1) 
gap_s_6 = np.arange(60,71,1) 
gap_s_7 = np.arange(70,81,1) 
gap_s_8 = np.arange(80,91,1) 
gap_s_9 = np.arange(90,101,1)
# 10 000 000
gap_s_10 = np.arange(100,111,1)
gap_s_11 = np.arange(110,121,1)
gap_s_12 = np.arange(120,131,1)
gap_s_13 = np.arange(130,141,1)
gap_s_14 = np.arange(140,151,1)
gap_s_15 = np.arange(150,161,1)
gap_s_16 = np.arange(160,171,1)
gap_s_17 = np.arange(170,181,1)
gap_s_18 = np.arange(180,191,1)
gap_s_19 = np.arange(190,201,1)
gap_s_20 = np.arange(200,211,1)
gap_s_21 = np.arange(210,221,1)
gap_s_22 = np.arange(220,231,1)
gap_s_23 = np.arange(230,241,1)
gap_s_24 = np.arange(240,251,1)
gap_s_25 = np.arange(250,261,1)
gap_s_26 = np.arange(260,271,1)
gap_s_27 = np.arange(270,281,1)
gap_s_28 = np.arange(280,291,1)
gap_s_29 = np.arange(290,301,1)
gap_s_30 = np.arange(300,311,1)
gap_s_31 = np.arange(310,321,1)
gap_s_32 = np.arange(320,331,1)
gap_s_33 = np.arange(330,341,1)
gap_s_34 = np.arange(340,351,1)
gap_s_35 = np.arange(350,361,1)
gap_s_36 = np.arange(360,371,1)
gap_s_37 = np.arange(370,381,1)
gap_s_38 = np.arange(380,391,1)
gap_s_39 = np.arange(390,401,1)
gap_s_40 = np.arange(400,411,1)
gap_s_41 = np.arange(410,421,1)
gap_s_42 = np.arange(420,431,1)
gap_s_43 = np.arange(430,441,1)
gap_s_44 = np.arange(440,451,1)
gap_s_45 = np.arange(450,461,1)
gap_s_46 = np.arange(460,471,1)
gap_s_47 = np.arange(470,481,1)
gap_s_48 = np.arange(480,491,1)
gap_s_49 = np.arange(490,501,1)

gap_k_1 = np.arange(100,210,10)
gap_k_2 = np.arange(200,310,10)
gap_k_3 = np.arange(300,410,10)
gap_k_4 = np.arange(400,510,10)
gap_k_5 = np.arange(500,610,10)
gap_k_6 = np.arange(600,710,10)
gap_k_7 = np.arange(700,810,10)
gap_k_8 = np.arange(800,910,10)
gap_k_9 = np.arange(900,1010,10)
gap_k_10 = np.arange(1000,1110,10)
(gap_k_9,gap_k_10)


def rate(arr_s,arr_k):
    arr_r = []
    for s in range(len(arr_k)):
        for k in range(len(arr_s)):
            val_d = arr_k[s]-arr_s[k]
            val_r = round(val_d/arr_s[k],3)
            arr_r.append([arr_s[k],arr_k[s],val_r])
    return sorted(arr_r)



print(rate(gap_s_1,gap_k_1))


