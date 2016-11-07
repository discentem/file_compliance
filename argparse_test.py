import argparse
if __name__ == "__main__":
    def gather_args():
        parser = argparse.ArgumentParser()

        replace_help_msg = "Used to replace illegal characters automatically"
        parser.add_argument('-l', '--log', dest='a')
        args = parser.parse_args()
        return args.a

    print(gather_args())
