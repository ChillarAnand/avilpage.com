import mmap
import sys

filename = sys.argv[1]

try:
    use_shared_memory = sys.argv[2]
except:
    use_shared_memory = None


if use_shared_memory:
    with open(filename, mode="r", encoding="utf8") as fh:
        with mmap.mmap(fh.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read().decode('utf-8') + '\n'
            num_lines = sum(1 for line in text.splitlines())
            print(num_lines)
            text = mmap_obj.read()
            num_lines = sum(1 for line in text.splitlines())
            print(num_lines)
else:
    with open(filename) as fh:
        num_lines = sum(1 for line in fh)
        print(num_lines)
