You are given two strings s and t.

* String t is generated by random shuffling string s and then add one more letter at a random position.

* Return the letter that was added to t.

 

## Example 1:

	Input: s = "abcd", t = "abcde"
	Output: "e"
	Explanation: 'e' is the letter that was added.

## Example 2:

	Input: s = "", t = "y"
	Output: "y"

## Example 3:

	Input: s = "a", t = "aa"
	Output: "a"
	
## Example 4:

	Input: s = "ae", t = "aea"
	Output: "a"
 

## Constraints:

* 0 <= s.length <= 1000
* t.length == s.length + 1
* s and t consist of lower-case English letters.

## [原題目連結點我](https://leetcode.com/problems/find-the-difference/)

## 我的心得:
* main.py
* 檢查`s`的時候就加入字典裡，如果沒有在字典裡就將其個數設為一，若有在字典裡了就直接個數加一(若直接寫加一會有沒有初始值的問題)
* 檢查`t`的時候就把字典相對應的字母的個數減掉，若個數被減為 0 了，或者根本沒有這個字母存在於字典裡，則代表此為 extra letter