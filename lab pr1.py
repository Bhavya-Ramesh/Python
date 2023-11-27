def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

        mapping_s_t = {}
    mapping_t_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_t:
            if mapping_s_t[char_s] != char_t:
                return False
        else:
            mapping_s_t[char_s] = char_t
