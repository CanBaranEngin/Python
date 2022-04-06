def name_format(person):
    for i in person:
        a=("Mr. " if i[3] == "M" else "Ms. ") + i[0] + " " + i[1]

    return a


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(name_format(people), sep='\n')