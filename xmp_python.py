import xml.etree.ElementTree as ET

xml_data = """
<person>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Briwer</last_name>
    <email>broski_briwer@gnail.com</email>
    <age>30</age>
    <address>
        <city>SPB</city>
        <street>Moskovskaya</street>
        <house>22</house>
        <zip>123541</zip>
    </address>
</person>
"""

root = ET.fromstring(xml_data)
print("Name:",root.find('first_name').text)
print("Family:",root.find('last_name').text)
print("Email:",root.find('email').text)
