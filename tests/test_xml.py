from xml.etree import ElementTree as ET


def test_xml():
    a = ET.Element("a")
    b = ET.SubElement(a, "b")
    c = ET.SubElement(b, "c")
    c.text = "c text"
    c.set("c1", "1")
    old = ET.tostring(a)

    c2 = a.find('b/c')
    c2.set('c1', "3")
    new = ET.tostring(a)
    assert old == new
