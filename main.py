import json
from math import acos, sin, cos, radians
from argparse import ArgumentParser


MEAN_EARTH_RADIUS_KM = 6371
MAX_RADIUS_KM = 100
INTERCOM_LAT_RADS = radians(53.339428)
INTERCOM_LON_RADS = radians(-6.257664)
INTERCOM_COORDS_RADS = (INTERCOM_LAT_RADS, INTERCOM_LON_RADS)


def parse_args():
	""" 
	Function that parses the arguments for this script.
	Returns an object containing the parsed arguments.
	"""
	parser = ArgumentParser(description='Take home test for Intercom.')
	parser.add_argument('-i', 
						'--input', 
						dest='file_path', 
						help='Relative path to the input file containing customer data.', 
						type=str, 
						required=True)
	parser.add_argument('-o', 
						'--output', 
						dest='output_path', 
						help='Optional relative path for the output file.', 
						type=str, 
						required=False)
	args = parser.parse_args()
	return args


def parse_file(file_path):
	"""
	Function that parses a file for customer JSON.
	Returns a list of customer dictionaries.
	"""
	file = open(file_path)
	line = file.readline()
	customers = []
	while line:
		customer = json.loads(line)
		customers.append(customer)
		line = file.readline()
	file.close()
	return customers


def write_to_file(customers, output_path):
	"""
	Function that writes customer data
	to the path specified by
	OUTPUT_PATH.
	"""
	file = open(output_path, "w+")
	for c in customers:
		formatted = json.dumps({
			'user_id': c['user_id'],
			'name': c['name'],
			'distance_km': c['distance_km']
		})
		print(formatted)
		file.write(formatted + '\n')


def compute_distance(coords):
	"""
	Function that computes the 
	great-circle distance between
	Intercom and the input co-ords.
	Returns the distance in kilometres.
	"""

	(lat_c, lon_c) = coords
	lat_c = radians(lat_c)
	lon_c = radians(lon_c)

	(lat_i, lon_i) = INTERCOM_COORDS_RADS

	sin_lats = sin(lat_c) * sin(lat_i)
	cos_lats = cos(lat_c) * cos(lat_i)
	delta_lon = abs(lon_i - lon_c)

	central_angle_rad = acos(sin_lats + cos_lats * cos(delta_lon))
	distance_km = MEAN_EARTH_RADIUS_KM * central_angle_rad
	return distance_km


def main(file_path, output_path):
	customers = parse_file(file_path)

	for c in customers:
		lat = float(c['latitude'])
		lon = float(c['longitude'])
		coords = (lat, lon)
		c['distance_km'] = compute_distance(coords)

	customers = [c for c in customers if c['distance_km'] <= MAX_RADIUS_KM]
	customers = sorted(customers, 
		   			   key=lambda c: c['user_id'])
	if output_path:
		write_to_file(customers, output_path)
	return customers


if __name__ == '__main__':
	args = parse_args()
	main(args.file_path, args.output_path)