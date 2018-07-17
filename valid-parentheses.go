package main

import(
    "fmt"
)

func isValid(s string) bool {
    if s == "" {
        return true
    }
    length := len(s)
    if length % 2 == 1 {
        return false
    }

    l := make([]byte, length)
    last := -1
    for _, d := range s {
        c := byte(d)
        if c == '(' || c == '{' || c == '[' {
            last += 1
            l[last] = c
            continue
        }else if c == ')' {
            if last == -1 || l[last] != '(' {
                return false
            }
            l[last] = '-'
        }else if c == '}' {
            if last == -1 || l[last] != '{' {
                return false
            }
            l[last] = '-'
        }else if c == ']' {
            if last == -1 || l[last] != '[' {
                return false
            }
            l[last] = '-'
        }else {
            return false
        }
        last -= 1
    }
    return l[0] == '-'
}

func main() {
    fmt.Println(isValid("") == true)
    fmt.Println(isValid("()") == true)
    fmt.Println(isValid("({") == false)
    fmt.Println(isValid("({[[") == false)
    fmt.Println(isValid("({}(") == false)
    fmt.Println(isValid("({})") == true)
    fmt.Println(isValid("}}]]") == false)
    fmt.Println(isValid("([)]") == false)
}
