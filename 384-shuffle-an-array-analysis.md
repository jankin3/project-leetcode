# 打乱数组

### 题目地址
https://leetcode-cn.com/problems/shuffle-an-array/

### 题目描述
打乱一个没有重复元素的数组。

```java
示例:

// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();

```
### 思想
数组随机的做法也就是对索引进行随机，然后返回值
做法一：
打乱一个数组的做法可以多次抽出旧的数组的数据到新的数组，然后用旧的数组的末尾补充到刚才拿走的位置
做法二：
对于一的做法，不使用额外数组．在一个数组中，对于当前位置ｘ放置一个随机元素，随机元素在x->n-1个索引中选择．然后使用交换的方法，　交换ｘ与target_index元素即可

### 代码
```php
class Solution {
    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
        $this->originList = $nums;
        $this->currentList = $this->originList;
    }
  
    /**
     * Resets the array to its original configuration and return it.
     * @return Integer[]
     */
    function reset() {
        return $this->originList;
    }
  
    /**
     * Returns a random shuffling of the array.
     * @return Integer[]
     */
    function shuffle() {
        $len = count($this->originList);
        for($i=0;$i<$len;$i++){
            $rand_index = rand($i, $len-1);
            # exchange
            $temp = $this->currentList[$i];
            $this->currentList[$i] = $this->currentList[$rand_index];
            $this->currentList[$rand_index] = $temp;
        }
        return $this->currentList;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = Solution($nums);
 * $ret_1 = $obj->reset();
 * $ret_2 = $obj->shuffle();
 */

```