def main() -> None:
    square = lambda a: a ** 2 # fkt sqr for map()
    iterator = map(square, range(1, 5)) 

    for i in iterator:
        print(i)

    print(f"{list(iterator) = }")
    iterator = map(square, range(1, 5))
    print(f"{list(iterator) = }")

    # map() is a 'lazy' fkt, it doesn't compute until you iterate over it.
    # the computed values are 'one-time-use'
    #   the values are computed in line 5 and printed to the console 
    #   in line 7 the computed values aren't saved in 'iterator' anymore -> list is empty
    #   in line 9 the values are computed newly 
    
if __name__ == "__main__":
    main()