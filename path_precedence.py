"""
Path conflicts finder.

Shows items in your path which are taking precedence over other items in your path with the same name.

Simple right?


TODO: compare the binaries (creation, version, etc)

"""

import sys, os
from collections import defaultdict

weighted_paths = []


for weight, path in enumerate( os.environ['PATH'].split(":") ):
    for item in os.listdir(path):
        weighted_paths.append((item, weight, os.path.join(path, item)))


binary_dict = defaultdict(list)


for path in sorted(weighted_paths):
    binary_dict[path[0]].append(path[2])


for binary, binary_paths in sorted(binary_dict.items()):

    if len(binary_paths) > 1:

        print (binary, binary_paths)

        last = binary_paths[0]
        for path in binary_paths[1:]:

            cmd = "diff %s %s" % (last, path)
            result = os.system(cmd)
            #print (result)
            last = path

