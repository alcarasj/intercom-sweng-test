from main import main, MAX_RADIUS_KM, parse_file
from unittest.mock import patch
import os


TEST_INPUTS_DIR = "./test_inputs/"
TEST_INPUT = TEST_INPUTS_DIR + "%s.txt"
TEST_OUTPUT_DIR = "./test_output.txt"


def test_no_customers():
	file_path = TEST_INPUT % "no_customers"
	main(file_path, TEST_OUTPUT_DIR)

	result = parse_file(TEST_OUTPUT_DIR)
	expected = 0
	assert len(result) == expected

	expected = []
	assert result == expected
	os.remove(TEST_OUTPUT_DIR)



def test_no_valid_customers():
	file_path = TEST_INPUT % "no_valid_customers"
	main(file_path, TEST_OUTPUT_DIR)

	result = parse_file(TEST_OUTPUT_DIR)
	expected = 0
	assert len(result) == expected

	expected = []
	assert result == expected
	os.remove(TEST_OUTPUT_DIR)


def test_one_valid_customer():
	file_path = TEST_INPUT % "one_valid_customer"
	main(file_path, TEST_OUTPUT_DIR)
	
	result = parse_file(TEST_OUTPUT_DIR)
	expected = 1
	assert len(result) == expected

	assert result[0]['distance_km'] <= MAX_RADIUS_KM

	expected = {
		"user_id": 4, 
		"name": "Ian Kehoe",
		"distance_km": 10.56693628851016
	}
	assert result[0] == expected
	os.remove(TEST_OUTPUT_DIR)


def test_multiple_valid_customers():
	file_path = TEST_INPUT % "multiple_valid_customers"
	main(file_path, TEST_OUTPUT_DIR)
	
	result = parse_file(TEST_OUTPUT_DIR)
	expected = 5
	assert len(result) == expected

	for c in result:
		assert c['distance_km'] <= MAX_RADIUS_KM

	expected = [
		{"user_id": 4, "name": "Ian Kehoe", "distance_km": 10.56693628851016},
		{"user_id": 6, "name": "Theresa Enright", "distance_km": 24.085360018691215},
		{"user_id": 13, "name": "Olive Ahearn", "distance_km": 62.23170226288675},
		{"user_id": 17, "name": "Patricia Cahill", "distance_km": 96.07859923628895},
		{"user_id": 26, "name": "Stephen McArdle", "distance_km": 98.87459926457565}
	]
	assert result == expected
	os.remove(TEST_OUTPUT_DIR)