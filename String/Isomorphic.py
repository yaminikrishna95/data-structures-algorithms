def areIsomorphic(s1, s2):
    m1 = {}
    m2 = {}

    for i in range(len(s1)):

        # If character not seen before, store its
        # first occurrence index
        if s1[i] not in m1:
            m1[s1[i]] = i
        if s2[i] not in m2:
            m2[s2[i]] = i
        if m1[s1[i]] != m2[s2[i]]:
            return False
    return True



if __name__ == "__main__":
    s1 = "aab"
    s2 = "xxy"
    if areIsomorphic(s1, s2):
        print("true")
    else:
        print("false")