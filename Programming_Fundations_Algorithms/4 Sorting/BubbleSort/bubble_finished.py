# Bubble sort algorithm

# for in for generally mean O(n^2)
def bubbleSort(dataset):
    # start with the array length and decrement each time
    for i in range(len(dataset)-1, 0, -1): #range(start, stop[, step])
        # examine each item pair
        for j in range(i):
            # swap items if needed
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp

        print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Starting state: ", list1)
    bubbleSort(list1)
    print("Final state: ", list1)


if __name__ == "__main__":
    main()
