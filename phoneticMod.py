import re

class PhoneticMod:
    ignores = ['A', 'E', 'I', 'H', 'O', 'U', 'W', 'Y']
    
    def __init__(self, term):
        self.setSearchTerm(term)
        
    def setSearchTerm(self, term):
        self._term = term.upper()
        
    def removeNonAlpha(self):
        self.setSearchTerm(re.sub(r'[^A-Z]', '', self._term))
        
    def removeIgnores(self):
        cut = self._term[1:]
        self.setSearchTerm(self._term[0] + re.sub('[%s]' % ''.join(self.ignores), '', cut))
        
    def removeDoubles(self):
        self.setSearchTerm(re.sub(r'([A-Z])\1+', r'\1', self._term))
                           
    def mod(self):
        self.removeDoubles()
        self.removeIgnores()
        self.removeNonAlpha()