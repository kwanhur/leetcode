package main

import(
    "fmt"
)

func romanToInt(s string) int {
    roman := map[byte]int {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    last := 0
    ret := 0
    for _, d := range s {
        c := byte(d)
        v, _ := roman[c]
        if v > last {
            ret += v - 2 * last
        }else{
            ret += v
        }
        last = v
    }
    return ret
}

func romanToInt3(s string) int {
    roman := map[byte]int {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rule := map[byte]byte {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C'}
    var last byte
    ret := 0
    for _, d := range s {
        c := byte(d)
        v, _ := roman[c]
        if c != 'I' {
            d, _ := rule[c]
            if last == d {
                r, _ := roman[last]
                ret += v - 2 * r
            }else{
                ret += v
            }
        }else{
            ret += v
        }
        last = c
    }
    return ret
}

func romanToInt2(s string) int {
    roman := map[byte]int {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rule := map[byte]byte {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C'}

    ret := 0
    i := 0
    length := len(s)
    for i < length {
        c := s[i]
        v, _ := roman[c]
        if i + 1 < length && s[i + 1] != 'I' {
            if d, _ := rule[s[i + 1]]; d == c {
                r, _ := roman[s[i + 1]]
                ret += r - v
                i += 2
                continue
            }
        }
        ret += v
        i += 1
    }
    return ret
}

func main() {
    fmt.Println(romanToInt("III"))
    fmt.Println(romanToInt("IV"))
    fmt.Println(romanToInt("LVIII"))
    fmt.Println(romanToInt("MCMXCIV"))
}
