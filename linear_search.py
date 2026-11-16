
def linear_search(lst, target):

    for i, value in enumerate(lst):
        if value == target:
            return i 
    return -1 


if __name__ == "__main__":
    data = [10, 25, 3, 47, 8, 91, 14]
    print(linear_search(data, 47)) 
    print(linear_search(data, 100)) 
