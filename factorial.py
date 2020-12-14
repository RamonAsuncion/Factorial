
import numpy as npy


def f(a, b):
    return [(a*a) - (b*b), (2*a*b)]


def c_length(a, b):
    return (npy.sqrt(a**2 + b**2))


def main():
    print(f(1, 2))
    print(c_length(2, 2))


if __name__ == "__main__":
    main()
