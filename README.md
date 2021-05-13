# DownloadSort
A dead simple script to use that automatically sorts your downloads based off the requested folders

#How it works
Essentially it uses a file watcher to move newly moved files into the downloads directory into other directories based off file extension.
The reason its cross-platform and works with any computer is because the user declares the paths themselves upon first use, which is stored in
a "settings.txt" file, which then is parsed by the program, and is used when running
