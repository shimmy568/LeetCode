template = """if <value> in counts and (<value> + 1) in counts:
    if counts[<value>] + counts[<value> + 1] > max_count:
        max_count = counts[<value>] + counts[<value> + 1]
elif <value> in counts:
    if counts[<value>] > max_count:
        max_count = counts[<value>]
"""

template2 = """    if not <value> in counts:
        counts[<value>] = 0
    counts[<value>] += 1
"""

print("counts = {}")
for n in range(2, 101):
    print("if len(a) == % s:" % (n))
    for x in range(n):
        rendered_text = template2.replace("<value>", str(x))
        print(rendered_text)

print("max_count = 0")
for v in range(1, 100):
    rendered_text = template.replace("<value>", str(v))
    print(rendered_text)
