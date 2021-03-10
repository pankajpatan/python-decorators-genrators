# You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

# For Henry Davids, the output should be:

# Mr. Henry Davids
# For Mary George, the output should be:

# Ms. Mary George


# Input :

# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F

# output:

# Mr. Mike Thomson
# Ms. Andria Bustle
# Mr. Robert Bustle


def person_lister(f):
    def inner(people):
        # complete the function
        return (f(i) for i in sorted(people,key=lambda x: x[2]))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')