import json
from download_sorter import DownloadSorter

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

instance = DownloadSorter(config['directory'], config['folder_file_map'],
                        config['delete_weekolds'], config['ignored_extensions'])
instance.sort_folder()
