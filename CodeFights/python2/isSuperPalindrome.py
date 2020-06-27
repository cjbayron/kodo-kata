def isSuperPalindrome(s, k):
    k <<= 1
    while k < len(s):
    	print s[:k/2] + " : " + s[k-1:k/2 - 1:-1] 
        if s[:k/2] != s[k-1:k/2 - 1:-1]:
            return False
        k <<= 1
    
    return True

print isSuperPalindrome("654neveroddoreven456", 5)
print isSuperPalindrome("www", 1)