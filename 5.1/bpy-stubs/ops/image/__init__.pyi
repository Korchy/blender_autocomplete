import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

class add_render_slot(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new render slot

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class change_frame(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        frame: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Interactively change the current frame number

        :param execution_context:
        :param undo:
        :param frame: Frame, (in [-1048574, 1048574], optional)
        :return: Result of the operator call.
        """

class clear_render_border(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the boundaries of the render region and disable render region

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class clear_render_slot(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the currently selected render slot

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class clipboard_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the image to the clipboard

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class clipboard_paste(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Paste new image from the clipboard

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class convert_to_mesh_plane(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        interpolation: typing.Literal["Linear", "Closest", "Cubic", "Smart"]
        | None = "Linear",
        extension: typing.Literal["CLIP", "EXTEND", "REPEAT"] | None = "CLIP",
        use_auto_refresh: bool | None = True,
        relative: bool | None = True,
        shader: typing.Literal["PRINCIPLED", "SHADELESS", "EMISSION"]
        | None = "PRINCIPLED",
        emit_strength: float | None = 1.0,
        use_transparency: bool | None = True,
        render_method: typing.Literal["DITHERED", "BLENDED"] | None = "DITHERED",
        use_backface_culling: bool | None = False,
        show_transparent_back: bool | None = True,
        overwrite_material: bool | None = True,
        name_from: typing.Literal["OBJECT", "IMAGE"] | None = "OBJECT",
        delete_ref: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert selected reference images to textured mesh plane

                :param execution_context:
                :param undo:
                :param interpolation: Interpolation, Texture interpolation (optional)

        Linear
        Linear -- Linear interpolation.

        Closest
        Closest -- No interpolation (sample closest texel).

        Cubic
        Cubic -- Cubic interpolation.

        Smart
        Smart -- Bicubic when magnifying, else bilinear (OSL only).
                :param extension: Extension, How the image is extrapolated past its original bounds (optional)

        CLIP
        Clip -- Clip to image size and set exterior pixels as transparent.

        EXTEND
        Extend -- Extend by repeating edge pixels of the image.

        REPEAT
        Repeat -- Cause the image to repeat horizontally and vertically.
                :param use_auto_refresh: Auto Refresh, Always refresh image on frame changes (optional)
                :param relative: Relative Paths, Use relative file paths (optional)
                :param shader: Shader, Node shader to use (optional)

        PRINCIPLED
        Principled -- Principled shader.

        SHADELESS
        Shadeless -- Only visible to camera and reflections.

        EMISSION
        Emission -- Emission shader.
                :param emit_strength: Emission Strength, Strength of emission (in [0, inf], optional)
                :param use_transparency: Use Alpha, Use alpha channel for transparency (optional)
                :param render_method: Render Method, (optional)

        DITHERED
        Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..

        BLENDED
        Blended -- Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..
                :param use_backface_culling: Backface Culling, Use backface culling to hide the back side of faces (optional)
                :param show_transparent_back: Show Backface, Render multiple transparent layers (may introduce transparency sorting problems) (optional)
                :param overwrite_material: Overwrite Material, Overwrite existing material with the same name (optional)
                :param name_from: Name After, Name for new mesh object and material (optional)

        OBJECT
        Source Object -- Name after object source with a suffix.

        IMAGE
        Source Image -- Name from loaded image.
                :param delete_ref: Delete Reference Object, Delete empty image object once mesh plane is created (optional)
                :return: Result of the operator call.
        """

class curves_point_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        point: typing.Literal["BLACK_POINT", "WHITE_POINT"] | None = "BLACK_POINT",
        size: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set black point or white point for curves

        :param execution_context:
        :param undo:
        :param point: Point, Set black point or white point for curves (optional)
        :param size: Sample Size, (in [1, 128], optional)
        :return: Result of the operator call.
        """

class cycle_render_slot(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        reverse: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Cycle through all non-void render slots

        :param execution_context:
        :param undo:
        :param reverse: Cycle in Reverse, (optional)
        :return: Result of the operator call.
        """

class external_edit(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Edit image in an external application

        :param execution_context:
        :param undo:
        :param filepath: filepath, (optional, never None)
        :return: Result of the operator call.
        """

class file_browse(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open an image file browser, hold Shift to open the file, Alt to browse containing directory

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param relative_path: Relative Path, Select the file relative to the blend file (optional)
                :param show_multiview: Enable Multi-View, (optional)
                :param use_multiview: Use Multi-View, (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :return: Result of the operator call.
        """

class flip(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_flip_x: bool | None = False,
        use_flip_y: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flip the image

        :param execution_context:
        :param undo:
        :param use_flip_x: Horizontal, Flip the image horizontally (optional)
        :param use_flip_y: Vertical, Flip the image vertically (optional)
        :return: Result of the operator call.
        """

class import_as_mesh_planes(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        interpolation: typing.Literal["Linear", "Closest", "Cubic", "Smart"]
        | None = "Linear",
        extension: typing.Literal["CLIP", "EXTEND", "REPEAT"] | None = "CLIP",
        use_auto_refresh: bool | None = True,
        relative: bool | None = True,
        shader: typing.Literal["PRINCIPLED", "SHADELESS", "EMISSION"]
        | None = "PRINCIPLED",
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
        size_mode: typing.Literal["ABSOLUTE", "CAMERA", "DPI", "DPBU"]
        | None = "ABSOLUTE",
        fill_mode: typing.Literal["FILL", "FIT"] | None = "FILL",
        height: float | None = 1.0,
        factor: float | None = 600.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create mesh plane(s) from image files with the appropriate aspect ratio

                :param execution_context:
                :param undo:
                :param interpolation: Interpolation, Texture interpolation (optional)

        Linear
        Linear -- Linear interpolation.

        Closest
        Closest -- No interpolation (sample closest texel).

        Cubic
        Cubic -- Cubic interpolation.

        Smart
        Smart -- Bicubic when magnifying, else bilinear (OSL only).
                :param extension: Extension, How the image is extrapolated past its original bounds (optional)

        CLIP
        Clip -- Clip to image size and set exterior pixels as transparent.

        EXTEND
        Extend -- Extend by repeating edge pixels of the image.

        REPEAT
        Repeat -- Cause the image to repeat horizontally and vertically.
                :param use_auto_refresh: Auto Refresh, Always refresh image on frame changes (optional)
                :param relative: Relative Paths, Use relative file paths (optional)
                :param shader: Shader, Node shader to use (optional)

        PRINCIPLED
        Principled -- Principled shader.

        SHADELESS
        Shadeless -- Only visible to camera and reflections.

        EMISSION
        Emission -- Emission shader.
                :param emit_strength: Emission Strength, Strength of emission (in [0, inf], optional)
                :param use_transparency: Use Alpha, Use alpha channel for transparency (optional)
                :param render_method: Render Method, (optional)

        DITHERED
        Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..

        BLENDED
        Blended -- Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..
                :param use_backface_culling: Backface Culling, Use backface culling to hide the back side of faces (optional)
                :param show_transparent_back: Show Backface, Render multiple transparent layers (may introduce transparency sorting problems) (optional)
                :param overwrite_material: Overwrite Material, Overwrite existing material with the same name (optional)
                :param filepath: File Path, Filepath used for importing the file (optional, never None)
                :param align: Align, (optional)

        WORLD
        World -- Align the new object to the world.

        VIEW
        View -- Align the new object to the view.

        CURSOR
        3D Cursor -- Use the 3D cursor orientation for the new object.
                :param location: Location, (array of 3 items, in [-inf, inf], optional)
                :param rotation: Rotation, (array of 3 items, in [-inf, inf], optional)
                :param files: files, (optional)
                :param directory: directory, (optional, never None)
                :param filter_image: filter_image, (optional)
                :param filter_movie: filter_movie, (optional)
                :param filter_folder: filter_folder, (optional)
                :param force_reload: Force Reload, Force reload the image if it is already opened elsewhere in Blender (optional)
                :param image_sequence: Detect Image Sequences, Import sequentially numbered images as an animated image sequence instead of separate planes (optional)
                :param offset: Offset Planes, Offset planes from each other. If disabled, multiple planes will be created at the same location (optional)
                :param offset_axis: Offset Direction, How planes are oriented relative to each others local axis (optional)

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
                :param offset_amount: Offset Distance, Set distance between each plane (in [-inf, inf], optional)
                :param align_axis: Align, How to align the planes (optional)

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
                :param prev_align_axis: prev_align_axis, (optional)

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
                :param align_track: Track Camera, Add a constraint to make the planes track the camera (optional)
                :param size_mode: Size Mode, Method for computing the plane size (optional)

        ABSOLUTE
        Absolute -- Use absolute size.

        CAMERA
        Scale to Camera Frame -- Scale to fit or fill the camera frame.

        DPI
        Pixels per Inch -- Scale based on pixels per inch.

        DPBU
        Pixels per Blender Unit -- Scale based on pixels per Blender Unit.
                :param fill_mode: Scale, Method to scale the plane with the camera frame (optional)

        FILL
        Fill -- Fill camera frame, spilling outside the frame.

        FIT
        Fit -- Fit entire image within the camera frame.
                :param height: Height, Height of the created plane (in [0.001, inf], optional)
                :param factor: Definition, Number of pixels per inch or Blender Unit (in [1, inf], optional)
                :return: Result of the operator call.
        """

class invert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        invert_r: bool | None = False,
        invert_g: bool | None = False,
        invert_b: bool | None = False,
        invert_a: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Invert images channels

        :param execution_context:
        :param undo:
        :param invert_r: Red, Invert red channel (optional)
        :param invert_g: Green, Invert green channel (optional)
        :param invert_b: Blue, Invert blue channel (optional)
        :param invert_a: Alpha, Invert alpha channel (optional)
        :return: Result of the operator call.
        """

class match_movie_length(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the images frame range to match the videos duration

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "Untitled",
        width: int | None = 1024,
        height: int | None = 1024,
        color: collections.abc.Sequence[float] | None = (0.0, 0.0, 0.0, 1.0),
        alpha: bool | None = True,
        generated_type: typing.Literal[
            bpy.stub_internal.rna_enums.ImageGeneratedTypeItems
        ]
        | None = "BLANK",
        float: bool | None = False,
        use_stereo_3d: bool | None = False,
        tiled: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new image

        :param execution_context:
        :param undo:
        :param name: Name, Image data-block name (optional, never None)
        :param width: Width, Image width (in [1, inf], optional)
        :param height: Height, Image height (in [1, inf], optional)
        :param color: Color, Default fill color (array of 4 items, in [0, inf], optional)
        :param alpha: Alpha, Create an image with an alpha channel (optional)
        :param generated_type: Generated Type, Fill the image with a grid for UV map testing (optional)
        :param float: 32-bit Float, Create image with 32-bit floating-point bit depth (optional)
        :param use_stereo_3d: Stereo 3D, Create an image with left and right views (optional)
        :param tiled: Tiled, Create a tiled image (optional)
        :return: Result of the operator call.
        """

class open(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open image

                :param execution_context:
                :param undo:
                :param allow_path_tokens: Allow the path to contain substitution tokens (optional)
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param files: Files, (optional)
                :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param relative_path: Relative Path, Select the file relative to the blend file (optional)
                :param show_multiview: Enable Multi-View, (optional)
                :param use_multiview: Use Multi-View, (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected images (based on file names) (optional)
                :param use_udim_detecting: Detect UDIMs, Detect selected UDIM files and load all matching tiles (optional)
                :return: Result of the operator call.
        """

class open_images(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param directory: directory, (optional, never None)
        :param files: files, (optional)
        :param relative_path: Use relative path, (optional)
        :param use_sequence_detection: Use sequence detection, (optional)
        :param use_udim_detection: Use UDIM detection, (optional)
        :return: Result of the operator call.
        """

class pack(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pack an image as embedded data into the .blend file

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class project_apply(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Project edited image back onto the object

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class project_edit(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Edit a snapshot of the 3D Viewport in an external image editor

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class read_viewlayers(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Read all the current scenes view layers from cache, as needed

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class reload(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reload current image from disk

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class remove_render_slot(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the current render slot

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class render_border(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xmin: int | None = 0,
        xmax: int | None = 0,
        ymin: int | None = 0,
        ymax: int | None = 0,
        wait_for_input: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the boundaries of the render region and enable render region

        :param execution_context:
        :param undo:
        :param xmin: X Min, (in [-inf, inf], optional)
        :param xmax: X Max, (in [-inf, inf], optional)
        :param ymin: Y Min, (in [-inf, inf], optional)
        :param ymax: Y Max, (in [-inf, inf], optional)
        :param wait_for_input: Wait for Input, (optional)
        :return: Result of the operator call.
        """

class replace(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Replace current image by another one from disk

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param relative_path: Relative Path, Select the file relative to the blend file (optional)
                :param show_multiview: Enable Multi-View, (optional)
                :param use_multiview: Use Multi-View, (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :return: Result of the operator call.
        """

class resize(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        size: collections.abc.Sequence[int] | None = (0, 0),
        all_udims: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Resize the image

        :param execution_context:
        :param undo:
        :param size: Size, (array of 2 items, in [1, inf], optional)
        :param all_udims: All UDIM Tiles, Scale all the images UDIM tiles (optional)
        :return: Result of the operator call.
        """

class rotate_orthogonal(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        degrees: typing.Literal["90", "180", "270"] | None = "90",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rotate the image

                :param execution_context:
                :param undo:
                :param degrees: Degrees, Amount of rotation in degrees (90, 180, 270) (optional)

        90
        90 Degrees -- Rotate 90 degrees clockwise.

        180
        180 Degrees -- Rotate 180 degrees clockwise.

        270
        270 Degrees -- Rotate 270 degrees clockwise.
                :return: Result of the operator call.
        """

class sample(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        size: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Use mouse to sample a color in current image

        :param execution_context:
        :param undo:
        :param size: Sample Size, (in [1, 128], optional)
        :return: Result of the operator call.
        """

class sample_line(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Sample a line and show it in Scope panels

        :param execution_context:
        :param undo:
        :param xstart: X Start, (in [-inf, inf], optional)
        :param xend: X End, (in [-inf, inf], optional)
        :param ystart: Y Start, (in [-inf, inf], optional)
        :param yend: Y End, (in [-inf, inf], optional)
        :param flip: Flip, (optional)
        :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
        :return: Result of the operator call.
        """

class save(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save the image with current name and settings

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class save_all_modified(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save all modified images

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class save_as(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save the image with another name and/or settings

                :param execution_context:
                :param undo:
                :param save_as_render: Save As Render, Save image with render color management.For display image formats like PNG, apply view and display transform.For intermediate image formats like OpenEXR, use the default render output color space(optional)
                :param copy: Copy, Create a new image file without modifying the current image in Blender (optional)
                :param allow_path_tokens: Allow the path to contain substitution tokens (optional)
                :param filepath: File Path, Path to file (optional, never None)
                :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
                :param filter_blender: Filter .blend files, (optional)
                :param filter_backup: Filter backup .blend files, (optional)
                :param filter_image: Filter image files, (optional)
                :param filter_movie: Filter movie files, (optional)
                :param filter_python: Filter Python files, (optional)
                :param filter_font: Filter font files, (optional)
                :param filter_sound: Filter sound files, (optional)
                :param filter_text: Filter text files, (optional)
                :param filter_archive: Filter archive files, (optional)
                :param filter_btx: Filter btx files, (optional)
                :param filter_alembic: Filter Alembic files, (optional)
                :param filter_usd: Filter USD files, (optional)
                :param filter_obj: Filter OBJ files, (optional)
                :param filter_volume: Filter OpenVDB volume files, (optional)
                :param filter_folder: Filter folders, (optional)
                :param filter_blenlib: Filter Blender IDs, (optional)
                :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
                :param relative_path: Relative Path, Select the file relative to the blend file (optional)
                :param show_multiview: Enable Multi-View, (optional)
                :param use_multiview: Use Multi-View, (optional)
                :param display_type: Display Type, (optional)

        DEFAULT
        Default -- Automatically determine display type for files.

        LIST_VERTICAL
        Short List -- Display files as short list.

        LIST_HORIZONTAL
        Long List -- Display files as a detailed list.

        THUMBNAIL
        Thumbnails -- Display files as thumbnails.
                :param sort_method: File sorting mode, (optional)
                :return: Result of the operator call.
        """

class save_sequence(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save a sequence of images

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class tile_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        number: int | None = 1002,
        count: int | None = 1,
        label: str = "",
        fill: bool | None = True,
        color: collections.abc.Sequence[float] | None = (0.0, 0.0, 0.0, 1.0),
        generated_type: typing.Literal[
            bpy.stub_internal.rna_enums.ImageGeneratedTypeItems
        ]
        | None = "BLANK",
        width: int | None = 1024,
        height: int | None = 1024,
        float: bool | None = False,
        alpha: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Adds a tile to the image

        :param execution_context:
        :param undo:
        :param number: Number, UDIM number of the tile (in [1001, 2000], optional)
        :param count: Count, How many tiles to add (in [1, inf], optional)
        :param label: Label, Optional tile label (optional, never None)
        :param fill: Fill, Fill new tile with a generated image (optional)
        :param color: Color, Default fill color (array of 4 items, in [0, inf], optional)
        :param generated_type: Generated Type, Fill the image with a grid for UV map testing (optional)
        :param width: Width, Image width (in [1, inf], optional)
        :param height: Height, Image height (in [1, inf], optional)
        :param float: 32-bit Float, Create image with 32-bit floating-point bit depth (optional)
        :param alpha: Alpha, Create an image with an alpha channel (optional)
        :return: Result of the operator call.
        """

class tile_fill(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        color: collections.abc.Sequence[float] | None = (0.0, 0.0, 0.0, 1.0),
        generated_type: typing.Literal[
            bpy.stub_internal.rna_enums.ImageGeneratedTypeItems
        ]
        | None = "BLANK",
        width: int | None = 1024,
        height: int | None = 1024,
        float: bool | None = False,
        alpha: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Fill the current tile with a generated image

        :param execution_context:
        :param undo:
        :param color: Color, Default fill color (array of 4 items, in [0, inf], optional)
        :param generated_type: Generated Type, Fill the image with a grid for UV map testing (optional)
        :param width: Width, Image width (in [1, inf], optional)
        :param height: Height, Image height (in [1, inf], optional)
        :param float: 32-bit Float, Create image with 32-bit floating-point bit depth (optional)
        :param alpha: Alpha, Create an image with an alpha channel (optional)
        :return: Result of the operator call.
        """

class tile_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Removes a tile from the image

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class unpack(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        method: typing.Literal[bpy.stub_internal.rna_enums.UnpackMethodItems]
        | None = "USE_LOCAL",
        id: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save an image packed in the .blend file to disk

        :param execution_context:
        :param undo:
        :param method: Method, How to unpack (optional)
        :param id: Image Name, Image data-block name to unpack (optional, never None)
        :return: Result of the operator call.
        """

class view_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        fit_view: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """View the entire image

        :param execution_context:
        :param undo:
        :param fit_view: Fit View, Fit frame to the viewport (optional)
        :return: Result of the operator call.
        """

class view_center_cursor(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Center the view so that the cursor is in the middle of the view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_cursor_center(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        fit_view: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set 2D cursor to center view location

        :param execution_context:
        :param undo:
        :param fit_view: Fit View, Fit frame to the viewport (optional)
        :return: Result of the operator call.
        """

class view_ndof(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Use a 3D mouse device to pan/zoom the view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_pan(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        offset: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pan the view

        :param execution_context:
        :param undo:
        :param offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image (array of 2 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class view_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """View all selected UVs

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_zoom(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        factor: float | None = 0.0,
        use_cursor_init: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Zoom in/out the image

        :param execution_context:
        :param undo:
        :param factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out (in [-inf, inf], optional)
        :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used (optional)
        :return: Result of the operator call.
        """

class view_zoom_border(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Zoom in the view to the nearest item contained in the border

        :param execution_context:
        :param undo:
        :param xmin: X Min, (in [-inf, inf], optional)
        :param xmax: X Max, (in [-inf, inf], optional)
        :param ymin: Y Min, (in [-inf, inf], optional)
        :param ymax: Y Max, (in [-inf, inf], optional)
        :param wait_for_input: Wait for Input, (optional)
        :param zoom_out: Zoom Out, (optional)
        :return: Result of the operator call.
        """

class view_zoom_in(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Zoom in the image (centered around 2D cursor)

        :param execution_context:
        :param undo:
        :param location: Location, Cursor location in screen coordinates (array of 2 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class view_zoom_out(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: collections.abc.Sequence[float] | mathutils.Vector | None = (
            0.0,
            0.0,
        ),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Zoom out the image (centered around 2D cursor)

        :param execution_context:
        :param undo:
        :param location: Location, Cursor location in screen coordinates (array of 2 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class view_zoom_ratio(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        ratio: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set zoom ratio of the view

        :param execution_context:
        :param undo:
        :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out (in [-inf, inf], optional)
        :return: Result of the operator call.
        """
