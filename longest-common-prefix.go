package main

import(
    "fmt"
)


func longestCommonPrefix(strs []string) string {
    if len(strs) == 0 {
        return ""
    }

    pre := "-"
    for _, s := range strs {
        if pre == "-" {
            pre = s
        }else if pre == ""{
            break
        }else {
            l, l2 := len(pre), len(s)
            if l > l2 {
                l, pre = l2, pre[:l2]
            }
            for i:= 0; i < l; i++ {
                if pre[i] != s[i] {
                    pre = pre[:i]
                    break
                }
            }
        }
    }
    return pre
}

func main() {
    s := []string {"aa", "a"}
    fmt.Println(longestCommonPrefix(s))
    s = []string {"dog"}
    fmt.Println(longestCommonPrefix(s))
    s = []string {"dog", "racecar", "car"}
    fmt.Println(longestCommonPrefix(s))
    s = []string {"flower", "flow", "fligth"}
    fmt.Println(longestCommonPrefix(s))
    s = []string {""}
    fmt.Println(longestCommonPrefix(s))
}
