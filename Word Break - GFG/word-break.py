#User function Template for python3

def wordBreak(line, dictionary):
    n = len(line)
    
    dp = [False] * (n + 1)
    dp[n] = True
    
    for i in range(n - 1, -1, -1):
        for w in dictionary:
            if (len(w) <= n - i) and dp[i + len(w)] and (w == line[i:i+len(w)]):
                dp[i] = True
                break
    return dp[0]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends