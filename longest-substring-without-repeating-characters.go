package main

import(
    "fmt"
)


func lengthOfLongestSubstring(s string) int {
    if s == ""{
        return 0
    }

    i := 0
    longest := -1

    subs := make(map[rune]int)
    for j, c := range s{
        if p, ok := subs[c]; ok && p >= i{
            i = p +1
        }
        if tmp := j - i + 1; tmp > longest{
            longest = tmp
        }
        subs[c] = j
    }
    return longest
}

func lengthOfLongestSubstring2(s string) int {
    if s == ""{
        return 0
    }

    i := 0
    j := 0
    longest := -1
    length := len(s)

    subs := make(map[byte]int)
    for j < length{
        c := s[j]
        if p, ok := subs[c]; ok{
            if p >= i{
                i = p + 1
            }
        }
        tmp := j - i + 1
        if tmp > longest{
            longest = tmp
        }
        subs[c] = j
        j++
    }
    return longest
}

func main() {
    fmt.Println(lengthOfLongestSubstring("bbbb"))
    fmt.Println(lengthOfLongestSubstring("b"))
    fmt.Println(lengthOfLongestSubstring("bba"))
    fmt.Println(lengthOfLongestSubstring("bacbc"))
    fmt.Println(lengthOfLongestSubstring("cdvgedd"))
    fmt.Println(lengthOfLongestSubstring("kkddv"))
}
