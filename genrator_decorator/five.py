

# Standardize Mobile Number Using Decorators

# You are given  mobile numbers. Sort them in ascending order then print them in the standard format shown below:


# The given mobile numbers may have +91,91,  or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.

# Input Format

# The first line of input contains an integer N, the number of mobile phone numbers.
#  N lines follow each containing a mobile number.

# Output Format

# Print  N mobile numbers on separate lines in the required format.


# Sample Input


# 07895462130
# 919875641230
# 9195969878
# Sample Output

# +91 78954 62130
# +91 91959 69878
# +91 98756 41230


def wrapper(f):
    def fun(l):
     
           f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
