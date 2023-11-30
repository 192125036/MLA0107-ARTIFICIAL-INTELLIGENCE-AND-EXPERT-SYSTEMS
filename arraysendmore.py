from itertools import permutations

def is_mapping_possible(arr, s):
    unique_chars = set(''.join(arr) + s)
    if len(unique_chars) > 10:
        return False  # More than 10 unique characters, not possible to map to digits
    
    for p in permutations('0123456789', len(unique_chars)):
        char_map = {char: digit for char, digit in zip(unique_chars, p)}
        if char_map[arr[0][0]] == '0' or char_map[arr[1][0]] == '0' or char_map[s[0]] == '0':
            continue  # Skip mappings where any word starts with 0
        
        num1 = int(''.join(char_map[c] for c in arr[0]))
        num2 = int(''.join(char_map[c] for c in arr[1]))
        sum_nums = num1 + num2
        target_num = int(''.join(char_map[c] for c in s))
        
        if sum_nums == target_num:
            return True
    
    return False

# Example usage
arr = ["SEND", "MORE"]
S = "MONEY"
result = is_mapping_possible(arr, S)

if result:
    print("Yes, it's possible to map the strings.")
else:
    print("No, it's not possible to map the strings.")
