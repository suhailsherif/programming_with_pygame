from xml.dom import minidom

assetnodes = minidom.parse('assets.xml').getElementsByTagName('asset')

assets = dict( [(i.attributes["name"].value, i.attributes["image"].value) for i in assetnodes] )

print assets
