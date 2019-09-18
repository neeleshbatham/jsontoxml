# Json to Xml

This module provides a conversion tool for converting from JSON to XML.



## Dependencies:

1 . LXML
```bash
sudo apt-get install python-dev libxml2 libxml2-dev libxslt-dev

sudo apt-get install python-lxml

pip3 install lxml
```

2. Install requirements

   run this command where setup.py exists
    ```bash
    pip install . --upgrade
    ```

## How to run ?

1. Import as a module.

```python
    from src.xmljsonconverter import XMLJSONConverter

    xml_obj = XMLJSONConverter()

    xml_obj.convertJSONtoXML( <json_file_path>, <xml_file_path>)
```

2. Run the file directly.
```bash
   python json2xml/src/xmljsonconverter.py

   Input JSON File Path : /path/to/file.json
   Output XML File  Path : /path/to/output_file.xml

```
