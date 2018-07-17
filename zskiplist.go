package main

import (
	"fmt"
	"math/rand"
	"time"
)

const (
	ZSKIPLIST_MAX_LEVEL = 32
	ZSKIPLIST_P         = 0.25
)

type zskiplistLevel struct {
	Forward *zskiplistNode
	Span    int //节点与节点间的跨度
}

type zskiplistNode struct {
	Key   int
	Value int
	Level []*zskiplistLevel
}

type zskiplist struct {
	Header *zskiplistNode
	Level  int
}

func (zslNode *zskiplistNode) equal(node *zskiplistNode) bool {
	if node == nil {
		return false
	}
	return zslNode.Key == node.Key && zslNode.Value == node.Value
}

func zslCreateNode(key int, value int) *zskiplistNode {
	node := &zskiplistNode{Key: key, Value: value, Level: make([]*zskiplistLevel, ZSKIPLIST_MAX_LEVEL)}
	for i := 0; i < ZSKIPLIST_MAX_LEVEL; i++ {
		node.Level[i] = &zskiplistLevel{Span: 0}
	}
	return node
}

func zslCreate() *zskiplist {
	return &zskiplist{Level: 0, Header: zslCreateNode(0, 0)}
}

func zslRandomLevel() int {
	ran := rand.New(rand.NewSource(time.Now().UnixNano()))
	level := ran.Intn(ZSKIPLIST_MAX_LEVEL)
	if level <= 0 {
		level = 1
	}
	return level
}

func (zsl *zskiplist) zslInsert(key int, value int) *zskiplistNode {
	update := make([]*zskiplistNode, ZSKIPLIST_MAX_LEVEL)
	header := zsl.Header
	//lookup position to insert
	for i := zsl.Level - 1; i >= 0; i-- {
		for header.Level[i].Forward != nil {
			if header.Level[i].Forward.Key < key ||
				(header.Level[i].Forward.Key == key && header.Level[i].Forward.Value < value) {
				header = header.Level[i].Forward // insert here
			} else {
				break
			}
		}
		update[i] = header
	}
	//locate at which level
	level := zslRandomLevel()
	//lastLevel := zsl.Level
	if level > zsl.Level {
		for i := zsl.Level; i < level; i++ {
			update[i] = zsl.Header
		}
		zsl.Level = level //max level in used
	}
	//insert data node
	node := zslCreateNode(key, value)
	for i := 0; i < level; i++ {
		node.Level[i].Forward = update[i].Level[i].Forward
		update[i].Level[i].Forward = node
		update[i].Level[i].Span = 1

	}
	return node
}

func (zsl *zskiplist) zslDeleteNode(node *zskiplistNode, update []*zskiplistNode) {
	for i := 0; i < zsl.Level; i++ {
		if update[i].Level[i].Forward != nil && update[i].Level[i].Forward.equal(node) {
			update[i].Level[i].Forward = node.Level[i].Forward
		}
	}
	for zsl.Level > 1 && zsl.Header.Level[zsl.Level-1].Forward == nil {
		zsl.Level -= 1
	}
}

func (zsl *zskiplist) zslDelete(key int, value int) bool {
	update := make([]*zskiplistNode, ZSKIPLIST_MAX_LEVEL)
	header := zsl.Header
	for i := zsl.Level - 1; i >= 0; i-- {
		for header.Level[i].Forward != nil {
			if header.Level[i].Forward.Key < key || (header.Level[i].Forward.Key == key &&
				header.Level[i].Forward.Value < value) {
				header = header.Level[i].Forward
			} else {
				break
			}
		}
		update[i] = header
	}

	node := header.Level[0].Forward
	if node != nil && key == node.Key && value == node.Value {
		zsl.zslDeleteNode(node, update)
		return true
	} else {
		return false
	}
}

func (zsl *zskiplist) zslPrint() {
	header := zsl.Header
	for i := zsl.Level - 1; i >= 0; i-- {
		p := header.Level[i].Forward
		for p != nil {
			fmt.Printf(" %d|%d", p.Key, p.Value)
			p = p.Level[i].Forward
		}
		fmt.Println()
	}
}

func main() {
	zslist := zslCreate()
	zslist.zslInsert(1, 2)
	zslist.zslInsert(4, 5)
	//zslist.zslInsert(2, 2)
	//zslist.zslPrint()
	//zslist.zslInsert(7, 2)
	//zslist.zslInsert(7, 3)
	//zslist.zslInsert(7, 3)
	//zslist.zslPrint()
	//ret := zslist.zslDelete(7, 3)
	//fmt.Println(ret)
	zslist.zslPrint()
}
