def main():
    x = 0
    # While loop loops a code block infinitely until a given condition specified is met.
    while (x < 5):
        print(x)
        x += 1

    # For loop loops for a given increment.
    for x in range(5, 10):
        print(x)
    
    # For loop over a collection:
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)

    # Break statement breaks out of the loop statement, Continue starts the loop over, but continues iterating unless conditions are met elsewhere.
    for x in range(5, 10):
        if x == 7: break 
        elif x % 2: continue
        print (x)

    # enumerate() over the collection to get the index.
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):
        print(i, d)

if __name__ == "__main__":
    main()
