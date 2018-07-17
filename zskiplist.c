#include<stdio.h>
#include<stdlib.h>
 
#define ZSKIPLIST_MAXLEVEL 32
#define ZSKIPLIST_P 0.25
#include <math.h>
 
//跳表节点
typedef struct zskiplistNode {
    int key;
    int value;
    struct zskiplistLevel {
        struct zskiplistNode *forward;
    } level[1];
} zskiplistNode;
 
//跳表
typedef struct zskiplist {
    struct zskiplistNode *header;
    int level;
} zskiplist;

//创建跳表的节点
zskiplistNode *zslCreateNode(int level, int key, int value) {
    zskiplistNode *zn = (zskiplistNode *)malloc(sizeof(*zn)+level*sizeof(zn->level));
    zn->key = key;
    zn->value = value;
    return zn;
}

//初始化跳表
zskiplist *zslCreate(void) {
    int j;
    zskiplist *zsl;
    zsl = (zskiplist *) malloc(sizeof(*zsl));
    zsl->level = 1;//将层级设置为1
    zsl->header = zslCreateNode(ZSKIPLIST_MAXLEVEL,NULL,NULL);
    for (j = 0; j < ZSKIPLIST_MAXLEVEL; j++) {
        zsl->header->level[j].forward = NULL;
    }
    return zsl;
}

//向跳表中插入元素时，随机一个层级，表示插入在哪一层
int zslRandomLevel(void) {
    int level = 1;
    while ((rand()&0xFFFF) < (ZSKIPLIST_P * 0xFFFF))
        level += 1;
    return (level<ZSKIPLIST_MAXLEVEL) ? level : ZSKIPLIST_MAXLEVEL;
}

//向跳表中插入元素
zskiplistNode *zslInsert(zskiplist *zsl, int key, int value) {
    zskiplistNode *update[ZSKIPLIST_MAXLEVEL], *x;
    int i, level;
    x = zsl->header;
    //在跳表中寻找合适的位置并插入元素
    for (i = zsl->level-1; i >= 0; i--) {
        while (x->level[i].forward &&
            (x->level[i].forward->key < key ||
                (x->level[i].forward->key == key &&
                x->level[i].forward->value < value))) {
            x = x->level[i].forward;
        }
        update[i] = x;
    }
    //获取元素所在的随机层数
    level = zslRandomLevel();
    if (level > zsl->level) {
        for (i = zsl->level; i < level; i++) {
            update[i] = zsl->header;
        }
        zsl->level = level;
    }
    //为新创建的元素创建数据节点
    x = zslCreateNode(level,key,value);
    for (i = 0; i < level; i++) {
        x->level[i].forward = update[i]->level[i].forward;
        update[i]->level[i].forward = x;
    }
    return x;
}

//跳表中删除节点的操作
void zslDeleteNode(zskiplist *zsl, zskiplistNode *x, zskiplistNode **update) {
    int i;
    for (i = 0; i < zsl->level; i++) {
        if (update[i]->level[i].forward == x) {
            update[i]->level[i].forward = x->level[i].forward;
        }
    }
    //如果层数变了，相应的将层数进行减1操作
    while(zsl->level > 1 && zsl->header->level[zsl->level-1].forward == NULL)
        zsl->level--;
}

//从跳表中删除元素
int zslDelete(zskiplist *zsl, int key, int value) {
    zskiplistNode *update[ZSKIPLIST_MAXLEVEL], *x;
    int i;
    x = zsl->header;
    //寻找待删除元素
    for (i = zsl->level-1; i >= 0; i--) {
        while (x->level[i].forward &&
            (x->level[i].forward->key < key ||
                (x->level[i].forward->key == key &&
                x->level[i].forward->value < value))) {
            x = x->level[i].forward;
        }
        update[i] = x;
    }
    x = x->level[0].forward;
    if (x && key == x->key && x->value == value) {
        zslDeleteNode(zsl, x, update);
        //别忘了释放节点所占用的存储空间
        free(x);
        return 1;
    } else {
        //未找到相应的元素
        return 0;
    }
    return 0;
}

//将链表中的元素打印出来
void printZslList(zskiplist *zsl) {
    zskiplistNode  *x;
    x = zsl->header;
    for (int i = zsl->level-1; i >= 0; i--) {
        zskiplistNode *p = x->level[i].forward;
        while (p) {
            printf(" %d|%d ",p->key,p->value);
            p = p->level[i].forward;
        }
        printf("\n");
    }
}

int main() {
    zskiplist *list = zslCreate();
    zslInsert(list,1,2);
    zslInsert(list,4,5);
    zslInsert(list,2,2);
    zslInsert(list,7,2);
    zslInsert(list,7,3);
    zslInsert(list,7,3);
    printZslList(list);
    //zslDelete(list,7,2);
    printZslList(list);
}
