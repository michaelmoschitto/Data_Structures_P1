def splitAdd(a):
    list = []
    if a == '':
        return []

    # print(a)
    for i in range(len(a)):
        char = a[0]
        simplr = a[1:]
        list.append(a)
        for i in range(len(simplr)):
            list.append(splitAdd(simplr[:i] + simplr[i:]))


    # for i in range(len(a)):
    #     list.append(a + 'c')

    return list



    return list




def main():
    print(splitAdd('abc'))

if __name__ == "__main__":
    main()
