"""
This object contains some data/methods regarding internationalization in Blender, and allows every py script
to feature translations for its own UI messages.


--------------------

[WARNING]
Most of this object should only be useful if you actually manipulate i18n stuff from Python.
If you are a regular add-on, you should only bother about contexts member,
and the register/unregister functions! The pgettext family of functions
should only be used in rare, specific cases (like e.g. complex "composited" UI strings...).

To add translations to your Python script, you must define a dictionary formatted like that:
{locale: {msg_key: msg_translation, ...}, ...}

 where:

* locale is either a lang ISO code (e.g. fr

), a lang+country code (e.g. pt_BR

),
a lang+variant code (e.g. sr@latin

), or a full code (e.g. uz_UZ@cyrilic

).
* msg_key is a tuple (context, org message) - use, as much as possible, the predefined contexts.
* msg_translation is the translated message in given language!

Then, call bpy.app.translations.register(__name__, your_dict)

 in your register()

 function, and
bpy.app.translations.unregister(__name__)

 in your unregister()

 one.

The Manage UI translations

 add-on has several functions to help you collect strings to translate, and
generate the needed Python code (the translation dictionary), as well as optional intermediary po files
if you want some... See
How to Translate Blender and
Using i18n in Blender Code
for more info.


--------------------

```../examples/bpy.app.translations.py```

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def locale_explode(locale) -> None:
    """Return all components and their combinations of the given ISO locale string.For non-complete locales, missing elements will be None.

    :param locale: The ISO locale string to explode.
    :return: A tuple (language, country, variant, language_country, language@variant).
    """

def pgettext(msgid: str | None, msgctxt: None | str | None = None) -> None:
    """Try to translate the given msgid (with optional msgctxt).

    :param msgid: The string to translate.
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :return: The translated string (or msgid if no translation was found).
    """

def pgettext_data(msgid: str | None, msgctxt: None | str | None = None) -> None:
    """Try to translate the given msgid (with optional msgctxt), if new data names translation is enabled.

    :param msgid: The string to translate.
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :return: The translated string (or msgid if no translation was found).
    """

def pgettext_iface(msgid: str | None, msgctxt: None | str | None = None) -> None:
    """Try to translate the given msgid (with optional msgctxt), if labels translation is enabled.

    :param msgid: The string to translate.
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :return: The translated string (or msgid if no translation was found).
    """

def pgettext_n(msgid: str | None, msgctxt: None | str | None = None) -> None:
    """Extract the given msgid to translation files. This is a no-op function that will only mark the string to extract, but not perform the actual translation.

    :param msgid: The string to extract.
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :return: The original string.
    """

def pgettext_rpt(msgid: str | None, msgctxt: None | str | None = None) -> None:
    """Try to translate the given msgid (with optional msgctxt), if reports translation is enabled.

    :param msgid: The string to translate.
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :return: The translated string (or msgid if no translation was found).
    """

def pgettext_tip(msgid: str | None, msgctxt: None | str | None = None) -> None:
    """Try to translate the given msgid (with optional msgctxt), if tooltips translation is enabled.

    :param msgid: The string to translate.
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :return: The translated string (or msgid if no translation was found).
    """

def register(
    module_name: str | None, translations_dict: dict[str, dict[str, str]] | None
) -> None:
    """Registers an addons UI translations.

        :param module_name: The name identifying the addon.
        :param translations_dict: A dictionary built like that:
    {locale: {msg_key: msg_translation, ...}, ...}
    """

def unregister(module_name: str | None) -> None:
    """Unregisters an addons UI translations.

    :param module_name: The name identifying the addon.
    """

contexts: typing.Any
""" Constant value bpy.app.translations.contexts(default_real=None, default=*, operator_default=Operator, ui_events_keymaps=UI_Events_KeyMaps, plural=Plural, countable=Countable, id_action=Action, id_armature=Armature, no_translation=Do not translate, id_brush=Brush, id_cachefile=CacheFile, id_camera=Camera, id_collection=Collection, id_curves=Curves, id_curve=Curve, id_fs_linestyle=FreestyleLineStyle, id_gpencil=GPencil, id_id=ID, id_image=Image, id_lattice=Lattice, id_library=Library, id_light=Light, id_lightprobe=LightProbe, id_mask=Mask, id_material=Material, id_mesh=Mesh, id_metaball=Metaball, id_movieclip=MovieClip, id_nodetree=NodeTree, id_object=Object, id_paintcurve=PaintCurve, id_palette=Palette, id_particlesettings=ParticleSettings, id_pointcloud=PointCloud, id_scene=Scene, id_screen=Screen, id_sequence=Sequence, id_shapekey=Key, id_simulation=Simulation, id_sound=Sound, id_speaker=Speaker, id_text=Text, id_texture=Texture, id_vfont=VFont, id_volume=Volume, id_windowmanager=WindowManager, id_workspace=WorkSpace, id_world=World, editor_filebrowser=File browser, editor_python_console=Python console, editor_preferences=Preferences, editor_view3d=View3D, amount=Amount, color=Color, constraint=Constraint, modifier=Modifier, navigation=Navigation, render_layer=Render Layer, time=Time, unit=Unit)
"""

contexts_C_to_py: typing.Any
""" A readonly dict mapping contexts C-identifiers to their py-identifiers.
"""

locale: typing.Any
""" The actual locale currently in use (will always return a void string when Blender is built without internationalization support).
"""

locales: typing.Any
""" All locales currently known by Blender (i.e. available as translations).
"""
