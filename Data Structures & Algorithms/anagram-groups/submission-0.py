class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for i,s in enumerate(strs):
        
            unicode = [ord(char) for char in s]
            unicode.sort()
            keyVal = "".join(str(x) for x in unicode)

            if keyVal not in result:
                result[keyVal] = [s]
            else:
                result[keyVal].append(s)
    
        final_output = list(result.values())
        
        return final_output
        