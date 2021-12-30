import os
import re


def get_file_list(path=os.getcwd(), type="all", pattern=None):
    """
    获取文件列表
    """
    if type not in ("all", "current"):
        raise TypeError("invalid type: {type}")

    file_list = []
    if type == "all":
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if (not pattern) or (pattern and re.match(pattern, filename)):
                    file_list.append(filepath)
        return file_list

    if type == "current":
        for filename in os.listdir(path):
            filepath = os.path.join(path, filename)
            if os.path.isfile(filepath):
                if (not pattern) or (pattern and re.match(pattern, filename)):
                    file_list.append(filepath)
        return file_list


def get_folder_list(path=os.getcwd(), type="all"):
    """
    获取文件夹列表
    """
    folder_list = []

    if type == "all":
        for dirpath, dirnames, filenames in os.walk(path):
            for dirname in dirnames:
                folder_list.append((os.path.join(dirpath, dirname)))
        return folder_list

    if type == "current":
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isdir(file_path):
                folder_list.append(file_path)
        return folder_list

    raise TypeError("invalid type: {type}")
