import os
import py_compile
from pathlib import Path
from os import walk, remove


class PycConverter:

    def __init__(self, **kwargs):
        self.Source_path = kwargs.get("Source_path")
        self.Destination_path = kwargs.get("Destination_path")
        self.DirectoryNamePyc = kwargs.get("DirectoryNamePyc")


    def convert_to_pyc(self):
        """
        Convert all .py files to .pyc files

        :param Source_path: Path to the source directory
        :param Destination_path: Path to the destination directory where the .pyc files will be stored
        :param DirectoryNamePyc: Name of the directory where the .pyc files will be stored
        :return: None
        
        :Example:
        >>> from pycconverter import PycConverter
        >>> PycConverter(Source_path="/home/user/ProjectsDirectory", Destination_path="/home/user/Projects/PycC", DirectoryNamePyc="BUILD").convert_to_pyc()

        """

        Source_path = str(self.Source_path)
        Destination_path = str(self.Destination_path)
        DirectoryNamePyc = str(self.DirectoryNamePyc)

        project_path = Source_path
        build_path = f"{Destination_path}/{DirectoryNamePyc}"

        try:
            os.system(f"rm -r -f {build_path}")
        except Exception as e:
            print(e)
        try:
            os.mkdir(f"{build_path}")
        except:
            print("can not build dir")

        try:
            os.system(f"cp -r {project_path} {build_path}")
        except:
            print("can not copy Build")

        # # os.system("python -m compileall ./BUILD")

        f = []
        for (dirpath, dirnames, filenames) in walk(build_path):
            f.extend(map(lambda filename: (dirpath) + "/" + filename, filenames))

        f = sorted(f)

        for i in f:
            if i.endswith(".py"):
                py_compile.compile(f"{i}", f"{i}c")
                remove(i)












    