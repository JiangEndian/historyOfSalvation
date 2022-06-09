import math
from django.shortcuts import render
import copy
import sys
from MyPython3 import *
sys.setrecursionlimit(3000) #应对RecursionError: maximum recursion depth exceeded

ID_BERESHITH                   = 0;
ID_NOAH                        = 1;
ID_LEHLEHA                     = 2;
ID_VAYERA                      = 3;
ID_HAYESARAH                   = 4;
ID_TOLEDOTH                    = 5;
ID_VAYETSE                     = 6;
ID_VAYISHLAH                   = 7;
ID_VAYESHEB                    = 8;
ID_MIKKETS                     = 9;
ID_VAYIGGASH                  = 10;
ID_VAYHEE                     = 11;
ID_SHEMOTH                    = 12;
ID_VAERA                      = 13;
ID_BO                         = 14;
ID_BESHALLAH                  = 15;
ID_YITHRO                     = 16;
ID_MISHPATIM                  = 17;
ID_TERUMAH                    = 18;
ID_TETSAVVEH                  = 19;
ID_KITISSA                    = 20;
ID_VAYAKHEL                   = 21;
ID_PEKUDE                     = 22;
ID_VAYIKRA                    = 23;
ID_TSAV                       = 24;
ID_SHEMINI                    = 25;
ID_TAZRIANG                   = 26;
ID_METSORANG                  = 27;
ID_AHAREMOTH                  = 28;
ID_KEDOSHIM                   = 29;
ID_EMOR                       = 30;
ID_BEHAR                      = 31;
ID_BEHUKKOTHAI                = 32;
ID_BEMIDBAR                   = 33;
ID_NASO                       = 34;
ID_BEHAALOTEHA                = 35;
ID_SHELAHLEHA                 = 36;
ID_KORAH                      = 37;
ID_HUKATH                     = 38;
ID_BALAK                      = 39;
ID_PINHAS                     = 40;
ID_MATOTH                     = 41;
ID_MASEH                      = 42;
ID_DEBARIM                    = 43;
ID_VAETHANAN                  = 44;
ID_EKEB                       = 45;
ID_REEH                       = 46;
ID_SHOFETIM                   = 47;
ID_KITETSE                    = 48;
ID_KITABO                     = 49;
ID_NITSABIM                   = 50;
ID_VAYELEH                    = 51;
ID_HAAZINU                    = 52;

ID_SIMHATHTORAH               = 53;
ID_SIMHATHTORAH_2             = 54;
ID_SIMHATHTORAH_3             = 55;

ID_ROSH_HODESH_SHABBAT        = 60;
ID_SHEKALIM                   = 61;
ID_ZAHOR                      = 62;
ID_PARAH                      = 63;
ID_HAHODESH                   = 64;
ID_HAGGADOL                   = 65;
ID_SHUVA                      = 66;

ID_ROSH_HASHANAH_I            = 70;
ID_ROSH_HASHANAH_II           = 71;
ID_FAST_OF_GEDALIAH           = 72;
ID_YOM_KIPPUR                 = 73;
ID_SUCCOTH_I                  = 74;
ID_SUCCOTH_II                 = 75;
ID_SUCCOTH_III_NO_SHABBAT     = 76;
ID_SUCCOTH_III                = 77;
ID_SUCCOTH_IV                 = 78;
ID_SUCCOTH_V_NO_SHABBAT       = 79;
ID_SUCCOTH_V                  = 80;
ID_SUCCOTH_VI_NO_SHABBAT      = 81;
ID_SUCCOTH_VI                 = 82;
ID_HOSHANAH_RABBAH            = 83;
ID_HOL_HAMOED_SUCCOTH         = 84;
ID_SHEMINI_AZERETH_1          = 85;
ID_FAST_OF_ESTHER             = 86;
ID_PURIM                      = 87;
ID_FAST_OF_TEVET_10           = 88;
ID_PESAH_I                    = 89;
ID_HOL_HAMOED_PESAH           = 90;
ID_PESAH_VII                  = 91;
ID_PESAH_VIII                 = 92;
ID_PESAH_VIII_NO_SHABBAT      = 93;
ID_SHAVUOTH_I                 = 94;
ID_SHAVUOTH_II_NO_SHABBAT     = 95; 
ID_SHAVUOTH_II                = 96;
ID_YOM_HAATZMAUT              = 97;
ID_FAST_OF_TAMMUZ_17          = 98;
ID_FAST_OF_TISHA_BAV          = 99;
ID_CHANUKKAH_I               = 100;
ID_CHANUKKAH_II              = 101;
ID_CHANUKKAH_III             = 102;
ID_CHANUKKAH_IV              = 103;
ID_CHANUKKAH_V               = 104;
ID_CHANUKKAH_VI              = 105;
ID_CHANUKKAH_VI_ROSH_HODESH  = 106;
ID_CHANUKKAH_VII             = 107;
ID_CHANUKKAH_VII_ROSH_HODESH = 108;
ID_CHANUKKAH_VIII            = 109;
ID_SECOND_SHABBAT_CHANUKKAH  = 110;
ID_ROSH_HODESH               = 111;
ID_PESAH_II                  = 112;
ID_PESAH_III                 = 113;
ID_PESAH_IV                  = 114;
ID_PESAH_IV_NOT_SUNDAY       = 115;
ID_PESAH_IV_SUNDAY           = 116;
ID_PESAH_V                   = 117;
ID_PESAH_V_NOT_MONDAY        = 118;
ID_PESAH_V_MONDAY            = 119;
ID_PESAH_VI                  = 120;

ID_SPECIAL_1                  = 150;
ID_SPECIAL_2                  = 151;
ID_SPECIAL_3                  = 152;
ID_SPECIAL_4                  = 153;
ID_SPECIAL_5                  = 154;
ID_SPECIAL_6                  = 155;
ID_SPECIAL_7                  = 156;
ID_SPECIAL_8                  = 157;
ID_SPECIAL_8A                 = 158;
ID_SPECIAL_9                  = 159;
ID_SPECIAL_10                 = 161;
ID_SPECIAL_11                 = 162;
ID_SPECIAL_12                 = 163;

ID_SHEMINI_AZERETH_2          = 170;
ID_SHEMINI_AZERETH_3          = 171;
ID_SHEMINI_AZERETH            = 172;

ID_MAX                        = 256;

ID_NULL                       = 1000;

torahSectionsA = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_SHEKALIM,ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_ZAHOR,   ID_NULL,      # 20 
   ID_KITISSA,             ID_PARAH,   ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_PEKUDE,  ID_HAHODESH,  # 22 
   ID_VAYIKRA,             ID_NULL,    ID_NULL,      # 24 
   ID_TSAV,                ID_HAGGADOL,ID_NULL,      # 25 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 26 
   ID_SHEMINI,             ID_NULL,    ID_NULL,      # 27 
   ID_TAZRIANG,           ID_METSORANG,ID_NULL,      # 28 
   ID_AHAREMOTH,           ID_KEDOSHIM,ID_NULL,      # 29 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 30 
   ID_BEHAR,            ID_BEHUKKOTHAI,ID_NULL,      # 31 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 32 
   ID_NASO,                ID_NULL,    ID_NULL,      # 33 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 34 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 35 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 36 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 37 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 38 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 39 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 40 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 41 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 42 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 43 
   ID_REEH,                ID_NULL,    ID_NULL,      # 44 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 45 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 46 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 47 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 48 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 49 
   ID_YOM_KIPPUR,          ID_NULL,    ID_NULL,      # 50 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 51 

torahSectionsB = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_SHEKALIM,ID_NULL,      # 18 
   ID_TERUMAH,             ID_ZAHOR,   ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_PARAH,   ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_PEKUDE,  ID_HAHODESH,  # 22 
   ID_VAYIKRA,             ID_NULL,    ID_NULL,      # 23 
   ID_TSAV,                ID_HAGGADOL,ID_NULL,      # 24 
   ID_PESAH_VII,           ID_NULL,    ID_NULL,      # 25 
   ID_SHEMINI,             ID_NULL,    ID_NULL,      # 26 
   ID_TAZRIANG,           ID_METSORANG,ID_NULL,      # 27 
   ID_AHAREMOTH,           ID_KEDOSHIM,ID_NULL,      # 28 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 29 
   ID_BEHAR,            ID_BEHUKKOTHAI,ID_NULL,      # 30 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 31 
   ID_NASO,                ID_NULL,    ID_NULL,      # 32 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 33 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 34 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 35 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 36 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 37 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 38 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 39 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 40 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 41 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 42 
   ID_REEH,                ID_NULL,    ID_NULL,      # 43 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 44 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 45 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 46 
   ID_NITSABIM,            ID_NULL,    ID_NULL,      # 47 
   ID_VAYELEH,             ID_NULL,    ID_NULL,      # 48 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 49 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 50 

torahSectionsCDiaspora = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_SHEKALIM,ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_ZAHOR,   ID_NULL,      # 20 
   ID_KITISSA,             ID_PARAH,   ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_PEKUDE,  ID_HAHODESH,  # 22 
   ID_VAYIKRA,             ID_NULL,    ID_NULL,      # 24 
   ID_TSAV,                ID_HAGGADOL,ID_NULL,      # 25 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 26 
   ID_SHEMINI,             ID_NULL,    ID_NULL,      # 27 
   ID_TAZRIANG,           ID_METSORANG,ID_NULL,      # 28 
   ID_AHAREMOTH,           ID_KEDOSHIM,ID_NULL,      # 29 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 30 
   ID_BEHAR,            ID_BEHUKKOTHAI,ID_NULL,      # 31 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 32 
   ID_SHAVUOTH_II,         ID_NULL,    ID_NULL,      # 33 
   ID_NASO,                ID_NULL,    ID_NULL,      # 34 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 35 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 36 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 37 
   ID_HUKATH,              ID_BALAK,   ID_NULL,      # 38 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 39 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 40 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 41 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 42 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 43 
   ID_REEH,                ID_NULL,    ID_NULL,      # 44 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 45 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 46 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 47 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 48 
   ID_ROSH_HASHANAH_I,     ID_NULL,    ID_NULL,      # 49 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 50 
   ID_SUCCOTH_I,           ID_NULL,    ID_NULL,      # 51 
   ID_SHEMINI_AZERETH,     ID_NULL,    ID_NULL];     # 52 

torahSectionsCIsrael = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_SHEKALIM,ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_ZAHOR,   ID_NULL,      # 20 
   ID_KITISSA,             ID_PARAH,   ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_PEKUDE,  ID_HAHODESH,  # 22 
   ID_VAYIKRA,             ID_NULL,    ID_NULL,      # 24 
   ID_TSAV,                ID_HAGGADOL,ID_NULL,      # 25 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 26 
   ID_SHEMINI,             ID_NULL,    ID_NULL,      # 27 
   ID_TAZRIANG,           ID_METSORANG,ID_NULL,      # 28 
   ID_AHAREMOTH,           ID_KEDOSHIM,ID_NULL,      # 29 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 30 
   ID_BEHAR,            ID_BEHUKKOTHAI,ID_NULL,      # 31 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 32 
   ID_NASO,                ID_NULL,    ID_NULL,      # 33 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 34 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 35 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 36 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 37 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 38 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 39 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 40 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 41 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 42 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 43 
   ID_REEH,                ID_NULL,    ID_NULL,      # 44 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 45 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 46 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 47 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 48 
   ID_ROSH_HASHANAH_I,     ID_NULL,    ID_NULL,      # 49 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 50 
   ID_SUCCOTH_I,           ID_NULL,    ID_NULL,      # 51 
   ID_SHEMINI_AZERETH,     ID_NULL,    ID_NULL];     # 52 

torahSectionsDDiaspora = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_SHEKALIM,ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_ZAHOR,   ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_PEKUDE,  ID_PARAH,     # 22 
   ID_VAYIKRA,             ID_HAHODESH,ID_NULL,      # 23 
   ID_TSAV,                ID_HAGGADOL,ID_NULL,      # 24 
   ID_PESAH_I,             ID_NULL,    ID_NULL,      # 25 
   ID_PESAH_VIII,          ID_NULL,    ID_NULL,      # 26 
   ID_SHEMINI,             ID_NULL,    ID_NULL,      # 27 
   ID_TAZRIANG,           ID_METSORANG,ID_NULL,      # 28 
   ID_AHAREMOTH,           ID_KEDOSHIM,ID_NULL,      # 29 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 30 
   ID_BEHAR,            ID_BEHUKKOTHAI,ID_NULL,      # 31 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 32 
   ID_NASO,                ID_NULL,    ID_NULL,      # 33 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 34 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 35 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 36 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 37 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 38 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 39 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 40 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 41 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 42 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 43 
   ID_REEH,                ID_NULL,    ID_NULL,      # 44 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 45 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 46 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 47 
   ID_NITSABIM,            ID_NULL,    ID_NULL,      # 48 
   ID_VAYELEH,             ID_NULL,    ID_NULL,      # 49 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 50 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 51 

torahSectionsDIsrael = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_SHEKALIM,ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_ZAHOR,   ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_PEKUDE,  ID_PARAH,     # 22 
   ID_VAYIKRA,             ID_HAHODESH,ID_NULL,      # 23 
   ID_TSAV,                ID_HAGGADOL,ID_NULL,      # 24 
   ID_PESAH_I,             ID_NULL,    ID_NULL,      # 25 
   ID_SHEMINI,             ID_NULL,    ID_NULL,      # 26 
   ID_TAZRIANG,           ID_METSORANG,ID_NULL,      # 27 
   ID_AHAREMOTH,           ID_KEDOSHIM,ID_NULL,      # 28 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 29 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 30 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 31 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 32 
   ID_NASO,                ID_NULL,    ID_NULL,      # 33 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 34 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 35 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 36 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 37 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 38 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 39 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 40 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 41 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 42 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 43 
   ID_REEH,                ID_NULL,    ID_NULL,      # 44 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 45 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 46 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 47 
   ID_NITSABIM,            ID_NULL,    ID_NULL,      # 48 
   ID_VAYELEH,             ID_NULL,    ID_NULL,      # 49 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 50 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 51 

torahSectionsEDiaspora = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_SHEKALIM,ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_ZAHOR,   ID_NULL,      # 20 
   ID_KITISSA,             ID_PARAH,   ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_PEKUDE,  ID_HAHODESH,  # 22 
   ID_VAYIKRA,             ID_NULL,    ID_NULL,      # 23 
   ID_TSAV,                ID_HAGGADOL,ID_NULL,      # 24 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 26 
   ID_SHEMINI,             ID_NULL,    ID_NULL,      # 27 
   ID_TAZRIANG,           ID_METSORANG,ID_NULL,      # 28 
   ID_AHAREMOTH,           ID_KEDOSHIM,ID_NULL,      # 29 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 30 
   ID_BEHAR,            ID_BEHUKKOTHAI,ID_NULL,      # 31 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 32 
   ID_SHAVUOTH_II,         ID_NULL,    ID_NULL,      # 33 
   ID_NASO,                ID_NULL,    ID_NULL,      # 34 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 35 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 36 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 37 
   ID_HUKATH,              ID_BALAK,   ID_NULL,      # 38 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 39 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 40 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 41 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 42 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 43 
   ID_REEH,                ID_NULL,    ID_NULL,      # 44 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 45 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 46 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 47 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 48 
   ID_ROSH_HASHANAH_I,     ID_NULL,    ID_NULL,      # 49 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 50 
   ID_SUCCOTH_I,           ID_NULL,    ID_NULL,      # 51 
   ID_SHEMINI_AZERETH,     ID_NULL,    ID_NULL];     # 52 

torahSectionsEIsrael = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_SHEKALIM,ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_ZAHOR,   ID_NULL,      # 20 
   ID_KITISSA,             ID_PARAH,   ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_PEKUDE,  ID_HAHODESH,  # 22 
   ID_VAYIKRA,             ID_NULL,    ID_NULL,      # 23 
   ID_TSAV,                ID_HAGGADOL,ID_NULL,      # 24 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 26 
   ID_SHEMINI,             ID_NULL,    ID_NULL,      # 27 
   ID_TAZRIANG,           ID_METSORANG,ID_NULL,      # 28 
   ID_AHAREMOTH,           ID_KEDOSHIM,ID_NULL,      # 29 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 30 
   ID_BEHAR,            ID_BEHUKKOTHAI,ID_NULL,      # 31 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 32 
   ID_NASO,                ID_NULL,    ID_NULL,      # 33 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 34 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 35 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 36 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 37 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 38 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 39 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 40 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 41 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 42 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 43 
   ID_REEH,                ID_NULL,    ID_NULL,      # 44 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 45 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 46 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 47 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 48 
   ID_ROSH_HASHANAH_I,     ID_NULL,    ID_NULL,      # 49 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 50 
   ID_SUCCOTH_I,           ID_NULL,    ID_NULL,      # 51 
   ID_SHEMINI_AZERETH,     ID_NULL,    ID_NULL];     # 52 

torahSectionsF = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_SHEKALIM,ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_ZAHOR,   ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_PARAH,   ID_NULL,      # 22 
   ID_PEKUDE,              ID_HAHODESH,ID_NULL,      # 23 
   ID_VAYIKRA,             ID_NULL,    ID_NULL,      # 24 
   ID_TSAV,                ID_HAGGADOL,ID_NULL,      # 25 
   ID_PESAH_VII,           ID_NULL,    ID_NULL,      # 26 
   ID_SHEMINI,             ID_NULL,    ID_NULL,      # 27 
   ID_TAZRIANG,           ID_METSORANG,ID_NULL,      # 28 
   ID_AHAREMOTH,           ID_KEDOSHIM,ID_NULL,      # 29 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 30 
   ID_BEHAR,            ID_BEHUKKOTHAI,ID_NULL,      # 31 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 32 
   ID_NASO,                ID_NULL,    ID_NULL,      # 34 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 35 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 36 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 37 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 38 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 39 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 40 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 41 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 42 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 43 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 44 
   ID_REEH,                ID_NULL,    ID_NULL,      # 45 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 46 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 47 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 48 
   ID_NITSABIM,            ID_NULL,    ID_NULL,      # 49 
   ID_VAYELEH,             ID_NULL,    ID_NULL,      # 50 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 51 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 52 

torahSectionsG = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_SHEKALIM,ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_ZAHOR,   ID_NULL,      # 20 
   ID_KITISSA,             ID_PARAH,   ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_PEKUDE,  ID_HAHODESH,  # 22 
   ID_VAYIKRA,             ID_NULL,    ID_NULL,      # 24 
   ID_TSAV,                ID_HAGGADOL,ID_NULL,      # 25 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 26 
   ID_SHEMINI,             ID_NULL,    ID_NULL,      # 27 
   ID_TAZRIANG,           ID_METSORANG,ID_NULL,      # 28 
   ID_AHAREMOTH,           ID_KEDOSHIM,ID_NULL,      # 29 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 30 
   ID_BEHAR,            ID_BEHUKKOTHAI,ID_NULL,      # 31 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 32 
   ID_NASO,                ID_NULL,    ID_NULL,      # 33 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 34 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 35 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 36 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 37 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 38 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 39 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 40 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 41 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 42 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 43 
   ID_REEH,                ID_NULL,    ID_NULL,      # 44 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 45 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 46 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 47 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 48 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 49 
   ID_YOM_KIPPUR,          ID_NULL,    ID_NULL,      # 50 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 51 

torahSectionsHDiaspora = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_SHEKALIM,ID_NULL,      # 22 
   ID_PEKUDE,              ID_NULL,    ID_NULL,      # 23 
   ID_VAYIKRA,             ID_ZAHOR,   ID_NULL,      # 24 
   ID_TSAV,                ID_PARAH,   ID_NULL,      # 25 
   ID_SHEMINI,             ID_HAHODESH,ID_NULL,      # 26 
   ID_TAZRIANG,            ID_NULL,    ID_NULL,      # 27 
   ID_METSORANG,           ID_HAGGADOL,ID_NULL,      # 28 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 29 
   ID_AHAREMOTH,           ID_NULL,    ID_NULL,      # 30 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 31 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 32 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 33 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 34 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 35 
   ID_SHAVUOTH_II,         ID_NULL,    ID_NULL,      # 36 
   ID_NASO,                ID_NULL,    ID_NULL,      # 37 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 38 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 39 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 40 
   ID_HUKATH,              ID_BALAK,   ID_NULL,      # 41 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 42 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 43 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 44 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 45 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 46 
   ID_REEH,                ID_NULL,    ID_NULL,      # 47 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 48 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 49 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 50 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 51 
   ID_ROSH_HASHANAH_I,     ID_NULL,    ID_NULL,      # 52 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 53 
   ID_SUCCOTH_I,           ID_NULL,    ID_NULL,      # 54 
   ID_SHEMINI_AZERETH,     ID_NULL,    ID_NULL];     # 55 

torahSectionsHIsrael = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_SHEKALIM,ID_NULL,      # 22 
   ID_PEKUDE,              ID_NULL,    ID_NULL,      # 23 
   ID_VAYIKRA,             ID_ZAHOR,   ID_NULL,      # 24 
   ID_TSAV,                ID_PARAH,   ID_NULL,      # 25 
   ID_SHEMINI,             ID_HAHODESH,ID_NULL,      # 26 
   ID_TAZRIANG,            ID_NULL,    ID_NULL,      # 27 
   ID_METSORANG,           ID_HAGGADOL,ID_NULL,      # 28 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 29 
   ID_AHAREMOTH,           ID_NULL,    ID_NULL,      # 30 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 31 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 32 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 33 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 34 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 35 
   ID_NASO,                ID_NULL,    ID_NULL,      # 36 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 37 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 38 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 39 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 40 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 41 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 42 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 43 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 44 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 45 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 46 
   ID_REEH,                ID_NULL,    ID_NULL,      # 47 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 48 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 49 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 50 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 51 
   ID_ROSH_HASHANAH_I,     ID_NULL,    ID_NULL,      # 52 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 53 
   ID_SUCCOTH_I,           ID_NULL,    ID_NULL,      # 54 
   ID_SHEMINI_AZERETH,     ID_NULL,    ID_NULL];     # 55 

torahSectionsI = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_NULL,    ID_NULL,      # 22 
   ID_PEKUDE,              ID_SHEKALIM,ID_NULL,      # 23 
   ID_VAYIKRA,             ID_ZAHOR,   ID_NULL,      # 24 
   ID_TSAV,                ID_NULL,    ID_NULL,      # 25 
   ID_SHEMINI,             ID_PARAH,   ID_NULL,      # 26 
   ID_TAZRIANG,            ID_HAHODESH,ID_NULL,      # 27 
   ID_METSORANG,           ID_NULL,    ID_NULL,      # 28 
   ID_AHAREMOTH,           ID_HAGGADOL,ID_NULL,      # 29 
   ID_PESAH_VII,           ID_NULL,    ID_NULL,      # 30 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 31 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 32 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 33 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 34 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 35 
   ID_NASO,                ID_NULL,    ID_NULL,      # 36 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 37 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 38 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 39 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 40 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 41 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 42 
   ID_MATOTH,              ID_NULL,    ID_NULL,      # 43 
   ID_MASEH,               ID_NULL,    ID_NULL,      # 44 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 45 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 46 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 47 
   ID_REEH,                ID_NULL,    ID_NULL,      # 48 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 49 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 50 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 51 
   ID_NITSABIM,            ID_NULL,    ID_NULL,      # 52 
   ID_VAYELEH,             ID_NULL,    ID_NULL,      # 53 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 54 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 55 

torahSectionsJ = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_SHEKALIM,ID_NULL,      # 22 
   ID_PEKUDE,              ID_NULL,    ID_NULL,      # 23 
   ID_VAYIKRA,             ID_ZAHOR,   ID_NULL,      # 24 
   ID_TSAV,                ID_PARAH,   ID_NULL,      # 25 
   ID_SHEMINI,             ID_HAHODESH,ID_NULL,      # 26 
   ID_TAZRIANG,            ID_NULL,    ID_NULL,      # 27 
   ID_METSORANG,           ID_HAGGADOL,ID_NULL,      # 28 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 29 
   ID_AHAREMOTH,           ID_NULL,    ID_NULL,      # 30 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 31 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 32 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 33 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 34 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 35 
   ID_NASO,                ID_NULL,    ID_NULL,      # 36 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 37 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 38 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 39 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 40 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 41 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 42 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 43 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 44 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 45 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 46 
   ID_REEH,                ID_NULL,    ID_NULL,      # 47 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 48 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 49 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 50 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 51 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 52 
   ID_YOM_KIPPUR,          ID_NULL,    ID_NULL,      # 53 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 54 

torahSectionsKDiaspora = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_SHEKALIM,ID_NULL,      # 22 
   ID_PEKUDE,              ID_NULL,    ID_NULL,      # 23 
   ID_VAYIKRA,             ID_ZAHOR,   ID_NULL,      # 24 
   ID_TSAV,                ID_NULL,    ID_NULL,      # 25 
   ID_SHEMINI,             ID_PARAH,   ID_NULL,      # 26 
   ID_TAZRIANG,            ID_HAHODESH,ID_NULL,      # 27 
   ID_METSORANG,           ID_HAGGADOL,ID_NULL,      # 28 
   ID_PESAH_I,             ID_NULL,    ID_NULL,      # 29 
   ID_PESAH_VIII,          ID_NULL,    ID_NULL,      # 30 
   ID_AHAREMOTH,           ID_NULL,    ID_NULL,      # 31 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 32 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 33 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 34 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 35 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 36 
   ID_NASO,                ID_NULL,    ID_NULL,      # 37 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 38 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 39 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 40 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 41 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 42 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 43 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 44 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 45 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 46 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 47 
   ID_REEH,                ID_NULL,    ID_NULL,      # 48 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 49 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 50 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 51 
   ID_NITSABIM,            ID_NULL,    ID_NULL,      # 52 
   ID_VAYELEH,             ID_NULL,    ID_NULL,      # 53 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 54 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 55 

torahSectionsKIsrael = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_SHEKALIM,ID_NULL,      # 22 
   ID_PEKUDE,              ID_NULL,    ID_NULL,      # 23 
   ID_VAYIKRA,             ID_ZAHOR,   ID_NULL,      # 24 
   ID_TSAV,                ID_NULL,    ID_NULL,      # 25 
   ID_SHEMINI,             ID_PARAH,   ID_NULL,      # 26 
   ID_TAZRIANG,            ID_HAHODESH,ID_NULL,      # 27 
   ID_METSORANG,           ID_HAGGADOL,ID_NULL,      # 28 
   ID_PESAH_I,             ID_NULL,    ID_NULL,      # 29 
   ID_AHAREMOTH,           ID_NULL,    ID_NULL,      # 30 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 31 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 32 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 33 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 34 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 35 
   ID_NASO,                ID_NULL,    ID_NULL,      # 36 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 37 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 38 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 39 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 40 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 41 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 42 
   ID_MATOTH,              ID_NULL,    ID_NULL,      # 43 
   ID_MASEH,               ID_NULL,    ID_NULL,      # 44 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 45 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 46 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 47 
   ID_REEH,                ID_NULL,    ID_NULL,      # 48 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 49 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 50 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 51 
   ID_NITSABIM,            ID_NULL,    ID_NULL,      # 52 
   ID_VAYELEH,             ID_NULL,    ID_NULL,      # 53 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 54 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 55 

torahSectionsLDiaspora = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_SHEKALIM,ID_NULL,      # 22 
   ID_PEKUDE,              ID_NULL,    ID_NULL,      # 23 
   ID_VAYIKRA,             ID_ZAHOR,  ID_NULL,      # 24 
   ID_TSAV,                ID_NULL,    ID_NULL,      # 25 
   ID_SHEMINI,             ID_PARAH,   ID_NULL,      # 26 
   ID_TAZRIANG,            ID_HAHODESH,ID_NULL,      # 27 
   ID_METSORANG,           ID_HAGGADOL,ID_NULL,      # 28 
   ID_PESAH_I,             ID_NULL,    ID_NULL,      # 29 
   ID_PESAH_VIII,          ID_NULL,    ID_NULL,      # 30 
   ID_AHAREMOTH,           ID_NULL,    ID_NULL,      # 31 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 32 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 33 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 34 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 35 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 36 
   ID_NASO,                ID_NULL,    ID_NULL,      # 37 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 38 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 39 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 40 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 41 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 42 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 43 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 44 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 45 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 46 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 47 
   ID_REEH,                ID_NULL,    ID_NULL,      # 48 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 49 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 50 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 51 
   ID_NITSABIM,            ID_NULL,    ID_NULL,      # 52 
   ID_VAYELEH,             ID_NULL,    ID_NULL,      # 53 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 54 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 55 

torahSectionsLIsrael = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_SHEKALIM,ID_NULL,      # 22 
   ID_PEKUDE,              ID_NULL,    ID_NULL,      # 23 
   ID_VAYIKRA,             ID_ZAHOR,  ID_NULL,      # 24 
   ID_TSAV,                ID_NULL,    ID_NULL,      # 25 
   ID_SHEMINI,             ID_PARAH,   ID_NULL,      # 26 
   ID_TAZRIANG,            ID_HAHODESH,ID_NULL,      # 27 
   ID_METSORANG,           ID_HAGGADOL,ID_NULL,      # 28 
   ID_PESAH_I,             ID_NULL,    ID_NULL,      # 29 
   ID_AHAREMOTH,           ID_NULL,    ID_NULL,      # 30 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 31 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 32 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 33 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 34 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 35 
   ID_NASO,                ID_NULL,    ID_NULL,      # 36 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 37 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 38 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 39 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 40 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 41 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 42 
   ID_MATOTH,              ID_NULL,    ID_NULL,      # 43 
   ID_MASEH,               ID_NULL,    ID_NULL,      # 44 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 45 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 46 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 47 
   ID_REEH,                ID_NULL,    ID_NULL,      # 48 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 49 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 50 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 51 
   ID_NITSABIM,            ID_NULL,    ID_NULL,      # 52 
   ID_VAYELEH,             ID_NULL,    ID_NULL,      # 53 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 54 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 55 

torahSectionsM = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_NULL,    ID_NULL,      # 22 
   ID_PEKUDE,              ID_SHEKALIM,ID_NULL,      # 23 
   ID_VAYIKRA,             ID_NULL,    ID_NULL,      # 24 
   ID_TSAV,                ID_ZAHOR,   ID_NULL,      # 25 
   ID_SHEMINI,             ID_PARAH,   ID_NULL,      # 26 
   ID_TAZRIANG,            ID_HAHODESH,ID_NULL,      # 27 
   ID_METSORANG,           ID_NULL,    ID_NULL,      # 28 
   ID_AHAREMOTH,           ID_HAGGADOL,ID_NULL,      # 29 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 30 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 31 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 32 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 33 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 34 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 35 
   ID_NASO,                ID_NULL,    ID_NULL,      # 36 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 37 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 38 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 39 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 40 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 41 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 42 
   ID_MATOTH,              ID_NULL,    ID_NULL,      # 43 
   ID_MASEH,               ID_NULL,    ID_NULL,      # 44 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 45 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 46 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 47 
   ID_REEH,                ID_NULL,    ID_NULL,      # 48 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 49 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 50 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 51 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 52 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 53 
   ID_YOM_KIPPUR,          ID_NULL,    ID_NULL,      # 54 
   ID_HOL_HAMOED_SUCCOTH,  ID_NULL,    ID_NULL];     # 55 

torahSectionsNDiaspora = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_SHEKALIM,ID_NULL,      # 22 
   ID_PEKUDE,              ID_NULL,    ID_NULL,      # 23 
   ID_VAYIKRA,             ID_ZAHOR,   ID_NULL,      # 24 
   ID_TSAV,                ID_PARAH,   ID_NULL,      # 25 
   ID_SHEMINI,             ID_HAHODESH,ID_NULL,      # 26 
   ID_TAZRIANG,            ID_NULL,    ID_NULL,      # 27 
   ID_METSORANG,           ID_HAGGADOL,ID_NULL,      # 28 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 29 
   ID_AHAREMOTH,           ID_NULL,    ID_NULL,      # 30 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 31 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 32 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 33 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 34 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 35 
   ID_SHAVUOTH_II,         ID_NULL,    ID_NULL,      # 36 
   ID_NASO,                ID_NULL,    ID_NULL,      # 37 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 38 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 39 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 40 
   ID_HUKATH,              ID_BALAK,   ID_NULL,      # 41 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 42 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 43 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 44 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 45 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 46 
   ID_REEH,                ID_NULL,    ID_NULL,      # 47 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 48 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 49 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 50 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 51 
   ID_ROSH_HASHANAH_I,     ID_NULL,    ID_NULL,      # 52 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 53 
   ID_SUCCOTH_I,           ID_NULL,    ID_NULL,      # 54 
   ID_SHEMINI_AZERETH,     ID_NULL,    ID_NULL];     # 55 

torahSectionsNIsrael = \
  [ID_BERESHITH,           ID_NULL,    ID_NULL,      #  1 
   ID_NOAH,                ID_NULL,    ID_NULL,      #  2 
   ID_LEHLEHA,             ID_NULL,    ID_NULL,      #  3 
   ID_VAYERA,              ID_NULL,    ID_NULL,      #  4 
   ID_HAYESARAH,           ID_NULL,    ID_NULL,      #  5 
   ID_TOLEDOTH,            ID_NULL,    ID_NULL,      #  6 
   ID_VAYETSE,             ID_NULL,    ID_NULL,      #  7 
   ID_VAYISHLAH,           ID_NULL,    ID_NULL,      #  8 
   ID_VAYESHEB,            ID_NULL,    ID_NULL,      #  9 
   ID_MIKKETS,             ID_NULL,    ID_NULL,      # 10 
   ID_VAYIGGASH,           ID_NULL,    ID_NULL,      # 11 
   ID_VAYHEE,              ID_NULL,    ID_NULL,      # 12 
   ID_SHEMOTH,             ID_NULL,    ID_NULL,      # 13 
   ID_VAERA,               ID_NULL,    ID_NULL,      # 14 
   ID_BO,                  ID_NULL,    ID_NULL,      # 15 
   ID_BESHALLAH,           ID_NULL,    ID_NULL,      # 16 
   ID_YITHRO,              ID_NULL,    ID_NULL,      # 17 
   ID_MISHPATIM,           ID_NULL,    ID_NULL,      # 18 
   ID_TERUMAH,             ID_NULL,    ID_NULL,      # 19 
   ID_TETSAVVEH,           ID_NULL,    ID_NULL,      # 20 
   ID_KITISSA,             ID_NULL,    ID_NULL,      # 21 
   ID_VAYAKHEL,            ID_SHEKALIM,ID_NULL,      # 22 
   ID_PEKUDE,              ID_NULL,    ID_NULL,      # 23 
   ID_VAYIKRA,             ID_ZAHOR,   ID_NULL,      # 24 
   ID_TSAV,                ID_PARAH,   ID_NULL,      # 25 
   ID_SHEMINI,             ID_HAHODESH,ID_NULL,      # 26 
   ID_TAZRIANG,            ID_NULL,    ID_NULL,      # 27 
   ID_METSORANG,           ID_HAGGADOL,ID_NULL,      # 28 
   ID_HOL_HAMOED_PESAH,    ID_NULL,    ID_NULL,      # 29 
   ID_AHAREMOTH,           ID_NULL,    ID_NULL,      # 30 
   ID_KEDOSHIM,            ID_NULL,    ID_NULL,      # 31 
   ID_EMOR,                ID_NULL,    ID_NULL,      # 32 
   ID_BEHAR,               ID_NULL,    ID_NULL,      # 33 
   ID_BEHUKKOTHAI,         ID_NULL,    ID_NULL,      # 34 
   ID_BEMIDBAR,            ID_NULL,    ID_NULL,      # 35 
   ID_NASO,                ID_NULL,    ID_NULL,      # 36 
   ID_BEHAALOTEHA,         ID_NULL,    ID_NULL,      # 37 
   ID_SHELAHLEHA,          ID_NULL,    ID_NULL,      # 38 
   ID_KORAH,               ID_NULL,    ID_NULL,      # 39 
   ID_HUKATH,              ID_NULL,    ID_NULL,      # 40 
   ID_BALAK,               ID_NULL,    ID_NULL,      # 41 
   ID_PINHAS,              ID_NULL,    ID_NULL,      # 42 
   ID_MATOTH,              ID_MASEH,   ID_NULL,      # 43 
   ID_DEBARIM,             ID_NULL,    ID_NULL,      # 44 
   ID_VAETHANAN,           ID_NULL,    ID_NULL,      # 45 
   ID_EKEB,                ID_NULL,    ID_NULL,      # 46 
   ID_REEH,                ID_NULL,    ID_NULL,      # 47 
   ID_SHOFETIM,            ID_NULL,    ID_NULL,      # 48 
   ID_KITETSE,             ID_NULL,    ID_NULL,      # 49 
   ID_KITABO,              ID_NULL,    ID_NULL,      # 50 
   ID_NITSABIM,            ID_VAYELEH, ID_NULL,      # 51 
   ID_ROSH_HASHANAH_I,     ID_NULL,    ID_NULL,      # 52 
   ID_HAAZINU,             ID_NULL,    ID_NULL,      # 53 
   ID_SUCCOTH_I,           ID_NULL,    ID_NULL,      # 54 
   ID_SHEMINI_AZERETH,     ID_NULL,    ID_NULL];     # 55 

def torahGetWeekday(absDate):
  return get_weekday_from_absdate(absDate)

def torahHebrewLeapYear(year):
  return hebrew_leap(year)

def torahLastMonthOfHebrewYear(year):
  return hebrew_year_months(year)

def getYearType(year):
  rhWeekday = torahGetWeekday(hebrew_to_absdate(year, 7, 1));
  lengthOfYear = int(hebrew_to_absdate(year+1, 7, 1) - hebrew_to_absdate(year, 7, 1));
  pesWeekday = torahGetWeekday(hebrew_to_absdate(year, 1, 15));

  if ((rhWeekday == 1) and (lengthOfYear == 353) and (pesWeekday == 2)):
    return 1;
  if ((rhWeekday == 6) and (lengthOfYear == 353) and (pesWeekday == 0)):
    return 2;
  if ((rhWeekday == 2) and (lengthOfYear == 354) and (pesWeekday == 4)):
    return 3;
  if ((rhWeekday == 4) and (lengthOfYear == 354) and (pesWeekday == 6)):
    return 4;
  if ((rhWeekday == 1) and (lengthOfYear == 355) and (pesWeekday == 4)):
    return 5;
  if ((rhWeekday == 4) and (lengthOfYear == 355) and (pesWeekday == 0)):
    return 6;
  if ((rhWeekday == 6) and (lengthOfYear == 355) and (pesWeekday == 2)):
    return 7;

  if ((rhWeekday == 1) and (lengthOfYear == 383) and (pesWeekday == 4)):
    return 8;
  if ((rhWeekday == 4) and (lengthOfYear == 383) and (pesWeekday == 0)):
    return 9;
  if ((rhWeekday == 6) and (lengthOfYear == 383) and (pesWeekday == 2)):
    return 10;
  if ((rhWeekday == 2) and (lengthOfYear == 384) and (pesWeekday == 6)):
    return 11;
  if ((rhWeekday == 1) and (lengthOfYear == 385) and (pesWeekday == 6)):
    return 12;
  if ((rhWeekday == 4) and (lengthOfYear == 385) and (pesWeekday == 2)):
    return 13;
  if ((rhWeekday == 6) and (lengthOfYear == 385) and (pesWeekday == 4)):
   return 14;

  return 0;

def determineBereshith(year):
  simchatTorah = hebrew_to_absdate(year, 7, 23);
  while (torahGetWeekday(simchatTorah) != 6):
    simchatTorah += 1;
  return (simchatTorah);

def getTorahSections(hebrewMonth, hebrewDay, hebrewYear, diaspora):
  shuvahDate = hebrew_to_absdate(hebrewYear, 7, 1)+1;
  while (torahGetWeekday(shuvahDate) != 6):
    shuvahDate += 1;

  torahDate = hebrew_to_absdate(hebrewYear, hebrewMonth, hebrewDay);
  if (torahGetWeekday(torahDate) == 6):
    bereshithDate = determineBereshith(hebrewYear);
    if (torahDate < bereshithDate):
      referenceYear = hebrewYear-1;
    else:
      referenceYear = hebrewYear;

    yearType = getYearType(referenceYear);
    bereshithDate = determineBereshith(referenceYear);
    torahWeekNo = int(int(torahDate-bereshithDate)/7);

    returnTorahSection = "";
    idTorah1 = ID_NULL;
    idTorah2 = ID_NULL;
    idTorah3 = ID_NULL;
#
# allgemein: A, B, F, G, I, J, M
# Israel/Diaspora: C, D, E, H, K, L, N
#

    if (yearType == 1): # A
      idTorah1 = torahSectionsA[torahWeekNo * 3 + 0];
      idTorah2 = torahSectionsA[torahWeekNo * 3 + 1];
      idTorah3 = torahSectionsA[torahWeekNo * 3 + 2];
    if (yearType == 2): # B
      idTorah1 = torahSectionsB[torahWeekNo * 3 + 0];
      idTorah2 = torahSectionsB[torahWeekNo * 3 + 1];
      idTorah3 = torahSectionsB[torahWeekNo * 3 + 2];
    if (yearType == 3): # C
      if diaspora:
        idTorah1 = torahSectionsCDiaspora[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsCDiaspora[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsCDiaspora[torahWeekNo * 3 + 2];
      else:
        idTorah1 = torahSectionsCIsrael[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsCIsrael[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsCIsrael[torahWeekNo * 3 + 2];
    if (yearType == 4): # D
      if diaspora:
        idTorah1 = torahSectionsDDiaspora[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsDDiaspora[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsDDiaspora[torahWeekNo * 3 + 2];
      else:
        idTorah1 = torahSectionsDIsrael[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsDIsrael[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsDIsrael[torahWeekNo * 3 + 2];
    if (yearType == 5): # E
      if diaspora:
        idTorah1 = torahSectionsEDiaspora[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsEDiaspora[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsEDiaspora[torahWeekNo * 3 + 2];
      else:
        idTorah1 = torahSectionsEIsrael[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsEIsrael[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsEIsrael[torahWeekNo * 3 + 2];
    if (yearType == 6): # F
      idTorah1 = torahSectionsF[torahWeekNo * 3 + 0];
      idTorah2 = torahSectionsF[torahWeekNo * 3 + 1];
      idTorah3 = torahSectionsF[torahWeekNo * 3 + 2];
    if (yearType == 7): # G
      idTorah1 = torahSectionsG[torahWeekNo * 3 + 0];
      idTorah2 = torahSectionsG[torahWeekNo * 3 + 1];
      idTorah3 = torahSectionsG[torahWeekNo * 3 + 2];
    if (yearType == 8): # H
      if diaspora:
        idTorah1 = torahSectionsHDiaspora[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsHDiaspora[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsHDiaspora[torahWeekNo * 3 + 2];
      else:
        idTorah1 = torahSectionsHIsrael[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsHIsrael[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsHIsrael[torahWeekNo * 3 + 2];
    if (yearType == 9): # I
      idTorah1 = torahSectionsI[torahWeekNo * 3 + 0];
      idTorah2 = torahSectionsI[torahWeekNo * 3 + 1];
      idTorah3 = torahSectionsI[torahWeekNo * 3 + 2];
    if (yearType == 10): # J
      idTorah1 = torahSectionsJ[torahWeekNo * 3 + 0];
      idTorah2 = torahSectionsJ[torahWeekNo * 3 + 1];
      idTorah3 = torahSectionsJ[torahWeekNo * 3 + 2];
    if (yearType == 11): # K
      if (diaspora):
        idTorah1 = torahSectionsKDiaspora[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsKDiaspora[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsKDiaspora[torahWeekNo * 3 + 2];
      else:
        idTorah1 = torahSectionsKIsrael[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsKIsrael[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsKIsrael[torahWeekNo * 3 + 2];
    if (yearType == 12): # L
      if (diaspora):
        idTorah1 = torahSectionsLDiaspora[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsLDiaspora[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsLDiaspora[torahWeekNo * 3 + 2];
      else:
        idTorah1 = torahSectionsLIsrael[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsLIsrael[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsLIsrael[torahWeekNo * 3 + 2];
    if (yearType == 13): # M
      idTorah1 = torahSectionsM[torahWeekNo * 3 + 0];
      idTorah2 = torahSectionsM[torahWeekNo * 3 + 1];
      idTorah3 = torahSectionsM[torahWeekNo * 3 + 2];
    if (yearType == 14): # N
      if diaspora:
        idTorah1 = torahSectionsNDiaspora[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsNDiaspora[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsNDiaspora[torahWeekNo * 3 + 2];
      else:
        idTorah1 = torahSectionsNIsrael[torahWeekNo * 3 + 0];
        idTorah2 = torahSectionsNIsrael[torahWeekNo * 3 + 1];
        idTorah3 = torahSectionsNIsrael[torahWeekNo * 3 + 2];

    if (idTorah1 != ID_NULL):
      torahSection = getTorahSectionName(idTorah1);
      if (torahSection != ""):
        if (returnTorahSection != ""):
          returnTorahSection = returnTorahSection + ", ";
        returnTorahSection = returnTorahSection + torahSection;
    if (idTorah2 != ID_NULL):
      torahSection = getTorahSectionName(idTorah2);
      if (torahSection != ""):
        if (returnTorahSection != ""):
          returnTorahSection = returnTorahSection + ", ";
        returnTorahSection = returnTorahSection + torahSection;
    if (idTorah3 != ID_NULL):
      torahSection = getTorahSectionName(idTorah3);
      if (torahSection != ""):
        if (returnTorahSection != ""):
          returnTorahSection = returnTorahSection + ", ";
        returnTorahSection = returnTorahSection + torahSection;

    if (torahDate == shuvahDate):
      if (returnTorahSection != ""):
        returnTorahSection = returnTorahSection + ", ";
      returnTorahSection = returnTorahSection + getTorahSectionName(ID_SHUVA);

    return (returnTorahSection);
  else:
    return "";

def getTorahSectionName(section):
  if (section == ID_BERESHITH):
    return "Bereshith";
  if (section == ID_NOAH):
    return "Noah";
  if (section == ID_LEHLEHA):
    return "Le'h Leha";
  if (section == ID_VAYERA):
    return "Vayera";
  if (section == ID_HAYESARAH):
    return "Haye Sarah";
  if (section == ID_TOLEDOTH):
    return "Toledoth";
  if (section == ID_VAYETSE):
    return "Vayetse";
  if (section == ID_VAYISHLAH):
    return "Vayishlah";
  if (section == ID_VAYESHEB):
    return "Vayesheb";
  if (section == ID_MIKKETS):
    return "Mikkets";
  if (section == ID_VAYIGGASH):
    return "Vayiggash";
  if (section == ID_VAYHEE):
    return "Vayhee";
  if (section == ID_SHEMOTH):
    return "Shemoth";
  if (section == ID_VAERA):
    return "Vaera";
  if (section == ID_BO):
    return "Bo";
  if (section == ID_BESHALLAH):
    return "Beshallah, Shabbat Shirah";
  if (section == ID_YITHRO):
    return "Yithro";
  if (section == ID_MISHPATIM):
    return "Mishpatim";
  if (section == ID_TERUMAH):
    return "Terumah";
  if (section == ID_TETSAVVEH):
    return "Tetsavveh";
  if (section == ID_KITISSA):
    return "Ki Tissa";
  if (section == ID_VAYAKHEL):
    return "Vayakhel";
  if (section == ID_PEKUDE):
    return "Pekude";
  if (section == ID_VAYIKRA):
    return "Vayikra";
  if (section == ID_TSAV):
    return "Tsav";
  if (section == ID_SHEMINI):
    return "Shemini";
  if (section == ID_TAZRIANG):
    return "Tazria";
  if (section == ID_METSORANG):
    return "Metsora";
  if (section == ID_AHAREMOTH):
    return "Aharemoth";
  if (section == ID_KEDOSHIM):
    return "Kedoshim";
  if (section == ID_EMOR):
    return "Emor";
  if (section == ID_BEHAR):
    return "Behar";
  if (section == ID_BEHUKKOTHAI):
    return "Behukkothai";
  if (section == ID_BEMIDBAR):
    return "Bemidbar";
  if (section == ID_NASO):
    return "Naso";
  if (section == ID_BEHAALOTEHA):
    return "Behaaloteha";
  if (section == ID_SHELAHLEHA):
    return "Shelah Leha";
  if (section == ID_KORAH):
    return "Korah";
  if (section == ID_HUKATH):
    return "Hukath";
  if (section == ID_BALAK):
    return "Balak";
  if (section == ID_PINHAS):
    return "Pinhas";
  if (section == ID_MATOTH):
    return "Matoth";
  if (section == ID_MASEH):
    return "Maseh";
  if (section == ID_DEBARIM):
    return "Debarim, Shabbat Hazon";
  if (section == ID_VAETHANAN):
    return "Vaethanan, Shabbat Nahamu";
  if (section == ID_EKEB):
    return "Ekeb";
  if (section == ID_REEH):
    return "Reeh";
  if (section == ID_SHOFETIM):
    return "Shofetim";
  if (section == ID_KITETSE):
    return "Ki Tetse";
  if (section == ID_KITABO):
    return "Ki Tabo";
  if (section == ID_NITSABIM):
    return "Nitsabim";
  if (section == ID_VAYELEH):
    return "Vayeleh";
  if (section == ID_HAAZINU):
    return "Haazinu";

  if (section == ID_SHEKALIM):
    return "Shabbat Shekalim";
  if (section == ID_ZAHOR):
    return "Shabbat Za'hor";
  if (section == ID_PARAH):
    return "Shabbat Parah";
  if (section == ID_HAHODESH):
    return "Shabbat Hahodesh";
  if (section == ID_SHUVA):
    return "Shabbat Shuva";

  return "";

def get_weekday_from_absdate(absdate):
  return absdate % 7

def leap_gregorian(year):
  if ((year % 4) == 0) and \
     ((year % 400) != 100) and \
     ((year % 400) != 200) and \
     ((year % 400) != 300):
    return True
  else:
    return False

def last_day_of_gregorian_month(month, year):
  if leap_gregorian(year) == True and month == 2:
    return 29
  else:
    lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return lengths[month-1]

def hebrew_leap(year):
  if ((((year*7)+1) % 19) < 7):
    return True
  else:
    return False

def hebrew_year_months(year):
  if hebrew_leap(year):
    return 13
  else:
    return 12

def _hebrew_calendar_elapsed_days(year):
  value = 235 * ((year-1) // 19)
  monthsElapsed = value

  value = 12 * ((year-1) % 19)
  monthsElapsed += value

  value = ((((year-1) % 19) * 7) + 1) // 19
  monthsElapsed += value;

  partsElapsed = (((monthsElapsed % 1080) * 793) + 204)
  hoursElapsed = (5 +
                   (monthsElapsed * 12) + \
                   ((monthsElapsed // 1080) * 793) + \
                   (partsElapsed // 1080));

  day = 1 + (29 * monthsElapsed) + (hoursElapsed//24)

  parts = ((hoursElapsed % 24) * 1080) + \
           (partsElapsed % 1080)

  if ((parts >= 19440) or \
      (((day % 7) == 2) and \
       (parts >= 9924)  and \
       (not hebrew_leap(year))) or \
      (((day % 7) == 1) and \
       (parts >= 16789) and \
       (hebrew_leap(year-1)))):
    alternativeDay = day+1
  else:
    alternativeDay = day

  if (((alternativeDay % 7) == 0) or \
      ((alternativeDay % 7) == 3) or \
      ((alternativeDay % 7) == 5)):
    alternativeDay += 1

  return alternativeDay

def days_in_hebrew_year(year):
  return (_hebrew_calendar_elapsed_days(year+1) - \
          _hebrew_calendar_elapsed_days(year))

def _long_heshvan(year):
  if ((days_in_hebrew_year(year) % 10) == 5):
    return True
  else:
    return False

def _short_kislev(year):
  if ((days_in_hebrew_year(year) % 10) == 3):
    return True
  else:
    return False

def hebrew_month_days(year, month):
  if ((month == 2) or \
      (month == 4) or \
      (month == 6) or \
      (month == 10) or \
      (month == 13)):
    return 29
  if ((month == 12) and (not hebrew_leap(year))):
    return 29
  if ((month == 8) and (not _long_heshvan(year))):
    return 29
  if ((month == 9) and (_short_kislev(year))):
    return 29
  return 30

def hebrew_to_absdate(year, month, day):
  value = day
  returnValue = value

  if month < 7:
    for m in range(7,hebrew_year_months(year)+1):
      value = hebrew_month_days(year, m)
      returnValue += value
    for m in range(1,month):
      value = hebrew_month_days(year, m)
      returnValue += value
  else:
    for m in range(7,month):
      value = hebrew_month_days(year, m)
      returnValue += value

  value = _hebrew_calendar_elapsed_days(year)
  returnValue += value

  value = 1373429
  returnValue -= value

  return returnValue

def absdate_to_hebrew(absdate): # year, month, day
  approx = (absdate+1373429) // 366

  y = approx
  while 1:
    temp = hebrew_to_absdate(y+1, 7, 1)
    if absdate < temp:
      break
    y += 1
  year = y

  temp = hebrew_to_absdate(year, 1, 1)
  if absdate < temp:
    start = 7
  else:
    start = 1

  m = start
  while 1:
    temp = hebrew_to_absdate(year, m, hebrew_month_days(year, m))
    if absdate <= temp:
      break
    m += 1
  month = m

  temp = hebrew_to_absdate(year, month, 1)
  day = absdate-temp+1

  return (year, month, day)

#把格里高利日历转换为天数，
def gregorian_to_absdate(year, month, day):
  value = day
  returnValue = value

  for m in range(1,month):
    value = last_day_of_gregorian_month(m, year)
    returnValue += value

  value = (365 * (year-1))
  returnValue += value

  value = ((year-1) // 4)
  returnValue += value

  value = ((year-1) // 100)
  returnValue -= value

  value = ((year-1) // 400)
  returnValue += value

  return returnValue

def absdate_to_gregorian(absdate):
  approx = absdate // 366

  y = approx
  while 1:
    temp = gregorian_to_absdate(y+1, 1, 1)
    if (absdate < temp):
      break
    y += 1
  year = y

  m = 1
  while 1:
    temp = gregorian_to_absdate(year, m, last_day_of_gregorian_month(m, year))
    if (absdate <= temp):
      break
    m += 1
  month = m

  temp = gregorian_to_absdate(year, month, 1)
  day = absdate-temp+1;

  return (year, month, day)
#The FormatTime12 function takes a calculated time and returns a formatted string, in which the time in am/pm format is contained
#The FormatTime24 function takes a calculated time and returns a formatted string, in which the time in 24 hour format is contained
#The GetSunrise function takes the gregorian month, day, year and the location. location is a tuple (latitude, longitude, timezone, elevation) It returns the Sunrise. Elevation is in metres (0 if not known), timezone is relative to GMT, e.g. 1 = GMT+1, for the values of latitude and longitude, the deegrees must be multiplied with hundred and then the minutes added, positive latitudes are north, negative latitudes are south, positive longitudes are east, negative longitudes are west.
#The GetSunriseDeegreesBelowHorizon function takes the gregorian month, day, year, the degrees below horizon and the location and returns the calculated time
#The GetSunset function takes the gregorian month, day, year and location. It returns the Sunset.
#The GetSunsetDeegreesBelowHorizon function takes the month, day, year, degrees below horizon and the location and returns the calculated time
#The AddMinutes function takes the time and the minutes. It returns a time to which minutes were added
#The SubtractMinutes function takes the time and the minutes. It returns a new time from which minutes were subtracted
#The GetProportionalHours function takes the number of the proportional hour, sunrise and the sunset. It returns the calculated time
#The GetShaaZmanit function takes the sunrise and the sunset and returns the length of a proportional hour (Shaa Zmanit)

# FormatTime12, FormatTime24
# GetSunrise, GetSunriseDegreesBelowHorizon
# GetSunset, GetSunsetDegreesBelowHorizon
# AddMinutes, SubtractMinutes
# GetProportionalHours, GetShaaZmanit

# Methods for Shabbat time calculation:
# location is a tuple (latitude, longitude, timezone, elevation)
# For example: Pforzheim has the tuple (4854, 842, 1, 257)
#
# GetSunset(uMonth, uDay, uYear, location)
# GetSunsetDegreesBelowHorizon(uMonth, uDay, uYear,
#                   fDegreesBelowHorizon, location)
# AddMinutes(time, min)
# SubtractMinutes(time, min)

locationPforzheim = (4854, 842, 1, 263)

def FormatTime12(time):
  if time == None:
    return "--:--"

  hour = time[0]
  min = time[1]

  hourModulo12 = hour % 12
  if (hourModulo12 == 0):
    hourModulo12 = 12

  if (hour >= 12):
    ampm = "PM"
  else:
    ampm = "AM"

  if (hourModulo12 < 10):
    hourStr = "0" + str(hourModulo12)
  else:
    hourStr = str(hourModulo12)
  if (min < 10):
    minStr = "0" + str(min)
  else:
    minStr = str(min)
  return hourStr + ":" + minStr + ampm

def FormatTime24(time):
  if time == None:
    return "--:--"

  hour = time[0]
  min = time[1]

  if (hour < 10):
    hourStr = "0" + str(hour)
  else:
    hourStr = str(hour)
  if (min < 10):
    minStr = "0" + str(min)
  else:
    minStr = str(min)
  return hourStr + ":" + minStr

def FormatTimeShaaZmanit(time):
  if time == None:
    return "--:--"

  hour = time[0]
  min = time[1]

  if (hour < 10):
    hourStr = "0" + str(hour)
  else:
    hourStr = str(hour)
  if (min < 10):
    minStr = "0" + str(min)
  else:
    minStr = str(min)
  return hourStr + ":" + minStr

def leap(y):
  if (y % 400 == 0):
    return True
  if (y % 100 != 0):
    if (y % 4 == 0):
      return True
  return False

def doy(d, m, y):
  monCount = [0, 1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
  if ((m > 2) and (leap(y))):
    return monCount[m] + d + 1
  else:
    return monCount[m] + d

def todec(deg, min):
  return (deg + min / 60.0)

def M(x):
  return (0.9856 * x - 3.251)

def L(x):
  return (x + 1.916 * math.sin(0.01745 * x) + 0.02 * math.sin(2 * 0.01745 * x) + 282.565)

def adj(x):
  return (-0.06571 * x - 6.620)

def float_abs(x):
  if (x < 0.0):
    return (-x)
  else:
    return (x)

def suntime(d, m, y, \
            zendeg, zenmin, \
            londeg, lonmin, ew, \
            latdeg, latmin, ns, \
            tz, \
            elevation): # Elevation in meters
  if (zendeg == 90):
    earthRadiusInMeters = 6356.9 * 1000.0
    elevationAdjustment = math.degrees \
      (math.acos(earthRadiusInMeters / (earthRadiusInMeters + elevation)))
    
    z = zendeg + zenmin / 60.0
    z += elevationAdjustment
    zendeg = math.floor(z)
    zenmin = (z - math.floor(z)) * 60
  
  day = doy(d, m, y)
  cosz = math.cos(0.01745 * todec(zendeg, zenmin))
    
  longitude = todec(londeg, lonmin)
  if ew != 0:
    longitude *= -1
  lonhr     = longitude / 15.0
  latitude  = todec(latdeg, latmin)
  if ns != 0:
    latitude *= -1
  coslat    = math.cos(0.01745 * latitude)
  sinlat    = math.sin(0.01745 * latitude)

  t_rise = day + (6.0 + lonhr) / 24.0
  t_set  = day + (18.0 + lonhr) / 24.0

  xm_rise = M(t_rise)
  xl_rise = L(xm_rise)
  xm_set  = M(t_set)
  xl_set  = L(xm_set)
  
  a_rise = 57.29578 * math.atan( 0.91746 * math.tan(0.01745 * xl_rise) )
  a_set  = 57.29578 * math.atan( 0.91746 * math.tan(0.01745 * xl_set) )
  if (float_abs(a_rise + 360.0 - xl_rise) > 90.0):
    a_rise += 180.0
  if (a_rise > 360.0):
    a_rise -= 360.0

  if (float_abs(a_set + 360.0 - xl_set) > 90.0):
    a_set += 180.0
  if (a_set > 360.0):
    a_set -= 360.0

  ahr_rise = a_rise / 15.0
  sindec = 0.39782 * math.sin(0.01745 * xl_rise)
  cosdec = math.sqrt(1.0 - sindec * sindec)
  h_rise = (cosz - sindec * sinlat) / (cosdec * coslat)

  ahr_set = a_set / 15.0
  sindec = 0.39782 * math.sin(0.01745 * xl_set)
  cosdec = math.sqrt(1.0 - sindec * sindec)
  h_set = (cosz - sindec * sinlat) / (cosdec * coslat)

  if (float_abs(h_rise) <= 1.0):
    h_rise = 57.29578 * math.acos(h_rise)
  else:
    return None # NO_SUNRISE

  if (float_abs(h_set) <= 1.0):
    h_set = 57.29578 * math.acos(h_set)
  else:
    return None # NO_SUNSET
  ut_rise  = ((360.0 - h_rise) / 15.0) + ahr_rise + adj(t_rise) + lonhr
  ut_set  = (h_rise / 15.0) + ahr_set + adj(t_set) + lonhr

  returnSunrise = ut_rise + tz  # sunrise
  returnSunset = ut_set  + tz  # sunset
  return (returnSunrise, returnSunset)

def timeadj(t):
  if (t < 0):
    t += 24.0

  hour = int(math.floor(t))
  min  = int(math.floor((t - hour) * 60.0 + 0.5))

  if (min >= 60):
    hour += 1
    min  -= 60

  if (hour > 24):
    hour -= 24

  return [hour, min]

def GetDegreesBelowHorizonAdd(uMonth, uDay, uYear, \
				fDegreesBelowHorizon, \
				location):
  iLatitude, iLongitude, iTimeZone, elevation = location
  if (iLongitude < 0):
    longitudeFlag = 0
  else:
    longitudeFlag = 1
  if (iLatitude < 0):
    latitudeFlag = 1
  else:
    latitudeFlag = 0
  returnTimes = suntime(uDay, uMonth, uYear, \
	      90, 50,  \
	      int(math.floor(math.fabs(iLongitude / 100.0))),  \
		abs(iLongitude) % 100, longitudeFlag, \
	      int(math.floor(math.fabs(iLatitude / 100.0))),  \
		abs(iLatitude) % 100, latitudeFlag, \
	      iTimeZone, elevation);
  if (returnTimes != ""):
    srTime = timeadj(returnTimes[1])
    while (srTime[0] > 12):
      srTime[0] -= 12

    db = fDegreesBelowHorizon + 90.0
    deghour = math.floor(db)
    db = db - deghour
    db *= 60.0
    degmin = math.floor(db)
    returnTimes = suntime(uDay, uMonth, uYear, \
		deghour, degmin, \
		int(math.floor(math.fabs(iLongitude / 100.0))), \
		  abs(iLongitude) % 100, longitudeFlag, \
		int(math.floor(math.fabs(iLatitude / 100.0))),  \
		  abs(iLatitude) % 100, latitudeFlag, \
		iTimeZone, elevation)
    if (returnTimes != ""):
      dbTime = timeadj(returnTimes[1])
      while (dbTime[0] > 12):
        dbTime[0] -= 12

      srTimeValue = srTime[0] * 60 + srTime[1]
      dbTimeValue = dbTime[0] * 60 + dbTime[1]
      return dbTimeValue - srTimeValue
  return None

def GetSunrise(uMonth, uDay, uYear, location):
  iLatitude, iLongitude, iTimeZone, elevation = location
  if (iLongitude < 0):
    longitudeFlag = 0
  else:
    longitudeFlag = 1
  if (iLatitude < 0):
    latitudeFlag = 1
  else:
    latitudeFlag = 0
  returnTimes = suntime(uDay, uMonth, uYear, \
	      90, 50,  \
	      int(math.floor(math.fabs(iLongitude / 100.0))),  \
		abs(iLongitude) % 100, longitudeFlag, \
	      int(math.floor(math.fabs(iLatitude / 100.0))),  \
		abs(iLatitude) % 100, latitudeFlag, \
	      iTimeZone, elevation)
  if (returnTimes != ""):
    returnTime = timeadj(returnTimes[0])
    #print(returnTime)
    
    while (returnTime[0] > 12):
      returnTime[0] -= 12
    
    return returnTime
  else:
    return None

def GetSunriseDegreesBelowHorizon(uMonth, uDay, uYear, \
				      fDegreesBelowHorizon, \
				      location):
  t = GetSunrise(uMonth, uDay, uYear, location)
  if (t != None):
    adding = GetDegreesBelowHorizonAdd(uMonth, uDay, uYear, fDegreesBelowHorizon, location)
    if (adding != None):
      return SubtractMinutes(t, adding)
    else:
      return None
  else:
    return None

def GetSunset(uMonth, uDay, uYear, \
		   location):
  iLatitude, iLongitude, iTimeZone, elevation = location
  if (iLongitude < 0):
    longitudeFlag = 0
  else:
    longitudeFlag = 1
  if (iLatitude < 0):
    latitudeFlag = 1
  else:
    latitudeFlag = 0
  returnTimes = suntime(uDay, uMonth, uYear, \
	      90, 50,  \
	      int(math.floor(math.fabs(iLongitude / 100.0))),  \
		abs(iLongitude) % 100, longitudeFlag, \
	      int(math.floor(math.fabs(iLatitude / 100.0))),  \
		abs(iLatitude) % 100, latitudeFlag, \
	      iTimeZone, elevation)
  if (returnTimes != None):
    returnTime = timeadj(returnTimes[1])

    while (returnTime[0] < 12):
      returnTime[0] += 12

    return returnTime
  else:
    return None

def GetSunsetDegreesBelowHorizon(uMonth, uDay, uYear, \
				      fDegreesBelowHorizon, \
				      location):
  t = GetSunset(uMonth, uDay, uYear, location)
  if (t != ""):
    adding = GetDegreesBelowHorizonAdd(uMonth, uDay, uYear, fDegreesBelowHorizon, location)
    if (adding != None):
      return AddMinutes(t, adding)
    else:
      return None
  else:
    return None

def AddMinutes(time, min):
  if (time == None):
    return None
  time2 = copy.deepcopy(time)
  time2[1] += min
  while (time2[1] >= 60):
    time2[1] -= 60
    time2[0] += 1
  return time2

def SubtractMinutes(time, min):
  if (time == None):
    return None
  time2 = copy.deepcopy(time)
  time2[1] -= min
  while (time2[1] < 0):
    time2[1] += 60
    time2[0] -= 1
  return time2

def GetProportionalHours(value, sunrise, sunset):
  if (sunrise == None or sunset == None):
    return None
  sr = sunrise[0] * 60 + sunrise[1]
  ss = sunset[0] * 60 + sunset[1]
  retval = sr + math.floor(((ss-sr) * value) / 12)
  return [int(math.floor(retval / 60)), int(retval % 60)]

def GetShaaZmanit(sunrise, sunset):
  sr = sunrise[0] * 60 + sunrise[1]
  ss = sunset[0] * 60 + sunset[1]
  return int(math.floor((ss - sr) / 12))

#Daylight Savings Time starts in Israel on the last Friday before 2nd of April and ends on the Sunday between Rosh Hashana and Yom Kippur. The following function isIsraeliDaylightSavingsTime checks for a Gregorian date whether Daylight Savings Time in Israel is in effect on that day or not.

def isIsraeliDaylightSavingsTime(day, month, year):
  absDateStart = gregorian_to_absdate(year,
         4,
         2)
  absDateStart -= 1
  while get_weekday_from_absdate(absDateStart) != 5: # Friday
    absDateStart -= 1

  absDate = gregorian_to_absdate(year, 12, 31)
  heb = absdate_to_hebrew(absDate)
  absDateEnd = hebrew_to_absdate(heb[0], 7, 9) # 9 Tishri
  while get_weekday_from_absdate(absDateEnd) != 0: # Sunday
    absDateEnd -= 1

  absDateNow = gregorian_to_absdate(year, month, day)
  if int(absDateNow) >= int(absDateStart) and int(absDateNow) < int(absDateEnd):
    return True
  else:
    return False





def getJewishMonthName(month, year):
    if month == 1:
        return "Nisan"
    elif month == 2:
        return "Iyyar"
    elif month == 3:
        return "Sivan"
    elif month == 4:
        return "Tammuz"
    elif month == 5:
        return "Av"
    elif month == 6:
        return "Elul"
    elif month == 7:
        return "Tishri"
    elif month == 8:
        return "Heshvan"
    elif month == 9:
        return "Kislev"
    elif month == 10:
        return "Teveth"
    elif month == 11:
        return "Shevat"
    elif month == 12:
        if hebrew_leap(year):
            return "Adar I"
        else:
            return "Adar"

    elif month == 13:
        return "Adar II"


def getWeekdayOfHebrewDate(hebDay, hebMonth, hebYear):
  absdate = hebrew_to_absdate(hebYear, hebMonth, hebDay)
  return get_weekday_from_absdate(absdate)



def calculate_holiday(g_day, g_month, g_year, diaspora):
  absdate = gregorian_to_absdate(g_year, g_month, g_day)
  hebYear, hebMonth, hebDay = absdate_to_hebrew(absdate)

  listHolidays = []
  
  if hebDay == 1:
    listHolidays.append("*.1 New Moon 新月") #新月，每犹太月1号

  # Holidays in Nisan

  hagadolDay = 15 #14号为大安息日，但得要是第6天才行，
  #15号是安息日也行的，因为前天晚上开始，和逾越节一样，原来算法有误

  #应该是这样算的，创世第1天，从晚上休息开始，然后，到第1天早上，然后第2天晚上
  #所以，绝对日子数%7, 得到的结果，如果是0, 代表7, 代表开始了第1日的晚上
  #如果得到的结果是6，则表示，开始了第7日的晚上，开始安息日
  #这样直接以逾越节为计算，看看是不是开始第7天安息日，不是就前推找到安息日
  #这样的话，耶稣的被杀日，应该以这个大安息日为准，
  #但耶稣时的大安息日，好像就是14号，这样的话，就能重合了
  while getWeekdayOfHebrewDate(hagadolDay, 1, hebYear) != 6: #等于6好像是意味着白天为安息日，确实，等于6的安息日，其实从等于5的前一天晚上开始的
    hagadolDay -= 1
  if hebDay == hagadolDay-1 and hebMonth == 1:
    listHolidays.append(f'预备日/按安息日计算，耶稣受难是周五\n晚上开始大安息日休息/耶稣开始安息')
  if hebDay == hagadolDay and hebMonth == 1:
    listHolidays.append(f"1.{hagadolDay} Shabat Hagadol 大安息日") 
    listHolidays.append(f"1.{hagadolDay} Shabat Hagadol 大安息日\n耶稣安息在新坟墓里至晚上") 
  if hebDay == hagadolDay+1 and hebMonth == 1:
    listHolidays.append(f"1.{hagadolDay+1} 耶稣复活日，第一日早晨被见证\n第七日晚上至第一日早晨之间复活") 

  if hebDay == 14 and hebMonth == 1: #逾越节是安息日吗？不知道。天数是以absdate算的
    listHolidays.append("1.14 Erev Pesach 逾越节前日\n(白天已经14号，14日晚上开始逾越节)\n逾越节晚上，羔羊被杀日")
  if hebDay == 15 and hebMonth == 1:
    listHolidays.append("1.15 Pesach I 逾越节I\n逾越节次日，15号Omer献禾捆")
    listHolidays.append("1.15 耶稣安息在新坟墓日\n但耶稣受难时的逾越节次日和安息日是同一天")
  if hebDay == 16 and hebMonth == 1:
    listHolidays.append("1.16 2022年的复活之日，正是主日，\n在22年的时候，逾越节也是受难日，和那时一样")
    if diaspora:
      listHolidays.append("1.16 Pesach II 逾越节II 流散于外的犹太人")
    else:
      listHolidays.append("1.16 Chol Hamoed 中间日")
  if hebDay == 17 and hebMonth == 1:
    listHolidays.append("1.17 Chol Hamoed 中间日")
  if hebDay == 18 and hebMonth == 1:
    listHolidays.append("1.18 Chol Hamoed 中间日")
  if hebDay == 19 and hebMonth == 1:
    listHolidays.append("1.19 Chol Hamoed 中间日")
  if hebDay == 20 and hebMonth == 1:
    listHolidays.append("1.20 Chol Hamoed 中间日")
  if hebDay == 21 and hebMonth == 1:
    if not diaspora:
      listHolidays.append("1.21 Pesach VII (Yizkor) 逾越节VII(纪念德系犹太人)")
    else:
      listHolidays.append("1.21 Pesach VII 逾越节VII")
  if hebDay == 22 and hebMonth == 1:
    if diaspora:
      listHolidays.append("1.22 Pesach VIII (Yizkor) 逾越节VIII(纪念德系犹太人)")

  # Yom Hashoah

  if getWeekdayOfHebrewDate(27, 1, hebYear) == 5:
    if hebDay == 26 and hebMonth == 1:
      listHolidays.append("1.26 Yom Hashoah 大屠杀纪念日")
  elif hebYear >= 5757 and getWeekdayOfHebrewDate(27, 1, hebYear) == 0:
    if hebDay == 28 and hebMonth == 1:
      listHolidays.append("1.28 Yom Hashoah 大屠杀纪念日")
  else:
    if hebDay == 27 and hebMonth == 1:
      listHolidays.append("1.27 Yom Hashoah 大屠杀纪念日")

  # Holidays in Iyar

  # Yom Hazikaron

  if getWeekdayOfHebrewDate(4, 2, hebYear) == 5: # If 4th of Iyar is a Thursday ...
    if hebDay == 2 and hebMonth == 2: # ... then Yom Hazicaron is on 2th of Iyar
      listHolidays.append("2.2 Yom Hazikaron 军人纪念日")
  elif getWeekdayOfHebrewDate(4, 2, hebYear) == 4:
    if hebDay == 3 and hebMonth == 2:
        listHolidays.append("2.3 Yom Hazikaron 军人纪念日")
  elif hebYear >= 5764 and getWeekdayOfHebrewDate(4, 2, hebYear) == 0:
    if hebDay == 5 and hebMonth == 2:
      listHolidays.append("2.5 Yom Hazikaron 军人纪念日")
  else:
    if hebDay == 4 and hebMonth == 2:
      listHolidays.append("2.4 Yom Hazikaron 军人纪念日")

  # Yom Ha'Azmaut

  if getWeekdayOfHebrewDate(5, 2, hebYear) == 6:
    if hebDay == 3 and hebMonth == 2:
      listHolidays.append("2.3 Yom Ha'Atzmaut 独立日")
  elif getWeekdayOfHebrewDate(5, 2, hebYear) == 5:
    if hebDay == 4 and hebMonth == 2:
      listHolidays.append("2.4 Yom Ha'Atzmaut 独立日")
  elif hebYear >= 5764 and getWeekdayOfHebrewDate(4, 2, hebYear) == 0:
    if hebDay == 6 and hebMonth == 2:
      listHolidays.append("2.6 Yom Ha'Atzmaut 独立日")
  else:
    if hebDay == 5 and hebMonth == 2:
      listHolidays.append("2.5 Yom Ha'Atzmaut 独立日")

  if hebDay == 14 and hebMonth == 2:
    listHolidays.append("2.14 Pesach Sheni 第二逾越节")
  if hebDay == 18 and hebMonth == 2:
    listHolidays.append("2.18 Lag B'Omer 篝火节 Omer第33天\nOmer:逾越节第二天素祭")
  if hebDay == 28 and hebMonth == 2:
    listHolidays.append("2.28 Yom Yerushalayim 耶路撒冷日(六日战争的统一)")
  
  #计算耶稣升天的日期，在五旬节，前一周的第七天
  #五旬节是安息日吗？不知道，安息日是以absdate算的。。。创世开始算。。。
  #哪个重要？月份的日子重要还是每周的第几天重要？看第几天为准
  ascendingDay = 28
  while getWeekdayOfHebrewDate(ascendingDay, 2, hebYear) != 6: #5旬节前7天再前推一个安息日
    ascendingDay -= 1
  if hebDay == ascendingDay and hebMonth == 2:
    listHolidays.append(f'2.{ascendingDay} 耶稣升天日，开始安息日的晚上\n或许耶稣是安息日的白天升天的，不知道\n但应该是到父那里过安息日了，毕竟，他的安息')
  #这样的话，用这个函数，来一天天的倒推，
  #找到有一天，那日是预备逾越节的日子，也就是，晚上开始14日，同时，安息日

  # Holidays in Sivan

  if hebDay == 5 and hebMonth == 3:
    listHolidays.append("3.5 Erev Shavuot 七周Omer完成节前日 Omer第49天")
  if hebDay == 6 and hebMonth == 3:
    if diaspora:
      listHolidays.append("3.6 Shavuot I 七周Omer完成节 Omer的第50天\n七七节/领受十诫日/感谢律法节/五旬节/收割节")
    else:
      listHolidays.append("3.6 Shavuot\n(Yizkor) 七周Omer完成节(纪念德系犹太人)")
  if hebDay == 7 and hebMonth == 3:
    if diaspora:
      listHolidays.append("3.7 Shavuot II\n(Yizkor) 七周Omer完成节II(Yizkor)")

  # Holidays in Tammuz

  if getWeekdayOfHebrewDate(17, 4, hebYear) == 6:
    if hebDay == 18 and hebMonth == 4:
      listHolidays.append("4.18 Fast of Tammuz 禁食纪念耶路撒冷攻破节(第二圣殿被毁前)")
  else:
    if hebDay == 17 and hebMonth == 4:
      listHolidays.append("4.17 Fast of Tammuz 禁食纪念耶路撒冷攻破节(第二圣殿被毁前)")

  # Holidays in Av

  if getWeekdayOfHebrewDate(9, 5, hebYear) == 6:
    if hebDay == 10 and hebMonth == 5:
      listHolidays.append("5.10 Fast of Av 纪念耶路撒冷圣殿被毁节")
  else:
    if hebDay == 9 and hebMonth == 5:
      listHolidays.append("5.9 Fast of Av 纪念耶路撒冷圣殿被毁节")
  if hebDay == 15 and hebMonth == 5:
    listHolidays.append("5.15 Tu B'Av 爱之节")

  # Holidays in Elul

  if hebDay == 29 and hebMonth == 6:
    listHolidays.append("6.29 Erev Rosh Hashana 新年前日")

  # Holidays in Tishri

  if hebDay == 1 and hebMonth == 7:
    listHolidays.append("7.1 Rosh Hashana I 新年I(吹角为圣)")
  if hebDay == 2 and hebMonth == 7:
    listHolidays.append("7.2 Rosh Hashana II 新年II")
  if getWeekdayOfHebrewDate(3, 7, hebYear) == 6:
    if hebDay == 4 and hebMonth == 7:
      listHolidays.append("7.4 Tzom Gedaliah 禁食纪念基大利被杀")
  else:
    if hebDay == 3 and hebMonth == 7:
      listHolidays.append("7.3 Tzom Gedaliah 禁食纪念基大利被杀")
  if hebDay == 9 and hebMonth == 7:
    listHolidays.append("7.9 Erev Yom Kippur 赎罪日前日")
  if hebDay == 10 and hebMonth == 7:
    listHolidays.append("7.10 Yom Kippur\n(Yizkor) 赎罪日(Yizkor)")
  if hebDay == 14 and hebMonth == 7:
    listHolidays.append("7.14 Erev Sukkot 住棚节前日")
  if hebDay == 15 and hebMonth == 7:
    if diaspora:
      listHolidays.append("7.15 Sukkot I 住棚节I(感谢秋收)")
    else:
      listHolidays.append("7.15 Sukkot 住棚节(感谢秋收)")
  if hebDay == 16 and hebMonth == 7:
    if diaspora:
      listHolidays.append("7.16 Sukkot II 住棚节II")
    else:
      listHolidays.append("7.16 Chol Hamoed 中间日")
  if hebDay == 17 and hebMonth == 7:
    listHolidays.append("7.17 Chol Hamoed 中间日")
  if hebDay == 18 and hebMonth == 7:
    listHolidays.append("7.18 Chol Hamoed 中间日")
  if hebDay == 19 and hebMonth == 7:
    listHolidays.append("7.19 Chol Hamoed 中间日")
  if hebDay == 20 and hebMonth == 7:
    listHolidays.append("7.20 Chol Hamoed 中间日")
  if hebDay == 21 and hebMonth == 7:
    listHolidays.append("7.21 Hoshana Raba 大赎罪日")
  if hebDay == 22 and hebMonth == 7:
    if not diaspora:
      listHolidays.append("7.22 Shemini Atzereth\n(Yizkor) Sukkot逗留日")
      listHolidays.append("7.22 Simchat Torah 妥拉欣喜(完成一年循环朗读)")
    else:
      listHolidays.append("7.22 Shemini Atzereth\n(Yizkor) Sukkot逗留日")
  if hebDay == 23 and hebMonth == 7:
    if diaspora:
      listHolidays.append("7.23 Simchat Torah 妥拉欣喜(完成一年循环朗读)")

  # Holidays in Kislev

  if hebDay == 25 and hebMonth == 9:
    listHolidays.append("9.25 Chanukka I 奉献节/光明节/马加比节")
  if hebDay == 26 and hebMonth == 9:
    listHolidays.append("9.26 Chanukka II 奉献节/光明节/马加比节")
  if hebDay == 27 and hebMonth == 9:
    listHolidays.append("9.27 Chanukka III 奉献节/光明节/马加比节")
  if hebDay == 28 and hebMonth == 9:
    listHolidays.append("9.28 Chanukka IV 奉献节/光明节/马加比节")
  if hebDay == 29 and hebMonth == 9:
    listHolidays.append("9.29 Chanukka V 奉献节/光明节/马加比节")
  # Holidays in Tevet

  if hebDay == 10 and hebMonth == 10:
    listHolidays.append("10.10 Fast of Tevet 十月禁食节")

  if hebrew_month_days(hebYear, 9) == 30:
    if hebDay == 30 and hebMonth == 9:
      listHolidays.append("9.30 Chanukka VI 奉献节/光明节/马加比节")
    if hebDay == 1 and hebMonth == 10:
      listHolidays.append("10.1 Chanukka VII 奉献节/光明节/马加比节")
    if hebDay == 2 and hebMonth == 10:
      listHolidays.append("10.2 Chanukka VIII 奉献节/光明节/马加比节")
  if hebrew_month_days(hebYear, 9) == 29: #有时29天有时30天呢
    if hebDay == 1 and hebMonth == 10:
      listHolidays.append("10.1 Chanukka VI 奉献节/光明节/马加比节")
    if hebDay == 2 and hebMonth == 10:
      listHolidays.append("10.2 Chanukka VII 奉献节/光明节/马加比节")
    if hebDay == 3 and hebMonth == 10:
      listHolidays.append("10.3 Chanukka VIII 奉献节/光明节/马加比节")

  # Holidays in Shevat

  if hebDay == 15 and hebMonth == 11:
    listHolidays.append("11.15 Tu(15) B'Shevat 树的新年")

  # Holidays in Adar (I)/Adar II

  if hebrew_leap(hebYear):
    monthEsther = 13
  else:
    monthEsther = 12
    
  if getWeekdayOfHebrewDate(13, monthEsther, hebYear) == 6:
    if hebDay == 11 and hebMonth == monthEsther:
      listHolidays.append("Adar.11 Fast of Esther 以斯帖的禁食日")
  else:
    if hebDay == 13 and hebMonth == monthEsther:
      listHolidays.append("Adar.13 Fast of Esther 以斯帖的禁食日")

  if hebDay == 14 and hebMonth == monthEsther:
    listHolidays.append("Adar.14 Purim 抽签节/普珥节")
  if hebDay == 15 and hebMonth == monthEsther:
    listHolidays.append("Adar.15 Shushan Purim 书珊普珥节")

  if hebrew_leap(hebYear):
    if hebDay == 14 and hebMonth == 12:
      listHolidays.append("12.14 Purim Katan 第二普珥节(闰年)")
    if hebDay == 15 and hebMonth == 12:
      listHolidays.append("12.15 Shushan Purim Katan 书珊第二普珥节(闰年)")

  return listHolidays

def getDaysHolidays(gYear, gMonth, gDay):
    holidays = calculate_holiday(gDay, gMonth, gYear, diaspora=True)
    #print(holidays)
    return holidays


def getDaysTorah(gYear, gMonth, gDay):
#for i in range(366):
    diaspora = True
    torahStr = getTorahSections(gMonth, gDay, gYear, diaspora)
    if torahStr != "":
        #print("Torah section(s): " + torahStr)
        return "Torah section(s): " + torahStr
    else:
        #print("No torah section(s) on that day")
        return None

def getMonthTorah():
    today = getdaystime(0)
    year = int(today[:4])
    month = int(today[4:6])
    #gDay = int(today[6:8])
    day = '-'
    diaspora = True
    lastDay = last_day_of_gregorian_month(month, year)
    torahMonth = []
    for day in range(1,lastDay+1):
        torahStr = getTorahSections(month, day, year, diaspora)
        if torahStr != "":
            print(str(day) + "." + str(month) + "."+str(year) + ": " + torahStr)
            torahMonth.append(str(day) + "." + str(month) + "."+str(year) + ": " + torahStr)
    return torahMonth


def getCalendarWeekDayContentDict():#{week1:{day1:[], day2:[]}, week2:{}}
    today = getdaystime(0)
    gYear = int(today[:4])
    gMonth = int(today[4:6])
    gDay = int(today[6:8])
    absdate_today = gregorian_to_absdate(gYear, gMonth, gDay)
    weekDay = {}
    #先手动添加上周数
    weekDay[111] = {}
    for i in "周日", '周一', '周二', '周三', '周四', '周五', '周六':
        weekDay[111][i] = ['weekNumber信息', True]
    dayContent = {}
    lastWeek = None
    
    todayMonthDay = gDay
    todayWeekNumber = int(datetime(gYear, gMonth, gDay).strftime('%U'))
    for days in range(9): #找到本周的第一天的absdate
        absdate = absdate_today - days
        gYear, gMonth, gDay = absdate_to_gregorian(absdate)
        weekNumber = int(datetime(gYear, gMonth, gDay).strftime('%U'))
        if weekNumber != todayWeekNumber: #换上周了，说明下一天是本周第一天
            absdateFirstDay = absdate + 1
            break

    lastWeekNumber = todayWeekNumber
    for days in range(7*40): #遍历60周的天数生成weekDay加上dayContent字典
    #我知道这个bug（60周总是从2023年开始并只有52周）的原因了，因为，用周数作为的key，后面就覆盖了。。。
    #解决方法：让周数不过于52周，或者在前面加上年份即可。限制吧，嗯。别过分贪心。耶稣救我。
        absdate = absdateFirstDay + days
        gYear, gMonth, gDay = absdate_to_gregorian(absdate)
        heYear, heMonth, heDay = absdate_to_hebrew(absdate)
        weekday = get_weekday_from_absdate(absdate)
        weekNumber = int(datetime(gYear, gMonth, gDay).strftime('%U'))
        locationOfIsrael = (31.771959, 35.217018, 2, 754)
        sunRise = GetSunrise(gMonth, gDay, gYear, locationOfIsrael)
        sunSet = GetSunset(gMonth, gDay, gYear, locationOfIsrael)
        holidaysToday = '\n'.join(getDaysHolidays(gYear, gMonth, gDay))
        torahToday = getDaysTorah(gYear, gMonth, gDay)
        ymd = f'{gYear}' + f'{gMonth:02}' + f'{gDay:02}'
            
        texts = []
        texts.append(f'Week: {weekNumber}, Day: {weekday+1}, 西历: {gYear}.{gMonth}.{gDay}')
        texts.append(f'Jewish: {heYear}, {heMonth} {getJewishMonthName(heMonth, heYear)}, {heDay}')
        texts.append(f'Sunrise {sunRise[0]}:{sunRise[1]}, Sunset {sunSet[0]}:{sunSet[1]}')
        texts.append(f'Holiday: {holidaysToday}')
        texts.append(f'Torah: {torahToday}')
        texts = '\n'.join(texts)
        dayData = []
        dayData.append(texts)
        if holidaysToday:
            dayData.append(True)
        else:
            dayData.append(False)

        if days == 0: #开始第一周
            dayContent = {}
            dayContent[gDay] = dayData
        elif weekNumber != lastWeekNumber: #换下周
            weekDay[lastWeekNumber] = copy.deepcopy(dayContent)
            dayContent = {} #开始一个新的dayContent字典
            dayContent[gDay] = dayData
            lastWeekNumber = weekNumber #开始新的一周
        else:
            dayContent[gDay] = dayData
    
    return weekDay, todayMonthDay, todayWeekNumber
    
def hebrewCalendar(request):
    weekDayContent, todayMonthDay, todayWeekNumber = getCalendarWeekDayContentDict()
    #print(weekDayContent)
    toBeReturned = {}
    toBeReturned['weekDayContent'] = weekDayContent
    toBeReturned['todayMonthDay'] = todayMonthDay
    toBeReturned['todayWeekNumber'] = todayWeekNumber
    print(todayMonthDay, todayWeekNumber)
    return render(request, 'hebrewCalendar.html', toBeReturned) #原来django的字典返回，网页引用的是字典内的名










