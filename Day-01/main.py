from typing import List, Tuple


def part1(l1: List[int], l2: List[int]):
    """
    Calculate the sum of distances between pairs of least values
    """

    diffs = 0

    for i, j in zip(sorted(l1), sorted(l2)):
        diffs += abs(i-j)

    print(f"Sum of LID diffs:  {diffs}")


def part2(l1: List[int], l2: List[int]):
    """
    Calculate Similarity Score of two lists:
    Sum of products of freqency of vales in <l1> appearance
    in <l2>
    """

    similarity_score = 0

    for i in l1:
        similarity_score += i * l2.count(i)

    print(f"Similarity Score:  {similarity_score}")


def parse_input(in_file: str) -> Tuple[List[int]]:
    """
    Parse puzzle input into two lists of intetegers and return
    a Tuple of those lists
    """

    l1 = []
    l2 = []

    with open(in_file, "r") as f:
        for line in f.readlines():
            v1, v2 = line.split()
            l1.append(int(v1))
            l2.append(int(v2))
            
    return l1, l2


if __name__ == "__main__":
    

    location_ids = parse_input("./input")

    part1(*location_ids) # Correct Value:  3569916
    part2(*location_ids) # Correct Value:  26407426
