from typing import Any
import math 

def NULL_not_found(object: Any) -> int:
	handlers = {
		type(None):	(lambda x: True, "Nothing"),
		float:		(math.isnan, "Cheese"),
		int:		(lambda x: x == 0, "Zero"),
		str:		(lambda x: x=="", "Empty"),
		bool:		(lambda x: x is False, "Fake")
	}
	obj_type = type(object)

	if obj_type in handlers:
		is_null_func, label = handlers[obj_type]
		if is_null_func(object):
			print(f"{label}: {object} {obj_type}")
			return 0

	print("Type not found")
	return 1



# def run_tests():
# 	assert NULL_not_found(None) == 0			# Nothing
# 	assert NULL_not_found(float('nan')) == 0	# Cheese
# 	assert NULL_not_found(0) == 0				# Zero
# 	assert NULL_not_found("") == 0				# Empty
# 	assert NULL_not_found(False) == 0	 		# Fake

# 	assert NULL_not_found(1) == 1				# Not null
# 	assert NULL_not_found("Hello") == 1			# Not null
# 	assert NULL_not_found(True) == 1			# Not null
# 	assert NULL_not_found([]) == 1				# Not in type_map
# 	assert NULL_not_found({}) == 1				# Not in type_map

# 	print("✅ All tests passed!")

# run_tests()