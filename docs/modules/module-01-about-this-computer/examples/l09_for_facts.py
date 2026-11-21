import platform

facts = [platform.machine(), platform.system(), platform.node()]
for fact in facts:
    print("-", fact)
print("Done:", len(facts), "facts")
