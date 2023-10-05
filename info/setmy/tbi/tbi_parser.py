import yaml


def parse_tbi(file_name: str):
    try:
        file_content = read_file(file_name)
        return yaml.safe_load(file_content)
    except yaml.YAMLError:
        return None
    pass


def read_file(file_name: str, error_return: str = ""):
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        return error_return
