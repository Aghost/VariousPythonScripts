#!/usr/bin/env python3

class Solution:
    def romanToInt(self, s: str) -> int:

        dic = {
                'I' : 1,
                'V' : 5,
                'X' : 10,
                'C' : 50,
                'L' : 100,
                'D' : 500,
                'M' : 1000,
        }

        total = 0
        curr = 0
        prev = 0

        for i in range(len(s)):
            curr = dic[s[i]]
            if curr > prev:
                total = total + curr - 2 * prev
            else:
                total += curr

            prev = curr

        return total

    def intToRoman(self, src : int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]

        roman_num = ''
        i = 0

        while src > 0:
            for _ in range(src // val[i]):
                roman_num += syb[i]
                src -= val[i]
            i += 1

        return roman_num

print(Solution.romanToInt("", "VXDDMXX"))
print(Solution.intToRoman("", 549))
