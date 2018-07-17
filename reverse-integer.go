package main

import(
    "fmt"
)

const(
    INT_MAX = (1 << 31 -1) / 10
    INT_MIN = (-1 << 31) / 10
)

func reverse(x int) int {
    if x == 0{
        return x
    }

    int_max := (1 << 31 -1) / 10
    int_min := (-1 << 31) / 10

    ret := 0
    for x != 0{
        v := x % 10
        x /= 10
        if ret > int_max || (ret == int_max && v > 7){
            return 0
        }
       if ret < int_min || (ret == int_min && v < -8){
            return 0
        }

        ret = ret * 10 + v
    }
    return ret
}

func main(){
    fmt.Println(INT_MAX)
    fmt.Println(INT_MIN)
    fmt.Println(reverse(1000))
    fmt.Println(reverse(1001))
    fmt.Println(reverse(-1000))
    fmt.Println(reverse(-1002))
    fmt.Println(reverse(9992))
    fmt.Println(reverse(-1563847412))
    fmt.Println(reverse(-1463847412))
}
