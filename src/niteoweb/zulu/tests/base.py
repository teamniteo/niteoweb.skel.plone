# -*- coding: utf-8 -*-
"""Base module for unittesting"""

import unittest2 as unittest

from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_ID
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import applyProfile
from plone.testing import z2


class NiteowebZuluLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import niteoweb.zulu
        self.loadZCML(package=niteoweb.zulu)
        z2.installProduct(app, 'niteoweb.zulu')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        applyProfile(portal, 'niteoweb.zulu:default')

        # Create test contemt
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        portal.invokeFactory('Folder', 'folder')

        # Commit so that the test browser sees these objects
        portal.portal_catalog.clearFindAndRebuild()
        import transaction
        transaction.commit()

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'niteoweb.zulu')


FIXTURE = NiteowebZuluLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="NiteowebZuluLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="NiteowebZuluLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
