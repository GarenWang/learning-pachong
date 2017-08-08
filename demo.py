#!/usr/bin/env python
import re
pattern = re.compile(r'world')

match = re.match(pattern,'hello world!')
if match:
	print match.group()
