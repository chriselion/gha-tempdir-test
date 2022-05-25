import os
import tempfile


def main():
    with tempfile.TemporaryDirectory() as tempdir:
        file_out = os.path.join(tempdir, "test_file.txt")
        with open(file_out, 'w') as f:
            f.write("hello world")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
