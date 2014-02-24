from phoneticMod import PhoneticMod
import sys

equivChars = [('A', 'E', 'I', 'O', 'U'),
            ('C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Y', 'Z'),
            ('B', 'F', 'P', 'V', 'W'),
            ('D', 'T'),
            ('M', 'N')]

def isEquiv(charOne, charTwo):
    for equiv in equivChars:
        if (charOne in equiv and charTwo in equiv):
            return True
    return False
    
def isMatch(termOne, termTwo):
    if (len(termOne) != len(termTwo)):
        return False
    
    for i in range(0, len(termOne)):
        if (termOne[i] != termTwo[i] and not isEquiv(termOne[i], termTwo[i])):
            return False
        
    return True

def main(argv):
    if (sys.stdin.isatty()):
        sys.stderr.write("ERROR: No stdin\n")
        sys.exit()
        
    names = [line.strip('\n') for line in sys.stdin.readlines()]
    
    if (argv[1]):
        for searchTerm in argv[1:]:
            answers = []
            termOne = PhoneticMod(searchTerm)
            termOne.mod()
            
            for name in names:
                termTwo = PhoneticMod(name)
                termTwo.mod()
                
                if isMatch(termOne._term, termTwo._term):
                    answers.append(name)
                    
                    
            print searchTerm + ": " + ', '.join(answers)
    else:
        sys.stderr.write("ERROR: No search terms\n")
        sys.exit()
    
if __name__ == "__main__":
    sys.exit(main(sys.argv))
