# Day 1

- 数据类型和字符串输入输出格式化
- Python下的list、tuple、dict、set
- 条件判断、循环

---

## 数据类型和字符串输入输出格式化

### 数据类型
- 任意大小的整数（十六进制加`0x`前缀），浮点数（可以用科学计数法表示`1.2e9`)
- 布尔值、空值`none`、变量、常量

### 字符串
- 使用 \' \' 或 \" \" 包裹的字符串，使用 \\ 进行转义。
- 使用`r`使引号内的字符默认不转义

### 输入
- 使用`name=input('tips')`输入

### 输出
- 输出使用`print()`
- 使用 \'\'\' 可以进行多行输出

### 格式化
- 使用`%`输出（`%`的转义需要`%%`)
- 常见的占位符有：
    - %d	整数
    - %f	浮点数
    - %s	字符串
    - %x	十六进制整数
- 使用`format()`格式化，传入参数用`{0}`、`{1}`...占位符

---

## Python下的list、tuple、dict、set

### list

- 使用`name=['first','second','third']`定义一个`list`。
- 使用`len()`获得list的元素个数。
- 使用索引`name[value]`可以查看元素。（可以使用-1等负数可以倒叙查看）
- list是可变的
    + 使用`name.append('fourth')`可以添加元素。
    + 使用`name.insert(value, 'add')`可以插入元素。
    + 使用`name.pop(value)`可以删除元素。
    + 使用`name[value] = xxx`可以直接赋值给对应位置。、
- `list`可以嵌套。
- `list`可以是空的，长度为0。

### tuple

- 使用`name=('first','second','third')`定义一个`tuple`。
- 因为`tuple`是不可变的，所以改变list的方法不可用，但是`len()` `name[value]`等方法是可用的。
- 由于`tuple`不可变，所以定义的时候就必须确定元素[^warning] 
- `tuple`里的`list`可以改变。 

### dict

- 使用`name = {key:value, key:value, key:value}`定义一个`dict`。
- 使用`name [key]`查找值。
- 用`key in name`判断key存不存在。
- 或者使用`name.get(key,return)`。
- 使用`name.pop(key)`删除元素。
- `list`或其他可变元素不能作为`dict`的key。

### set

- 使用`name = ([1,2,3])`定义一个`set`。（`set`无序不重复）
- 使用`add(key)`和`remove(key)`添加或移除key。
- 不可用可变元素作为`set`的key。

---

## 条件判断、循环

### 条件判断

- 使用`if`进行条件判断，注意`:`，可以有多个`elif`，从上至下执行，一旦为`True`就跳出循环。
	> age = 3
	>	if age >= 18:
    >		print('adult')
	>	elif age >= 6:
    >		print('teenager')
	>	else:
    >		print('kid')

### 循环

- 进行`for x in y`循环，把y中元素代入x中执行循环语句。
- 使用`range()`可以输出顺序序列。
- 进行`while x:`循环，直至不满足x的条件。
- `break`和`continue`的用法和C语言一样，需要配合`if`使用。

---

2019年11月18日
李子夏

[^warning]: 如果只定义一个元素的tuple，一定要加一个逗号，否则是赋值操作。