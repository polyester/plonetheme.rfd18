# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.rfd18


class PlonethemeRfd18Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.rfd18)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.rfd18:default')


PLONETHEME_RFD18_FIXTURE = PlonethemeRfd18Layer()


PLONETHEME_RFD18_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_RFD18_FIXTURE,),
    name='PlonethemeRfd18Layer:IntegrationTesting'
)


PLONETHEME_RFD18_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_RFD18_FIXTURE,),
    name='PlonethemeRfd18Layer:FunctionalTesting'
)


PLONETHEME_RFD18_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_RFD18_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeRfd18Layer:AcceptanceTesting'
)
