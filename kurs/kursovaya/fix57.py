# -*- coding: utf-8 -*-
import re, sys, importlib.util
f = sys.argv[1] if len(sys.argv) > 1 else 'content57.py'
FIX = [("  ", " "), (" ,", ","), (" .", ".")]
s = open(f, encoding='utf-8').read()
for a, b in FIX:
    s = s.replace(a, b)
open(f, 'w', encoding='utf-8').write(s)
spec = importlib.util.spec_from_file_location('m57x', f)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
nums = [int(re.match(r'Мисоли (\d+)', b[1]).group(1)) for b in m.C if b[0] == 'p' and b[1].startswith('Мисоли')]
ok = nums == list(range(1, len(nums) + 1))
print('examples:', len(nums), 'seq ok:', ok)
