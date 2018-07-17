package main

import(
    "fmt"
)

func isPalindrome(x int) bool {
    if x < 0 || (x != 0 && x % 10 == 0) {
        return false
    }

    ret := 0
    for x > ret {
        ret = ret * 10 + x % 10
        x /= 10
    }
    return ret == x || x == ret / 10
}

func isPalindrome2(x int) bool {
    if x < 0 {
        return false
    }

    x_str := fmt.Sprint(x)
    length := len(x_str)
    for i, c :=  range x_str[:length / 2] {
        if int(c) != int(x_str[length - i - 1]) {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(isPalindrome(10))
    fmt.Println(isPalindrome(-10))
    fmt.Println(isPalindrome(1))
    fmt.Println(isPalindrome(0))
    fmt.Println(isPalindrome(10))
    fmt.Println(isPalindrome(11))
    fmt.Println(isPalindrome(101))
    fmt.Println(isPalindrome(1001))
    fmt.Println(isPalindrome(1000))
    fmt.Println(isPalindrome(1234321))
}
