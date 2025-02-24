import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums
import bpy.types
import mathutils

def add_render_slot(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a new render slot

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def change_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: int | None = 0,
):
    """Interactively change the current frame number

    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame
    :type frame: int | None
    """

def clear_render_border(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear the boundaries of the render region and disable render region

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clear_render_slot(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear the currently selected render slot

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clipboard_copy(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy the image to the clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clipboard_paste(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Paste new image from the clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def convert_to_mesh_plane(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    interpolation: typing.Literal["Linear", "Closest", "Cubic", "Smart"]
    | None = "Linear",
    extension: typing.Literal["CLIP", "EXTEND", "REPEAT"] | None = "CLIP",
    alpha_mode: typing.Literal["STRAIGHT", "PREMUL", "CHANNEL_PACKED", "NONE"]
    | None = "STRAIGHT",
    use_auto_refresh: bool | None = True,
    relative: bool | None = True,
    shader: typing.Literal["PRINCIPLED", "SHADELESS", "EMISSION"] | None = "PRINCIPLED",
    emit_strength: float | None = 1.0,
    use_transparency: bool | None = True,
    render_method: typing.Literal["DITHERED", "BLENDED"] | None = "DITHERED",
    use_backface_culling: bool | None = False,
    show_transparent_back: bool | None = True,
    overwrite_material: bool | None = True,
    name_from: typing.Literal["OBJECT", "IMAGE"] | None = "OBJECT",
    delete_ref: bool | None = True,
):
    """Convert selected reference images to textured mesh plane

        :type execution_context: int | str | None
        :type undo: bool | None
        :param interpolation: Interpolation, Texture interpolation

    Linear
    Linear -- Linear interpolation.

    Closest
    Closest -- No interpolation (sample closest texel).

    Cubic
    Cubic -- Cubic interpolation.

    Smart
    Smart -- Bicubic when magnifying, else bilinear (OSL only).
        :type interpolation: typing.Literal['Linear','Closest','Cubic','Smart'] | None
        :param extension: Extension, How the image is extrapolated past its original bounds

    CLIP
    Clip -- Clip to image size and set exterior pixels as transparent.

    EXTEND
    Extend -- Extend by repeating edge pixels of the image.

    REPEAT
    Repeat -- Cause the image to repeat horizontally and vertically.
        :type extension: typing.Literal['CLIP','EXTEND','REPEAT'] | None
        :param alpha_mode: Alpha Mode, Representation of alpha in the image file, to convert to and from when saving and loading the image

    STRAIGHT
    Straight -- Store RGB and alpha channels separately with alpha acting as a mask, also known as unassociated alpha. Commonly used by image editing applications and file formats like PNG..

    PREMUL
    Premultiplied -- Store RGB channels with alpha multiplied in, also known as associated alpha. The natural format for renders and used by file formats like OpenEXR..

    CHANNEL_PACKED
    Channel Packed -- Different images are packed in the RGB and alpha channels, and they should not affect each other. Channel packing is commonly used by game engines to save memory..

    NONE
    None -- Ignore alpha channel from the file and make image fully opaque.
        :type alpha_mode: typing.Literal['STRAIGHT','PREMUL','CHANNEL_PACKED','NONE'] | None
        :param use_auto_refresh: Auto Refresh, Always refresh image on frame changes
        :type use_auto_refresh: bool | None
        :param relative: Relative Paths, Use relative file paths
        :type relative: bool | None
        :param shader: Shader, Node shader to use

    PRINCIPLED
    Principled -- Principled shader.

    SHADELESS
    Shadeless -- Only visible to camera and reflections.

    EMISSION
    Emission -- Emission shader.
        :type shader: typing.Literal['PRINCIPLED','SHADELESS','EMISSION'] | None
        :param emit_strength: Emission Strength, Strength of emission
        :type emit_strength: float | None
        :param use_transparency: Use Alpha, Use alpha channel for transparency
        :type use_transparency: bool | None
        :param render_method: Render Method

    DITHERED
    Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..

    BLENDED
    Blended -- Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..
        :type render_method: typing.Literal['DITHERED','BLENDED'] | None
        :param use_backface_culling: Backface Culling, Use backface culling to hide the back side of faces
        :type use_backface_culling: bool | None
        :param show_transparent_back: Show Backface, Render multiple transparent layers (may introduce transparency sorting problems)
        :type show_transparent_back: bool | None
        :param overwrite_material: Overwrite Material, Overwrite existing material with the same name
        :type overwrite_material: bool | None
        :param name_from: Name After, Name for new mesh object and material

    OBJECT
    Source Object -- Name after object source with a suffix.

    IMAGE
    Source Image -- name from laoded image.
        :type name_from: typing.Literal['OBJECT','IMAGE'] | None
        :param delete_ref: Delete Reference Object, Delete empty image object once mesh plane is created
        :type delete_ref: bool | None
    """

def curves_point_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    point: typing.Literal["BLACK_POINT", "WHITE_POINT"] | None = "BLACK_POINT",
    size: int | None = 1,
):
    """Set black point or white point for curves

    :type execution_context: int | str | None
    :type undo: bool | None
    :param point: Point, Set black point or white point for curves
    :type point: typing.Literal['BLACK_POINT','WHITE_POINT'] | None
    :param size: Sample Size
    :type size: int | None
    """

def cycle_render_slot(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    reverse: bool | None = False,
):
    """Cycle through all non-void render slots

    :type execution_context: int | str | None
    :type undo: bool | None
    :param reverse: Cycle in Reverse
    :type reverse: bool | None
    """

def external_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
):
    """Edit image in an external application

    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str
    """

def file_browse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = True,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
):
    """Open an image file browser, hold Shift to open the file, Alt to browse containing directory

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

def flip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_flip_x: bool | None = False,
    use_flip_y: bool | None = False,
):
    """Flip the image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_flip_x: Horizontal, Flip the image horizontally
    :type use_flip_x: bool | None
    :param use_flip_y: Vertical, Flip the image vertically
    :type use_flip_y: bool | None
    """

def import_as_mesh_planes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    interpolation: typing.Literal["Linear", "Closest", "Cubic", "Smart"]
    | None = "Linear",
    extension: typing.Literal["CLIP", "EXTEND", "REPEAT"] | None = "CLIP",
    alpha_mode: typing.Literal["STRAIGHT", "PREMUL", "CHANNEL_PACKED", "NONE"]
    | None = "STRAIGHT",
    use_auto_refresh: bool | None = True,
    relative: bool | None = True,
    shader: typing.Literal["PRINCIPLED", "SHADELESS", "EMISSION"] | None = "PRINCIPLED",
    emit_strength: float | None = 1.0,
    use_transparency: bool | None = True,
    render_method: typing.Literal["DITHERED", "BLENDED"] | None = "DITHERED",
    use_backface_culling: bool | None = False,
    show_transparent_back: bool | None = True,
    overwrite_material: bool | None = True,
    filepath: str = "",
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str = "",
    filter_image: bool | None = True,
    filter_movie: bool | None = True,
    filter_folder: bool | None = True,
    force_reload: bool | None = False,
    image_sequence: bool | None = False,
    offset: bool | None = True,
    offset_axis: typing.Literal["+X", "+Y", "+Z", "-X", "-Y", "-Z"] | None = "+X",
    offset_amount: float | None = 0.1,
    align_axis: typing.Literal["+X", "+Y", "+Z", "-X", "-Y", "-Z", "CAM", "CAM_AX"]
    | None = "CAM_AX",
    prev_align_axis: typing.Literal[
        "+X", "+Y", "+Z", "-X", "-Y", "-Z", "CAM", "CAM_AX", "NONE"
    ]
    | None = "NONE",
    align_track: bool | None = False,
    size_mode: typing.Literal["ABSOLUTE", "CAMERA", "DPI", "DPBU"] | None = "ABSOLUTE",
    fill_mode: typing.Literal["FILL", "FIT"] | None = "FILL",
    height: float | None = 1.0,
    factor: float | None = 600.0,
):
    """Create mesh plane(s) from image files with the appropriate aspect ratio

        :type execution_context: int | str | None
        :type undo: bool | None
        :param interpolation: Interpolation, Texture interpolation

    Linear
    Linear -- Linear interpolation.

    Closest
    Closest -- No interpolation (sample closest texel).

    Cubic
    Cubic -- Cubic interpolation.

    Smart
    Smart -- Bicubic when magnifying, else bilinear (OSL only).
        :type interpolation: typing.Literal['Linear','Closest','Cubic','Smart'] | None
        :param extension: Extension, How the image is extrapolated past its original bounds

    CLIP
    Clip -- Clip to image size and set exterior pixels as transparent.

    EXTEND
    Extend -- Extend by repeating edge pixels of the image.

    REPEAT
    Repeat -- Cause the image to repeat horizontally and vertically.
        :type extension: typing.Literal['CLIP','EXTEND','REPEAT'] | None
        :param alpha_mode: Alpha Mode, Representation of alpha in the image file, to convert to and from when saving and loading the image

    STRAIGHT
    Straight -- Store RGB and alpha channels separately with alpha acting as a mask, also known as unassociated alpha. Commonly used by image editing applications and file formats like PNG..

    PREMUL
    Premultiplied -- Store RGB channels with alpha multiplied in, also known as associated alpha. The natural format for renders and used by file formats like OpenEXR..

    CHANNEL_PACKED
    Channel Packed -- Different images are packed in the RGB and alpha channels, and they should not affect each other. Channel packing is commonly used by game engines to save memory..

    NONE
    None -- Ignore alpha channel from the file and make image fully opaque.
        :type alpha_mode: typing.Literal['STRAIGHT','PREMUL','CHANNEL_PACKED','NONE'] | None
        :param use_auto_refresh: Auto Refresh, Always refresh image on frame changes
        :type use_auto_refresh: bool | None
        :param relative: Relative Paths, Use relative file paths
        :type relative: bool | None
        :param shader: Shader, Node shader to use

    PRINCIPLED
    Principled -- Principled shader.

    SHADELESS
    Shadeless -- Only visible to camera and reflections.

    EMISSION
    Emission -- Emission shader.
        :type shader: typing.Literal['PRINCIPLED','SHADELESS','EMISSION'] | None
        :param emit_strength: Emission Strength, Strength of emission
        :type emit_strength: float | None
        :param use_transparency: Use Alpha, Use alpha channel for transparency
        :type use_transparency: bool | None
        :param render_method: Render Method

    DITHERED
    Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..

    BLENDED
    Blended -- Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..
        :type render_method: typing.Literal['DITHERED','BLENDED'] | None
        :param use_backface_culling: Backface Culling, Use backface culling to hide the back side of faces
        :type use_backface_culling: bool | None
        :param show_transparent_back: Show Backface, Render multiple transparent layers (may introduce transparency sorting problems)
        :type show_transparent_back: bool | None
        :param overwrite_material: Overwrite Material, Overwrite existing material with the same name
        :type overwrite_material: bool | None
        :param filepath: File Path, Filepath used for importing the file
        :type filepath: str
        :param align: Align

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param files: files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param directory: directory
        :type directory: str
        :param filter_image: filter_image
        :type filter_image: bool | None
        :param filter_movie: filter_movie
        :type filter_movie: bool | None
        :param filter_folder: filter_folder
        :type filter_folder: bool | None
        :param force_reload: Force Reload, Force reload the image if it is already opened elsewhere in Blender
        :type force_reload: bool | None
        :param image_sequence: Detect Image Sequences, Import sequentially numbered images as an animated image sequence instead of separate planes
        :type image_sequence: bool | None
        :param offset: Offset Planes, Offset planes from each other. If disabled, multiple planes will be created at the same location
        :type offset: bool | None
        :param offset_axis: Offset Direction, How planes are oriented relative to each others' local axis

    +X
    +X -- Side by Side to the Left.

    +Y
    +Y -- Side by Side, Downward.

    +Z
    +Z -- Stacked Above.

    -X
    -X -- Side by Side to the Right.

    -Y
    -Y -- Side by Side, Upward.

    -Z
    -Z -- Stacked Below.
        :type offset_axis: typing.Literal['+X','+Y','+Z','-X','-Y','-Z'] | None
        :param offset_amount: Offset Distance, Set distance between each plane
        :type offset_amount: float | None
        :param align_axis: Align, How to align the planes

    +X
    +X -- Facing positive X.

    +Y
    +Y -- Facing positive Y.

    +Z
    +Z -- Facing positive Z.

    -X
    -X -- Facing negative X.

    -Y
    -Y -- Facing negative Y.

    -Z
    -Z -- Facing negative Z.

    CAM
    Face Camera -- Facing camera.

    CAM_AX
    Camera's Main Axis -- Facing the camera's dominant axis.
        :type align_axis: typing.Literal['+X','+Y','+Z','-X','-Y','-Z','CAM','CAM_AX'] | None
        :param prev_align_axis: prev_align_axis

    +X
    +X -- Facing positive X.

    +Y
    +Y -- Facing positive Y.

    +Z
    +Z -- Facing positive Z.

    -X
    -X -- Facing negative X.

    -Y
    -Y -- Facing negative Y.

    -Z
    -Z -- Facing negative Z.

    CAM
    Face Camera -- Facing camera.

    CAM_AX
    Camera's Main Axis -- Facing the camera's dominant axis.

    NONE
    Undocumented.
        :type prev_align_axis: typing.Literal['+X','+Y','+Z','-X','-Y','-Z','CAM','CAM_AX','NONE'] | None
        :param align_track: Track Camera, Add a constraint to make the planes track the camera
        :type align_track: bool | None
        :param size_mode: Size Mode, Method for computing the plane size

    ABSOLUTE
    Absolute -- Use absolute size.

    CAMERA
    Scale to Camera Frame -- Scale to fit or fill the camera frame.

    DPI
    Pixels per Inch -- Scale based on pixels per inch.

    DPBU
    Pixels per Blender Unit -- Scale based on pixels per Blender Unit.
        :type size_mode: typing.Literal['ABSOLUTE','CAMERA','DPI','DPBU'] | None
        :param fill_mode: Scale, Method to scale the plane with the camera frame

    FILL
    Fill -- Fill camera frame, spilling outside the frame.

    FIT
    Fit -- Fit entire image within the camera frame.
        :type fill_mode: typing.Literal['FILL','FIT'] | None
        :param height: Height, Height of the created plane
        :type height: float | None
        :param factor: Definition, Number of pixels per inch or Blender Unit
        :type factor: float | None
    """

def invert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    invert_r: bool | None = False,
    invert_g: bool | None = False,
    invert_b: bool | None = False,
    invert_a: bool | None = False,
):
    """Invert image's channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param invert_r: Red, Invert red channel
    :type invert_r: bool | None
    :param invert_g: Green, Invert green channel
    :type invert_g: bool | None
    :param invert_b: Blue, Invert blue channel
    :type invert_b: bool | None
    :param invert_a: Alpha, Invert alpha channel
    :type invert_a: bool | None
    """

def match_movie_length(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Set image's user's length to the one of this video

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "Untitled",
    width: int | None = 1024,
    height: int | None = 1024,
    color: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 1.0),
    alpha: bool | None = True,
    generated_type: bpy._typing.rna_enums.ImageGeneratedTypeItems | None = "BLANK",
    float: bool | None = False,
    use_stereo_3d: bool | None = False,
    tiled: bool | None = False,
):
    """Create a new image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Image data-block name
    :type name: str
    :param width: Width, Image width
    :type width: int | None
    :param height: Height, Image height
    :type height: int | None
    :param color: Color, Default fill color
    :type color: collections.abc.Iterable[float] | None
    :param alpha: Alpha, Create an image with an alpha channel
    :type alpha: bool | None
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :type generated_type: bpy._typing.rna_enums.ImageGeneratedTypeItems | None
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :type float: bool | None
    :param use_stereo_3d: Stereo 3D, Create an image with left and right views
    :type use_stereo_3d: bool | None
    :param tiled: Tiled, Create a tiled image
    :type tiled: bool | None
    """

def open(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    allow_path_tokens: bool | None = True,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = True,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    use_sequence_detection: bool | None = True,
    use_udim_detecting: bool | None = True,
):
    """Open image

        :type execution_context: int | str | None
        :type undo: bool | None
        :param allow_path_tokens: Allow the path to contain substitution tokens
        :type allow_path_tokens: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected images (based on file names)
        :type use_sequence_detection: bool | None
        :param use_udim_detecting: Detect UDIMs, Detect selected UDIM files and load all matching tiles
        :type use_udim_detecting: bool | None
    """

def open_images(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    relative_path: bool | None = True,
    use_sequence_detection: bool | None = True,
    use_udim_detection: bool | None = True,
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param directory: directory
    :type directory: str
    :param files: files
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param relative_path: Use relative path
    :type relative_path: bool | None
    :param use_sequence_detection: Use sequence detection
    :type use_sequence_detection: bool | None
    :param use_udim_detection: Use UDIM detection
    :type use_udim_detection: bool | None
    """

def pack(execution_context: int | str | None = None, undo: bool | None = None):
    """Pack an image as embedded data into the .blend file

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def project_apply(execution_context: int | str | None = None, undo: bool | None = None):
    """Project edited image back onto the object

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def project_edit(execution_context: int | str | None = None, undo: bool | None = None):
    """Edit a snapshot of the 3D Viewport in an external image editor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def read_viewlayers(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Read all the current scene's view layers from cache, as needed

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def reload(execution_context: int | str | None = None, undo: bool | None = None):
    """Reload current image from disk

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def remove_render_slot(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the current render slot

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def render_border(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
):
    """Set the boundaries of the render region and enable render region

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    """

def replace(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = True,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
):
    """Replace current image by another one from disk

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

def resize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: collections.abc.Iterable[int] | None = (0, 0),
):
    """Resize the image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param size: Size
    :type size: collections.abc.Iterable[int] | None
    """

def rotate_orthogonal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    degrees: typing.Literal["90", "180", "270"] | None = "90",
):
    """Rotate the image

        :type execution_context: int | str | None
        :type undo: bool | None
        :param degrees: Degrees, Amount of rotation in degrees (90, 180, 270)

    90
    90 Degrees -- Rotate 90 degrees clockwise.

    180
    180 Degrees -- Rotate 180 degrees clockwise.

    270
    270 Degrees -- Rotate 270 degrees clockwise.
        :type degrees: typing.Literal['90','180','270'] | None
    """

def sample(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: int | None = 1,
):
    """Use mouse to sample a color in current image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param size: Sample Size
    :type size: int | None
    """

def sample_line(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    flip: bool | None = False,
    cursor: int | None = 5,
):
    """Sample a line and show it in Scope panels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xstart: X Start
    :type xstart: int | None
    :param xend: X End
    :type xend: int | None
    :param ystart: Y Start
    :type ystart: int | None
    :param yend: Y End
    :type yend: int | None
    :param flip: Flip
    :type flip: bool | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int | None
    """

def save(execution_context: int | str | None = None, undo: bool | None = None):
    """Save the image with current name and settings

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def save_all_modified(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Save all modified images

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def save_as(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    save_as_render: bool | None = False,
    copy: bool | None = False,
    allow_path_tokens: bool | None = True,
    filepath: str = "",
    check_existing: bool | None = True,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = True,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
):
    """Save the image with another name and/or settings

        :type execution_context: int | str | None
        :type undo: bool | None
        :param save_as_render: Save As Render, Save image with render color management.For display image formats like PNG, apply view and display transform.For intermediate image formats like OpenEXR, use the default render output color space
        :type save_as_render: bool | None
        :param copy: Copy, Create a new image file without modifying the current image in Blender
        :type copy: bool | None
        :param allow_path_tokens: Allow the path to contain substitution tokens
        :type allow_path_tokens: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

def save_sequence(execution_context: int | str | None = None, undo: bool | None = None):
    """Save a sequence of images

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def tile_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number: int | None = 1002,
    count: int | None = 1,
    label: str = "",
    fill: bool | None = True,
    color: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 1.0),
    generated_type: bpy._typing.rna_enums.ImageGeneratedTypeItems | None = "BLANK",
    width: int | None = 1024,
    height: int | None = 1024,
    float: bool | None = False,
    alpha: bool | None = True,
):
    """Adds a tile to the image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param number: Number, UDIM number of the tile
    :type number: int | None
    :param count: Count, How many tiles to add
    :type count: int | None
    :param label: Label, Optional tile label
    :type label: str
    :param fill: Fill, Fill new tile with a generated image
    :type fill: bool | None
    :param color: Color, Default fill color
    :type color: collections.abc.Iterable[float] | None
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :type generated_type: bpy._typing.rna_enums.ImageGeneratedTypeItems | None
    :param width: Width, Image width
    :type width: int | None
    :param height: Height, Image height
    :type height: int | None
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :type float: bool | None
    :param alpha: Alpha, Create an image with an alpha channel
    :type alpha: bool | None
    """

def tile_fill(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    color: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 1.0),
    generated_type: bpy._typing.rna_enums.ImageGeneratedTypeItems | None = "BLANK",
    width: int | None = 1024,
    height: int | None = 1024,
    float: bool | None = False,
    alpha: bool | None = True,
):
    """Fill the current tile with a generated image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param color: Color, Default fill color
    :type color: collections.abc.Iterable[float] | None
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :type generated_type: bpy._typing.rna_enums.ImageGeneratedTypeItems | None
    :param width: Width, Image width
    :type width: int | None
    :param height: Height, Image height
    :type height: int | None
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :type float: bool | None
    :param alpha: Alpha, Create an image with an alpha channel
    :type alpha: bool | None
    """

def tile_remove(execution_context: int | str | None = None, undo: bool | None = None):
    """Removes a tile from the image

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def unpack(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    method: bpy._typing.rna_enums.UnpackMethodItems | None = "USE_LOCAL",
    id: str = "",
):
    """Save an image packed in the .blend file to disk

    :type execution_context: int | str | None
    :type undo: bool | None
    :param method: Method, How to unpack
    :type method: bpy._typing.rna_enums.UnpackMethodItems | None
    :param id: Image Name, Image data-block name to unpack
    :type id: str
    """

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fit_view: bool | None = False,
):
    """View the entire image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param fit_view: Fit View, Fit frame to the viewport
    :type fit_view: bool | None
    """

def view_center_cursor(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Center the view so that the cursor is in the middle of the view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_cursor_center(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fit_view: bool | None = False,
):
    """Set 2D Cursor To Center View location

    :type execution_context: int | str | None
    :type undo: bool | None
    :param fit_view: Fit View, Fit frame to the viewport
    :type fit_view: bool | None
    """

def view_ndof(execution_context: int | str | None = None, undo: bool | None = None):
    """Use a 3D mouse device to pan/zoom the view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_pan(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Pan the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image
    :type offset: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def view_selected(execution_context: int | str | None = None, undo: bool | None = None):
    """View all selected UVs

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
    use_cursor_init: bool | None = True,
):
    """Zoom in/out the image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out
    :type factor: float | None
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool | None
    """

def view_zoom_border(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    zoom_out: bool | None = False,
):
    """Zoom in the view to the nearest item contained in the border

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    :param zoom_out: Zoom Out
    :type zoom_out: bool | None
    """

def view_zoom_in(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Zoom in the image (centered around 2D cursor)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Cursor location in screen coordinates
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def view_zoom_out(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Zoom out the image (centered around 2D cursor)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Cursor location in screen coordinates
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def view_zoom_ratio(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.0,
):
    """Set zoom ratio of the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
    :type ratio: float | None
    """
