# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from soignies.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of soignies.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if soignies.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('soignies.urban.dataimport'))

    def test_uninstall(self):
        """Test if soignies.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['soignies.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('soignies.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ISoigniesUrbanDataimportLayer is registered."""
        from soignies.urban.dataimport.interfaces import ISoigniesUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(ISoigniesUrbanDataimportLayer in utils.registered_layers())
