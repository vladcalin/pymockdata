from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Token, Template
import pymockdata.data as datasets


class FileExtensionGenerator(BaseGenerator):
    ID = "file_extension"

    _templates = [
        Template(
            Token.DatasetValue(datasets.FILE_EXTENSIONS)
        )
    ]


if __name__ == "__main__":
    print(FileExtensionGenerator().generate())
