from collections import Counter
def maxnumberofBallons_optimal(text):
    freq = {}
    for ch in text:
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
    print(freq)


    return min(
        freq.get('b', 0),
        freq.get('a', 0),
        freq.get('l', 0) // 2,
        freq.get('o', 0) // 2,
        freq.get('n', 0)
    )



# Driver Program
text = "loonbalxballpoon"

print(maxnumberofBallons_optimal(text))