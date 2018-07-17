package main

import(
    "fmt"
)

func twoSum(nums []int, target int) []int {
    res := make([]int, 2)

    count := len(nums)
    ret := make(map[int]int, count)
    num := -1
    for i := 0; i < count; i++ {
        num = target - nums[i] 
        if j, ok := ret[num]; ok {
            res[0] = j
            res[1] = i
            return res
        }else{
            ret[nums[i]] = i
        }
    }
    return res
}

func main(){
    var nums = make([]int, 4)
    nums[0] = 2
    nums[1] = 7
    nums[2] = 11
    nums[3] = 15
    var target = 9
    res := twoSum(nums, target)
    fmt.Println(res)
    target = 19
    res = twoSum(nums, target)
    fmt.Println(res)
}

