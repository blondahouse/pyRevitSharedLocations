import math

FEET_TO_MM = 304.8
RADIANS_TO_DEGREES = 180 / math.pi

linked_instances = FilteredElementCollector(doc).OfClass(RevitLinkInstance).ToElements()
linked_documents = set()

for instance in linked_instances:
    linked_document = instance.GetLinkDocument()
    if linked_document is not None:
        linked_documents.add(linked_document)

for link_doc in linked_documents:
    # d = doc
    # print(len(list(link_doc)))
    print(link_doc.Title)

    # active_location = d.ActiveProjectLocation
    project_locations = list(link_doc.ProjectLocations)
    # site_location = d.SiteLocation

    for index, ploc in enumerate(project_locations):
        print(ploc.Name)
        bp = ploc.GetProjectPosition(XYZ())
        lpbpEW = round(bp.EastWest * FEET_TO_MM, 2)
        lpbpNS = round(bp.NorthSouth * FEET_TO_MM, 2)
        lpbpElev = round(bp.Elevation * FEET_TO_MM, 2)
        lpbpAngle = round(bp.Angle * RADIANS_TO_DEGREES, 8)
        lpbpAngle = -lpbpAngle if lpbpAngle <= 0 else 360 - lpbpAngle
        print(index, "project_location: E/W:", lpbpEW, " N/S:", lpbpNS, " Elev:", lpbpElev, " Angle:", lpbpAngle)
    print()
