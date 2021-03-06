from zope.interface import Attribute
from zope.interface import Interface


class IGeoreferenceable(Interface):
    """Marks classes that may be annotated with georeferencing properties.
    """


class IGeoreferenced(Interface):
    """A geographically referenced object.

    The spatial reference system is implicitly long, lat WGS84. Geometry types
    and coordinates shall follow the Python geo interface specification, which
    itself tracks the GeoJSON draft specification at http://geojson.org.
    """

    type = Attribute(
        """The name of the geometry type: 'Point', 'LineString', 'Polygon'""")
    coordinates = Attribute("""A sequence of coordinate tuples""")

    crs = Attribute("""A coordinate reference system as a dict.
        The default is decimal degree longitude and latitude using the
        WGS 1984 reference system.""")


class IWritableGeoreference(Interface):

    def setGeoInterface(self, type, coordinates, crs):
        """Set the geometry via the geo interface.

        :param type: Point or LineString or Polygon
        :type type: string
        :param coordinates: a sequence of coordinates
        :type coordinates: tuple
        :param crs: A coordinate reference system as a dict
        :type crs: dict
        """

    def removeGeoInterface(self):
        """Remove the geometry via the geo interface."""


class IWriteGeoreferenced(IGeoreferenced, IWritableGeoreference):
    """Supports read/write georeferencing.
    """


class IGeoCoder(Interface):
    """Adapter for geocoding feature
    """

    def retrieve(self, address=None, google_api=None):
        """Retrieve coordinates by an address

        :param address: a string representing an address
            to be converted in coordinates
        :type address: string
        :param google_api: google api token
        :type google_api: string
        :returns: a sequence of coordinates representing a point
        :rtype: tuple
        """


class IGeoView(Interface):
    """View to access coordinates
    """

    def isGeoreferenceable(self):
        """Returns True if an object is Georeferenceable

        :returns: return True if context can be geo referenced
        :rtype: boolean
        """

    def getCoordinates(self):
        """Public function to get object coordinates

        :returns: (coordinate type, (a sequence of coordinates)) or None
        :rtype: tuple
        """
