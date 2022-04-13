


def jaccard_similariy(setA, setB, alternativeUnion=False):
    

    if isinstance(setA, set) and isinstance(setB, set):

        intersection = len(setA.intersection(setB))

        if alternativeUnion:
            union = len(setA) + len(setB)
        else:
            union = len(setA.union(setB))

        return intersection / union

    if isinstance(setA, (list, tuple)) and isinstance(setB, (list, tuple)):

        intersection = [element for element in setA if element in setB]

        if alternativeUnion:
            union = len(setA) + len(setB)
        else:
            union = setA + [element for element in setB if element not in setA]

        return len(intersection) / len(union)


if __name__ == "__main__":

    setA = {"a", "b", "c", "d", "e"}
    setB = {"c", "d", "e", "f", "h", "i"}
    print(jaccard_similariy(setA, setB))
