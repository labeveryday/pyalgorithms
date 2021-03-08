import ngenerator
# Binary Search and Big O Notation

"""
Binary Serach - start in the middle and eliminate half of the list everytime until you get your answer.
- Only works when your list is in sorted order

---Big O notation ---- worst case senario for a search 
Linear Time O(n) - Search just as long as number of guesses
Logarithmic time Binary Searcg O(log n) - 

"""

def binary_search(a_list, item):
    steps = 0
    low = 0
    high = len(a_list) - 1                                  # Takes the length of list and minus one
    while low <= high:                                      # While low is less than or eq to high      
        mid = (low + high) // 2                             # Sets mid to 1/2 the value of high
        guess = a_list[mid]                                 # Guess equals the element number list number (represented by mid) num_list[0]
        if guess == item:                                   # If guess equals item return mid
            print(f'{a_list[mid]} is at position {mid}')
        if guess > item:                                    # If guess greater than item high equals mid - 1
            high = mid - 1                  
        else:                                               # If guess less than item low equals mid + 1
            low = mid + 1
        steps += 1
        print(steps)
    return None


if __name__ == '__main__':
    number = int(input('Enter range between 1 and 1,000,000,000: '))
    item = int(input('Number guess: '))
    number_list = ngenerator.get_number_list(number)
    print(binary_search(number_list, item))