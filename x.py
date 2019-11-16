def get_my_list(count):
    my_list=[]
    while count <10:
        my_list.append(count)
        print(count)
        count=count+1

    print(my_list)

    return my_list
def main():
    print("hello world")
    count = 0
    while count < 10:
        my_list = get_my_list(count)

        for x in my_list:
            print(x)
        count = count+1

if __name__ == "__main__":
    main()
