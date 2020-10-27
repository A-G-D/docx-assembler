#   specifications.py
#
#   Copyright (C) 2020 Aloever Dulay
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from os import path


class Specifications:

    def __init__(self, file_path):
        self.__dict = {}
        if file_path:
            self.__open(file_path)

    def __iter__(self):
        return self.__dict

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __getitem__(self, key):
        return self.__dict[key] if key in self.__dict else ''

    def __setitem__(self, key, value):
        self.__dict[key] = value

    def open(self, file_path):
        with open(file_path) as file:
            lines = file.read().splitlines()
            file.close()

            for line in lines:
                pair = line.split('=', 1)
                self.__dict[pair[0].split()[0]] = pair[1].split()[0]

            self.source_dir         = path.abspath(self.__dict['SOURCE_DIR']) if 'SOURCE_DIR' in self.__dict else ""
            self.target_dir         = path.abspath(self.__dict['TARGET_DIR']) if 'TARGET_DIR' in self.__dict else ""
            self.doc_file_path      = path.join(self.target_dir, self['DOC_FILE_NAME'])
            self.pdf_file_path      = path.join(self.target_dir, self['PDF_FILE_NAME'])
            self.doc_file_name      = self['DOC_FILE_NAME']
            self.pdf_file_name      = self['PDF_FILE_NAME']
            self.doc_file_type      = self['DOC_FILE_TYPE']

            self['SOURCE_DIR']      = self.source_dir
            self['TARGET_DIR']      = self.target_dir
            self['DOC_FILE_PATH']   = self.doc_file_path
            self['PDF_FILE_PATH']   = self.pdf_file_path


    __open = open
