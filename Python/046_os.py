import os

os_fun = dir(os)
# if (not os.path.exists("dev")):
#     os.mkdir("dev")
# for i in range(0,10):
#     os.mkdir(f"dev/pyhton_{i}")
for i in os_fun:
    s = f"os.{i}"
    print(f"{i} : {help (s)}")