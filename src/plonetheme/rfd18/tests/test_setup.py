# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plonetheme.rfd18.testing import PLONETHEME_RFD18_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.rfd18 is properly installed."""

    layer = PLONETHEME_RFD18_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.rfd18 is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.rfd18'))

    def test_browserlayer(self):
        """Test that IPlonethemeRfd18Layer is registered."""
        from plonetheme.rfd18.interfaces import (
            IPlonethemeRfd18Layer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeRfd18Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_RFD18_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.rfd18'])

    def test_product_uninstalled(self):
        """Test if plonetheme.rfd18 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.rfd18'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeRfd18Layer is removed."""
        from plonetheme.rfd18.interfaces import \
            IPlonethemeRfd18Layer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeRfd18Layer, utils.registered_layers())
