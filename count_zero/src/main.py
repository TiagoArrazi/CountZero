from src.utils.counter import Counter


if __name__ == '__main__':

    while True:

        try:
            print(Counter.count_zeroes(input('Put your string in here >> ')))

        except KeyboardInterrupt:
            exit(0)
