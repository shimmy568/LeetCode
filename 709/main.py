class Solution:
    def charToLowerCase(self, c):
        o = ord(c)
        if o >= ord('A') and o <= ord('Z'):
            return chr(o - (ord('A') - ord('a')))
        return c
        
    def toLowerCase(self, s: str) -> str:
        return ''.join(list(map(lambda x: self.charToLowerCase(x), s)))
