# Day 3

- 高级特性
  - 切片
  - 迭代
  - 列表生成式
  - 生成器
  - 迭代器
- 函数式编程
- 模块

---

## 高级特性

### 切片

- 使用切片操作符`listname[start : end : step]`获取元素。
- 切片可以对`list`、`tuple`、`字符串`进行操作。

### 迭代

- 在Python中，迭代通过`for...in...`实现。
- 迭代`dict`：
  - 迭代`key`：`for key in dict`
  - 迭代`value`：`for value in dict.values()`
  - 同时迭代：`for key,value in dict.items()`
- 使用`collection`模块中的`Iterable`判断对象是否可迭代。
- 使用Python内置的`enumerate`函数可以把一个list变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身。

### 列表生成式

- 使用`list = [生成元素表达式  生成元素条件式]`生成一个`list`。
- 条件式可以多层，表达式可以有多个变量，或是函数。

### 生成器generator

- 通过某种算法在循环过程中得出元素，一边循环一边计算。可以用`next()`调用下一个值。
  - 把列表生成式的`[]`改成`()`,使用`for`调用元素。
  - 一个函数定义中包含`yield`关键字，那么这个函数就不再是一个普通函数，而是一个generator。但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中。

### 迭代器Iterator

- 凡是可作用于for循环的对象都是Iterable类型；凡是可作用于next()函数的对象都是Iterator类型。
- 集合数据类型如`list`、`dict`、`str`等是`Iterable`但不是`Iterator`，不过可以通过`iter()`函数获得一个`Iterator`对象。
- 

