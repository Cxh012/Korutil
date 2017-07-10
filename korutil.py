#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
initials = ['g', 'gg', 'n', 'd', 'dd', 'r', 'm', 'b', 'bb', 's', 'ss', '', 'j', 'jj', 'ch', 'k', 't', 'p', 'h']
medials  = ['a', 'ae', 'ya', 'yae', 'eo', 'e', 'yeo', 'ye', 'o', 'wa', 'wae', 'oe', 'yo', 'u', 'wo', 'we', 'wi', 'yu',
           'eu', 'eui', 'i']
finals   = ['', 'g', 'gg', 'gs', 'n', 'nj', 'nh', 'd', 'l', 'lg', 'lm', 'lb', 'ls', 'lt', 'lp', 'lh', 'm', 'b', 'bs',
            's','ss', 'ng', 'j', 'ch', 'k', 't', 'p', 'h']
def kor2rom(str):
    rom = ""
    for char in str:
        unicode = ord(char) - 44032   # 44032 => 0xAC00
        x = int (unicode / (28 * 21))
        y = int (unicode / 28) % 21
        z = unicode % 28
        rom = rom + initials[x] + medials[y] + finals[z] + " "
    return rom

def rom2kor(str):
    rom = str.split(' ')
    kor = ""
    for r in rom:
        match = re.match("([^aeiouwy]*)([aeiouwy]+)([^aeiouwy]*)",r)
        x = initials.index(match.group(1))
        y = medials.index(match.group(2))
        z = finals.index(match.group(3))
        kor = kor + chr( 44032 + ( x * 21 + y ) * 28 + z )
    return kor

def seubnida(str):
    u = ord(str[-2])
    print(str[-2])
    z = int ( u - 44032 ) % 28
    if z == 0 or z == 8:
        return str[0:-2] + chr(u - z + 17) + "니다"
    else:
        return str[0:-1] + "습니다"

if __name__ == "__main__":
    print(kor2rom("갑니다"))
    print(rom2kor("dol sot bi bim bab"))
    print(seubnida("가다"))