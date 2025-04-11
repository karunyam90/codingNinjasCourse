# Problem statement
# You have been given a circular array/list ‘ARR’ containing ‘N’ integers. You have to find out the maximum possible sum of a non-empty subarray of ‘ARR’.
#
# A circular array is an array/list in which the end of the array connects to the beginning of the array.
#
# A subarray may only include each element of the fixed buffer of ‘ARR’ at most once. (Formally, for a subarray ‘ARR[i]’, ‘ARR[i+1]’, ..., ‘ARR[j]’, there does not exist ‘i’ <= ‘k1’, ‘k2’ <= ‘j’ with ‘k1’ % ‘N’ = k2 % ‘N’.)
#
# For Example:
#
# The ‘ARR’ = [1, 2, -3, -4, 5], the subarray [5, 1, 2] has the maximum possible sum which is 8. This is possible as 5 is connected to 1 because ‘ARR’ is a circular array.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 10^5
# -10^5 <= ARR[i] <= 10^5
#
# Time Limit: 1 sec
# Sample Input 1:
# 2
# 3
# -2 -3 -1
# 4
# 1 2 3 4
# Sample Output 1:
# -1
# 10
# Explanation Of Sample Input 1:
# For the first test case:
# The sub-array [-1] in the given ‘ARR’ has the maximum sum which is -1.
#
# For the second test case:
# The sub-array [1, 2, 3, 4] in the given ‘ARR’ has the maximum sum which is 10.
# Sample Input 2:
# 2
# 4
# 3 1 -2 9
# 1
# 10
# Sample Output 2:
# 13
# 10
# Explanation Of Sample Input 2:
# For the first test case:
# The sub-array [9, 3, 1]  in the given ‘ARR’ has the maximum sum which is 13. Since ‘ARR’ is a circular array/list,  9 is connected to 3.
#
# For the second test case:
# The sub-array [10] in the given  ‘ARR’ has the maximum sum which is 10.
# Python (3.5)
# 123
def maxSubarraySum(arr, n):
	 pass

# maxSubarraySum([1,-2,-3,4,5],5)

