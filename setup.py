from setuptools import setup
from setuptools import find_packages

version = '5.0b3'

setup(
    name='Products.CMFPlone',
    version=version,
    description="The Plone Content Management System (core)",
    long_description=open("README.rst").read() + "\n" +
    open("CHANGES.rst").read(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords='Plone CMF python Zope',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='http://plone.org/',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    extras_require=dict(
        archetypes=[
            'Products.ATContentTypes',
        ],
        test=[
            'lxml',
            'plone.app.robotframework',
            'plone.app.testing',
            'zope.globalrequest',
            'zope.testing',
        ]
    ),
    install_requires=[
        'setuptools',
        'Acquisition',
        'DateTime',
        'ExtensionClass',
        'Pillow',
        'Products.CMFCore',
        'Products.CMFDiffTool',
        'Products.CMFDynamicViewFTI',
        'Products.CMFEditions',
        'Products.CMFQuickInstallerTool',
        'Products.CMFUid',
        'Products.DCWorkflow',
        'Products.ExtendedPathIndex',
        'Products.ExternalEditor',
        'Products.GenericSetup >=1.4',
        'Products.MimetypesRegistry',
        'Products.PasswordResetTool',
        'Products.PlacelessTranslationService',
        # 'Products.PloneLanguageTool',
        'Products.PlonePAS',
        'Products.PluggableAuthService',
        'Products.PluginRegistry',
        'Products.PortalTransforms',
        'Products.ResourceRegistries',
        'Products.contentmigration',
        'Products.statusmessages',
        'ZODB3',
        'Zope2 > 2.13.0',
        'borg.localrole',
        'cssmin',
        'five.customerize',
        'five.localsitemanager',
        'five.pt',
        'mockup',
        'plone.app.content',
        'plone.app.contentlisting',
        'plone.app.contentmenu >= 1.1.6dev-r22380',
        'plone.app.contentrules',
        'plone.app.contenttypes',
        'plone.app.controlpanel',
        'plone.app.customerize',
        'plone.app.dexterity',
        'plone.app.discussion',
        'plone.app.folder',
        'plone.app.i18n',
        'plone.app.multilingual',
        'plone.app.layout >=1.1.7dev-r23744',
        'plone.app.linkintegrity >=1.0.3',
        'plone.app.locales',
        'plone.app.portlets',
        'plone.app.redirector',
        'plone.app.registry',
        'plone.app.theming',
        'plone.app.users',
        'plone.app.uuid',
        'plone.app.viewletmanager',
        'plone.app.vocabularies',
        'plone.app.widgets',
        'plone.app.workflow',
        'plone.batching',
        'plone.browserlayer >= 1.0rc4',
        'plone.contentrules',
        'plone.i18n',
        'plone.indexer',
        'plone.intelligenttext',
        'plone.locking',
        'plone.memoize',
        'plone.outputfilters',
        'plone.portlet.collection',
        'plone.portlet.static',
        'plone.portlets',
        'plone.protect >= 3.0.0a1',
        'plone.registry',
        'plone.schema',
        'plone.session',
        'plone.theme',
        'plonetheme.barceloneta',
        'slimit',
        'transaction',
        'z3c.autoinclude',
        'zope.app.locales >= 3.6.0',
        'zope.cachedescriptors',
        'zope.component',
        'zope.container',
        'zope.deferredimport',
        'zope.deprecation',
        'zope.dottedname',
        'zope.event',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.location',
        'zope.pagetemplate',
        'zope.publisher',
        'zope.site',
        'zope.structuredtext',
        'zope.tal',
        'zope.tales',
        'zope.traversing',
    ],
    entry_points="""\
      [console_scripts]
      plone-generate-gruntfile = Products.CMFPlone._scripts.generate_gruntfile:main
      plone-compile-resources = Products.CMFPlone._scripts.compile_resources:main
      """
)
