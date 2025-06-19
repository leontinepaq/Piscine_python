from typing import Any #any as in the subject the does not exist

def all_thing_is_obj(object: Any) -> int:
	type_map = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
	}

	obj_type = type(object)

	if obj_type in type_map:
		print(f"{type_map[obj_type]} : {obj_type}")
	elif obj_type == str:
		print(f"{object} is in the kitchen : {obj_type}")
	else:
		print("Type not found")
	return 42



##other version with match function

# def all_thing_is_obj(object: any) -> int:
# 	match object:
# 		case list():
# 			print("List :", type(object))
# 		case tuple():
# 			print("Tuple :", type(object))
# 		case set():
# 			print("Set :", type(object))
# 		case dict():
# 			print("Dict :", type(object))
# 		case str():
# 			print(f"{object} is in the kitchen :", type(object))
# 		case _:
# 			print("Type not found")
# 	return 42