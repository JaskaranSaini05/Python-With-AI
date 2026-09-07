# Whenever python program is executed,
# it is executed by the main thread

# Magic Variables or Dunders
# print('__name__ is:',__name__) # output : __main__
print('__name__ is:',__name__)

def main():
    print("This is first statement")

    for index in range(0,5):
        print(index)
    print("This is last statement")

# We need to manually(explicitly) execute the main function
if __name__ == '__main__':
    main()