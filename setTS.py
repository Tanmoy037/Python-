set_1= set() #empty

set_of_cars = {"Audi","Bmw","Range rover"}
another_set_of_cars = {"Maruthi","Honda","Tata","Audi"}

#print(set_of_cars)

set_of_cars.add("Volvo")

#print(set_of_cars)

union_set_3 = set_of_cars.union(another_set_of_cars)
print(union_set_3)

intersec_set_3 = set_of_cars.intersection(another_set_of_cars)
print(intersec_set_3)

a = {1,2,3,4,5} # superset
b = {2,5}  #subset

print(b.issubset(a))
print(a.issuperset(b))