import re

def strip_colors(input_string: str) -> str:
	"""
	Strips color information from a string
	"""
	return re.sub(f'\\^\\w+?;', '', input_string)
