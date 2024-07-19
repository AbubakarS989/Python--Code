# os modules Operating System
# It is use to access files and folder through python
'''
The `os` module in Python provides a way to use operating system-dependent functionality like reading or writing to the file system. Here are some commonly used functions and features of the `os` module:

1. **File and Directory Operations**:
    - `os.getcwd()`: Returns the current working directory. 
    - `os.chdir(path)`: Changes the current working directory to the specified path.
    - `os.listdir(path)`: Returns a list of entries in the specified directory.
    - `os.mkdir(path)`: Creates a directory at the specified path.
    - `os.makedirs(path)`: Creates directories, including intermediate directories.
    - `os.remove(path)`: Removes (deletes) the file at the specified path.
    - `os.rmdir(path)`: Removes (deletes) the directory at the specified path (the directory must be empty).
    - `os.rename(src, dst)`: Renames the file or directory from `src` to `dst`.
    - `os.path.exists(path)`: Returns `True` if the path exists.

2. **Environment Variables**:
    - `os.environ`: A dictionary containing the environment variables.
    - `os.getenv(key, default=None)`: Returns the value of the environment variable `key` if it exists, otherwise returns `default`.

3. **Path Operations** (in `os.path` submodule):
    - `os.path.basename(path)`: Returns the base name of the pathname.
    - `os.path.dirname(path)`: Returns the directory name of the pathname.
    - `os.path.join(path, *paths)`: Joins one or more path components intelligently.
    - `os.path.split(path)`: Splits the pathname into a pair (head, tail).
    - `os.path.splitext(path)`: Splits the pathname into a pair (root, ext).

4. **Process Management**:
    - `os.system(command)`: Executes the command (a string) in a subshell.
    - `os.popen(command)`: Opens a pipe to or from the command. The return value is an open file object connected to the pipe.
    - `os.getpid()`: Returns the current process ID.
    - `os.getppid()`: Returns the parent process ID.

5. **File Descriptors**:
    - `os.open(file, flags[, mode])`: Opens the file and returns a file descriptor.
    - `os.read(fd, n)`: Reads at most `n` bytes from file descriptor `fd`.
    - `os.write(fd, str)`: Writes the string `str` to file descriptor `fd`.
    - `os.close(fd)`: Closes the file descriptor `fd`.

Here's a simple example demonstrating some basic `os` module operations:

python '''
import os

"""# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Create a new directory in the current directory 
new_directory = os.path.join(current_directory, 'new_folder')
os.mkdir(new_directory)
print("Directory Created:", new_directory)

# List contents of the current directory
contents = os.listdir(current_directory)
print("Directory Contents:", contents)

# Rename the new directory
renamed_directory = os.path.join(current_directory, 'renamed_folder')
os.rename(new_directory, renamed_directory)
print("Directory Renamed:", renamed_directory)

# Remove the renamed directory
os.rmdir(renamed_directory)
print("Directory Removed:", renamed_directory)
"""

# From code with harry


if (not os.path.exists("Folder")):
    os.mkdir("Folder")




#? Remove a specific folder [into directory]
# os.rmdir("Folder/Sub folder")

# os.rename(f"{os.getcwd()}'\main.py","Chat-gpt.py")


# ? Get the current directory name
current_directory=os.getcwd()
print(current_directory)