setA = {10,5,50,90,6}
setB = {22,11,10,6,9,85,23}
print("Set A =",setA)
print("Set B =",setB)

print(f"Set A union set B = {setA.union(setB)}")
print(f"Set A intersection set B = {setA.intersection(setB)}")
print(f"Set A difference set B = {setA.difference(setB)}")
print(f"Set B difference set A = {setB.difference(setA)}")
print(f"Set A symmetric difference set B = {setA.symmetric_difference(setB)}")