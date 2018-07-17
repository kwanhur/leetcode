package main

import(
    "fmt"
    "bytes"
)

type ListNode struct {
    Val int
    Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    l3 := &ListNode{}
    last := l3
    extra := 0

    for l1 != nil || l2 != nil {
        val1 := 0
        val2 := 0
        if l1 != nil {
            val1 = l1.Val
        }
        if l2 != nil {
            val2 = l2.Val
        }
        val := val1 + val2 + extra
        if val >= 10 {
            val = val - 10
            extra = 1
        }else{
            extra = 0
        }
        last.Next = &ListNode{ Val: val }
        last = last.Next

        if l1 != nil {
            l1 = l1.Next
        }
        if l2 != nil {
            l2 = l2.Next
        }
    }
    if extra == 1 {
        last.Next = &ListNode{ Val:1 }
    }
    return l3.Next
}

func addNext(l *ListNode) *ListNode {
    last := l
    extra := 1
    for {
        val := l.Val + extra
        if val >= 10 {
            val = val - 10
            extra = 1
        }else{
            extra = 0
        }

        l.Val = val
        if extra == 0 {
            if l.Next == nil {
                break
            }else{
                l = l.Next
            }
        }else{
            if l.Next == nil {
                n := &ListNode{ Val: 1 }
                l.Next = n
                break
            }else{
                l = l.Next
            }
        }
    }
    return last
}

func genNode(nums []int) *ListNode {
    l := &ListNode{ Val: nums[0] }
    last := l
    for i := 1; i < len(nums); i++ {
        n := &ListNode{ Val: nums[i] }
        last.Next = n
        last = n
    }
    return l
}

func outputNode(l *ListNode) {
    var buffer bytes.Buffer
    for {
       buffer.WriteString(fmt.Sprint(l.Val))
       if l.Next != nil{
            buffer.WriteString("->")
            l = l.Next
       }else{
            break
       }
    }
    fmt.Println( buffer.String())
}

func main() {
    n1 := make([]int, 3)
    n1[0] = 6
    n1[1] = 4
    n1[2] = 3

    n2 := make([]int, 3)
    n2[0] = 5
    n2[1] = 6
    n2[2] = 6

    l1 := genNode(n1)
    l2 := genNode(n2)
    outputNode(l1)
    outputNode(l2)
    l3 := addTwoNumbers(l1, l2)
    outputNode(l3)

    n3 := make([]int, 1)
    n3[0] = 0
    n4 := make([]int, 2)
    n4[0] = 1
    n4[1] = 8
    l1 = genNode(n3)
    l2 = genNode(n4)
    l3 = addTwoNumbers(l1, l2)
    outputNode(l3)
}
