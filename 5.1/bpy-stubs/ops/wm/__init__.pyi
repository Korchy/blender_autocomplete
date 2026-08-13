import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bl_operators.wm
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

class alembic_export(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = True,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
        filter_python: bool | None = False,
        filter_font: bool | None = False,
        filter_sound: bool | None = False,
        filter_text: bool | None = False,
        filter_archive: bool | None = False,
        filter_btx: bool | None = False,
        filter_alembic: bool | None = True,
        filter_usd: bool | None = False,
        filter_obj: bool | None = False,
        filter_volume: bool | None = False,
        filter_folder: bool | None = True,
        filter_blenlib: bool | None = False,
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        filter_glob: str = "*.abc",
        start: int | None = -2147483648,
        end: int | None = -2147483648,
        xsamples: int | None = 1,
        gsamples: int | None = 1,
        sh_open: float | None = 0.0,
        sh_close: float | None = 1.0,
        selected: bool | None = False,
        flatten: bool | None = False,
        collection: str = "",
        uvs: bool | None = True,
        packuv: bool | None = True,
        normals: bool | None = True,
        vcolors: bool | None = False,
        orcos: bool | None = True,
        face_sets: bool | None = False,
        subdiv_schema: bool | None = False,
        apply_subdiv: bool | None = False,
        curves_as_mesh: bool | None = False,
        use_instancing: bool | None = True,
        global_scale: float | None = 1.0,
        triangulate: bool | None = False,
        quad_method: typing.Literal[
            bpy.stub_internal.rna_enums.ModifierTriangulateQuadMethodItems
        ]
        | None = "SHORTEST_DIAGONAL",
        ngon_method: typing.Literal[
            bpy.stub_internal.rna_enums.ModifierTriangulateNgonMethodItems
        ]
        | None = "BEAUTY",
        export_hair: bool | None = True,
        export_particles: bool | None = True,
        export_custom_properties: bool | None = True,
        as_background_job: bool | None = False,
        evaluation_mode: typing.Literal["RENDER", "VIEWPORT"] | None = "RENDER",
        init_scene_frame_range: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Export current scene in an Alembic archive

                :param execution_context:
                :param undo:
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
                :param filter_glob: (optional, never None)
                :param start: Start Frame, Start frame of the export, use the default value to take the start frame of the current scene (in [-inf, inf], optional)
                :param end: End Frame, End frame of the export, use the default value to take the end frame of the current scene (in [-inf, inf], optional)
                :param xsamples: Transform Samples, Number of times per frame transformations are sampled (in [1, 128], optional)
                :param gsamples: Geometry Samples, Number of times per frame object data are sampled (in [1, 128], optional)
                :param sh_open: Shutter Open, Time at which the shutter is open (in [-1, 1], optional)
                :param sh_close: Shutter Close, Time at which the shutter is closed (in [-1, 1], optional)
                :param selected: Selected Objects Only, Export only selected objects (optional)
                :param flatten: Flatten Hierarchy, Do not preserve objects parent/children relationship (optional)
                :param collection: Collection, (optional, never None)
                :param uvs: UV Coordinates, Export UV coordinates (optional)
                :param packuv: Merge UVs, (optional)
                :param normals: Normals, Export normals (optional)
                :param vcolors: Color Attributes, Export color attributes (optional)
                :param orcos: Generated Coordinates, Export undeformed mesh vertex coordinates (optional)
                :param face_sets: Face Sets, Export per face shading group assignments (optional)
                :param subdiv_schema: Use Subdivision Schema, Export meshes using Alembics subdivision schema (optional)
                :param apply_subdiv: Apply Subdivision Surface, Export subdivision surfaces as meshes (optional)
                :param curves_as_mesh: Curves as Mesh, Export curves and NURBS surfaces as meshes (optional)
                :param use_instancing: Use Instancing, Export data of duplicated objects as Alembic instances; speeds up the export and can be disabled for compatibility with other software (optional)
                :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin (in [0.0001, 1000], optional)
                :param triangulate: Triangulate, Export polygons (quads and n-gons) as triangles (optional)
                :param quad_method: Quad Method, Method for splitting the quads into triangles (optional)
                :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles (optional)
                :param export_hair: Export Hair, Exports hair particle systems as animated curves (optional)
                :param export_particles: Export Particles, Exports non-hair particle systems (optional)
                :param export_custom_properties: Export Custom Properties, Export custom properties to Alembic .userProperties (optional)
                :param as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job (optional)
                :param evaluation_mode: Settings, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering (optional)

        RENDER
        Render -- Use Render settings for object visibility, modifier settings, etc.

        VIEWPORT
        Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
                :param init_scene_frame_range: (optional)
                :return: Result of the operator call.
        """

class alembic_import(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        directory: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        check_existing: bool | None = False,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
        filter_python: bool | None = False,
        filter_font: bool | None = False,
        filter_sound: bool | None = False,
        filter_text: bool | None = False,
        filter_archive: bool | None = False,
        filter_btx: bool | None = False,
        filter_alembic: bool | None = True,
        filter_usd: bool | None = False,
        filter_obj: bool | None = False,
        filter_volume: bool | None = False,
        filter_folder: bool | None = True,
        filter_blenlib: bool | None = False,
        filemode: int | None = 8,
        relative_path: bool | None = True,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        filter_glob: str = "*.abc",
        scale: float | None = 1.0,
        set_frame_range: bool | None = True,
        validate_meshes: bool | None = False,
        always_add_cache_reader: bool | None = False,
        is_sequence: bool | None = False,
        as_background_job: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load an Alembic archive

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param files: Files, (optional)
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
                :param filter_glob: (optional, never None)
                :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin (in [0.0001, 1000], optional)
                :param set_frame_range: Set Frame Range, If checked, update scenes start and end frame to match those of the Alembic archive (optional)
                :param validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing) (optional)
                :param always_add_cache_reader: Always Add Cache Reader, Add cache modifiers and constraints to imported objects even if they are not animated so that they can be updated when reloading the Alembic archive (optional)
                :param is_sequence: Is Sequence, Set to true if the cache is split into separate files (optional)
                :param as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job (optional)
                :return: Result of the operator call.
        """

class append(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        directory: str = "",
        filename: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        check_existing: bool | None = False,
        filter_blender: bool | None = True,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filter_blenlib: bool | None = True,
        filemode: int | None = 1,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        link: bool | None = False,
        do_reuse_local_id: bool | None = False,
        clear_asset_data: bool | None = False,
        autoselect: bool | None = True,
        active_collection: bool | None = True,
        instance_collections: bool | None = False,
        instance_object_data: bool | None = True,
        set_fake: bool | None = False,
        use_recursive: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Append from a Library .blend file

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param filename: File Name, Name of the file (optional, never None)
                :param files: Files, (optional)
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
                :param link: Link, Link the objects or data-blocks rather than appending (optional)
                :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy (optional)
                :param clear_asset_data: Clear Asset Data, Dont add asset meta-data or tags from the original data-block (optional)
                :param autoselect: Select, Select new objects (optional)
                :param active_collection: Active Collection, Put new objects on the active collection (optional)
                :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene (optional)
                :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects (optional)
                :param set_fake: Fake User, Set "Fake User" for appended items (except objects and collections) (optional)
                :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries (optional)
                :return: Result of the operator call.
        """

class batch_rename(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_type: typing.Literal[
            "OBJECT",
            "COLLECTION",
            "MATERIAL",
            "MESH",
            "CURVE",
            "META",
            "VOLUME",
            "GREASEPENCIL",
            "ARMATURE",
            "LATTICE",
            "LIGHT",
            "LIGHT_PROBE",
            "CAMERA",
            "SPEAKER",
            "BONE",
            "NODE",
            "SEQUENCE_STRIP",
            "ACTION_CLIP",
            "SCENE",
            "BRUSH",
        ]
        | None = "OBJECT",
        data_source: typing.Literal["SELECT", "ALL"] | None = "SELECT",
        actions: bpy.types.bpy_prop_collection[bl_operators.wm.BatchRenameAction]
        | None = None,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Rename multiple items at once

        :param execution_context:
        :param undo:
        :param data_type: Type, Type of data to rename (optional)
        :param data_source: Source, (optional)
        :param actions: actions, (optional)
        :return: Result of the operator call.
        """

class blend_strings_utf8_validate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Check and fix all strings in current .blend file to be valid UTF-8 Unicode (needed for some old, 2.4x area files)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class call_asset_shelf_popover(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a predefined asset shelf in a popup

        :param execution_context:
        :param undo:
        :param name: Asset Shelf Name, Identifier of the asset shelf to display (optional, never None)
        :return: Result of the operator call.
        """

class call_menu(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a predefined menu

        :param execution_context:
        :param undo:
        :param name: Name, Name of the menu (optional, never None)
        :return: Result of the operator call.
        """

class call_menu_pie(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a predefined pie menu

        :param execution_context:
        :param undo:
        :param name: Name, Name of the pie menu (optional, never None)
        :return: Result of the operator call.
        """

class call_panel(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        keep_open: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a predefined panel

        :param execution_context:
        :param undo:
        :param name: Name, Name of the menu (optional, never None)
        :param keep_open: Keep Open, (optional)
        :return: Result of the operator call.
        """

class clear_recent_files(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        remove: typing.Literal["ALL", "MISSING"] | None = "ALL",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the recent files list

        :param execution_context:
        :param undo:
        :param remove: Remove, (optional)
        :return: Result of the operator call.
        """

class collection_export_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Invoke all configured exporters for all collections

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class context_collection_boolean_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path_iter: str = "",
        data_path_item: str = "",
        type: typing.Literal["TOGGLE", "ENABLE", "DISABLE"] | None = "TOGGLE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set boolean values for a collection of items

        :param execution_context:
        :param undo:
        :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable (optional, never None)
        :param data_path_item: data_path_item, The data path from each iterable to the value (int or float) (optional, never None)
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class context_cycle_array(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        reverse: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set a context array value (useful for cycling the active mesh edit mode)

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param reverse: Reverse, Cycle backwards (optional)
        :return: Result of the operator call.
        """

class context_cycle_enum(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        reverse: bool | None = False,
        wrap: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle a context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param reverse: Reverse, Cycle backwards (optional)
        :param wrap: Wrap, Wrap back to the first/last values (optional)
        :return: Result of the operator call.
        """

class context_cycle_int(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        reverse: bool | None = False,
        wrap: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set a context value (useful for cycling active material, shape keys, groups, etc.)

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param reverse: Reverse, Cycle backwards (optional)
        :param wrap: Wrap, Wrap back to the first/last values (optional)
        :return: Result of the operator call.
        """

class context_menu_enum(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :return: Result of the operator call.
        """

class context_modal_mouse(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path_iter: str = "",
        data_path_item: str = "",
        header_text: str = "",
        input_scale: float | None = 0.01,
        invert: bool | None = False,
        initial_x: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Adjust arbitrary values with mouse input

        :param execution_context:
        :param undo:
        :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable (optional, never None)
        :param data_path_item: data_path_item, The data path from each iterable to the value (int or float) (optional, never None)
        :param header_text: Header Text, Text to display in header during scale (optional, never None)
        :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta (in [-inf, inf], optional)
        :param invert: invert, Invert the mouse input (optional)
        :param initial_x: initial_x, (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class context_pie_enum(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :return: Result of the operator call.
        """

class context_scale_float(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        value: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Scale a float context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param value: Value, Assign value (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class context_scale_int(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        value: float | None = 1.0,
        always_step: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Scale an int context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param value: Value, Assign value (in [-inf, inf], optional)
        :param always_step: Always Step, Always adjust the value by a minimum of 1 when value is not 1.0 (optional)
        :return: Result of the operator call.
        """

class context_set_boolean(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        value: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set a context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param value: Value, Assignment value (optional)
        :return: Result of the operator call.
        """

class context_set_enum(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        value: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set a context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param value: Value, Assignment value (as a string) (optional, never None)
        :return: Result of the operator call.
        """

class context_set_float(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        value: float | None = 0.0,
        relative: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set a context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param value: Value, Assignment value (in [-inf, inf], optional)
        :param relative: Relative, Apply relative to the current value (delta) (optional)
        :return: Result of the operator call.
        """

class context_set_id(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        value: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set a context value to an ID data-block

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param value: Value, Assign value (optional, never None)
        :return: Result of the operator call.
        """

class context_set_int(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        value: int | None = 0,
        relative: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set a context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param value: Value, Assign value (in [-inf, inf], optional)
        :param relative: Relative, Apply relative to the current value (delta) (optional)
        :return: Result of the operator call.
        """

class context_set_string(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        value: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set a context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param value: Value, Assign value (optional, never None)
        :return: Result of the operator call.
        """

class context_set_value(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        value: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set a context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param value: Value, Assignment value (as a string) (optional, never None)
        :return: Result of the operator call.
        """

class context_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        module: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle a context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param module: Module, Optionally override the context with a module (optional, never None)
        :return: Result of the operator call.
        """

class context_toggle_enum(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        value_1: str = "",
        value_2: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle a context value

        :param execution_context:
        :param undo:
        :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file) (optional, never None)
        :param value_1: Value, Toggle enum (optional, never None)
        :param value_2: Value, Toggle enum (optional, never None)
        :return: Result of the operator call.
        """

class debug_menu(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        debug_value: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a popup to set the debug level

        :param execution_context:
        :param undo:
        :param debug_value: Debug Value, (in [-32768, 32767], optional)
        :return: Result of the operator call.
        """

class doc_view(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        doc_id: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open online reference docs in a web browser

        :param execution_context:
        :param undo:
        :param doc_id: Doc ID, (optional, never None)
        :return: Result of the operator call.
        """

class doc_view_manual(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        doc_id: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load online manual

        :param execution_context:
        :param undo:
        :param doc_id: Doc ID, (optional, never None)
        :return: Result of the operator call.
        """

class doc_view_manual_ui_context(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """View a context based online manual in a web browser

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class drop_blend_file(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param filepath: filepath, (optional, never None)
        :return: Result of the operator call.
        """

class drop_import_file(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        directory: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Operator that allows file handlers to receive file drops

        :param execution_context:
        :param undo:
        :param directory: Directory, Directory of the file (optional, never None)
        :param files: Files, (optional)
        :return: Result of the operator call.
        """

class fbx_import(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        directory: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        check_existing: bool | None = False,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        global_scale: float | None = 1.0,
        mtl_name_collision_mode: typing.Literal["MAKE_UNIQUE", "REFERENCE_EXISTING"]
        | None = "MAKE_UNIQUE",
        import_colors: typing.Literal["NONE", "SRGB", "LINEAR"] | None = "SRGB",
        use_custom_normals: bool | None = True,
        use_custom_props: bool | None = True,
        use_custom_props_enum_as_string: bool | None = True,
        import_subdivision: bool | None = False,
        ignore_leaf_bones: bool | None = False,
        validate_meshes: bool | None = True,
        use_anim: bool | None = True,
        anim_offset: float | None = 1.0,
        filter_glob: str = "*.fbx",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Import FBX file into current scene

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param files: Files, (optional)
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
                :param global_scale: Scale, (in [1e-06, 1e+06], optional)
                :param mtl_name_collision_mode: Material Name Collision, Behavior when the name of an imported material conflicts with an existing material (optional)

        MAKE_UNIQUE
        Make Unique -- Import each FBX material as a unique Blender material.

        REFERENCE_EXISTING
        Reference Existing -- If a material with the same name already exists, reference that instead of importing.
                :param import_colors: Vertex Colors, Import vertex color attributes (optional)

        NONE
        None -- Do not import color attributes.

        SRGB
        sRGB -- Vertex colors in the file are in sRGB color space.

        LINEAR
        Linear -- Vertex colors in the file are in linear color space.
                :param use_custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will compute them) (optional)
                :param use_custom_props: Custom Properties, Import user properties as custom properties (optional)
                :param use_custom_props_enum_as_string: Enums As Strings, Store custom property enumeration values as strings (optional)
                :param import_subdivision: Subdivision Data, Import FBX subdivision information as subdivision surface modifiers (optional)
                :param ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone) (optional)
                :param validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing) (optional)
                :param use_anim: Import Animation, Import FBX animation (optional)
                :param anim_offset: Offset, Offset to apply to animation timestamps, in frames (in [-1e+06, 1e+06], optional)
                :param filter_glob: Extension Filter, (optional, never None)
                :return: Result of the operator call.
        """

class grease_pencil_export_pdf(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = True,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
        filter_python: bool | None = False,
        filter_font: bool | None = False,
        filter_sound: bool | None = False,
        filter_text: bool | None = False,
        filter_archive: bool | None = False,
        filter_btx: bool | None = False,
        filter_alembic: bool | None = False,
        filter_usd: bool | None = False,
        filter_obj: bool | None = True,
        filter_volume: bool | None = False,
        filter_folder: bool | None = True,
        filter_blenlib: bool | None = False,
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        use_fill: bool | None = True,
        selected_object_type: typing.Literal["ACTIVE", "SELECTED", "VISIBLE"]
        | None = "ACTIVE",
        frame_mode: typing.Literal["ACTIVE", "SELECTED", "SCENE"] | None = "ACTIVE",
        stroke_sample: float | None = 0.0,
        use_uniform_width: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Export Grease Pencil to PDF

                :param execution_context:
                :param undo:
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
                :param use_fill: Fill, Export strokes with fill enabled (optional)
                :param selected_object_type: Object, Which objects to include in the export (optional)

        ACTIVE
        Active -- Include only the active object.

        SELECTED
        Selected -- Include selected objects.

        VISIBLE
        Visible -- Include all visible objects.
                :param frame_mode: Frames, Which frames to include in the export (optional)

        ACTIVE
        Active -- Include only active frame.

        SELECTED
        Selected -- Include selected frames.

        SCENE
        Scene -- Include all scene frames.
                :param stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling (in [0, 100], optional)
                :param use_uniform_width: Uniform Width, Export strokes with uniform width (optional)
                :return: Result of the operator call.
        """

class grease_pencil_export_svg(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = True,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
        filter_python: bool | None = False,
        filter_font: bool | None = False,
        filter_sound: bool | None = False,
        filter_text: bool | None = False,
        filter_archive: bool | None = False,
        filter_btx: bool | None = False,
        filter_alembic: bool | None = False,
        filter_usd: bool | None = False,
        filter_obj: bool | None = True,
        filter_volume: bool | None = False,
        filter_folder: bool | None = True,
        filter_blenlib: bool | None = False,
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        use_fill: bool | None = True,
        selected_object_type: typing.Literal["ACTIVE", "SELECTED", "VISIBLE"]
        | None = "ACTIVE",
        frame_mode: typing.Literal["ACTIVE", "SELECTED", "SCENE"] | None = "ACTIVE",
        stroke_sample: float | None = 0.0,
        use_uniform_width: bool | None = False,
        use_clip_camera: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Export Grease Pencil to SVG

                :param execution_context:
                :param undo:
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
                :param use_fill: Fill, Export strokes with fill enabled (optional)
                :param selected_object_type: Object, Which objects to include in the export (optional)

        ACTIVE
        Active -- Include only the active object.

        SELECTED
        Selected -- Include selected objects.

        VISIBLE
        Visible -- Include all visible objects.
                :param frame_mode: Frames, Which frames to include in the export (optional)

        ACTIVE
        Active -- Include only active frame.

        SELECTED
        Selected -- Include selected frames.

        SCENE
        Scene -- Include all scene frames.
                :param stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling (in [0, 100], optional)
                :param use_uniform_width: Uniform Width, Export strokes with uniform width (optional)
                :param use_clip_camera: Clip Camera, Clip drawings to camera size when exporting in camera view (optional)
                :return: Result of the operator call.
        """

class grease_pencil_import_svg(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        directory: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        check_existing: bool | None = False,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
        filter_python: bool | None = False,
        filter_font: bool | None = False,
        filter_sound: bool | None = False,
        filter_text: bool | None = False,
        filter_archive: bool | None = False,
        filter_btx: bool | None = False,
        filter_alembic: bool | None = False,
        filter_usd: bool | None = False,
        filter_obj: bool | None = True,
        filter_volume: bool | None = False,
        filter_folder: bool | None = True,
        filter_blenlib: bool | None = False,
        filemode: int | None = 8,
        relative_path: bool | None = True,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        resolution: int | None = 10,
        scale: float | None = 10.0,
        use_scene_unit: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Import SVG into Grease Pencil

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param files: Files, (optional)
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
                :param resolution: Resolution, Resolution of the generated strokes (in [1, 100000], optional)
                :param scale: Scale, Scale of the final strokes (in [1e-06, 1e+06], optional)
                :param use_scene_unit: Scene Unit, Apply current scenes unit (as defined by unit scale) to imported data (optional)
                :return: Result of the operator call.
        """

class id_linked_relocate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        id_session_uid: int | None = 0,
        filepath: str = "",
        directory: str = "",
        filename: str = "",
        check_existing: bool | None = False,
        filter_blender: bool | None = True,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filter_blenlib: bool | None = True,
        filemode: int | None = 1,
        relative_path: bool | None = True,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        link: bool | None = True,
        do_reuse_local_id: bool | None = False,
        clear_asset_data: bool | None = False,
        autoselect: bool | None = True,
        active_collection: bool | None = False,
        instance_collections: bool | None = False,
        instance_object_data: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Relocate a linked ID, i.e. select another ID to link, and remap its local usages to that newly linked data-block). Currently only designed as an internal operator, not directly exposed to the user

                :param execution_context:
                :param undo:
                :param id_session_uid: Linked ID Session UID, Unique runtime identifier for the linked ID to relocate (in [0, inf], optional)
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param filename: File Name, Name of the file (optional, never None)
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
                :param link: Link, Link the objects or data-blocks rather than appending (optional)
                :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy (optional)
                :param clear_asset_data: Clear Asset Data, Dont add asset meta-data or tags from the original data-block (optional)
                :param autoselect: Select, Select new objects (optional)
                :param active_collection: Active Collection, Put new objects on the active collection (optional)
                :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene (optional)
                :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects (optional)
                :return: Result of the operator call.
        """

class interface_theme_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a custom theme to the preset list

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class interface_theme_preset_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove a custom theme from the preset list

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class interface_theme_preset_save(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save a custom theme in the preset list

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class keyconfig_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a custom keymap configuration to the preset list

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class keyconfig_preset_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove a custom keymap configuration from the preset list

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :return: Result of the operator call.
        """

class lib_reload(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        library: str = "",
        filepath: str = "",
        directory: str = "",
        filename: str = "",
        hide_props_region: bool | None = True,
        check_existing: bool | None = False,
        filter_blender: bool | None = True,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        relative_path: bool | None = True,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reload the given library

                :param execution_context:
                :param undo:
                :param library: Library, Library to reload (optional, never None)
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param filename: File Name, Name of the file (optional, never None)
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

class lib_relocate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        library: str = "",
        filepath: str = "",
        directory: str = "",
        filename: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        hide_props_region: bool | None = True,
        check_existing: bool | None = False,
        filter_blender: bool | None = True,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        relative_path: bool | None = True,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Relocate the given library to one or several others

                :param execution_context:
                :param undo:
                :param library: Library, Library to relocate (optional, never None)
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param filename: File Name, Name of the file (optional, never None)
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

class link(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        directory: str = "",
        filename: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        check_existing: bool | None = False,
        filter_blender: bool | None = True,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filter_blenlib: bool | None = True,
        filemode: int | None = 1,
        relative_path: bool | None = True,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        link: bool | None = True,
        do_reuse_local_id: bool | None = False,
        clear_asset_data: bool | None = False,
        autoselect: bool | None = True,
        active_collection: bool | None = True,
        instance_collections: bool | None = True,
        instance_object_data: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Link from a Library .blend file

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param filename: File Name, Name of the file (optional, never None)
                :param files: Files, (optional)
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
                :param link: Link, Link the objects or data-blocks rather than appending (optional)
                :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy (optional)
                :param clear_asset_data: Clear Asset Data, Dont add asset meta-data or tags from the original data-block (optional)
                :param autoselect: Select, Select new objects (optional)
                :param active_collection: Active Collection, Put new objects on the active collection (optional)
                :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene (optional)
                :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects (optional)
                :return: Result of the operator call.
        """

class memory_statistics(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Print memory statistics to the console

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class obj_export(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = True,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        export_animation: bool | None = False,
        start_frame: int | None = -2147483648,
        end_frame: int | None = 2147483647,
        forward_axis: typing.Literal[
            "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
        ]
        | None = "NEGATIVE_Z",
        up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
        | None = "Y",
        global_scale: float | None = 1.0,
        apply_modifiers: bool | None = True,
        apply_transform: bool | None = True,
        export_eval_mode: typing.Literal["DAG_EVAL_RENDER", "DAG_EVAL_VIEWPORT"]
        | None = "DAG_EVAL_VIEWPORT",
        export_selected_objects: bool | None = False,
        export_uv: bool | None = True,
        export_normals: bool | None = True,
        export_colors: bool | None = False,
        export_materials: bool | None = True,
        export_pbr_extensions: bool | None = False,
        path_mode: typing.Literal[
            "AUTO", "ABSOLUTE", "RELATIVE", "MATCH", "STRIP", "COPY"
        ]
        | None = "AUTO",
        export_triangulated_mesh: bool | None = False,
        export_curves_as_nurbs: bool | None = False,
        export_object_groups: bool | None = False,
        export_material_groups: bool | None = False,
        export_vertex_groups: bool | None = False,
        export_smooth_groups: bool | None = False,
        smooth_group_bitflags: bool | None = False,
        filter_glob: str = "*.obj;*.mtl",
        collection: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save the scene to a Wavefront OBJ file

                :param execution_context:
                :param undo:
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
                :param export_animation: Export Animation, Export multiple frames instead of the current frame only (optional)
                :param start_frame: Start Frame, The first frame to be exported (in [-inf, inf], optional)
                :param end_frame: End Frame, The last frame to be exported (in [-inf, inf], optional)
                :param forward_axis: Forward Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param up_axis: Up Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin (in [0.0001, 10000], optional)
                :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes (optional)
                :param apply_transform: Apply Transform, Apply object transforms to exported vertices (optional)
                :param export_eval_mode: Object Properties, Determines properties like object visibility, modifiers etc., where they differ for Render and Viewport (optional)

        DAG_EVAL_RENDER
        Render -- Export objects as they appear in render.

        DAG_EVAL_VIEWPORT
        Viewport -- Export objects as they appear in the viewport.
                :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects (optional)
                :param export_uv: Export UVs, (optional)
                :param export_normals: Export Normals, Export per-face normals if the face is flat-shaded, per-face-corner normals if smooth-shaded (optional)
                :param export_colors: Export Colors, Export per-vertex colors (optional)
                :param export_materials: Export Materials, Export MTL library. There must be a Principled-BSDF node for image textures to be exported to the MTL file (optional)
                :param export_pbr_extensions: Export Materials with PBR Extensions, Export MTL library using PBR extensions (roughness, metallic, sheen, coat, anisotropy, transmission) (optional)
                :param path_mode: Path Mode, Method used to reference paths (optional)

        AUTO
        Auto -- Use relative paths with subdirectories only.

        ABSOLUTE
        Absolute -- Always write absolute paths.

        RELATIVE
        Relative -- Write relative paths where possible.

        MATCH
        Match -- Match absolute/relative setting with input path.

        STRIP
        Strip -- Write filename only.

        COPY
        Copy -- Copy the file to the destination path.
                :param export_triangulated_mesh: Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4 (optional)
                :param export_curves_as_nurbs: Export Curves as NURBS, Export curves in parametric form instead of exporting as mesh (optional)
                :param export_object_groups: Export Object Groups, Append mesh name to object name, separated by a _ (optional)
                :param export_material_groups: Export Material Groups, Generate an OBJ group for each part of a geometry using a different material (optional)
                :param export_vertex_groups: Export Vertex Groups, Export the name of the vertex group of a face. It is approximated by choosing the vertex group with the most members among the vertices of a face (optional)
                :param export_smooth_groups: Export Smooth Groups, Generate smooth groups identifiers for each group of smooth faces, as unique integer values by default (optional)
                :param smooth_group_bitflags: Bitflags Smooth Groups, If exporting smoothgroups, generate bitflags values for the groups, instead of unique integer values. The same bitflag value can be re-used for different groups of smooth faces, as long as they have no common sharp edges or vertices (optional)
                :param filter_glob: Extension Filter, (optional, never None)
                :param collection: Collection, (optional, never None)
                :return: Result of the operator call.
        """

class obj_import(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        directory: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        check_existing: bool | None = False,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        global_scale: float | None = 1.0,
        clamp_size: float | None = 0.0,
        forward_axis: typing.Literal[
            "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
        ]
        | None = "NEGATIVE_Z",
        up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
        | None = "Y",
        use_split_objects: bool | None = True,
        use_split_groups: bool | None = False,
        import_vertex_groups: bool | None = False,
        validate_meshes: bool | None = True,
        close_spline_loops: bool | None = True,
        collection_separator: str = "",
        mtl_name_collision_mode: typing.Literal["MAKE_UNIQUE", "REFERENCE_EXISTING"]
        | None = "MAKE_UNIQUE",
        filter_glob: str = "*.obj;*.mtl",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load a Wavefront OBJ scene

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param files: Files, (optional)
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
                :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin (in [0.0001, 10000], optional)
                :param clamp_size: Clamp Bounding Box, Resize the objects to keep bounding box under this value. Value 0 disables clamping (in [0, 1000], optional)
                :param forward_axis: Forward Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param up_axis: Up Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param use_split_objects: Split By Object, Import each OBJ o as a separate object (optional)
                :param use_split_groups: Split By Group, Import each OBJ g as a separate object (optional)
                :param import_vertex_groups: Vertex Groups, Import OBJ groups as vertex groups (optional)
                :param validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing) (optional)
                :param close_spline_loops: Detect Cyclic Curves, Join curve endpoints if overlapping control points are detected (if disabled, no curves will be cyclic) (optional)
                :param collection_separator: Path Separator, Character used to separate objects name into hierarchical structure (optional, never None)
                :param mtl_name_collision_mode: Material Name Collision, How to handle naming collisions when importing materials (optional)

        MAKE_UNIQUE
        Make Unique -- Create new materials with unique names for each OBJ file.

        REFERENCE_EXISTING
        Reference Existing -- Use existing materials with same name instead of creating new ones.
                :param filter_glob: Extension Filter, (optional, never None)
                :return: Result of the operator call.
        """

class open_mainfile(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        hide_props_region: bool | None = True,
        check_existing: bool | None = False,
        filter_blender: bool | None = True,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        load_ui: bool | None = True,
        use_scripts: bool | None = False,
        display_file_selector: bool | None = True,
        state: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a Blender file

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
                :param load_ui: Load UI, Load user interface setup in the .blend file (optional)
                :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences (optional)
                :param display_file_selector: Display File Selector, (optional)
                :param state: State, (in [-inf, inf], optional)
                :return: Result of the operator call.
        """

class operator_cheat_sheet(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """List all the operators in a text-block, useful for scripting

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class operator_defaults(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the active operator to its default values

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class operator_pie_enum(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        prop_string: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param data_path: Operator, Operator name (in Python as string) (optional, never None)
        :param prop_string: Property, Property name (as a string) (optional, never None)
        :return: Result of the operator call.
        """

class operator_preset_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        remove_name: bool | None = False,
        remove_active: bool | None = False,
        operator: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add or remove an Operator Preset

        :param execution_context:
        :param undo:
        :param name: Name, Name of the preset, used to make the path name (optional, never None)
        :param remove_name: remove_name, (optional)
        :param remove_active: remove_active, (optional)
        :param operator: Operator, (optional, never None)
        :return: Result of the operator call.
        """

class operator_presets_cleanup(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        operator: str = "",
        properties: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove outdated operator properties from presets that may cause problems

        :param execution_context:
        :param undo:
        :param operator: operator, (optional, never None)
        :param properties: properties, (optional)
        :return: Result of the operator call.
        """

class owner_disable(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        owner_id: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Disable add-on for workspace

        :param execution_context:
        :param undo:
        :param owner_id: UI Tag, (optional, never None)
        :return: Result of the operator call.
        """

class owner_enable(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        owner_id: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Enable add-on for workspace

        :param execution_context:
        :param undo:
        :param owner_id: UI Tag, (optional, never None)
        :return: Result of the operator call.
        """

class path_open(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a path in a file browser

        :param execution_context:
        :param undo:
        :param filepath: filepath, (optional, never None)
        :return: Result of the operator call.
        """

class ply_export(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = True,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        forward_axis: typing.Literal[
            "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
        ]
        | None = "Y",
        up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
        | None = "Z",
        global_scale: float | None = 1.0,
        apply_modifiers: bool | None = True,
        export_selected_objects: bool | None = False,
        collection: str = "",
        export_uv: bool | None = True,
        export_normals: bool | None = False,
        export_colors: typing.Literal["NONE", "SRGB", "LINEAR"] | None = "SRGB",
        export_attributes: bool | None = True,
        export_triangulated_mesh: bool | None = False,
        ascii_format: bool | None = False,
        filter_glob: str = "*.ply",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save the scene to a PLY file

                :param execution_context:
                :param undo:
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
                :param forward_axis: Forward Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param up_axis: Up Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin (in [0.0001, 10000], optional)
                :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes (optional)
                :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects (optional)
                :param collection: Source Collection, Export only objects from this collection (and its children) (optional, never None)
                :param export_uv: Export UVs, (optional)
                :param export_normals: Export Vertex Normals, Export specific vertex normals if available, export calculated normals otherwise (optional)
                :param export_colors: Export Vertex Colors, Export vertex color attributes (optional)

        NONE
        None -- Do not import/export color attributes.

        SRGB
        sRGB -- Vertex colors in the file are in sRGB color space.

        LINEAR
        Linear -- Vertex colors in the file are in linear color space.
                :param export_attributes: Export Vertex Attributes, Export custom vertex attributes (optional)
                :param export_triangulated_mesh: Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4 (optional)
                :param ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise (optional)
                :param filter_glob: Extension Filter, (optional, never None)
                :return: Result of the operator call.
        """

class ply_import(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        directory: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        check_existing: bool | None = False,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        global_scale: float | None = 1.0,
        use_scene_unit: bool | None = False,
        forward_axis: typing.Literal[
            "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
        ]
        | None = "Y",
        up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
        | None = "Z",
        merge_verts: bool | None = False,
        import_colors: typing.Literal["NONE", "SRGB", "LINEAR"] | None = "SRGB",
        import_attributes: bool | None = True,
        filter_glob: str = "*.ply",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Import an PLY file as an object

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param files: Files, (optional)
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
                :param global_scale: Scale, (in [1e-06, 1e+06], optional)
                :param use_scene_unit: Scene Unit, Apply current scenes unit (as defined by unit scale) to imported data (optional)
                :param forward_axis: Forward Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param up_axis: Up Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param merge_verts: Merge Vertices, Merges vertices by distance (optional)
                :param import_colors: Vertex Colors, Import vertex color attributes (optional)

        NONE
        None -- Do not import/export color attributes.

        SRGB
        sRGB -- Vertex colors in the file are in sRGB color space.

        LINEAR
        Linear -- Vertex colors in the file are in linear color space.
                :param import_attributes: Vertex Attributes, Import custom vertex attributes (optional)
                :param filter_glob: Extension Filter, (optional, never None)
                :return: Result of the operator call.
        """

class previews_batch_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        directory: str = "",
        filter_blender: bool | None = True,
        filter_folder: bool | None = True,
        use_scenes: bool | None = True,
        use_collections: bool | None = True,
        use_objects: bool | None = True,
        use_intern_data: bool | None = True,
        use_trusted: bool | None = False,
        use_backups: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear selected .blend files previews

        :param execution_context:
        :param undo:
        :param files: files, (optional)
        :param directory: directory, (optional, never None)
        :param filter_blender: filter_blender, (optional)
        :param filter_folder: filter_folder, (optional)
        :param use_scenes: Scenes, Clear scenes previews (optional)
        :param use_collections: Collections, Clear collections previews (optional)
        :param use_objects: Objects, Clear objects previews (optional)
        :param use_intern_data: Materials & Textures, Clear internal previews (materials, textures, images, etc.) (optional)
        :param use_trusted: Trusted Blend Files, Enable Python evaluation for selected files (optional)
        :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews (optional)
        :return: Result of the operator call.
        """

class previews_batch_generate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        directory: str = "",
        filter_blender: bool | None = True,
        filter_folder: bool | None = True,
        use_scenes: bool | None = True,
        use_collections: bool | None = True,
        use_objects: bool | None = True,
        use_intern_data: bool | None = True,
        use_trusted: bool | None = False,
        use_backups: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Generate selected .blend files previews

        :param execution_context:
        :param undo:
        :param files: Collection of file paths with common directory root (optional)
        :param directory: Root path of all files listed in files collection (optional, never None)
        :param filter_blender: Show Blender files in the File Browser (optional)
        :param filter_folder: Show folders in the File Browser (optional)
        :param use_scenes: Scenes, Generate scenes previews (optional)
        :param use_collections: Collections, Generate collections previews (optional)
        :param use_objects: Objects, Generate objects previews (optional)
        :param use_intern_data: Materials & Textures, Generate internal previews (materials, textures, images, etc.) (optional)
        :param use_trusted: Trusted Blend Files, Enable Python evaluation for selected files (optional)
        :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews (optional)
        :return: Result of the operator call.
        """

class previews_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        id_type: set[
            typing.Literal[
                "ALL",
                "GEOMETRY",
                "SHADING",
                "SCENE",
                "COLLECTION",
                "OBJECT",
                "MATERIAL",
                "LIGHT",
                "WORLD",
                "TEXTURE",
                "IMAGE",
            ]
        ]
        | None = set(),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear data-block previews (only for some types like objects, materials, textures, etc.)

                :param execution_context:
                :param undo:
                :param id_type: Data-Block Type, Which data-block previews to clear (optional)

        ALL
        All Types.

        GEOMETRY
        All Geometry Types -- Clear previews for scenes, collections and objects.

        SHADING
        All Shading Types -- Clear previews for materials, lights, worlds, textures and images.

        SCENE
        Scenes.

        COLLECTION
        Collections.

        OBJECT
        Objects.

        MATERIAL
        Materials.

        LIGHT
        Lights.

        WORLD
        Worlds.

        TEXTURE
        Textures.

        IMAGE
        Images.
                :return: Result of the operator call.
        """

class previews_ensure(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class properties_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add your own property to the data-block

        :param execution_context:
        :param undo:
        :param data_path: Property Edit, Property data_path edit (optional, never None)
        :return: Result of the operator call.
        """

class properties_context_change(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        context: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Jump to a different tab inside the properties editor

        :param execution_context:
        :param undo:
        :param context: Context, (optional, never None)
        :return: Result of the operator call.
        """

class properties_edit(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        property_name: str = "",
        property_type: typing.Literal[
            "FLOAT",
            "FLOAT_ARRAY",
            "INT",
            "INT_ARRAY",
            "BOOL",
            "BOOL_ARRAY",
            "STRING",
            "DATA_BLOCK",
            "PYTHON",
        ]
        | None = "FLOAT",
        is_overridable_library: bool | None = False,
        description: str = "",
        use_soft_limits: bool | None = False,
        array_length: int | None = 3,
        default_int: collections.abc.Sequence[int] | None = (
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ),
        min_int: int | None = -10000,
        max_int: int | None = 10000,
        soft_min_int: int | None = -10000,
        soft_max_int: int | None = 10000,
        step_int: int | None = 1,
        default_bool: collections.abc.Sequence[bool] | None = (
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ),
        default_float: collections.abc.Sequence[float] | None = (
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ),
        min_float: float | None = -10000.0,
        max_float: float | None = -10000.0,
        soft_min_float: float | None = -10000.0,
        soft_max_float: float | None = -10000.0,
        precision: int | None = 3,
        step_float: float | None = 0.1,
        subtype: str | None = "",
        default_string: str = "",
        id_type: typing.Literal[
            "ACTION",
            "ARMATURE",
            "BRUSH",
            "CACHEFILE",
            "CAMERA",
            "COLLECTION",
            "CURVE",
            "CURVES",
            "FONT",
            "GREASEPENCIL",
            "GREASEPENCIL_V3",
            "IMAGE",
            "KEY",
            "LATTICE",
            "LIBRARY",
            "LIGHT",
            "LIGHT_PROBE",
            "LINESTYLE",
            "MASK",
            "MATERIAL",
            "MESH",
            "META",
            "MOVIECLIP",
            "NODETREE",
            "OBJECT",
            "PAINTCURVE",
            "PALETTE",
            "PARTICLE",
            "POINTCLOUD",
            "SCENE",
            "SCREEN",
            "SOUND",
            "SPEAKER",
            "TEXT",
            "TEXTURE",
            "VOLUME",
            "WINDOWMANAGER",
            "WORKSPACE",
            "WORLD",
        ]
        | None = "OBJECT",
        eval_string: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change a custom propertys type, or adjust how it is displayed in the interface

                :param execution_context:
                :param undo:
                :param data_path: Property Edit, Property data_path edit (optional, never None)
                :param property_name: Property Name, Property name edit (optional, never None)
                :param property_type: Type, (optional)

        FLOAT
        Float -- A single floating-point value.

        FLOAT_ARRAY
        Float Array -- An array of floating-point values.

        INT
        Integer -- A single integer.

        INT_ARRAY
        Integer Array -- An array of integers.

        BOOL
        Boolean -- A true or false value.

        BOOL_ARRAY
        Boolean Array -- An array of true or false values.

        STRING
        String -- A string value.

        DATA_BLOCK
        Data-Block -- A data-block value.

        PYTHON
        Python -- Edit a Python value directly, for unsupported property types.
                :param is_overridable_library: Library Overridable, Allow the property to be overridden when the data-block is linked (optional)
                :param description: Description, (optional, never None)
                :param use_soft_limits: Soft Limits, Limits the Property Value slider to a range, values outside the range must be inputted numerically (optional)
                :param array_length: Array Length, (in [1, 32], optional)
                :param default_int: Default Value, (array of 32 items, in [-inf, inf], optional)
                :param min_int: Min, (in [-inf, inf], optional)
                :param max_int: Max, (in [-inf, inf], optional)
                :param soft_min_int: Soft Min, (in [-inf, inf], optional)
                :param soft_max_int: Soft Max, (in [-inf, inf], optional)
                :param step_int: Step, (in [1, inf], optional)
                :param default_bool: Default Value, (array of 32 items, optional)
                :param default_float: Default Value, (array of 32 items, in [-inf, inf], optional)
                :param min_float: Min, (in [-inf, inf], optional)
                :param max_float: Max, (in [-inf, inf], optional)
                :param soft_min_float: Soft Min, (in [-inf, inf], optional)
                :param soft_max_float: Soft Max, (in [-inf, inf], optional)
                :param precision: Precision, (in [0, 8], optional)
                :param step_float: Step, (in [0.001, inf], optional)
                :param subtype: Subtype, (optional)
                :param default_string: Default Value, (optional, never None)
                :param id_type: ID Type, (optional)
                :param eval_string: Value, Python value for unsupported custom property types (optional, never None)
                :return: Result of the operator call.
        """

class properties_edit_value(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        property_name: str = "",
        eval_string: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Edit the value of a custom property

        :param execution_context:
        :param undo:
        :param data_path: Property Edit, Property data_path edit (optional, never None)
        :param property_name: Property Name, Property name edit (optional, never None)
        :param eval_string: Value, Value for custom property types that can only be edited as a Python expression (optional, never None)
        :return: Result of the operator call.
        """

class properties_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path: str = "",
        property_name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Internal use (edit a property data_path)

        :param execution_context:
        :param undo:
        :param data_path: Property Edit, Property data_path edit (optional, never None)
        :param property_name: Property Name, Property name edit (optional, never None)
        :return: Result of the operator call.
        """

class quit_blender(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Quit Blender

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class radial_control(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        data_path_primary: str = "",
        data_path_secondary: str = "",
        use_secondary: str = "",
        rotation_path: str = "",
        color_path: str = "",
        fill_color_path: str = "",
        fill_color_override_path: str = "",
        fill_color_override_test_path: str = "",
        zoom_path: str = "",
        image_id: str = "",
        secondary_tex: bool | None = False,
        release_confirm: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set some size property (e.g. brush size) with mouse wheel

        :param execution_context:
        :param undo:
        :param data_path_primary: Primary Data Path, Primary path of property to be set by the radial control (optional, never None)
        :param data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control (optional, never None)
        :param use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths (optional, never None)
        :param rotation_path: Rotation Path, Path of property used to rotate the texture display (optional, never None)
        :param color_path: Color Path, Path of property used to set the color of the control (optional, never None)
        :param fill_color_path: Fill Color Path, Path of property used to set the fill color of the control (optional, never None)
        :param fill_color_override_path: Fill Color Override Path, (optional, never None)
        :param fill_color_override_test_path: Fill Color Override Test, (optional, never None)
        :param zoom_path: Zoom Path, Path of property used to set the zoom level for the control (optional, never None)
        :param image_id: Image ID, Path of ID that is used to generate an image for the control (optional, never None)
        :param secondary_tex: Secondary Texture, Tweak brush secondary/mask texture (optional)
        :param release_confirm: Confirm On Release, Finish operation on key release (optional)
        :return: Result of the operator call.
        """

class read_factory_settings(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_factory_startup_app_template_only: bool | None = False,
        app_template: str = "Template",
        use_empty: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load factory default startup file and preferences. To make changes permanent, use "Save Startup File" and "Save Preferences"

        :param execution_context:
        :param undo:
        :param use_factory_startup_app_template_only: Factory Startup App-Template Only, (optional)
        :param app_template: (optional, never None)
        :param use_empty: Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, ... (optional)
        :return: Result of the operator call.
        """

class read_factory_userpref(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_factory_startup_app_template_only: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load factory default preferences. To make changes to preferences permanent, use "Save Preferences"

        :param execution_context:
        :param undo:
        :param use_factory_startup_app_template_only: Factory Startup App-Template Only, (optional)
        :return: Result of the operator call.
        """

class read_history(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reloads history and bookmarks

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class read_homefile(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        load_ui: bool | None = True,
        use_splash: bool | None = False,
        use_factory_startup: bool | None = False,
        use_factory_startup_app_template_only: bool | None = False,
        app_template: str = "Template",
        use_empty: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open the default file

        :param execution_context:
        :param undo:
        :param filepath: File Path, Path to an alternative start-up file (optional, never None)
        :param load_ui: Load UI, Load user interface setup from the .blend file (optional)
        :param use_splash: Splash, (optional)
        :param use_factory_startup: Factory Startup, Load the default (factory startup) blend file. This is independent of the normal start-up file that the user can save (optional)
        :param use_factory_startup_app_template_only: Factory Startup App-Template Only, (optional)
        :param app_template: (optional, never None)
        :param use_empty: Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, ... (optional)
        :return: Result of the operator call.
        """

class read_userpref(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Load last saved preferences

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class recover_auto_save(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        hide_props_region: bool | None = True,
        check_existing: bool | None = False,
        filter_blender: bool | None = True,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filter_folder: bool | None = False,
        filter_blenlib: bool | None = False,
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "LIST_VERTICAL",
        sort_method: str | None = "",
        use_scripts: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open an automatically saved file to recover it

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
                :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences (optional)
                :return: Result of the operator call.
        """

class recover_last_session(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_scripts: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open the last closed file ("quit.blend")

        :param execution_context:
        :param undo:
        :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences (optional)
        :return: Result of the operator call.
        """

class redraw_timer(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "DRAW",
            "DRAW_SWAP",
            "DRAW_WIN",
            "DRAW_WIN_SWAP",
            "ANIM_STEP",
            "ANIM_PLAY",
            "UNDO",
        ]
        | None = "DRAW",
        iterations: int | None = 10,
        time_limit: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Simple redraw timer to test the speed of updating the interface

                :param execution_context:
                :param undo:
                :param type: Type, (optional)

        DRAW
        Draw Region -- Draw region.

        DRAW_SWAP
        Draw Region & Swap -- Draw region and swap.

        DRAW_WIN
        Draw Window -- Draw window.

        DRAW_WIN_SWAP
        Draw Window & Swap -- Draw window and swap.

        ANIM_STEP
        Animation Step -- Animation steps.

        ANIM_PLAY
        Animation Play -- Animation playback.

        UNDO
        Undo/Redo -- Undo and redo.
                :param iterations: Iterations, Number of times to redraw (in [1, inf], optional)
                :param time_limit: Time Limit, Seconds to run the test for (override iterations) (in [0, inf], optional)
                :return: Result of the operator call.
        """

class revert_mainfile(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_scripts: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reload the saved file

        :param execution_context:
        :param undo:
        :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences (optional)
        :return: Result of the operator call.
        """

class save_as_mainfile(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        hide_props_region: bool | None = True,
        check_existing: bool | None = True,
        filter_blender: bool | None = True,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        compress: bool | None = False,
        relative_remap: bool | None = True,
        copy: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save the current file in the desired location

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
                :param compress: Compress, Write compressed .blend file (optional)
                :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory (optional)
                :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active (optional)
                :return: Result of the operator call.
        """

class save_homefile(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make the current file the default startup file

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class save_mainfile(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        hide_props_region: bool | None = True,
        check_existing: bool | None = True,
        filter_blender: bool | None = True,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        compress: bool | None = False,
        relative_remap: bool | None = False,
        exit: bool | None = False,
        incremental: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save the current Blender file

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
                :param compress: Compress, Write compressed .blend file (optional)
                :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory (optional)
                :param exit: Exit, Exit Blender after saving (optional)
                :param incremental: Incremental, Save the current Blender file with a numerically incremented name that does not overwrite any existing files (optional)
                :return: Result of the operator call.
        """

class save_userpref(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make the current preferences default

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class search_menu(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pop-up a search over all menus in the current context

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class search_operator(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pop-up a search over all available operators in current context

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class search_single_menu(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        menu_idname: str = "",
        initial_query: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pop-up a search for a menu in current context

        :param execution_context:
        :param undo:
        :param menu_idname: Menu Name, Menu to search in (optional, never None)
        :param initial_query: Initial Query, Query to insert into the search box (optional, never None)
        :return: Result of the operator call.
        """

class set_stereo_3d(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        display_mode: typing.Literal[bpy.stub_internal.rna_enums.Stereo3DDisplayItems]
        | None = "ANAGLYPH",
        anaglyph_type: typing.Literal[
            bpy.stub_internal.rna_enums.Stereo3DAnaglyphTypeItems
        ]
        | None = "RED_CYAN",
        interlace_type: typing.Literal[
            bpy.stub_internal.rna_enums.Stereo3DInterlaceTypeItems
        ]
        | None = "ROW_INTERLEAVED",
        use_interlace_swap: bool | None = False,
        use_sidebyside_crosseyed: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle 3D stereo support for current window (or change the display mode)

        :param execution_context:
        :param undo:
        :param display_mode: Display Mode, (optional)
        :param anaglyph_type: Anaglyph Type, (optional)
        :param interlace_type: Interlace Type, (optional)
        :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels (optional)
        :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice versa (optional)
        :return: Result of the operator call.
        """

class set_working_color_space(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        convert_colors: bool | None = True,
        working_space: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the working color space of all colors in this blend file

        :param execution_context:
        :param undo:
        :param convert_colors: Convert Colors in All Data-blocks, Change colors in all data-blocks to the new working space (optional)
        :param working_space: Working Space, Color space to set (optional)
        :return: Result of the operator call.
        """

class splash(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open the splash screen with release info

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class splash_about(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a window with information about Blender

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class stl_export(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = True,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        ascii_format: bool | None = False,
        use_batch: bool | None = False,
        export_selected_objects: bool | None = False,
        collection: str = "",
        global_scale: float | None = 1.0,
        use_scene_unit: bool | None = False,
        forward_axis: typing.Literal[
            "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
        ]
        | None = "Y",
        up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
        | None = "Z",
        apply_modifiers: bool | None = True,
        filter_glob: str = "*.stl",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Save the scene to an STL file

                :param execution_context:
                :param undo:
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
                :param ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise (optional)
                :param use_batch: Batch Export, Export each object to a separate file (optional)
                :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects (optional)
                :param collection: Source Collection, Export only objects from this collection (and its children) (optional, never None)
                :param global_scale: Scale, (in [1e-06, 1e+06], optional)
                :param use_scene_unit: Scene Unit, Apply current scenes unit (as defined by unit scale) to exported data (optional)
                :param forward_axis: Forward Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param up_axis: Up Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes (optional)
                :param filter_glob: Extension Filter, (optional, never None)
                :return: Result of the operator call.
        """

class stl_import(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        directory: str = "",
        files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
        | None = None,
        check_existing: bool | None = False,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
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
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        global_scale: float | None = 1.0,
        use_scene_unit: bool | None = False,
        use_facet_normal: bool | None = False,
        forward_axis: typing.Literal[
            "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
        ]
        | None = "Y",
        up_axis: typing.Literal["X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"]
        | None = "Z",
        use_mesh_validate: bool | None = True,
        filter_glob: str = "*.stl",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Import an STL file as an object

                :param execution_context:
                :param undo:
                :param filepath: File Path, Path to file (optional, never None)
                :param directory: Directory, Directory of the file (optional, never None)
                :param files: Files, (optional)
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
                :param global_scale: Scale, (in [1e-06, 1e+06], optional)
                :param use_scene_unit: Scene Unit, Apply current scenes unit (as defined by unit scale) to imported data (optional)
                :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading) (optional)
                :param forward_axis: Forward Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param up_axis: Up Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param use_mesh_validate: Validate Mesh, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing) (optional)
                :param filter_glob: Extension Filter, (optional, never None)
                :return: Result of the operator call.
        """

class sysinfo(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Generate system information, saved into a text file

        :param execution_context:
        :param undo:
        :param filepath: filepath, (optional, never None)
        :return: Result of the operator call.
        """

class tool_set_by_brush_type(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        brush_type: str = "",
        space_type: typing.Literal[
            "EMPTY",
            "VIEW_3D",
            "IMAGE_EDITOR",
            "NODE_EDITOR",
            "SEQUENCE_EDITOR",
            "CLIP_EDITOR",
            "DOPESHEET_EDITOR",
            "GRAPH_EDITOR",
            "NLA_EDITOR",
            "TEXT_EDITOR",
            "CONSOLE",
            "INFO",
            "TOPBAR",
            "STATUSBAR",
            "OUTLINER",
            "PROPERTIES",
            "FILE_BROWSER",
            "SPREADSHEET",
            "PREFERENCES",
        ]
        | None = "EMPTY",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Look up the most appropriate tool for the given brush type and activate that

        :param execution_context:
        :param undo:
        :param brush_type: Brush Type, Brush type identifier for which the most appropriate tool will be looked up (optional, never None)
        :param space_type: Type, (optional)
        :return: Result of the operator call.
        """

class tool_set_by_id(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        cycle: bool | None = False,
        as_fallback: bool | None = False,
        space_type: typing.Literal[
            "EMPTY",
            "VIEW_3D",
            "IMAGE_EDITOR",
            "NODE_EDITOR",
            "SEQUENCE_EDITOR",
            "CLIP_EDITOR",
            "DOPESHEET_EDITOR",
            "GRAPH_EDITOR",
            "NLA_EDITOR",
            "TEXT_EDITOR",
            "CONSOLE",
            "INFO",
            "TOPBAR",
            "STATUSBAR",
            "OUTLINER",
            "PROPERTIES",
            "FILE_BROWSER",
            "SPREADSHEET",
            "PREFERENCES",
        ]
        | None = "EMPTY",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the tool by name (for key-maps)

        :param execution_context:
        :param undo:
        :param name: Identifier, Identifier of the tool (optional, never None)
        :param cycle: Cycle, Cycle through tools in this group (optional)
        :param as_fallback: Set Fallback, Set the fallback tool instead of the primary tool (optional)
        :param space_type: Type, (optional)
        :return: Result of the operator call.
        """

class tool_set_by_index(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
        cycle: bool | None = False,
        expand: bool | None = True,
        as_fallback: bool | None = False,
        space_type: typing.Literal[
            "EMPTY",
            "VIEW_3D",
            "IMAGE_EDITOR",
            "NODE_EDITOR",
            "SEQUENCE_EDITOR",
            "CLIP_EDITOR",
            "DOPESHEET_EDITOR",
            "GRAPH_EDITOR",
            "NLA_EDITOR",
            "TEXT_EDITOR",
            "CONSOLE",
            "INFO",
            "TOPBAR",
            "STATUSBAR",
            "OUTLINER",
            "PROPERTIES",
            "FILE_BROWSER",
            "SPREADSHEET",
            "PREFERENCES",
        ]
        | None = "EMPTY",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the tool by index (for key-maps)

        :param execution_context:
        :param undo:
        :param index: Index in Toolbar, (in [-inf, inf], optional)
        :param cycle: Cycle, Cycle through tools in this group (optional)
        :param expand: expand, Include tool subgroups (optional)
        :param as_fallback: Set Fallback, Set the fallback tool instead of the primary (optional)
        :param space_type: Type, (optional)
        :return: Result of the operator call.
        """

class toolbar(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class toolbar_fallback_pie(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class toolbar_prompt(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Leader key like functionality for accessing tools

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class url_open(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        url: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a website in the web browser

        :param execution_context:
        :param undo:
        :param url: URL, URL to open (optional, never None)
        :return: Result of the operator call.
        """

class url_open_preset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a preset website in the web browser

        :param execution_context:
        :param undo:
        :param type: Site, (optional)
        :return: Result of the operator call.
        """

class usd_export(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = True,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
        filter_python: bool | None = False,
        filter_font: bool | None = False,
        filter_sound: bool | None = False,
        filter_text: bool | None = False,
        filter_archive: bool | None = False,
        filter_btx: bool | None = False,
        filter_alembic: bool | None = False,
        filter_usd: bool | None = True,
        filter_obj: bool | None = False,
        filter_volume: bool | None = False,
        filter_folder: bool | None = True,
        filter_blenlib: bool | None = False,
        filemode: int | None = 8,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        filter_glob: str = "*.usd",
        selected_objects_only: bool | None = False,
        collection: str = "",
        export_animation: bool | None = False,
        export_hair: bool | None = False,
        export_uvmaps: bool | None = True,
        rename_uvmaps: bool | None = True,
        export_mesh_colors: bool | None = True,
        export_normals: bool | None = True,
        export_materials: bool | None = True,
        export_subdivision: typing.Literal["IGNORE", "TESSELLATE", "BEST_MATCH"]
        | None = "BEST_MATCH",
        export_armatures: bool | None = True,
        only_deform_bones: bool | None = False,
        export_shapekeys: bool | None = True,
        use_instancing: bool | None = False,
        evaluation_mode: typing.Literal["RENDER", "VIEWPORT"] | None = "RENDER",
        generate_preview_surface: bool | None = True,
        generate_materialx_network: bool | None = False,
        convert_orientation: bool | None = False,
        export_global_forward_selection: typing.Literal[
            "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
        ]
        | None = "NEGATIVE_Z",
        export_global_up_selection: typing.Literal[
            "X", "Y", "Z", "NEGATIVE_X", "NEGATIVE_Y", "NEGATIVE_Z"
        ]
        | None = "Y",
        export_textures_mode: typing.Literal["KEEP", "PRESERVE", "NEW"] | None = "NEW",
        overwrite_textures: bool | None = False,
        relative_paths: bool | None = True,
        xform_op_mode: typing.Literal["TRS", "TOS", "MAT"] | None = "TRS",
        root_prim_path: str = "/root",
        export_custom_properties: bool | None = True,
        custom_properties_namespace: str = "userProperties",
        accessibility_label: str = "",
        accessibility_description: str = "",
        author_blender_name: bool | None = True,
        convert_world_material: bool | None = True,
        allow_unicode: bool | None = True,
        export_meshes: bool | None = True,
        export_lights: bool | None = True,
        export_cameras: bool | None = True,
        export_curves: bool | None = True,
        export_points: bool | None = True,
        export_volumes: bool | None = True,
        triangulate_meshes: bool | None = False,
        quad_method: typing.Literal[
            bpy.stub_internal.rna_enums.ModifierTriangulateQuadMethodItems
        ]
        | None = "SHORTEST_DIAGONAL",
        ngon_method: typing.Literal[
            bpy.stub_internal.rna_enums.ModifierTriangulateNgonMethodItems
        ]
        | None = "BEAUTY",
        usdz_downscale_size: typing.Literal[
            "KEEP", "256", "512", "1024", "2048", "4096", "CUSTOM"
        ]
        | None = "KEEP",
        usdz_downscale_custom_size: int | None = 128,
        merge_parent_xform: bool | None = False,
        convert_scene_units: typing.Literal[
            "METERS",
            "KILOMETERS",
            "CENTIMETERS",
            "MILLIMETERS",
            "INCHES",
            "FEET",
            "YARDS",
            "CUSTOM",
        ]
        | None = "METERS",
        meters_per_unit: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Export current scene in a USD archive

                :param execution_context:
                :param undo:
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
                :param filter_glob: (optional, never None)
                :param selected_objects_only: Selection Only, Only export selected objects. Unselected parents of selected objects are exported as empty transform (optional)
                :param collection: Collection, (optional, never None)
                :param export_animation: Animation, Export all frames in the render frame range, rather than only the current frame (optional)
                :param export_hair: Hair, Export hair particle systems as USD curves (optional)
                :param export_uvmaps: UV Maps, Include all mesh UV maps in the export (optional)
                :param rename_uvmaps: Rename UV Maps, Rename active render UV map to "st" to match USD conventions (optional)
                :param export_mesh_colors: Color Attributes, Include mesh color attributes in the export (optional)
                :param export_normals: Normals, Include normals of exported meshes in the export (optional)
                :param export_materials: Materials, Export viewport settings of materials as USD preview materials, and export material assignments as geometry subsets (optional)
                :param export_subdivision: Subdivision, Choose how subdivision modifiers will be mapped to the USD subdivision scheme during export (optional)

        IGNORE
        Ignore -- Scheme = None. Export base mesh without subdivision.

        TESSELLATE
        Tessellate -- Scheme = None. Export subdivided mesh.

        BEST_MATCH
        Best Match -- Scheme = Catmull-Clark, when possible. Reverts to exporting the subdivided mesh for the Simple subdivision type.
                :param export_armatures: Armatures, Export armatures and meshes with armature modifiers as USD skeletons and skinned meshes (optional)
                :param only_deform_bones: Only Deform Bones, Only export deform bones and their parents (optional)
                :param export_shapekeys: Shape Keys, Export shape keys as USD blend shapes (optional)
                :param use_instancing: Instancing, Export instanced objects as references in USD rather than real objects (optional)
                :param evaluation_mode: Use Settings for, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering (optional)

        RENDER
        Render -- Use Render settings for object visibility, modifier settings, etc.

        VIEWPORT
        Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
                :param generate_preview_surface: USD Preview Surface Network, Generate an approximate USD Preview Surface shader representation of a Principled BSDF node network (optional)
                :param generate_materialx_network: MaterialX Network, Generate a MaterialX network representation of the materials (optional)
                :param convert_orientation: Convert Orientation, Convert orientation axis to a different convention to match other applications (optional)
                :param export_global_forward_selection: Forward Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param export_global_up_selection: Up Axis, (optional)

        X
        X -- Positive X axis.

        Y
        Y -- Positive Y axis.

        Z
        Z -- Positive Z axis.

        NEGATIVE_X
        -X -- Negative X axis.

        NEGATIVE_Y
        -Y -- Negative Y axis.

        NEGATIVE_Z
        -Z -- Negative Z axis.
                :param export_textures_mode: Export Textures, Texture export method (optional)

        KEEP
        Keep -- Use original location of textures.

        PRESERVE
        Preserve -- Preserve file paths of textures from already imported USD files.
        Export remaining textures to a textures folder next to the USD file.

        NEW
        New Path -- Export textures to a textures folder next to the USD file.
                :param overwrite_textures: Overwrite Textures, Overwrite existing files when exporting textures (optional)
                :param relative_paths: Relative Paths, Use relative paths to reference external files (i.e. textures, volumes) in USD, otherwise use absolute paths (optional)
                :param xform_op_mode: Xform Ops, The type of transform operators to write (optional)

        TRS
        Translate, Rotate, Scale -- Export with translate, rotate, and scale Xform operators.

        TOS
        Translate, Orient, Scale -- Export with translate, orient quaternion, and scale Xform operators.

        MAT
        Matrix -- Export matrix operator.
                :param root_prim_path: Root Prim, If set, add a transform primitive with the given path to the stage as the parent of all exported data (optional, never None)
                :param export_custom_properties: Custom Properties, Export custom properties as USD attributes (optional)
                :param custom_properties_namespace: Namespace, If set, add the given namespace as a prefix to exported custom property names. This only applies to property names that do not already have a prefix (e.g., it would apply to name bar but not foo:bar) and does not apply to blender object and data names which are always exported in the userProperties:blender namespace (optional, never None)
                :param accessibility_label: Label, Set the accessibility label for the exported stages default prim (optional, never None)
                :param accessibility_description: Description, Set the accessibility description for the exported stages default prim (optional, never None)
                :param author_blender_name: Blender Names, Author USD custom attributes containing the original Blender object and object data names (optional)
                :param convert_world_material: World Dome Light, Convert the world material to a USD dome light. Currently works for simple materials, consisting of an environment texture connected to a background shader, with an optional vector multiply of the texture color (optional)
                :param allow_unicode: Allow Unicode, Preserve UTF-8 encoded characters when writing USD prim and property names (requires software utilizing USD 24.03 or greater when opening the resulting files) (optional)
                :param export_meshes: Meshes, Export all meshes (optional)
                :param export_lights: Lights, Export all lights (optional)
                :param export_cameras: Cameras, Export all cameras (optional)
                :param export_curves: Curves, Export all curves (optional)
                :param export_points: Point Clouds, Export all point clouds (optional)
                :param export_volumes: Volumes, Export all volumes (optional)
                :param triangulate_meshes: Triangulate Meshes, Triangulate meshes during export (optional)
                :param quad_method: Quad Method, Method for splitting the quads into triangles (optional)
                :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles (optional)
                :param usdz_downscale_size: USDZ Texture Downsampling, Choose a maximum size for all exported textures (optional)

        KEEP
        Keep -- Keep all current texture sizes.

        256
        256 -- Resize to a maximum of 256 pixels.

        512
        512 -- Resize to a maximum of 512 pixels.

        1024
        1024 -- Resize to a maximum of 1024 pixels.

        2048
        2048 -- Resize to a maximum of 2048 pixels.

        4096
        4096 -- Resize to a maximum of 4096 pixels.

        CUSTOM
        Custom -- Specify a custom size.
                :param usdz_downscale_custom_size: USDZ Custom Downscale Size, Custom size for downscaling exported textures (in [64, 16384], optional)
                :param merge_parent_xform: Merge parent Xform, Merge USD primitives with their Xform parent if possible. USD does not allow nested UsdGeomGprims, intermediary Xform prims will be defined to keep the USD file valid when encountering object hierarchies. (optional)
                :param convert_scene_units: Units, Set the USD Stage meters per unit to the chosen measurement, or a custom value (optional)

        METERS
        Meters -- Scene meters per unit to 1.0.

        KILOMETERS
        Kilometers -- Scene meters per unit to 1000.0.

        CENTIMETERS
        Centimeters -- Scene meters per unit to 0.01.

        MILLIMETERS
        Millimeters -- Scene meters per unit to 0.001.

        INCHES
        Inches -- Scene meters per unit to 0.0254.

        FEET
        Feet -- Scene meters per unit to 0.3048.

        YARDS
        Yards -- Scene meters per unit to 0.9144.

        CUSTOM
        Custom -- Specify a custom scene meters per unit value.
                :param meters_per_unit: Meters Per Unit, Custom value for meters per unit in the USD Stage (in [0.0001, 1000], optional)
                :return: Result of the operator call.
        """

class usd_import(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
        check_existing: bool | None = False,
        filter_blender: bool | None = False,
        filter_backup: bool | None = False,
        filter_image: bool | None = False,
        filter_movie: bool | None = False,
        filter_python: bool | None = False,
        filter_font: bool | None = False,
        filter_sound: bool | None = False,
        filter_text: bool | None = False,
        filter_archive: bool | None = False,
        filter_btx: bool | None = False,
        filter_alembic: bool | None = False,
        filter_usd: bool | None = True,
        filter_obj: bool | None = False,
        filter_volume: bool | None = False,
        filter_folder: bool | None = True,
        filter_blenlib: bool | None = False,
        filemode: int | None = 8,
        relative_path: bool | None = True,
        display_type: typing.Literal[
            "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
        ]
        | None = "DEFAULT",
        sort_method: str | None = "",
        filter_glob: str = "*.usd",
        scale: float | None = 1.0,
        set_frame_range: bool | None = True,
        import_cameras: bool | None = True,
        import_curves: bool | None = True,
        import_lights: bool | None = True,
        import_materials: bool | None = True,
        import_meshes: bool | None = True,
        import_volumes: bool | None = True,
        import_shapes: bool | None = True,
        import_skeletons: bool | None = True,
        import_blendshapes: bool | None = True,
        import_points: bool | None = True,
        import_subdivision: bool | None = False,
        support_scene_instancing: bool | None = True,
        import_visible_only: bool | None = True,
        create_collection: bool | None = False,
        read_mesh_uvs: bool | None = True,
        read_mesh_colors: bool | None = True,
        read_mesh_attributes: bool | None = True,
        prim_path_mask: str = "",
        import_guide: bool | None = False,
        import_proxy: bool | None = False,
        import_render: bool | None = True,
        import_all_materials: bool | None = False,
        import_usd_preview: bool | None = True,
        set_material_blend: bool | None = True,
        light_intensity_scale: float | None = 1.0,
        mtl_purpose: typing.Literal["MTL_ALL_PURPOSE", "MTL_PREVIEW", "MTL_FULL"]
        | None = "MTL_FULL",
        mtl_name_collision_mode: typing.Literal["MAKE_UNIQUE", "REFERENCE_EXISTING"]
        | None = "MAKE_UNIQUE",
        import_textures_mode: typing.Literal[
            "IMPORT_NONE", "IMPORT_PACK", "IMPORT_COPY"
        ]
        | None = "IMPORT_PACK",
        import_textures_dir: str = "//textures/",
        tex_name_collision_mode: typing.Literal["USE_EXISTING", "OVERWRITE"]
        | None = "USE_EXISTING",
        property_import_mode: typing.Literal["NONE", "USER", "ALL"] | None = "ALL",
        validate_meshes: bool | None = False,
        create_world_material: bool | None = True,
        import_defined_only: bool | None = True,
        merge_parent_xform: bool | None = True,
        apply_unit_conversion_scale: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Import USD stage into current scene

                :param execution_context:
                :param undo:
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
                :param filter_glob: (optional, never None)
                :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the worlds origin (in [0.0001, 1000], optional)
                :param set_frame_range: Set Frame Range, Update the scenes start and end frame to match those of the USD archive (optional)
                :param import_cameras: Cameras, (optional)
                :param import_curves: Curves, (optional)
                :param import_lights: Lights, (optional)
                :param import_materials: Materials, (optional)
                :param import_meshes: Meshes, (optional)
                :param import_volumes: Volumes, (optional)
                :param import_shapes: USD Shapes, (optional)
                :param import_skeletons: Armatures, (optional)
                :param import_blendshapes: Shape Keys, (optional)
                :param import_points: Point Clouds, (optional)
                :param import_subdivision: Import Subdivision Scheme, Create subdivision surface modifiers based on the USD SubdivisionScheme attribute (optional)
                :param support_scene_instancing: Scene Instancing, Import USD scene graph instances as collection instances (optional)
                :param import_visible_only: Visible Primitives Only, Do not import invisible USD primitives. Only applies to primitives with a non-animated visibility attribute. Primitives with animated visibility will always be imported (optional)
                :param create_collection: Create Collection, Add all imported objects to a new collection (optional)
                :param read_mesh_uvs: UV Coordinates, Read mesh UV coordinates (optional)
                :param read_mesh_colors: Color Attributes, Read mesh color attributes (optional)
                :param read_mesh_attributes: Mesh Attributes, Read USD Primvars as mesh attributes (optional)
                :param prim_path_mask: Path Mask, Import only the primitive at the given path and its descendants. Multiple paths may be specified in a list delimited by commas or semicolons (optional, never None)
                :param import_guide: Guide, Import guide geometry (optional)
                :param import_proxy: Proxy, Import proxy geometry (optional)
                :param import_render: Render, Import final render geometry (optional)
                :param import_all_materials: Import All Materials, Also import materials that are not used by any geometry. Note that when this option is false, materials referenced by geometry will still be imported (optional)
                :param import_usd_preview: Import USD Preview, Convert UsdPreviewSurface shaders to Principled BSDF shader networks (optional)
                :param set_material_blend: Set Material Blend, If the Import USD Preview option is enabled, the material blend method will automatically be set based on the shaders opacity and opacityThreshold inputs (optional)
                :param light_intensity_scale: Light Intensity Scale, Scale for the intensity of imported lights (in [0.0001, 10000], optional)
                :param mtl_purpose: Material Purpose, Attempt to import materials with the given purpose. If no material with this purpose is bound to the primitive, fall back on loading any other bound material (optional)

        MTL_ALL_PURPOSE
        All Purpose -- Attempt to import allPurpose materials..

        MTL_PREVIEW
        Preview -- Attempt to import preview materials. Load allPurpose materials as a fallback.

        MTL_FULL
        Full -- Attempt to import full materials. Load allPurpose or preview materials, in that order, as a fallback.
                :param mtl_name_collision_mode: Material Name Collision, Behavior when the name of an imported material conflicts with an existing material (optional)

        MAKE_UNIQUE
        Make Unique -- Import each USD material as a unique Blender material.

        REFERENCE_EXISTING
        Reference Existing -- If a material with the same name already exists, reference that instead of importing.
                :param import_textures_mode: Import Textures, Behavior when importing textures from a USDZ archive (optional)

        IMPORT_NONE
        None -- Dont import textures.

        IMPORT_PACK
        Packed -- Import textures as packed data.

        IMPORT_COPY
        Copy -- Copy files to textures directory.
                :param import_textures_dir: Textures Directory, Path to the directory where imported textures will be copied (optional, never None)
                :param tex_name_collision_mode: File Name Collision, Behavior when the name of an imported texture file conflicts with an existing file (optional)

        USE_EXISTING
        Use Existing -- If a file with the same name already exists, use that instead of copying.

        OVERWRITE
        Overwrite -- Overwrite existing files.
                :param property_import_mode: Custom Properties, Behavior when importing USD attributes as Blender custom properties (optional)

        NONE
        None -- Do not import USD custom attributes.

        USER
        User -- Import USD attributes in the userProperties namespace as Blender custom properties. The namespace will be stripped from the property names.

        ALL
        All Custom -- Import all USD custom attributes as Blender custom properties. Namespaces will be retained in the property names.
                :param validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing) (optional)
                :param create_world_material: World Dome Light, Convert the first discovered USD dome light to a world background shader (optional)
                :param import_defined_only: Defined Primitives Only, Import only defined USD primitives. When disabled this allows importing USD primitives which are not defined, such as those with an override specifier (optional)
                :param merge_parent_xform: Merge parent Xform, Allow USD primitives to merge with their Xform parent if they are the only child in the hierarchy (optional)
                :param apply_unit_conversion_scale: Apply Unit Conversion Scale, Scale the scene objects by the USD stages meters per unit value. This scaling is applied in addition to the value specified in the Scale option (optional)
                :return: Result of the operator call.
        """

class window_close(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Close the current window

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class window_fullscreen_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle the current window full-screen

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class window_new(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new window

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class window_new_main(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new main window with its own workspace and scene selection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class xr_navigation_fly(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal[
            "FORWARD",
            "BACK",
            "LEFT",
            "RIGHT",
            "UP",
            "DOWN",
            "TURNLEFT",
            "TURNRIGHT",
            "VIEWER_FORWARD",
            "VIEWER_BACK",
            "VIEWER_LEFT",
            "VIEWER_RIGHT",
            "CONTROLLER_FORWARD",
        ]
        | None = "VIEWER_FORWARD",
        snap_turn_threshold: float | None = 0.95,
        lock_location_z: bool | None = False,
        lock_direction: bool | None = False,
        speed_frame_based: bool | None = False,
        turn_speed_factor: float | None = 0.333333,
        fly_speed_factor: float | None = 0.333333,
        speed_interpolation0: collections.abc.Sequence[float]
        | mathutils.Vector
        | None = (0.0, 0.0),
        speed_interpolation1: collections.abc.Sequence[float]
        | mathutils.Vector
        | None = (1.0, 1.0),
        alt_mode: typing.Literal[
            "FORWARD",
            "BACK",
            "LEFT",
            "RIGHT",
            "UP",
            "DOWN",
            "TURNLEFT",
            "TURNRIGHT",
            "VIEWER_FORWARD",
            "VIEWER_BACK",
            "VIEWER_LEFT",
            "VIEWER_RIGHT",
            "CONTROLLER_FORWARD",
        ]
        | None = "VIEWER_FORWARD",
        alt_lock_location_z: bool | None = False,
        alt_lock_direction: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move/turn relative to the VR viewer or controller

                :param execution_context:
                :param undo:
                :param mode: Mode, Fly mode (optional)

        FORWARD
        Forward -- Move along navigation forward axis.

        BACK
        Back -- Move along navigation back axis.

        LEFT
        Left -- Move along navigation left axis.

        RIGHT
        Right -- Move along navigation right axis.

        UP
        Up -- Move along navigation up axis.

        DOWN
        Down -- Move along navigation down axis.

        TURNLEFT
        Turn Left -- Turn counter-clockwise around navigation up axis.

        TURNRIGHT
        Turn Right -- Turn clockwise around navigation up axis.

        VIEWER_FORWARD
        Viewer Forward -- Move along viewers forward axis.

        VIEWER_BACK
        Viewer Back -- Move along viewers back axis.

        VIEWER_LEFT
        Viewer Left -- Move along viewers left axis.

        VIEWER_RIGHT
        Viewer Right -- Move along viewers right axis.

        CONTROLLER_FORWARD
        Controller Forward -- Move along controllers forward axis.
                :param snap_turn_threshold: Snap Turn Threshold, Input state threshold when using snap turn (in [0, 1], optional)
                :param lock_location_z: Lock Elevation, Prevent changes to viewer elevation (optional)
                :param lock_direction: Lock Direction, Limit movement to viewers initial direction (optional)
                :param speed_frame_based: Frame Based Speed, Apply fixed movement deltas every update (optional)
                :param turn_speed_factor: Turn Speed Factor, Ratio between the min and max turn speed (in [0, 1], optional)
                :param fly_speed_factor: Fly Speed Factor, Ratio between the min and max fly speed (in [0, 1], optional)
                :param speed_interpolation0: Speed Interpolation 0, First cubic spline control point between min/max speeds (array of 2 items, in [0, 1], optional)
                :param speed_interpolation1: Speed Interpolation 1, Second cubic spline control point between min/max speeds (array of 2 items, in [0, 1], optional)
                :param alt_mode: Mode (Alt), Fly mode when hands are swapped (optional)

        FORWARD
        Forward -- Move along navigation forward axis.

        BACK
        Back -- Move along navigation back axis.

        LEFT
        Left -- Move along navigation left axis.

        RIGHT
        Right -- Move along navigation right axis.

        UP
        Up -- Move along navigation up axis.

        DOWN
        Down -- Move along navigation down axis.

        TURNLEFT
        Turn Left -- Turn counter-clockwise around navigation up axis.

        TURNRIGHT
        Turn Right -- Turn clockwise around navigation up axis.

        VIEWER_FORWARD
        Viewer Forward -- Move along viewers forward axis.

        VIEWER_BACK
        Viewer Back -- Move along viewers back axis.

        VIEWER_LEFT
        Viewer Left -- Move along viewers left axis.

        VIEWER_RIGHT
        Viewer Right -- Move along viewers right axis.

        CONTROLLER_FORWARD
        Controller Forward -- Move along controllers forward axis.
                :param alt_lock_location_z: Lock Elevation (Alt), When hands are swapped, prevent changes to viewer elevation (optional)
                :param alt_lock_direction: Lock Direction (Alt), When hands are swapped, limit movement to viewers initial direction (optional)
                :return: Result of the operator call.
        """

class xr_navigation_grab(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        lock_location: bool | None = False,
        lock_location_z: bool | None = False,
        lock_rotation: bool | None = False,
        lock_rotation_z: bool | None = False,
        lock_scale: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Navigate the VR scene by grabbing with controllers

        :param execution_context:
        :param undo:
        :param lock_location: Lock Location, Prevent changes to viewer location (optional)
        :param lock_location_z: Lock Elevation, Prevent changes to viewer elevation (optional)
        :param lock_rotation: Lock Rotation, Prevent changes to viewer rotation (optional)
        :param lock_rotation_z: Lock Up Orientation, Prevent changes to viewer up orientation (optional)
        :param lock_scale: Lock Scale, Prevent changes to viewer scale (optional)
        :return: Result of the operator call.
        """

class xr_navigation_reset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: bool | None = True,
        rotation: bool | None = True,
        scale: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset VR navigation deltas relative to session base pose

        :param execution_context:
        :param undo:
        :param location: Location, Reset location deltas (optional)
        :param rotation: Rotation, Reset rotation deltas (optional)
        :param scale: Scale, Reset scale deltas (optional)
        :return: Result of the operator call.
        """

class xr_navigation_swap_hands(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Swap VR navigation controls between left / right controllers

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class xr_navigation_teleport(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        selectable_only: bool | None = True,
        force: float | None = 8.5,
        range: float | None = 0.15,
        ray_line_width: float | None = 6.0,
        destination_indicator_width: float | None = 0.18,
        hit_color: collections.abc.Sequence[float] | None = (0.4, 0.6, 0.9, 1.0),
        miss_color: collections.abc.Sequence[float] | None = (1.0, 0.35, 0.35, 1.0),
        fallback_color: collections.abc.Sequence[float] | None = (0.5, 0.45, 0.8, 1.0),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set VR viewer location to controller raycast hit location

        :param execution_context:
        :param undo:
        :param selectable_only: Selectable Only, Only allow selectable objects to influence raycast result (optional)
        :param force: Force, Velocity force controlling the teleportation arc parabola in m/s (in [0, inf], optional)
        :param range: Range, Time step range controlling the teleportation arc parabola (in [0, inf], optional)
        :param ray_line_width: Ray Line Width, Visual width of the teleportation ray line (in [0, inf], optional)
        :param destination_indicator_width: Destination Indicator Width, Visual width of the hit destination indicator (in [0, inf], optional)
        :param hit_color: Hit Color, Color of raycast when it succeeds (array of 4 items, in [0, 1], optional)
        :param miss_color: Miss Color, Color of raycast when it misses (array of 4 items, in [0, 1], optional)
        :param fallback_color: Fallback Color, Color of raycast when a fallback case succeeds (array of 4 items, in [0, 1], optional)
        :return: Result of the operator call.
        """

class xr_session_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Open a view for use with virtual reality headsets, or close it if already opened

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
