#常数时间插入、删除和获取随机元素

### 题目地址
https://leetcode-cn.com/problems/insert-delete-getrandom-o1/

###题目描述

设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。

### 思想
实现一个集合
使用字典的话，getRandom存在问题
使用数组的话，remove存在问题

所以采用二者结合实现集合；

数组中存储数组，
字典中存储值到索引的映射．
1. insert 简单
2. remove, 先从字段找到索引，然后数组删除，这时候直接删除数组元素，其后面元素会向前移动，所以采用使用替换的方法，将数组的最后一个元素替换到被删除的位置即可
3. getRandom, 直接使用数组索引随机即可


### 代码
```php
class RandomizedSet {
    /**
     * Initialize your data structure here.
     */
    function __construct() {
        $this->_dict = []; // 哈希表
        $this->_array = []; // 数组
    }
  
    /**
     * Inserts a value to the set. Returns true if the set did not already contain the specified element.
     * @param Integer $val
     * @return Boolean
     */
    function insert($val) {
        if (isset($this->_dict[$val])){
            return False;
        }
        $this->_array[count($this->_array)] = $val;
        $this->_dict[$val] = count($this->_array) - 1;
        return True;
    }
  
    /**
     * Removes a value from the set. Returns true if the set contained the specified element.
     * @param Integer $val
     * @return Boolean
     */
    function remove($val) {
        if (!isset($this->_dict[$val])){
            return False;
        }

        $remove_index = $this->_dict[$val];

        $this->_array[$remove_index] = $this->_array[count($this->_array)-1]; // 最后一个放上去
        unset($this->_array[count($this->_array)-1]); // 删除最后一个
        unset($this->_dict[$val]);

        $this->_dict[$this->_array[$remove_index]] = $remove_index; // 字典改变
        return True;
    }
  
    /**
     * Get a random element from the set.
     * @return Integer
     */
    function getRandom() {
        $rand_index = rand(0, count($this->_array)-1);
        return $this->_array[$rand_index];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * $obj = RandomizedSet();
 * $ret_1 = $obj->insert($val);
 * $ret_2 = $obj->remove($val);
 * $ret_3 = $obj->getRandom();
 */
```
