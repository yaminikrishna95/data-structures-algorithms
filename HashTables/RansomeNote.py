def canConstruct(ransomNote, magazine):
    freq = {}

    # count magazine letters
    for ch in magazine:
        freq[ch] = freq.get(ch, 0) + 1

    # try to build ransomNote
    for ch in ransomNote:
        if freq.get(ch, 0) == 0:
            return False
        freq[ch] -= 1

    return True

if __name__ == "__main__":
    ransomenote="aa"
    magzine="ab"

    print(canConstruct(ransomenote,magzine))