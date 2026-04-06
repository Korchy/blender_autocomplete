import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

def add_render_slot(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new render slot"""

def change_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: int | None = 0,
) -> None:
    """Interactively change the current frame number

    :param frame: Frame
    """

def clear_render_border(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the boundaries of the render region and disable render region"""

def clear_render_slot(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the currently selected render slot"""

def clipboard_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the image to the clipboard"""

def clipboard_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Paste new image from the clipboard"""

def convert_to_mesh_plane(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    interpolation: typing.Literal["Linear", "Closest", "Cubic", "Smart"]
    | None = "Linear",
    extension: typing.Literal["CLIP", "EXTEND", "REPEAT"] | None = "CLIP",
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
) -> None:
    """Convert selected reference images to textured mesh plane

        :param interpolation: Interpolation, Texture interpolation

    Linear
    Linear -- Linear interpolation.

    Closest
    Closest -- No interpolation (sample closest texel).

    Cubic
    Cubic -- Cubic interpolation.

    Smart
    Smart -- Bicubic when magnifying, else bilinear (OSL only).
        :param extension: Extension, How the image is extrapolated past its original bounds

    CLIP
    Clip -- Clip to image size and set exterior pixels as transparent.

    EXTEND
    Extend -- Extend by repeating edge pixels of the image.

    REPEAT
    Repeat -- Cause the image to repeat horizontally and vertically.
        :param use_auto_refresh: Auto Refresh, Always refresh image on frame changes
        :param relative: Relative Paths, Use relative file paths
        :param shader: Shader, Node shader to use

    PRINCIPLED
    Principled -- Principled shader.

    SHADELESS
    Shadeless -- Only visible to camera and reflections.

    EMISSION
    Emission -- Emission shader.
        :param emit_strength: Emission Strength, Strength of emission
        :param use_transparency: Use Alpha, Use alpha channel for transparency
        :param render_method: Render Method

    DITHERED
    Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..

    BLENDED
    Blended -- Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..
        :param use_backface_culling: Backface Culling, Use backface culling to hide the back side of faces
        :param show_transparent_back: Show Backface, Render multiple transparent layers (may introduce transparency sorting problems)
        :param overwrite_material: Overwrite Material, Overwrite existing material with the same name
        :param name_from: Name After, Name for new mesh object and material

    OBJECT
    Source Object -- Name after object source with a suffix.

    IMAGE
    Source Image -- Name from loaded image.
        :param delete_ref: Delete Reference Object, Delete empty image object once mesh plane is created
    """

def curves_point_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    point: typing.Literal["BLACK_POINT", "WHITE_POINT"] | None = "BLACK_POINT",
    size: int | None = 1,
) -> None:
    """Set black point or white point for curves

    :param point: Point, Set black point or white point for curves
    :param size: Sample Size
    """

def cycle_render_slot(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    reverse: bool | None = False,
) -> None:
    """Cycle through all non-void render slots

    :param reverse: Cycle in Reverse
    """

def external_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
) -> None:
    """Edit image in an external application

    :param filepath: filepath
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
) -> None:
    """Open an image file browser, hold Shift to open the file, Alt to browse containing directory

        :param filepath: File Path, Path to file
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :param filter_blender: Filter .blend files
        :param filter_backup: Filter .blend files
        :param filter_image: Filter image files
        :param filter_movie: Filter movie files
        :param filter_python: Filter Python files
        :param filter_font: Filter font files
        :param filter_sound: Filter sound files
        :param filter_text: Filter text files
        :param filter_archive: Filter archive files
        :param filter_btx: Filter btx files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param relative_path: Relative Path, Select the file relative to the blend file
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :param sort_method: File sorting mode
    """

def flip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_flip_x: bool | None = False,
    use_flip_y: bool | None = False,
) -> None:
    """Flip the image

    :param use_flip_x: Horizontal, Flip the image horizontally
    :param use_flip_y: Vertical, Flip the image vertically
    """

def import_as_mesh_planes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    interpolation: typing.Literal["Linear", "Closest", "Cubic", "Smart"]
    | None = "Linear",
    extension: typing.Literal["CLIP", "EXTEND", "REPEAT"] | None = "CLIP",
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
) -> None:
    """Create mesh plane(s) from image files with the appropriate aspect ratio

        :param interpolation: Interpolation, Texture interpolation

    Linear
    Linear -- Linear interpolation.

    Closest
    Closest -- No interpolation (sample closest texel).

    Cubic
    Cubic -- Cubic interpolation.

    Smart
    Smart -- Bicubic when magnifying, else bilinear (OSL only).
        :param extension: Extension, How the image is extrapolated past its original bounds

    CLIP
    Clip -- Clip to image size and set exterior pixels as transparent.

    EXTEND
    Extend -- Extend by repeating edge pixels of the image.

    REPEAT
    Repeat -- Cause the image to repeat horizontally and vertically.
        :param use_auto_refresh: Auto Refresh, Always refresh image on frame changes
        :param relative: Relative Paths, Use relative file paths
        :param shader: Shader, Node shader to use

    PRINCIPLED
    Principled -- Principled shader.

    SHADELESS
    Shadeless -- Only visible to camera and reflections.

    EMISSION
    Emission -- Emission shader.
        :param emit_strength: Emission Strength, Strength of emission
        :param use_transparency: Use Alpha, Use alpha channel for transparency
        :param render_method: Render Method

    DITHERED
    Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..

    BLENDED
    Blended -- Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..
        :param use_backface_culling: Backface Culling, Use backface culling to hide the back side of faces
        :param show_transparent_back: Show Backface, Render multiple transparent layers (may introduce transparency sorting problems)
        :param overwrite_material: Overwrite Material, Overwrite existing material with the same name
        :param filepath: File Path, Filepath used for importing the file
        :param align: Align

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :param location: Location
        :param rotation: Rotation
        :param files: files
        :param directory: directory
        :param filter_image: filter_image
        :param filter_movie: filter_movie
        :param filter_folder: filter_folder
        :param force_reload: Force Reload, Force reload the image if it is already opened elsewhere in Blender
        :param image_sequence: Detect Image Sequences, Import sequentially numbered images as an animated image sequence instead of separate planes
        :param offset: Offset Planes, Offset planes from each other. If disabled, multiple planes will be created at the same location
        :param offset_axis: Offset Direction, How planes are oriented relative to each others local axis

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
        :param offset_amount: Offset Distance, Set distance between each plane
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
    Cameras Main Axis -- Facing the cameras dominant axis.
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
    Cameras Main Axis -- Facing the cameras dominant axis.

    NONE
    Undocumented.
        :param align_track: Track Camera, Add a constraint to make the planes track the camera
        :param size_mode: Size Mode, Method for computing the plane size

    ABSOLUTE
    Absolute -- Use absolute size.

    CAMERA
    Scale to Camera Frame -- Scale to fit or fill the camera frame.

    DPI
    Pixels per Inch -- Scale based on pixels per inch.

    DPBU
    Pixels per Blender Unit -- Scale based on pixels per Blender Unit.
        :param fill_mode: Scale, Method to scale the plane with the camera frame

    FILL
    Fill -- Fill camera frame, spilling outside the frame.

    FIT
    Fit -- Fit entire image within the camera frame.
        :param height: Height, Height of the created plane
        :param factor: Definition, Number of pixels per inch or Blender Unit
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
) -> None:
    """Invert images channels

    :param invert_r: Red, Invert red channel
    :param invert_g: Green, Invert green channel
    :param invert_b: Blue, Invert blue channel
    :param invert_a: Alpha, Invert alpha channel
    """

def match_movie_length(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set images users length to the one of this video"""

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
    generated_type: bpy.stub_internal.rna_enums.ImageGeneratedTypeItems
    | None = "BLANK",
    float: bool | None = False,
    use_stereo_3d: bool | None = False,
    tiled: bool | None = False,
) -> None:
    """Create a new image

    :param name: Name, Image data-block name
    :param width: Width, Image width
    :param height: Height, Image height
    :param color: Color, Default fill color
    :param alpha: Alpha, Create an image with an alpha channel
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :param use_stereo_3d: Stereo 3D, Create an image with left and right views
    :param tiled: Tiled, Create a tiled image
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
) -> None:
    """Open image

        :param allow_path_tokens: Allow the path to contain substitution tokens
        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param files: Files
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :param filter_blender: Filter .blend files
        :param filter_backup: Filter .blend files
        :param filter_image: Filter image files
        :param filter_movie: Filter movie files
        :param filter_python: Filter Python files
        :param filter_font: Filter font files
        :param filter_sound: Filter sound files
        :param filter_text: Filter text files
        :param filter_archive: Filter archive files
        :param filter_btx: Filter btx files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param relative_path: Relative Path, Select the file relative to the blend file
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :param sort_method: File sorting mode
        :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected images (based on file names)
        :param use_udim_detecting: Detect UDIMs, Detect selected UDIM files and load all matching tiles
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
) -> None:
    """Undocumented, consider contributing.

    :param directory: directory
    :param files: files
    :param relative_path: Use relative path
    :param use_sequence_detection: Use sequence detection
    :param use_udim_detection: Use UDIM detection
    """

def pack(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Pack an image as embedded data into the .blend file"""

def project_apply(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Project edited image back onto the object"""

def project_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Edit a snapshot of the 3D Viewport in an external image editor"""

def read_viewlayers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Read all the current scenes view layers from cache, as needed"""

def reload(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reload current image from disk"""

def remove_render_slot(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the current render slot"""

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
) -> None:
    """Set the boundaries of the render region and enable render region

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
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
) -> None:
    """Replace current image by another one from disk

        :param filepath: File Path, Path to file
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :param filter_blender: Filter .blend files
        :param filter_backup: Filter .blend files
        :param filter_image: Filter image files
        :param filter_movie: Filter movie files
        :param filter_python: Filter Python files
        :param filter_font: Filter font files
        :param filter_sound: Filter sound files
        :param filter_text: Filter text files
        :param filter_archive: Filter archive files
        :param filter_btx: Filter btx files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param relative_path: Relative Path, Select the file relative to the blend file
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :param sort_method: File sorting mode
    """

def resize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: collections.abc.Iterable[int] | None = (0, 0),
    all_udims: bool | None = False,
) -> None:
    """Resize the image

    :param size: Size
    :param all_udims: All UDIM Tiles, Scale all the images UDIM tiles
    """

def rotate_orthogonal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    degrees: typing.Literal["90", "180", "270"] | None = "90",
) -> None:
    """Rotate the image

        :param degrees: Degrees, Amount of rotation in degrees (90, 180, 270)

    90
    90 Degrees -- Rotate 90 degrees clockwise.

    180
    180 Degrees -- Rotate 180 degrees clockwise.

    270
    270 Degrees -- Rotate 270 degrees clockwise.
    """

def sample(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: int | None = 1,
) -> None:
    """Use mouse to sample a color in current image

    :param size: Sample Size
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
) -> None:
    """Sample a line and show it in Scope panels

    :param xstart: X Start
    :param xend: X End
    :param ystart: Y Start
    :param yend: Y End
    :param flip: Flip
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    """

def save(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Save the image with current name and settings"""

def save_all_modified(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Save all modified images"""

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
) -> None:
    """Save the image with another name and/or settings

        :param save_as_render: Save As Render, Save image with render color management.For display image formats like PNG, apply view and display transform.For intermediate image formats like OpenEXR, use the default render output color space
        :param copy: Copy, Create a new image file without modifying the current image in Blender
        :param allow_path_tokens: Allow the path to contain substitution tokens
        :param filepath: File Path, Path to file
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :param filter_blender: Filter .blend files
        :param filter_backup: Filter .blend files
        :param filter_image: Filter image files
        :param filter_movie: Filter movie files
        :param filter_python: Filter Python files
        :param filter_font: Filter font files
        :param filter_sound: Filter sound files
        :param filter_text: Filter text files
        :param filter_archive: Filter archive files
        :param filter_btx: Filter btx files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param relative_path: Relative Path, Select the file relative to the blend file
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :param sort_method: File sorting mode
    """

def save_sequence(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Save a sequence of images"""

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
    generated_type: bpy.stub_internal.rna_enums.ImageGeneratedTypeItems
    | None = "BLANK",
    width: int | None = 1024,
    height: int | None = 1024,
    float: bool | None = False,
    alpha: bool | None = True,
) -> None:
    """Adds a tile to the image

    :param number: Number, UDIM number of the tile
    :param count: Count, How many tiles to add
    :param label: Label, Optional tile label
    :param fill: Fill, Fill new tile with a generated image
    :param color: Color, Default fill color
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :param width: Width, Image width
    :param height: Height, Image height
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :param alpha: Alpha, Create an image with an alpha channel
    """

def tile_fill(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    color: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 1.0),
    generated_type: bpy.stub_internal.rna_enums.ImageGeneratedTypeItems
    | None = "BLANK",
    width: int | None = 1024,
    height: int | None = 1024,
    float: bool | None = False,
    alpha: bool | None = True,
) -> None:
    """Fill the current tile with a generated image

    :param color: Color, Default fill color
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :param width: Width, Image width
    :param height: Height, Image height
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :param alpha: Alpha, Create an image with an alpha channel
    """

def tile_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Removes a tile from the image"""

def unpack(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    method: bpy.stub_internal.rna_enums.UnpackMethodItems | None = "USE_LOCAL",
    id: str = "",
) -> None:
    """Save an image packed in the .blend file to disk

    :param method: Method, How to unpack
    :param id: Image Name, Image data-block name to unpack
    """

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fit_view: bool | None = False,
) -> None:
    """View the entire image

    :param fit_view: Fit View, Fit frame to the viewport
    """

def view_center_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Center the view so that the cursor is in the middle of the view"""

def view_cursor_center(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fit_view: bool | None = False,
) -> None:
    """Set 2D Cursor To Center View location

    :param fit_view: Fit View, Fit frame to the viewport
    """

def view_ndof(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Use a 3D mouse device to pan/zoom the view"""

def view_pan(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Pan the view

    :param offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image
    """

def view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """View all selected UVs"""

def view_zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
    use_cursor_init: bool | None = True,
) -> None:
    """Zoom in/out the image

    :param factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
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
) -> None:
    """Zoom in the view to the nearest item contained in the border

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    :param zoom_out: Zoom Out
    """

def view_zoom_in(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Zoom in the image (centered around 2D cursor)

    :param location: Location, Cursor location in screen coordinates
    """

def view_zoom_out(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Zoom out the image (centered around 2D cursor)

    :param location: Location, Cursor location in screen coordinates
    """

def view_zoom_ratio(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.0,
) -> None:
    """Set zoom ratio of the view

    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
    """
