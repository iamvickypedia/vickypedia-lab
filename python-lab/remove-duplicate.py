# A random but challenging problem , still under construction
main_array = [
   {
      "one":"on-line",
      "index":58,
      "three":65,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"10–20",
      "index":118,
      "three":123,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"10-20",
      "index":142,
      "three":147,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"nano-materials",
      "index":208,
      "three":222,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"min-max",
      "index":236,
      "three":243,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"min–max",
      "index":288,
      "three":295,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"ultra-violet",
      "index":353,
      "three":365,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"infra-red",
      "index":428,
      "three":437,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"micro-scopic",
      "index":527,
      "three":539,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"hyper-active",
      "index":587,
      "three":599,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"60-85",
      "index":927,
      "three":932,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"20-30",
      "index":987,
      "three":992,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"60-85",
      "index":1019,
      "three":1024,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"3-year",
      "index":1062,
      "three":1068,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"three-year-old",
      "index":1200,
      "three":1214,
      "module":"Dashes",
      "sub_module":"Category_3"
   },
   {
      "one":"5-hydroxytryptamine",
      "index":1382,
      "three":1401,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"5-mm",
      "index":1463,
      "three":1467,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"twenty-five",
      "index":1665,
      "three":1676,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"twenty-one",
      "index":1827,
      "three":1837,
      "module":"Dashes",
      "sub_module":"Category_2"
   },
   {
      "one":"3-year-old",
      "index":1062,
      "three":1072,
      "module":"Dashes",
      "sub_module":"Category_3"
   },
   {
      "one":"three-year",
      "index":1200,
      "three":1210,
      "module":"Dashes",
      "sub_module":"Category_2"
   }
]
import copy
buffer_arr = copy.deepcopy(main_array)
buffer_dict = {}
just_index = []
check_dupes = []

# [1062,1200]

for ind in range(len(main_array)):
	# just_index.append(main_array[ind]["index"])

	# if main_array[ind]["index"] not in check_dupes:
	# 	check_dupes.append(main_array[ind]["index"])

	if main_array[ind]["index"] not in buffer_dict.keys():
		buffer_dict[main_array[ind]["index"]] = main_array[ind]
	else:
		if buffer_dict[main_array[ind]["index"]]["sub_module"] == "Category_2":
			buffer_arr.remove(buffer_dict[main_array[ind]["index"]])
		else:
			buffer_dict[main_array[ind]["index"]] = main_array[ind]
			if buffer_dict[main_array[ind]["index"]]["sub_module"] == "Category_2":
				buffer_arr.remove(buffer_dict[main_array[ind]["index"]])

# [x for x in buffer_arr if x['index']==1062]
#import pdb;pdb.set_trace()

# def get_unique_arr(arr):
# 	return list(set(arr))

# arr = [28, 42, 28, 16, 90, 42, 42, 28]
# print("Original Array {}".format(arr))
# print("Unique Array {}".format(get_unique_arr(arr)))
