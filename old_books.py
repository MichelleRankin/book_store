def old_books():
    old_input = input("How many old books are you buying? ")
    old_total = int(old_input) * 2
    return old_total

def new_books():
    new_input = input("How many new books are you buying? ")
    new_total = int(new_input) * 4
    return new_total


def total(new_total, old_total):
    total = new_total + old_total 
    return total

def main():
    print("Hello! Welcome to the Book Store")
    print("New books are $4 \nOld books are $2")
    old = old_books()
    new = new_books()
    total(new, old) 
    print("Thanks! Your total is $" + str(total(new, old)))

if __name__ == '__main__':
    main()