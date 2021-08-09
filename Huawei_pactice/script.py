import sys
import script_for_rewriting as scr
import script_for_rewriting_opps as scr_ops
# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])


#hot_fields = set({'a', 'b'})
from pycparser import parse_file, c_ast, c_generator
d = dict({'int': 2, 'char': 1, 'int8_t': 1, 'int16_t': 2, 
	'int32_t': 4, 'int64_t': 8, 'uint8_t': 1, 'uint16_t': 2,
	 'uint32_t': 4, 'uint64_t': 8, 'double': 8, 'float': 4,
	  'long': 8, 'short': 2, 'signed char': 0, 'unsigned char': 1,
	   'short int': 2, 'signed short': 2, 'signed short int': 2,
	    'unsigned short': 2, 'unsigned short int': 2, 'signed': 4,
	     'signed int': 4, 'unsigned': 4, 'unsigned int': 4,
	      'unsigned long': 4, 'unsigned long int': 4,
	       'long long': 8, 'long long int': 8, 'signed long long': 8,
	        'signed long long int': 8, 'long double': 8}
)


struct_name_list = list()
hot_field = set()

def iter(head):
	cold_fields = set()
	types = list()
	print('New block')

	if (type(head) == c_ast.FuncDef):
		scr_ops.script(head, struct_name_list, hot_field)	
		#print(head)	
	# 	iter(head.body)
	if (type(head) == c_ast.Decl): #проверка на Decl
		if (type(head.type) == c_ast.Struct): # Проверка для струтур
			num = 1

			print('Insert the name of hot_fields in structure ', head.type.name, ': ', sep = '', end = '')
			hot_fields = set(input().split())
			for elem in head.type.decls:
				if (type(elem) == c_ast.Decl):
					if elem.name not in hot_fields: # создание cold_fields по hot 
						cold_fields.add(elem.name)
					_type = elem.type.type.names
					_type = ' '.join(_type)
					types.append(_type)
					cur_coords = elem.coord
		start = head.coord
		end = cur_coords
		struct_name = head.type.name
		struct_name_list.append(struct_name)
		scr.script(start, end, head.type.decls, struct_name, hot_fields)
		print('Cold Fields: ', cold_fields)
		for f in hot_fields:
			hot_field.add(f)





	elif (type(head.body) == c_ast.Compound): #проверка на Compound
		for elem in head.body.block_items:
			if (type(elem) == c_ast.Decl):
				_type = elem.type.type.names
				_type = ' '.join(_type)	
				types.append(_type)


	print('Order of types in decloration:', types)




if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename  = sys.argv[1]

    ast = parse_file(filename, use_cpp=True,
            cpp_path='gcc',
            cpp_args=['-E', r'-Iutils/fake_libc_include'])
    #ast.show():
    #print(ast.children())
    head = ast.children()
    #print(ast.ext)
    #print(head[90][1])
    for elem in head:
    	elem = elem[1]

    	if (type(elem) == c_ast.Decl or type(elem) == c_ast.FuncDef):
    		name = str(elem.coord)
    		#print(elem)
    		iter(elem)
  #  print(type(head[0][1].body))
   # head = head[0][1].body
   # print(head.block_items[0])
   # head  = head.block_items[0]
    #print(head.name)
    #print(head.type.type.names)
    #print(type(head.type))


generator = c_generator.CGenerator()
s = generator.visit(ast)
num_begin = 0
flag = 0
for num, line in enumerate(s.split('\n')):
	#print(num, line)
	if line.split(' ')[0] == 'typedef':
		num_end = num
	if line.split(' ')[0] == 'struct':
		flag = 1
	if line == "};" and flag:
		num_end = num
		flag = 0 
#print(num_end)
ans = ''
for num, line in enumerate(s.split('\n')):
	if (num > num_end):
		ans += line + '\n'
file_name = name[:name.find('.'):] + '_output.c'
f_out = open(file_name, 'a')
f_out.write(ans)
f_out.close()


#final ochka 
#print(head.children())
#name = scr.get_name(head.coord())
# print(name)
# file_name = name[:name.find('.'):] + '_output.c'
# file_ans = open('answer.c', 'w')
# f = open(filename, 'r')
# for line in f.readlines():
# 	w
