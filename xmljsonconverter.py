# Author(s): 'Neelesh Batham' <neelesh.batham007@gmail.com

import json
import logging
from lxml import etree

logger = logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("XMLJSON")


class XMLJSONConverter(object):

    def __init__(self):

        self.null_tag = "null"
        self.integer_tag = "number"
        self.string_tag = "string"
        self.bool_tag = "boolean"
        self.list_tag = "array"
        self.dict_tag = "object"

    def _tostr(self, tree):
        try:
            if tree is not None:
                xml_str = etree.tostring(tree, encoding='utf8', method='xml', pretty_print=True)
                print xml_str
                return xml_str
        except Exception as e:
            print e
            logger.error("Error while converting XML str".format(e))

    def _process_null(self):
        try:
            root = etree.Element(self.null_tag)
            return root
        except Exception as e:
            logger.error("Error while converting into XML null".format(e))

    def _process_int(self, data):
        try:
            root = etree.Element(self.integer_tag)
            root.text = str(data)
            return root
        except Exception as e:
            logger.error("Error while converting into XML int".format(e))

    def _process_string(self, data):
        try:
            root = etree.Element(self.string_tag)
            root.tag = self.string_tag
            root.text = str(data)
            return root
        except Exception as e:
            logger.error("Error while converting into XML string".format(e))

    def _process_bool(self, data):
        try:
            root = etree.Element(self.bool_tag)
            root.tag = self.bool_tag
            root.text = str(data)
            return root
        except Exception as e:
            logger.error("Error while converting into XML bool".format(e))

    def _process_list(self, data, name=None):
        try:
            if len(data) != 0:
                if name is None:
                    root = etree.Element(self.list_tag)
                else:
                    root = etree.Element(self.list_tag)
                    root.tag = self.list_tag
                    root.attrib['name'] = name

                for each in data:
                    if type(each) is int:
                        child = self._process_int(each)
                        child.text = str(each)
                        root.append(child)

                    elif type(each) is unicode:
                        child = self._process_string(each)
                        child.text = str(each)
                        root.append(child)

                    elif type(each) is bool:
                        child = self._process_bool(each)
                        child.text = str(each)
                        root.append(child)

                    elif type(each) is dict:
                        child = self._process_dict(each)
                        root.append(child)

                return root
        except Exception as e:
            print e
            logger.error("Error while converting into XML list".format(e))

    def _process_dict(self, data, name=None):
        try:
            if name is None:
                root = etree.Element(self.dict_tag)
            else:
                root = etree.Element(self.dict_tag)
                root.tag = self.dict_tag
                root.attrib['name'] = name

            if len(data) != 0:
                for k, v in data.items():
                    if type(v) is int:
                        child_root = self._process_int(v)
                        child_root.attrib["name"] = k
                        root.append(child_root)

                    elif type(v) is unicode:
                        child_root = self._process_string(v)
                        child_root.attrib["name"] = k
                        root.append(child_root)

                    elif type(v) is bool:
                        child_root = self._process_bool(v)
                        child_root.attrib["name"] = k
                        root.append(child_root)

                    if type(v) is list:
                        child_root = self._process_list(v, k)
                        child_root.attrib["name"] = k
                        root.append(child_root)

                    elif type(v) is dict:
                        child_root = self._process_dict(v)
                        child_root.attrib["name"] = k
                        root.append(child_root)

                    elif v is None:
                        child_root = self._process_null()
                        child_root.attrib["name"] = k
                        root.append(child_root)

                return root
        except Exception as e:
            print e
            logger.error("Error while generating XML dict".format(str(e)))

    def process(self, data):
        """
        Identify the type of the data. 
        :param data: JSON data
        :return: 
        """
        try:
            if data is None:
                return self._tostr(self._process_null())

            elif type(data) is int:
                return self._tostr(self._process_int(data))

            elif type(data) is unicode:
                return self._tostr(self._process_string(data))

            elif type(data) is bool:
                return self._tostr(self._process_bool(data))

            elif type(data) is list:
                return self._tostr(self._process_list(data))

            elif type(data) is dict:
                return self._tostr(self._process_dict(data))

        except Exception as e:
            logger.error("Error while processing data".format(e))

    def convertJSONtoXML(self, json_file, xml_file):
        pass

if __name__ == "__main__":

    try:
        # data = json.loads(input_text)
        # XMLJSONConverter().process(data)

        json_file_path = raw_input("Input JSON File Path : ")
        xml_file_path = raw_input("Input XML Output Path : ")

        XMLJSONConverter().convertJSONtoXML(json_file_path, xml_file_path)
    except Exception as e:
        logger.error("Error while reading JSON input, please check the format".format(e))

