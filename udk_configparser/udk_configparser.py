import configparser
import os

__version__ = "1.0.2"


class MultiValueConfigDict(dict):

    def __setitem__(self, key, value):
        if key in self and isinstance(value, list):
            self[key].extend(value)
        else:
            super().__setitem__(key, value)


class UDKConfigParser(configparser.ConfigParser):

    def __init__(self,
                 *args,
                 strict=False,
                 dict_type=MultiValueConfigDict,
                 converters=None,
                 comment_prefixes="@",
                 **kwargs):

        if converters is None:
            converters = {
                "list": UDKConfigParser.getlist,
            }
        super().__init__(
            *args, strict=strict, dict_type=dict_type,
            converters=converters, comment_prefixes=comment_prefixes,
            **kwargs,
        )
        self.optionxform = str

    @staticmethod
    def getlist(value):
        return value.split(os.sep)

    def _write_section(self, fp, section_name, section_items, delimiter):
        fp.write("[{}]\n".format(section_name))
        for key, value in section_items:
            value = self._interpolation.before_write(
                self, section_name, key, value)
            if value is not None or not self._allow_no_value:
                if str(value).count("\n") > 1:
                    # Multi value case.
                    split = str(value).split("\n")
                    first = split[0]
                    rest = split[1:]
                    first = "{delimiter}{first}\n{key}{delimiter}".format(
                        delimiter=delimiter,
                        first=first,
                        key=key,
                    )
                    rest = "\n{key}{delimiter}".format(
                        key=key,
                        delimiter=delimiter,
                    ).join(rest)
                    value = first + rest
                else:
                    value = delimiter + str(value).replace("\n", "\n\t")
            else:
                value = ""
            fp.write("{}{}\n".format(key, value))
        fp.write("\n")
