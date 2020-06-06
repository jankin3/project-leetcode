# 字符串转整数
###题目地址
https://leetcode-cn.com/problems/string-to-integer-atoi/
###题目描述

请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：
本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

### 代码
```php
class Solution {

    /**
     * @param String $str
     * @return Integer
     */
    const INT_MAX = 2147483647;
    const INT_MIN = -2147483648;
    function myAtoi($str) {
        if(empty($str)){
            return 0;
        }
        $result = 0;
        $temp = 1;
        $str = ltrim($str);
        if(empty($str) || (!in_array($str[0], ['+', '-']) && !is_numeric($str[$i]))){
            return 0;
        }
        for($i=0; $i<strlen($str); $i++){
            if ($i==0 && in_array($str[$i], ['+', '-'])){
                $temp = $str[$i] == '+' ? 1 : -1;
            }else if(is_numeric($str[$i])){
                $result = $result*10 + $str[$i];
            }else{
                break;
            }
        }
        $result = $result*$temp;

        if ($result > Solution::INT_MAX){
            return Solution::INT_MAX;
        }
        if ($result < Solution::INT_MIN){
            return Solution::INT_MIN;
        }

        return $result;
    }
}
```
注意：
1. const 是类的常量
2. is_numeric() 判断变量是否是数字或者数字字符串
3. 强转字符串为整形的时候, 如果该字符串以合法的数值开始，则使用该数值。否则其值为 0（零）

