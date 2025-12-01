class Solution:
    def isValid(self, s: str) -> bool:
        open_paren = ['(', '{', '[']
        close_paren = [')', '}', ']']
        data = []
        for chr in s:
            if chr in open_paren:
                data.append(chr)
            else:
                if not data:
                    return False
                last = data.pop()
                if open_paren.index(last) != close_paren.index(chr):
                    return False
       
        return len(data) == 0

            

        