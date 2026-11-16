
import random

from linear_search import linear_search


def main():
    random.seed(42)
    data = [random.randint(0, 999) for _ in range(100)]
    print("Список из 100 случайных чисел:")
    print(data)
    print()

    targets = [913, 654, 44, 71, 999, 1000]
    print("Результаты поиска:")
    for t in targets:
        idx = linear_search(data, t)
        if idx != -1:
            print(f"  {t:>5} -> индекс {idx} (data[{idx}] == {data[idx]})")
        else:
            print(f"  {t:>5} -> не найден (-1)")


if __name__ == "__main__":
    main()
