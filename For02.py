def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    x=""
    for i in range(n):
        x=x+","+str(i)
        x.lstrip(",")
    return x[1:]
print(main(3))