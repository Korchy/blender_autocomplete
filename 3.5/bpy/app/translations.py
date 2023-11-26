import sys
import typing

GenericType = typing.TypeVar("GenericType")


def locale_explode(locale: typing.Optional[typing.Any]):
    ''' Return all components and their combinations of the given ISO locale string. >>> bpy.app.translations.locale_explode("sr_RS@latin") ("sr", "RS", "latin", "sr_RS", "sr@latin") For non-complete locales, missing elements will be None.

    :type msgid: typing.Optional[str]
    :param locale:  The ISO locale string to explode.
    :type locale: typing.Optional[typing.Any]
    '''

    pass


def pgettext(msgid: typing.Optional[str],
             msgctxt: typing.Optional[str] = None):
    ''' Try to translate the given msgid (with optional msgctxt).

    :param msgid: The string to translate.
    :type msgid: typing.Optional[str]
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: typing.Optional[str]
    '''

    pass


def pgettext_data(msgid: typing.Optional[str],
                  msgctxt: typing.Optional[str] = None):
    ''' Try to translate the given msgid (with optional msgctxt), if new data name's translation is enabled.

    :param msgid: The string to translate.
    :type msgid: typing.Optional[str]
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: typing.Optional[str]
    '''

    pass


def pgettext_iface(msgid: typing.Optional[str],
                   msgctxt: typing.Optional[str] = None):
    ''' Try to translate the given msgid (with optional msgctxt), if labels' translation is enabled.

    :param msgid: The string to translate.
    :type msgid: typing.Optional[str]
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: typing.Optional[str]
    '''

    pass


def pgettext_tip(msgid: typing.Optional[str],
                 msgctxt: typing.Optional[str] = None):
    ''' Try to translate the given msgid (with optional msgctxt), if tooltips' translation is enabled.

    :param msgid: The string to translate.
    :type msgid: typing.Optional[str]
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: typing.Optional[str]
    '''

    pass


def register(module_name: typing.Optional[str],
             translations_dict: typing.Optional[typing.Dict]):
    ''' Registers an addon's UI translations.

    :param module_name: The name identifying the addon.
    :type module_name: typing.Optional[str]
    :param translations_dict: ``{locale: {msg_key: msg_translation, ...}, ...}``
    :type translations_dict: typing.Optional[typing.Dict]
    '''

    pass


def unregister(module_name: typing.Optional[str]):
    ''' Unregisters an addon's UI translations.

    :param module_name: The name identifying the addon.
    :type module_name: typing.Optional[str]
    '''

    pass


contexts = None
''' Constant value bpy.app.translations.contexts(default_real=None, default='*', operator_default='Operator', ui_events_keymaps='UI_Events_KeyMaps', plural='Plural', id_action='Action', id_armature='Armature', id_brush='Brush', id_camera='Camera', id_cachefile='CacheFile', id_collection='Collection', id_curve='Curve', id_fs_linestyle='FreestyleLineStyle', id_gpencil='GPencil', id_curves='Curves', id_id='ID', id_image='Image', id_shapekey='Key', id_light='Light', id_library='Library', id_lattice='Lattice', id_mask='Mask', id_material='Material', id_metaball='Metaball', id_mesh='Mesh', id_movieclip='MovieClip', id_nodetree='NodeTree', id_object='Object', id_paintcurve='PaintCurve', id_palette='Palette', id_particlesettings='ParticleSettings', id_pointcloud='PointCloud', id_lightprobe='LightProbe', id_scene='Scene', id_screen='Screen', id_sequence='Sequence', id_simulation='Simulation', id_speaker='Speaker', id_sound='Sound', id_texture='Texture', id_text='Text', id_vfont='VFont', id_volume='Volume', id_world='World', id_workspace='WorkSpace', id_windowmanager='WindowManager', editor_view3d='View3D', editor_filebrowser='File browser', virtual_reality='Virtual reality', constraint='Constraint', color='Color', amount='Amount', unit='Unit')
'''

contexts_C_to_py = None
''' A readonly dict mapping contexts' C-identifiers to their py-identifiers.
'''

locale = None
''' The actual locale currently in use (will always return a void string when Blender is built without internationalization support).
'''

locales = None
''' All locales currently known by Blender (i.e. available as translations).
'''
