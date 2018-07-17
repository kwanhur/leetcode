package main

import(
    "fmt"
)

type ListNode struct {
    Val int
    Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    if l1 == nil {
        return l2
    }
    if l2 == nil {
        return l1
    }

    root := &ListNode{}
    c := root
    for {
        if l1 != nil && l2 != nil {
            if l1.Val == l2.Val {
                t1, t2 := l1, l2
                l1, l2 = l1.Next, l2.Next
                c.Next, c = t1, t1
                c.Next, c = t2, t2
            }else if l1.Val < l2.Val {
                c.Next, c = l1, l1
                l1 = l1.Next
            }else {
                c.Next, c = l2, l2
                l2 = l2.Next
            }
        }else if l1 == nil {
            c.Next = l2
            break
        }else {
            c.Next = l1
            break
        }
    }
    return root.Next
}

func gen(l []int) *ListNode {
    root := &ListNode{}
    c := root
    for _, v := range l {
        n := &ListNode{Val: v}
        c.Next = n
        c = c.Next
    }
    return root.Next
}

func printList(l *ListNode) {
    if l == nil {
        fmt.Println("")
    }else {
        for l != nil {
            fmt.Printf("%d->", l.Val)
            l = l.Next
        }
        fmt.Println()
    }
}

func main() {
    l1 := gen([]int {2,2,4,5,7,8})
    l2 := gen([]int {1,3,4,5})

    l3 := mergeTwoLists(l1, l2)
    printList(l3)
}
