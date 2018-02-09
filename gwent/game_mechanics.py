def duel(a, b):
    if b < a:
        return b
    return a + duel(b-a, a)
