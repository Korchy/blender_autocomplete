import sys
import typing
from . import icons
from . import handlers
from . import timers
from . import translations

GenericType = typing.TypeVar("GenericType")


def help_text(all: typing.Optional[bool] = False):
    ''' Return the help text as a string.

    :param all: Return all arguments, even those which aren't available for the current platform.
    :type all: typing.Optional[bool]
    '''

    pass


def is_job_running(job_type: typing.Optional[str]) -> typing.Any:
    ''' Check whether a job of the given type is running.

    :param job_type: `rna_enum_wm_job_type_items`.
    :type job_type: typing.Optional[str]
    :rtype: typing.Any
    :return: Whether a job of the given type is currently running.
    '''

    pass


alembic = None
''' Constant value bpy.app.alembic(supported=True, version=(1, 8, 3), version_string=' 1, 8, 3')
'''

autoexec_fail = None
''' Undocumented, consider `contributing <https://developer.blender.org/>`__.
'''

autoexec_fail_message = None
''' Undocumented, consider `contributing <https://developer.blender.org/>`__.
'''

autoexec_fail_quiet = None
''' Undocumented, consider `contributing <https://developer.blender.org/>`__.
'''

background = None
''' Boolean, True when blender is running without a user interface (started with -b)
'''

binary_path = None
''' The location of Blender's executable, useful for utilities that open new instances. Read-only unless Blender is built as a Python module - in this case the value is an empty string which script authors may point to a Blender binary.
'''

build_branch = None
''' The branch this blender instance was built from
'''

build_cflags = None
''' C compiler flags
'''

build_commit_date = None
''' The date of commit this blender instance was built
'''

build_commit_time = None
''' The time of commit this blender instance was built
'''

build_commit_timestamp = None
''' The unix timestamp of commit this blender instance was built
'''

build_cxxflags = None
''' C++ compiler flags
'''

build_date = None
''' The date this blender instance was built
'''

build_hash = None
''' The commit hash this blender instance was built with
'''

build_linkflags = None
''' Binary linking flags
'''

build_options = None
''' Constant value bpy.app.build_options(bullet=True, codec_avi=True, codec_ffmpeg=True, codec_sndfile=True, compositor_cpu=True, cycles=True, cycles_osl=True, freestyle=True, image_cineon=True, image_dds=True, image_hdr=True, image_openexr=True, image_openjpeg=True, image_tiff=True, input_ndof=True, audaspace=True, international=True, openal=True, opensubdiv=True, sdl=True, sdl_dynload=True, coreaudio=False, jack=True, pulseaudio=True, wasapi=False, libmv=True, mod_oceansim=True, mod_remesh=True, collada=True, io_wavefront_obj=True, io_ply=True, io_stl=True, io_gpencil=True, opencolorio=True, openmp=True, openvdb=True, alembic=True, usd=True, fluid=True, xr_openxr=True, potrace=True, pugixml=True, haru=True)
'''

build_platform = None
''' The platform this blender instance was built for
'''

build_system = None
''' Build system used
'''

build_time = None
''' The time this blender instance was built
'''

build_type = None
''' The type of build (Release, Debug)
'''

debug = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_depsgraph = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_depsgraph_build = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_depsgraph_eval = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_depsgraph_pretty = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_depsgraph_tag = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_depsgraph_time = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_events = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_ffmpeg = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_freestyle = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_handlers = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_io = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_python = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_simdata = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

debug_value = None
''' Short, number which can be set to non-zero values for testing purposes
'''

debug_wm = None
''' Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name)
'''

driver_namespace = None
''' Dictionary for drivers namespace, editable in-place, reset on file load (read-only) File Loading & Order of Initialization Since drivers may be evaluated immediately after loading a blend-file it is necessary to ensure the driver name-space is initialized beforehand. This can be done by registering text data-blocks to execute on startup, which executes the scripts before drivers are evaluated. See *Text -> Register* from Blender's text editor. .. hint:: You may prefer to use external files instead of Blender's text-blocks. This can be done using a text-block which executes an external file. This example runs ``driver_namespace.py`` located in the same directory as the text-blocks blend-file: .. code-block:: import os import bpy blend_dir = os.path.normalize(os.path.join(__file__, "..", "..")) bpy.utils.execfile(os.path.join(blend_dir, "driver_namespace.py")) Using ``__file__`` ensures the text resolves to the expected path even when library-linked from another file. Other methods of populating the drivers name-space can be made to work but tend to be error prone: Using The ``--python`` command line argument to populate name-space often fails to achieve the desired goal because the initial evaluation will lookup a function that doesn't exist yet, marking the driver as invalid - preventing further evaluation. Populating the driver name-space before the blend-file loads also doesn't work since opening a file clears the name-space. It is possible to run a script via the ``--python`` command line argument, before the blend file. This can register a load-post handler (:mod:`bpy.app.handlers.load_post`) that initialized the name-space. While this works for background tasks it has the downside that opening the file from the file selector won't setup the name-space.
'''

factory_startup = None
''' Boolean, True when blender is running with --factory-startup)
'''

ffmpeg = None
''' Constant value bpy.app.ffmpeg(supported=True, avcodec_version=(60, 3, 100), avcodec_version_string='60, 3, 100', avdevice_version=(60, 1, 100), avdevice_version_string='60, 1, 100', avformat_version=(60, 3, 100), avformat_version_string='60, 3, 100', avutil_version=(58, 2, 100), avutil_version_string='58, 2, 100', swscale_version=(7, 1, 100), swscale_version_string=' 7, 1, 100')
'''

ocio = None
''' Constant value bpy.app.ocio(supported=True, version=(2, 2, 0), version_string=' 2, 2, 0')
'''

oiio = None
''' Constant value bpy.app.oiio(supported=True, version=(2, 4, 15), version_string=' 2, 4, 15')
'''

opensubdiv = None
''' Constant value bpy.app.opensubdiv(supported=True, version=(3, 5, 0), version_string=' 3, 5, 0')
'''

openvdb = None
''' Constant value bpy.app.openvdb(supported=True, version=(10, 0, 0), version_string='10, 0, 0')
'''

render_icon_size = None
''' Reference size for icon/preview renders (read-only)
'''

render_preview_size = None
''' Reference size for icon/preview renders (read-only)
'''

sdl = None
''' Constant value bpy.app.sdl(supported=True, version=(0, 0, 0), version_string='Unknown', available=False)
'''

tempdir = None
''' String, the temp directory used by blender (read-only)
'''

usd = None
''' Constant value bpy.app.usd(supported=True, version=(0, 23, 5), version_string=' 0, 23, 5')
'''

use_event_simulate = None
''' Boolean, for application behavior (started with ``--enable-*`` matching this attribute name)
'''

use_userpref_skip_save_on_exit = None
''' Boolean, for application behavior (started with ``--enable-*`` matching this attribute name)
'''

version = None
''' The Blender version as a tuple of 3 numbers. eg. (2, 83, 1)
'''

version_cycle = None
''' The release status of this build alpha/beta/rc/release
'''

version_file = None
''' The Blender version, as a tuple, last used to save a .blend file, compatible with ``bpy.data.version``. This value should be used for handling compatibility changes between Blender versions
'''

version_string = None
''' The Blender version formatted as a string
'''
