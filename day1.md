

## Python下的list、tuple、dict

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

---

### dict

- 使用`name = {key:value, key:value, key:value}`定义一个`dict`。
- 使用`name [key]`查找值。
- 用`key in name`判断key存不存在。
- 或者使用`name.get(key,return)`。
- 使用`name.pop(key)`删除元素。
- `list`或其他可变元素不能作为`dict`的元素。

[^warning]: 如果只定义一个元素的tuple，一定要加一个逗号，否则是赋值操作。