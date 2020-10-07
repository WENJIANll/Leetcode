# 中序表达式变后序
# A * B + (H / Y + T)
# AB*HY/T++
import string

from pythonds.basic import Stack


def mid2end(s: string):
    slist = s.split()
    stac = Stack()
    outlist = []
    level = {}
    level['*'] = 3
    level['/'] = 3
    level['+'] = 2
    level['-'] = 2
    level['('] = 1  # 因为栈中的元素都需要和下一个扫描到的为运算符的标记作优先级的比较，所以加了‘（’

    for cur in slist:
        # 如果是大写字母（操作数）就将他加在列表的末尾
        if cur in string.ascii_uppercase:
            outlist.append(cur)
        # 如果是‘（’，压入栈
        elif cur == '(':
            stac.push(cur)
        # 如果是‘）’，将除（之外的一切加到列表后面
        elif cur == ')':
            topstac = stac.pop()
            while topstac != '(':
                outlist.append(topstac)
                topstac = stac.pop()
        # 如果是运算符，在将栈内优先级大于等于该运算符优先级的运算符取出加在输出列表的后面之后，再将该运算符压入栈中
        else:
            while (not stac.isEmpty()) and level[stac.peek()] >= level[cur]:
                # 这里是大于等于，因为在栈中已存在的元素代表先出现的，所以同级别的运算符按照从左到右的优先级顺序，要将其拿出
                outlist.append(stac.pop())
            stac.push(cur)
    while not stac.isEmpty():
        outlist.append(stac.pop())

    return " ".join(outlist)


# out = mid2end('A * B + ( H / Y + T )')
out = mid2end('( A + B ) * ( C + D )')

print(out)
