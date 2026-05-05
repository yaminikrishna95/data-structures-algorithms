def backspaceCompare(s: str, t: str) -> bool:
    i, j = len(s) - 1, len(t) - 1

    def get_next_valid_char_index(string, idx):
        backspace = 0

        while idx >= 0:
            if string[idx] == "#":
                backspace += 1
                idx -= 1
            elif backspace > 0:
                backspace -= 1
                idx -= 1
            else:
                break

        return idx

    while i >= 0 or j >= 0:
        i = get_next_valid_char_index(s, i)
        j = get_next_valid_char_index(t, j)

        if i < 0 and j < 0:
            return True

        if i < 0 or j < 0:
            return False

        if s[i] != t[j]:
            return False

        i -= 1
        j -= 1

    return True
if __name__ == "__main__":
    arr = "a#c"
    arr2="b"
    print(backspaceCompare(arr,arr2))
