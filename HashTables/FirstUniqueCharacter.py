def UniqueCharacter(word):

    letter_count={}
    for ch in word:
        if ch.isalpha():
            letter_count[ch]=letter_count.get(ch,0)+1
    print(letter_count)
    for i,ch in enumerate(word):
        if letter_count[ch]==1:
            return i
    return -1


if __name__ == "__main__":
    word="leetcode"

    print(UniqueCharacter(word))
