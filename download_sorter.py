import os
import datetime
import shutil


class DownloadSorter:
    def __init__(self, directory, folder_file_map, delete_weekolds, ignored_extensions):
        self.directory = directory
        self.folder_file_map = folder_file_map
        self.delete_weekolds = delete_weekolds
        self.ignored_extensions = ignored_extensions

    def sort_folder(self):
        weekdays = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
        today = datetime.datetime.today()
        weekday = weekdays[today.weekday()]
        today_string = today.strftime('%Y-%m-%d')
        today_dirname = weekday + '-' + today_string + '-' + 'sorted'

        for filename in os.listdir(self.directory):
            # Handle folders
            if not os.path.isfile(os.path.join(self.directory, filename)):
                # Remove folder form this day last week
                if (
                    self.delete_weekolds and
                    filename.startswith(weekday) and
                    filename.endswith('-sorted') and
                    filename != today_dirname
                ):
                    shutil.rmtree(os.path.join(self.directory, filename))
                # Move folder into folders folder
                elif not filename.endswith('-sorted'):
                    target_path = os.path.join(
                        self.directory, today_dirname, 'folders', filename)
                    source_path = os.path.join(self.directory, filename)
                    while os.path.isdir(target_path):
                        filename = filename + '_copy'
                        target_path = os.path.join(
                            self.directory, today_dirname, 'folders', filename)
                    shutil.move(source_path, target_path)
                continue

            target_folder_name = None
            stripped_filename, file_extension = os.path.splitext(filename)

            if filename[0] == '.' or file_extension in self.ignored_extensions:
                continue
            # Determine destination folder
            for key in self.folder_file_map:
                if file_extension in self.folder_file_map[key]:
                    target_folder_name = key
                    break
            if target_folder_name is None:
                target_folder_name = 'unclassified'

            target_directory = os.path.join(
                self.directory, today_dirname, target_folder_name)
            target_filepath = os.path.join(target_directory, filename)
            source_filepath = os.path.join(self.directory, filename)

            # If name exists, append _copy
            while os.path.isfile(target_filepath):
                stripped_filename = stripped_filename + '_copy'
                filename = stripped_filename + file_extension
                target_filepath = os.path.join(target_directory, filename)

            os.makedirs(target_directory, exist_ok=True)
            os.rename(source_filepath, target_filepath)
