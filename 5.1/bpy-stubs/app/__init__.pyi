"""
This module contains application values that remain unchanged during runtime.

bpy.app.handlers.rst
bpy.app.translations.rst
bpy.app.icons.rst
bpy.app.timers.rst

:maxdepth: 1
:caption: Submodules

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

from . import handlers as handlers
from . import icons as icons
from . import timers as timers
from . import translations as translations

def help_text(*, all: bool | None = False) -> str:
    """Return the help text as a string.

    :param all: Return all arguments, even those which arent available for the current platform.
    :return: Help text.
    """

def is_job_running(job_type: bpy.stub_internal.rna_enums.WmJobTypeItems) -> bool:
    """Check whether a job of the given type is running.

    :param job_type: job type in `rna_enum_wm_job_type_items`.
    :return: Whether a job of the given type is currently running.
    """

def memory_usage_undo() -> int:
    """Get undo memory usage information.

    :return: Memory usage of the undo stack in bytes.
    """

alembic: typing.Any
""" Constant value bpy.app.alembic(supported=True, version=(1, 8, 3), version_string= 1,  8,  3)
"""

autoexec_fail: bool
""" Boolean, True when auto-execution of scripts failed (read-only).
"""

autoexec_fail_message: str
""" String, message describing the auto-execution failure (read-only).
"""

autoexec_fail_quiet: bool
""" Boolean, True when auto-execution failure should be quiet, set after the warning is shown once for the current blend file (read-only).
"""

background: bool
""" Boolean, True when blender is running without a user interface (started with -b)
"""

binary_path: str
""" The location of Blenders executable, useful for utilities that open new instances. Read-only unless Blender is built as a Python module - in this case the value is an empty string which script authors may point to a Blender binary.
"""

build_branch: bytes
""" The branch this blender instance was built from
"""

build_cflags: bytes
""" C compiler flags
"""

build_commit_date: bytes
""" The date of the commit this Blender instance was built from
"""

build_commit_time: bytes
""" The time of the commit this Blender instance was built from
"""

build_commit_timestamp: int
""" The unix timestamp of the commit this Blender instance was built from
"""

build_cxxflags: bytes
""" C++ compiler flags
"""

build_date: bytes
""" The date this Blender instance was built
"""

build_hash: bytes
""" The commit hash this Blender instance was built with
"""

build_linkflags: bytes
""" Binary linking flags
"""

build_options: typing.Any
""" Constant value bpy.app.build_options(bullet=True, codec_avi=False, codec_ffmpeg=True, codec_sndfile=True, compositor_cpu=True, cycles=True, cycles_osl=True, freestyle=True, image_cineon=True, image_dds=True, image_hdr=True, image_openexr=True, image_openjpeg=True, image_tiff=True, image_webp=True, input_ndof=True, audaspace=True, international=True, openal=True, opensubdiv=True, sdl=False, coreaudio=False, jack=True, pulseaudio=True, wasapi=False, libmv=True, mod_oceansim=True, mod_remesh=True, io_wavefront_obj=True, io_ply=True, io_stl=True, io_fbx=True, io_gpencil=True, opencolorio=True, openmp=False, openvdb=True, alembic=True, usd=True, fluid=True, xr_openxr=True, potrace=True, pugixml=True, haru=True, experimental_features=False)
"""

build_platform: bytes
""" The platform this blender instance was built for
"""

build_system: bytes
""" Build system used
"""

build_time: bytes
""" The time this Blender instance was built
"""

build_type: bytes
""" The type of build (Release, Debug)
"""

cachedir: None | str
""" String, the cache directory used by blender (read-only).If the parent of the cache folder (i.e. the part of the path that is not Blender-specific) does not exist, returns None.
"""

debug: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_depsgraph: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_depsgraph_build: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_depsgraph_eval: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_depsgraph_pretty: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_depsgraph_tag: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_depsgraph_time: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_events: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_freestyle: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_handlers: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_io: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_python: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_simdata: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

debug_value: int
""" Integer value which can be set to non-zero values for testing purposes.
"""

debug_wm: bool
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name).
"""

driver_namespace: dict[str, typing.Any]
""" Dictionary for drivers namespace, editable in-place, reset on file load (read-only).
"""

factory_startup: bool
""" Boolean, True when blender is running with --factory-startup
"""

ffmpeg: typing.Any
""" Constant value bpy.app.ffmpeg(supported=True, avcodec_version=(61, 19, 101), avcodec_version_string=61, 19, 101, avdevice_version=(61, 3, 100), avdevice_version_string=61,  3, 100, avformat_version=(61, 7, 100), avformat_version_string=61,  7, 100, avutil_version=(59, 39, 100), avutil_version_string=59, 39, 100, swscale_version=(8, 3, 100), swscale_version_string= 8,  3, 100)
"""

module: bool
""" Boolean, True when running Blender as a python module
"""

ocio: typing.Any
""" Constant value bpy.app.ocio(supported=True, version=(2, 5, 0), version_string= 2,  5,  0)
"""

oiio: typing.Any
""" Constant value bpy.app.oiio(supported=True, version=(3, 1, 7), version_string= 3,  1,  7)
"""

online_access: bool
""" Boolean, true when internet access is allowed by Blender & 3rd party scripts (read-only).
"""

online_access_override: bool
""" Boolean, true when internet access preference is overridden by the command line (read-only).
"""

opensubdiv: typing.Any
""" Constant value bpy.app.opensubdiv(supported=True, version=(3, 7, 0), version_string= 3,  7,  0)
"""

openvdb: typing.Any
""" Constant value bpy.app.openvdb(supported=True, version=(13, 0, 0), version_string=13,  0,  0)
"""

portable: bool
""" Boolean, True unless blender was built to reference absolute paths (on UNIX).
"""

python_args: tuple[str, ...]
""" Leading arguments to use when calling Python directly (via sys.executable). These arguments match settings Blender uses to ensure Python runs with a compatible environment (read-only).
"""

render_icon_size: int
""" Reference size for icon renders (read-only).
"""

render_preview_size: int
""" Reference size for preview renders (read-only).
"""

sdl: typing.Any
""" Constant value bpy.app.sdl(supported=False, version=(0, 0, 0), version_string=Unknown)
"""

tempdir: str
""" String, the temp directory used by blender (read-only).
"""

usd: typing.Any
""" Constant value bpy.app.usd(supported=True, version=(0, 25, 8), version_string= 0, 25,  8)
"""

use_event_simulate: bool
""" Boolean, for application behavior (started with --enable-* matching this attribute name)
"""

use_userpref_skip_save_on_exit: bool
""" Boolean, for application behavior (started with --enable-* matching this attribute name)
"""

version: tuple[int, int, int]
""" The Blender version as a tuple of 3 numbers (major, minor, micro). eg. (4, 3, 1)
"""

version_cycle: str
""" The release status of this build alpha/beta/rc/release
"""

version_file: tuple[int, int, int]
""" The Blender File version, as a tuple of 3 numbers (major, minor, file sub-version), that will be used to save a .blend file. The last item in this tuple indicates the file sub-version, which is different from the release micro version (the last item of the bpy.app.version tuple). The file sub-version can be incremented multiple times while a Blender version is under development. This value is, and should be, used for handling compatibility changes between Blender versions
"""

version_string: str
""" The Blender version formatted as a string
"""
