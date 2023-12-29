#!/usr/bin/env python

import os

for (root, subs, files) in os.walk('/home/admin/middleware/stack/github_space/PracticalProgramming/Python'):
    print("Root Folder: ", root)
    print("Sub Folder: ", subs)
    print("Files in sub folder: ", files)




