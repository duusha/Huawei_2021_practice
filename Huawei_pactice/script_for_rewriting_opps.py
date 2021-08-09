import script_for_rewriting as scr
from pycparser import c_ast
def script(head,struct_name_list, hot):
	#print(hot)
	for (child_name, child) in head.children():	
		#print(child_name)
		if (type(child) == c_ast.StructRef):
			#print(child.name)
			if (child.name.name in struct_name_list):
			 	if child.field.name in hot:
			 		child.name.name += '1'
			 	else:
			 		child.name.name += '2'
			#print(child)
		else:
			script(child, struct_name_list, hot)







	# #print(body.block_items[0].coord)
	# #print(struct_name_list)
	# file_name = scr.get_name(str(body.block_items[0].coord))
	# lines_to_change = dict()
	# for elem in body.block_items:
	# 	#print(elem)
	# 	cords = str(elem.coord)
	# 	if (type(elem) == c_ast.Assignment):
	# 		if(type(elem.lvalue) == c_ast.StructRef and type(elem.rvalue) == c_ast.StructRef):

	# 			if(elem.lvalue.field.name in hot):
	# 				cord = int(cords[cords.find(':'):cords.find(':'):])
	# 				if ( cord in lines_to_change):
	# 					lines_to_change[int(cords[cords.find(':'):cords.find(':'):])] = '\t' + elem.lvalue.name.name + '1' + elem.lvalue.field.name
	# 			#print('YAY')
	# 		#if elem.lvalue
	# 	#print(elem)
	# #print(body)