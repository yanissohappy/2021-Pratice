Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

* Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

* The order of output does not matter.

## Example 1:

	Input:
	s: "cbaebabacd" p: "abc"

	Output:
	[0, 6]

	Explanation:
	The substring with start index = 0 is "cba", which is an anagram of "abc".
	The substring with start index = 6 is "bac", which is an anagram of "abc".
	
## Example 2:

	Input:
	s: "abab" p: "ab"

	Output:
	[0, 1, 2]

	Explanation:
	The substring with start index = 0 is "ab", which is an anagram of "ab".
	The substring with start index = 1 is "ba", which is an anagram of "ab".
	The substring with start index = 2 is "ab", which is an anagram of "ab".

## [原題目連結點我](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

## 我的心得:
* main.py
* 這個結果會是對的，但是會跑出 TLE QQ
* 簡而言之這版的作法就是先產生要測試的所有排列組合，最後再在`s`字串中所有的 index 一一檢查這個排列組合。
-----

* main1.py
* 是使用`Counter`的寫法，但是這個寫法在測"aaaaaaaaaaaa...aaaaaaaa"和"aaaa...aaaaaaa"(中間都有很多的 a)會 TLE
* 於是必須從這個方法再改進，也就是一開始就直接先 check s 的 Counter 情形，以下改進
-----

* main2.py
* 依舊是用`Counter`的寫法，只是在 sliding window 那邊改進
* 每一個回合都是拔掉第一個字母，塞入 sliding window 的下一個字母
* 並且要小心在拔掉第一個字母的時候，要檢查 Counter 在該字母那邊是否計數個數為 0，若是，那就要把它`del`，否則在判斷`s`和`p`的 Counter 是否相等的時候，會永遠判斷是不同的
* 上述的原因是可能 s 的 Counter 會產生這種例子`{u'a':0}`，而 p 只會有計數個數都是 1 的 Counter。