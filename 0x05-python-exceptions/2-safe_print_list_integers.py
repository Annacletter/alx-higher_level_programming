#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for item in my_list[:x]:
        try:
            print('{:d}'.format(item), end='')
            count += 1
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")
            continue
    print()
    return count
