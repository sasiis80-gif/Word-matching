#function to check whether
#first and last letters of a word match
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word > 1) and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of the words which have first and last characters the same\n", lst)
    return ctr

count = match_words(['abc', 'xyz', 'cfc', 'aba', '1221'])
print("The number of words which have the first and last letter the same:", count)    