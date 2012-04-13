import idaapi
import sys
import os
import inspect

VALID_TEMPLATE_EXT = ".txt"
PLUGIN_DIR = os.path.dirname(inspect.getfile(inspect.currentframe())) # this plugins' directory
TEMPLATE_DIR = PLUGIN_DIR+"/templates/"
template_dict = {}

def go_callback(*args):
	temp_name = ''.join('%c' % c for c in args)
	sEA = ScreenEA()
	SetFunctionCmt(sEA,template_dict[temp_name],True)
	return 1


# Add menu item
try:
	if ctx:
		idaapi.del_menu_item(ctx)
except:
	pass


dir_list = os.listdir(TEMPLATE_DIR)
for fname in dir_list:
	if fname.endswith(VALID_TEMPLATE_EXT):
		f = open(TEMPLATE_DIR+"/"+fname,"r")
		temp_data = f.read()
		template_dict[fname]=temp_data

for template in template_dict:
	ctx = idaapi.add_menu_item("Edit/Plugins/", "CTemplate > "+template, "", 0, go_callback, tuple(template))
	if ctx is None:
		print "Failed to add menu!"
		del ctx
	else:
		print "Menu added successfully!"





