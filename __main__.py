import json
from folder_sorter import FolderSorter

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

instance = FolderSorter(config['directory'], config['folder_file_map'],
                        config['delete_weekolds'], config['ignored_extensions'])
instance.sort_folder()
