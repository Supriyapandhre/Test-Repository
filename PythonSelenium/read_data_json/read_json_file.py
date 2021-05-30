import json

file_path = "E:\\15feb2021\\PythonSelenium\\read_data_json\\test_data.json"
def get_json_data(file_path=file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        file_data = json.loads(data)
        return file_data