import re

def list_to_str(list: list, join: str) -> str:
	return join.join(str(l) for l in list)

def strip_colors(input_string: str) -> str:
	"""
	Strips the color information from a string in starbound
	"""
	return re.sub(f'\\^\\w+?;', '', input_string)

def strip_planet_number(input_string: str) -> str:
	return re.sub(f'[VI]+(?![\\w])( - [a-z])?', '', strip_colors(input_string)).strip()

def playtime_to_string(time: float) -> str:
	"""
	Taken from the (probably) original implementation:
	https://github.com/rwf93/Starbound/blob/416da8fe8f102213160562ba372adc2a42bcdfca/source/core/StarTime.cpp#L23-L46
	"""
	hours: str = ""
	minutes: str = ""
	seconds: str = ""
	milliseconds: str = ""

	if time >= 3600:
		numHours: int = int(time / 3600)
		hours = f"{numHours} hour{'' if numHours == 1 else 's'}"
	if time >= 60:
		numMinutes: int = int((time / 60) % 60)
		minutes = f"{numMinutes} minute{'' if numMinutes == 1 else 's'}"
	if time >= 1:
		numSeconds: int = int(time % 60)
		seconds = f"{numSeconds} second{'' if numSeconds == 1 else 's'}"
	numMilliseconds: int = round(time * 1000)
	milliseconds = f"{numMilliseconds} millisecond{'' if numMilliseconds == 1 else 's'}"

	return ", ".join(x for x in [hours, minutes, seconds, milliseconds] if x)
