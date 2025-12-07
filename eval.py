from core.model import get_result
import time

with open("./dane_final_test/orig_final.txt") as f:
    lines = f.readlines()

t = time.time()
with open("./output.txt", "w+") as f:
    for line in lines:
        f.write(get_result(line)["redacted"])

dt = time.time() - t

print("Total time:", dt)