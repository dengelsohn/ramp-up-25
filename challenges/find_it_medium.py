def find_it(items, name):
	for key in items:
		if key == name:
			return key.title() + " is gone..." 
	return name.title() + " is here!"