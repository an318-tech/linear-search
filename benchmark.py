
import time
import random
import matplotlib.pyplot as plt

from linear_search import linear_search


def measure_time(n, repeats=2000, seed=42):
    random.seed(seed)
    lst = list(range(n))
    target = -1

    t0 = time.perf_counter()
    for _ in range(repeats):
        linear_search(lst, target)
    return (time.perf_counter() - t0) / repeats


def main():
    sizes = [10, 100, 1000, 10000]
    repeats = {10: 50000, 100: 10000, 1000: 2000, 10000: 300}

    times = []
    print(f"{'n':>8} | {'время, мкс':>12} | {'нс/элемент':>12}")
    print("-" * 40)
    for n in sizes:
        t = measure_time(n, repeats[n])
        times.append(t)
        print(f"{n:>8} | {t * 1e6:>12.2f} | {t / n * 1e9:>12.2f}")

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, [t * 1e6 for t in times], "o-", color="#fc3f1d")
    plt.xlabel("Размер списка n (элементов)")
    plt.ylabel("Среднее время поиска, мкс")
    plt.title("Линейный поиск: время выполнения от размера списка")
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig("benchmark.png", dpi=150)
    print("\nГрафик сохранён в benchmark.png")


if __name__ == "__main__":
    main()
