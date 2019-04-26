import sys

sys.path.insert(0, 'E:/PythonProjects/CLAP---tests/')
import tests.features.registration


def multiply(args):
    # return args[0] * args[1]
    print(int(args[1]) * int(args[2]))
    print(args[2])


if __name__ == '__main__':
    tests.features.registration.registration(sys.argv[1])
