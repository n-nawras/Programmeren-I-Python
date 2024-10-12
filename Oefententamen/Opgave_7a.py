def count_char(zin, let):
    """
    Telt hoe vaak de letter 'let' voorkomt in de string 'zin'.
    
    Parameters:
    zin (str): De zin waarin de frequentie van de letter wordt gezocht.
    let (str): De te zoeken letter.

    Returns:
    int: Het aantal keren dat 'let' voorkomt in 'zin'.
    """
    count = 0
    for char in zin:
        if char == let:
            count += 1
    return count

assert count_char("NMBCPZNCJ", "C") == 2
assert count_char("abcabcabc", "a") == 3 
assert count_char("hello world", "x") == 0
