#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    return number * (-1) if number <= 0 else number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    return [i + suffixe for i in prefixes]


def est_premier(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def prime_integer_summation() -> int:
    liste_nombre = [2]
    count = 0
    while len(liste_nombre) < 100:
        count += 1
        last = liste_nombre[-1] + count
        if est_premier(last) is True:
            liste_nombre.append(last)
            count = 0
    return sum(liste_nombre)


def factorial(number: int) -> int:
    # Without recursion
    result = 1
    for i in range(number):
        result *= number - i
    return result

    # Recursion
    #if number <= 1:
        #return 1
    #return number * factorial(number - 1)


def use_continue() -> None:
    for i in range(11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    accept = []
    for i in groups:
        verdict = True

        if len(i) <= 3 or len(i) > 10:
            verdict = False

        elif 25 in i and verdict:
            accept.append(True)
            continue

        for j in i:
            if j < 18 or (50 in i and j > 70):
                verdict = False
                break

        accept.append(verdict)

    return accept



def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
        [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
        [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
