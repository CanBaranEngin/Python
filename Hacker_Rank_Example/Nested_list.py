import operator
if __name__ == '__main__':
    score_list=set()
    record=[]
    second_lowest=[]
    for _ in range(int(input("Range Value: "))):
        name = input()
        marks = float(input())
        record.append([name,marks])
        score_list.add(marks)

    record=sorted(record, key=operator.itemgetter(1))
    score_list=sorted(score_list)
    for i,j in record:
        if j==score_list[1]:
            second_lowest.append(i)
            second_lowest=sorted(second_lowest)
    print(*second_lowest,sep="\n")
    