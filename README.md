# Download sorter

Download sorter is a simple python tool that sorts your download folder by weekday and type.

## Usage

The tool should be run periodically as a cron job.

Create a config.json file in the root directory of this tool and use config.example.json as a template.
Sorting by weekday is based on the day that a file or folder is sorted rather than the date of creation.
Sorting by type is based on file extensions

Config variables:

- directory - Absolute path to your download folder.
- delete_weekolds - Specifies whether to delete the sorted folder for the same weekday of previous weeks
- folder_file_map - Maps file types to destination folder
- ignored_extensions - Extensions to ignore

NOTE: The "ignored_extensions" list should contain the extension of incomplete downloads used by each of your browsers or other software that downloads to the download folder. This ensures that incomplete downloads are not sorted. The config example holds these extensions for chrome, safari, firefox and edge.

## Authors

- [@geogrigor](https://www.github.com/geogrigor)

## License

[MIT](https://choosealicense.com/licenses/mit/)