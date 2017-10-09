# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.urbaweb.importer import UrbawebDataImporter
from soignies.urban.dataimport.interfaces import ISoigniesDataImporter


class SoigniesDataImporter(UrbawebDataImporter):
    """ """

    implements(ISoigniesDataImporter)
