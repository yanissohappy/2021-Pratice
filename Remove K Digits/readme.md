Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

## Note:
* The length of num is less than 10002 and will be ≥ k.
* The given num does not contain any leading zero.

## Example 1:

	Input: num = "1432219", k = 3
	Output: "1219"
	Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

## Example 2:

	Input: num = "10200", k = 1
	Output: "200"
	Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

## Example 3:

	Input: num = "10", k = 2
	Output: "0"
	Explanation: Remove all the digits from the number and it is left with nothing which is 0.

## [原題目連結點我](https://leetcode.com/problems/remove-k-digits/)

## 我的心得:
* main.py
* 會使用到 stack，想法是現在在 stack 最後一個東西若比現在在比較的 num 大的話，就把 stack pop 掉，因為 pop 掉了，所以 k 要減一（k 表示要減掉的 char 個數），直到`k==0`為止或者是 stack 最後一個東西比現在在比的數值還小。
* 上面的舉動會一直把數值塞入 stack，因為我們保持的順序都是底部的數值要是最小的（或是零也可以）
* 最後要小心可能會有這種`"0000"`、`"0000000"`的 case，這種東西可以利用 Counter 計數 0 的個數是否等於字串長度，若是，則代表該數整個都為 0，於焉完成。