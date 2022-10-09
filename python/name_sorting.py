
#func-> builds a pair of names from a given list
def build_pair_list(dataset_list, number_of_pairs):
    dataset_list_split = []
    for a in range (0, number_of_pairs):
        dataset_list_split.append(["",""])

        for z in range (0, number_of_pairs):
            x= 2*z
            y= x+1
            dataset_list_split[z][1] = dataset_list[y]

        return dataset_list_split

#func-> swaps the set of pair of names in ascending/alphabetical order
def swap_ascending(name1, name2):
    length_of_shortest_name = len(name1) if len(name1) < len(name2) else len(name2)


    for char_index in range (0, length_of_shortest_name):
        if ord(name2[char_index]):
            temp_name = name1
            name1 = name2
            name2 = temp_name
            break

        return name1, name2

names = ["Charles", "Amelia", "Dennis", "Charlotte", "Brian"]
names2 = ["charles", "Amelia", "Dennis", "Charlotte", "Brian", "Alice", "Bramwell"]
names_sorted = []
#func-> determines number of pairs a given list can create
def number_of_pairs(dataset_list ):
    number_of_pairs = int(len(dataset_list) / 2 )+ len(dataset_list) % 2
    return number_of_pairs

#print (names_pairs = build_pair_list(names2, number_of_pairs(names2)))

#names expected = [["Charles", "Amelia"],["Dennis", "Charlotte"], ["Brian", ""] ]
print(build_pair_list(names2, number_of_pairs(names2) ))
print("hello")
print(build_pair_list(names,3))