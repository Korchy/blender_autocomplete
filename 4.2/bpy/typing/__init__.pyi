import typing
import collections.abc
import typing_extensions

type AssetLibraryTypeItems = typing.Literal[
    "ALL",  # All.Show assets from all of the listed asset libraries.
    "LOCAL",  # Current File.Show the assets currently available in this Blender session.
    "ESSENTIALS",  # Essentials.Show the basic building blocks and utilities coming with Blender.
    "CUSTOM",  # Custom.Show assets from the asset libraries configured in the Preferences.
]
type AttributeCurvesDomainItems = typing.Literal[
    "POINT",  # Control Point.
    "CURVE",  # Curve.
]
type AttributeDomainEdgeFaceItems = typing.Literal[
    "EDGE",  # Edge.Attribute on mesh edge.
    "FACE",  # Face.Attribute on mesh faces.
]
type AttributeDomainItems = typing.Literal[
    "POINT",  # Point.Attribute on point.
    "EDGE",  # Edge.Attribute on mesh edge.
    "FACE",  # Face.Attribute on mesh faces.
    "CORNER",  # Face Corner.Attribute on mesh face corner.
    "CURVE",  # Spline.Attribute on spline.
    "INSTANCE",  # Instance.Attribute on instance.
    "LAYER",  # Layer.Attribute on Grease Pencil layer.
]
type AttributeDomainOnlyMeshItems = typing.Literal[
    "POINT",  # Point.Attribute on point.
    "EDGE",  # Edge.Attribute on mesh edge.
    "FACE",  # Face.Attribute on mesh faces.
    "CORNER",  # Face Corner.Attribute on mesh face corner.
]
type AttributeDomainOnlyMeshNoCornerItems = typing.Literal[
    "POINT",  # Point.Attribute on point.
    "EDGE",  # Edge.Attribute on mesh edge.
    "FACE",  # Face.Attribute on mesh faces.
]
type AttributeDomainOnlyMeshNoEdgeItems = typing.Literal[
    "POINT",  # Point.Attribute on point.
    "FACE",  # Face.Attribute on mesh faces.
    "CORNER",  # Face Corner.Attribute on mesh face corner.
]
type AttributeDomainPointEdgeFaceCurveItems = typing.Literal[
    "POINT",  # Point.Attribute on point.
    "EDGE",  # Edge.Attribute on mesh edge.
    "FACE",  # Face.Attribute on mesh faces.
    "CURVE",  # Spline.Attribute on spline.
]
type AttributeDomainPointFaceCurveItems = typing.Literal[
    "POINT",  # Point.Attribute on point.
    "FACE",  # Face.Attribute on mesh faces.
    "CURVE",  # Spline.Attribute on spline.
]
type AttributeDomainWithAutoItems = typing.Literal[
    "AUTO",  # Auto.
    "POINT",  # Point.Attribute on point.
    "EDGE",  # Edge.Attribute on mesh edge.
    "FACE",  # Face.Attribute on mesh faces.
    "CORNER",  # Face Corner.Attribute on mesh face corner.
    "CURVE",  # Spline.Attribute on spline.
    "INSTANCE",  # Instance.Attribute on instance.
    "LAYER",  # Layer.Attribute on Grease Pencil layer.
]
type AttributeDomainWithoutCornerItems = typing.Literal[
    "POINT",  # Point.Attribute on point.
    "EDGE",  # Edge.Attribute on mesh edge.
    "FACE",  # Face.Attribute on mesh faces.
    "CURVE",  # Spline.Attribute on spline.
    "INSTANCE",  # Instance.Attribute on instance.
    "LAYER",  # Layer.Attribute on Grease Pencil layer.
]
type AttributeTypeItems = typing.Literal[
    "FLOAT",  # Float.Floating-point value.
    "INT",  # Integer.32-bit integer.
    "FLOAT_VECTOR",  # Vector.3D vector with floating-point values.
    "FLOAT_COLOR",  # Color.RGBA color with 32-bit floating-point values.
    "BYTE_COLOR",  # Byte Color.RGBA color with 8-bit positive integer values.
    "STRING",  # String.Text string.
    "BOOLEAN",  # Boolean.True or false.
    "FLOAT2",  # 2D Vector.2D vector with floating-point values.
    "INT8",  # 8-Bit Integer.Smaller integer with a range from -128 to 127.
    "INT32_2D",  # 2D Integer Vector.32-bit signed integer vector.
    "QUATERNION",  # Quaternion.Floating point quaternion rotation.
    "FLOAT4X4",  # 4x4 Matrix.Floating point matrix.
]
type AttributeTypeWithAutoItems = typing.Literal[
    "AUTO",  # Auto.
    "FLOAT",  # Float.Floating-point value.
    "INT",  # Integer.32-bit integer.
    "FLOAT_VECTOR",  # Vector.3D vector with floating-point values.
    "FLOAT_COLOR",  # Color.RGBA color with 32-bit floating-point values.
    "BYTE_COLOR",  # Byte Color.RGBA color with 8-bit positive integer values.
    "STRING",  # String.Text string.
    "BOOLEAN",  # Boolean.True or false.
    "FLOAT2",  # 2D Vector.2D vector with floating-point values.
    "FLOAT2",  # 2D Vector.2D vector with floating-point values.
    "INT32_2D",  # 2D Integer Vector.32-bit signed integer vector.
    "QUATERNION",  # Quaternion.Floating point quaternion rotation.
    "FLOAT4X4",  # 4x4 Matrix.Floating point matrix.
]
type AxisFlagXyzItems = typing.Literal[
    "X",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "X" (ordinal 24)
    "Y",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "Y" (ordinal 25)
    "Z",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "Z" (ordinal 26)
]
type AxisXyItems = typing.Literal[
    "X",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "X" (ordinal 24)
    "Y",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "Y" (ordinal 25)
]
type AxisXyzItems = typing.Literal[
    "X",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "X" (ordinal 24)
    "Y",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "Y" (ordinal 25)
    "Z",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "Z" (ordinal 26)
]
type BakeMarginTypeItems = typing.Literal[
    "ADJACENT_FACES",  # Adjacent Faces.Use pixels from adjacent faces across UV seams.
    "EXTEND",  # Extend.Extend border pixels outwards.
]
type BakePassFilterTypeItems = typing.Literal[
    "NONE",  # None.
    "EMIT",  # Emit.
    "DIRECT",  # Direct.
    "INDIRECT",  # Indirect.
    "COLOR",  # Color.
    "DIFFUSE",  # Diffuse.
    "GLOSSY",  # Glossy.
    "TRANSMISSION",  # Transmission.
]
type BakePassTypeItems = typing.Literal[
    "COMBINED",  # Combined.
    "AO",  # Ambient Occlusion.
    "SHADOW",  # Shadow.
    "POSITION",  # Position.
    "NORMAL",  # Normal.
    "UV",  # UV.
    "ROUGHNESS",  # ROUGHNESS.
    "EMIT",  # Emit.
    "ENVIRONMENT",  # Environment.
    "DIFFUSE",  # Diffuse.
    "GLOSSY",  # Glossy.
    "TRANSMISSION",  # Transmission.
]
type BakeSaveModeItems = typing.Literal[
    "INTERNAL",  # Internal.Save the baking map in an internal image data-block.
    "EXTERNAL",  # External.Save the baking map in an external file.
]
type BakeTargetItems = typing.Literal[
    "IMAGE_TEXTURES",  # Image Textures.Bake to image data-blocks associated with active image texture nodes in materials.
    "VERTEX_COLORS",  # Active Color Attribute.Bake to the active color attribute on meshes.
]
type BeztripleInterpolationEasingItems = typing.Literal[
    "AUTO",  # Automatic Easing.Easing type is chosen automatically based on what the type of interpolation used (e.g. Ease In for transitional types, and Ease Out for dynamic effects).
    "EASE_IN",  # Ease In.Only on the end closest to the next keyframe.
    "EASE_OUT",  # Ease Out.Only on the end closest to the first keyframe.
    "EASE_IN_OUT",  # Ease In and Out.Segment between both keyframes.
]
type BeztripleInterpolationModeItems = typing.Literal[
    "CONSTANT",  # Constant.No interpolation, value of A gets held until B is encountered.
    "LINEAR",  # Linear.Straight-line interpolation between A and B (i.e. no ease in/out).
    "BEZIER",  # Bézier.Smooth interpolation between A and B, with some control over curve shape.
    "SINE",  # Sinusoidal.Sinusoidal easing (weakest, almost linear but with a slight curvature).
    "QUAD",  # Quadratic.Quadratic easing.
    "CUBIC",  # Cubic.Cubic easing.
    "QUART",  # Quartic.Quartic easing.
    "QUINT",  # Quintic.Quintic easing.
    "EXPO",  # Exponential.Exponential easing (dramatic).
    "CIRC",  # Circular.Circular easing (strongest and most dynamic).
    "BACK",  # Back.Cubic easing with overshoot and settle.
    "BOUNCE",  # Bounce.Exponentially decaying parabolic bounce, like when objects collide.
    "ELASTIC",  # Elastic.Exponentially decaying sine wave, like an elastic band.
]
type BeztripleKeyframeTypeItems = typing.Literal[
    "KEYFRAME",  # Keyframe.Normal keyframe, e.g. for key poses.
    "BREAKDOWN",  # Breakdown.A breakdown pose, e.g. for transitions between key poses.
    "MOVING_HOLD",  # Moving Hold.A keyframe that is part of a moving hold.
    "EXTREME",  # Extreme.An "extreme" pose, or some other purpose as needed.
    "JITTER",  # Jitter.A filler or baked keyframe for keying on ones, or some other purpose as needed.
    "GENERATED",  # Generated.A key generated automatically by a tool, not manually created.
]
type BoidruleTypeItems = typing.Literal[
    "GOAL",  # Goal.Go to assigned object or loudest assigned signal source.
    "AVOID",  # Avoid.Get away from assigned object or loudest assigned signal source.
    "AVOID_COLLISION",  # Avoid Collision.Maneuver to avoid collisions with other boids and deflector objects in near future.
    "SEPARATE",  # Separate.Keep from going through other boids.
    "FLOCK",  # Flock.Move to center of neighbors and match their velocity.
    "FOLLOW_LEADER",  # Follow Leader.Follow a boid or assigned object.
    "AVERAGE_SPEED",  # Average Speed.Maintain speed, flight level or wander.
    "FIGHT",  # Fight.Go to closest enemy and attack when in range.
]
type BrushAutomaskingFlagItems = typing.Literal[
    "use_automasking_topology",  # Topology.Affect only vertices connected to the active vertex under the brush.
    "use_automasking_face_sets",  # Face Sets.Affect only vertices that share Face Sets with the active vertex.
    "use_automasking_boundary_edges",  # Mesh Boundary Auto-Masking.Do not affect non manifold boundary edges.
    "use_automasking_boundary_face_sets",  # Face Sets Boundary Automasking.Do not affect vertices that belong to a Face Set boundary.
    "use_automasking_cavity",  # Cavity Mask.Do not affect vertices on peaks, based on the surface curvature.
    "use_automasking_cavity_inverted",  # Inverted Cavity Mask.Do not affect vertices within crevices, based on the surface curvature.
    "use_automasking_custom_cavity_curve",  # Custom Cavity Curve.Use custom curve.
]
type BrushCurvePresetItems = typing.Literal[
    "CUSTOM",  # Custom.
    "SMOOTH",  # Smooth.
    "SMOOTHER",  # Smoother.
    "SPHERE",  # Sphere.
    "ROOT",  # Root.
    "SHARP",  # Sharp.
    "LIN",  # Linear.
    "POW4",  # Sharper.
    "INVSQUARE",  # Inverse Square.
    "CONSTANT",  # Constant.
]
type BrushCurvesSculptToolItems = typing.Literal[
    "SELECTION_PAINT",  # Paint Selection.
    "ADD",  # Add.
    "DELETE",  # Delete.
    "DENSITY",  # Density.
    "COMB",  # Comb.
    "SNAKE_HOOK",  # Snake Hook.
    "GROW_SHRINK",  # Grow / Shrink.
    "PINCH",  # Pinch.
    "PUFF",  # Puff.
    "SMOOTH",  # Smooth.
    "SLIDE",  # Slide.
]
type BrushGpencilSculptTypesItems = typing.Literal[
    "SMOOTH",  # Smooth.Smooth stroke points.
    "THICKNESS",  # Thickness.Adjust thickness of strokes.
    "STRENGTH",  # Strength.Adjust color strength of strokes.
    "RANDOMIZE",  # Randomize.Introduce jitter/randomness into strokes.
    "GRAB",  # Grab.Translate the set of points initially within the brush circle.
    "PUSH",  # Push.Move points out of the way, as if combing them.
    "TWIST",  # Twist.Rotate points around the midpoint of the brush.
    "PINCH",  # Pinch.Pull points towards the midpoint of the brush.
    "CLONE",  # Clone.Paste copies of the strokes stored on the internal clipboard.
]
type BrushGpencilTypesItems = typing.Literal[
    "DRAW",  # Draw.The brush is of type used for drawing strokes.
    "FILL",  # Fill.The brush is of type used for filling areas.
    "ERASE",  # Erase.The brush is used for erasing strokes.
    "TINT",  # Tint.The brush is of type used for tinting strokes.
]
type BrushGpencilVertexTypesItems = typing.Literal[
    "DRAW",  # Draw.Paint a color on stroke points.
    "BLUR",  # Blur.Smooth out the colors of adjacent stroke points.
    "AVERAGE",  # Average.Smooth out colors with the average color under the brush.
    "SMEAR",  # Smear.Smudge colors by grabbing and dragging them.
    "REPLACE",  # Replace.Replace the color of stroke points that already have a color applied.
]
type BrushGpencilWeightTypesItems = typing.Literal[
    "WEIGHT",  # Weight.Paint weight in active vertex group.
    "BLUR",  # Blur.Blur weight in active vertex group.
    "AVERAGE",  # Average.Average weight in active vertex group.
    "SMEAR",  # Smear.Smear weight in active vertex group.
]
type BrushImageToolItems = typing.Literal[
    "DRAW",  # Draw.
    "SOFTEN",  # Soften.
    "SMEAR",  # Smear.
    "CLONE",  # Clone.
    "FILL",  # Fill.
    "MASK",  # Mask.
]
type BrushSculptToolItems = typing.Literal[
    "DRAW",  # Draw.
    "DRAW_SHARP",  # Draw Sharp.
    "CLAY",  # Clay.
    "CLAY_STRIPS",  # Clay Strips.
    "CLAY_THUMB",  # Clay Thumb.
    "LAYER",  # Layer.
    "INFLATE",  # Inflate.
    "BLOB",  # Blob.
    "CREASE",  # Crease.
    "SMOOTH",  # Smooth.
    "FLATTEN",  # Flatten.
    "FILL",  # Fill.
    "SCRAPE",  # Scrape.
    "MULTIPLANE_SCRAPE",  # Multi-plane Scrape.
    "PINCH",  # Pinch.
    "GRAB",  # Grab.
    "ELASTIC_DEFORM",  # Elastic Deform.
    "SNAKE_HOOK",  # Snake Hook.
    "THUMB",  # Thumb.
    "POSE",  # Pose.
    "NUDGE",  # Nudge.
    "ROTATE",  # Rotate.
    "TOPOLOGY",  # Slide Relax.
    "BOUNDARY",  # Boundary.
    "CLOTH",  # Cloth.
    "SIMPLIFY",  # Simplify.
    "MASK",  # Mask.
    "DRAW_FACE_SETS",  # Draw Face Sets.
    "DISPLACEMENT_ERASER",  # Multires Displacement Eraser.
    "DISPLACEMENT_SMEAR",  # Multires Displacement Smear.
    "PAINT",  # Paint.
    "SMEAR",  # Smear.
]
type BrushVertexToolItems = typing.Literal[
    "DRAW",  # Draw.
    "BLUR",  # Blur.
    "AVERAGE",  # Average.
    "SMEAR",  # Smear.
]
type BrushWeightToolItems = typing.Literal[
    "DRAW",  # Draw.
    "BLUR",  # Blur.
    "AVERAGE",  # Average.
    "SMEAR",  # Smear.
]
type ClipEditorModeItems = typing.Literal[
    "TRACKING",  # Tracking.Show tracking and solving tools.
    "MASK",  # Mask.Show mask editing tools.
]
type CollectionColorItems = typing.Literal[
    "NONE",  # None.Assign no color tag to the collection.
    "COLOR_01",  # Color 01.
    "COLOR_02",  # Color 02.
    "COLOR_03",  # Color 03.
    "COLOR_04",  # Color 04.
    "COLOR_05",  # Color 05.
    "COLOR_06",  # Color 06.
    "COLOR_07",  # Color 07.
    "COLOR_08",  # Color 08.
]
type ColorAttributeDomainItems = typing.Literal[
    "POINT",  # Vertex.
    "CORNER",  # Face Corner.
]
type ColorAttributeTypeItems = typing.Literal[
    "FLOAT_COLOR",  # Color.RGBA color 32-bit floating-point values.
    "BYTE_COLOR",  # Byte Color.RGBA color with 8-bit positive integer values.
]
type ColorSetsItems = typing.Literal[
    "DEFAULT",  # Default Colors.
    "THEME01",  # 01 - Theme Color Set.
    "THEME02",  # 02 - Theme Color Set.
    "THEME03",  # 03 - Theme Color Set.
    "THEME04",  # 04 - Theme Color Set.
    "THEME05",  # 05 - Theme Color Set.
    "THEME06",  # 06 - Theme Color Set.
    "THEME07",  # 07 - Theme Color Set.
    "THEME08",  # 08 - Theme Color Set.
    "THEME09",  # 09 - Theme Color Set.
    "THEME10",  # 10 - Theme Color Set.
    "THEME11",  # 11 - Theme Color Set.
    "THEME12",  # 12 - Theme Color Set.
    "THEME13",  # 13 - Theme Color Set.
    "THEME14",  # 14 - Theme Color Set.
    "THEME15",  # 15 - Theme Color Set.
    "THEME16",  # 16 - Theme Color Set.
    "THEME17",  # 17 - Theme Color Set.
    "THEME18",  # 18 - Theme Color Set.
    "THEME19",  # 19 - Theme Color Set.
    "THEME20",  # 20 - Theme Color Set.
    "CUSTOM",  # Custom Color Set.
]
type ColorSpaceConvertDefaultItems = typing.Literal[
    "NONE",  # None.Do not perform any color transform on load, treat colors as in scene linear space already.
]
type ConstraintTypeItems = typing.Literal[
    "CAMERA_SOLVER",  # Camera Solver.
    "FOLLOW_TRACK",  # Follow Track.
    "OBJECT_SOLVER",  # Object Solver.
    "COPY_LOCATION",  # Copy Location.Copy the location of a target (with an optional offset), so that they move together.
    "COPY_ROTATION",  # Copy Rotation.Copy the rotation of a target (with an optional offset), so that they rotate together.
    "COPY_SCALE",  # Copy Scale.Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.
    "COPY_TRANSFORMS",  # Copy Transforms.Copy all the transformations of a target, so that they move together.
    "LIMIT_DISTANCE",  # Limit Distance.Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).
    "LIMIT_LOCATION",  # Limit Location.Restrict movement along each axis within given ranges.
    "LIMIT_ROTATION",  # Limit Rotation.Restrict rotation along each axis within given ranges.
    "LIMIT_SCALE",  # Limit Scale.Restrict scaling along each axis with given ranges.
    "MAINTAIN_VOLUME",  # Maintain Volume.Compensate for scaling one axis by applying suitable scaling to the other two axes.
    "TRANSFORM",  # Transformation.Use one transform property from target to control another (or same) property on owner.
    "TRANSFORM_CACHE",  # Transform Cache.Look up the transformation matrix from an external file.
    "CLAMP_TO",  # Clamp To.Restrict movements to lie along a curve by remapping location along curve's longest axis.
    "DAMPED_TRACK",  # Damped Track.Point towards a target by performing the smallest rotation necessary.
    "IK",  # Inverse Kinematics.Control a chain of bones by specifying the endpoint target (Bones only).
    "LOCKED_TRACK",  # Locked Track.Rotate around the specified ('locked') axis to point towards a target.
    "SPLINE_IK",  # Spline IK.Align chain of bones along a curve (Bones only).
    "STRETCH_TO",  # Stretch To.Stretch along Y-Axis to point towards a target.
    "TRACK_TO",  # Track To.Legacy tracking constraint prone to twisting artifacts.
    "ACTION",  # Action.Use transform property of target to look up pose for owner from an Action.
    "ARMATURE",  # Armature.Apply weight-blended transformation from multiple bones like the Armature modifier.
    "CHILD_OF",  # Child Of.Make target the 'detachable' parent of owner.
    "FLOOR",  # Floor.Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner cannot cross.
    "FOLLOW_PATH",  # Follow Path.Use to animate an object/bone following a path.
    "PIVOT",  # Pivot.Change pivot point for transforms (buggy).
    "SHRINKWRAP",  # Shrinkwrap.Restrict movements to surface of target mesh.
]
type ContextModeItems = typing.Literal[
    "EDIT_MESH",  # Mesh Edit.
    "EDIT_CURVE",  # Curve Edit.
    "EDIT_CURVES",  # Curves Edit.
    "EDIT_SURFACE",  # Surface Edit.
    "EDIT_TEXT",  # Text Edit.
    "EDIT_ARMATURE",  # Armature Edit.
    "EDIT_METABALL",  # Metaball Edit.
    "EDIT_LATTICE",  # Lattice Edit.
    "EDIT_GREASE_PENCIL",  # Grease Pencil Edit.
    "EDIT_POINT_CLOUD",  # Point Cloud Edit.
    "POSE",  # Pose.
    "SCULPT",  # Sculpt.
    "PAINT_WEIGHT",  # Weight Paint.
    "PAINT_VERTEX",  # Vertex Paint.
    "PAINT_TEXTURE",  # Texture Paint.
    "PARTICLE",  # Particle.
    "OBJECT",  # Object.
    "PAINT_GPENCIL",  # Grease Pencil Paint.
    "EDIT_GPENCIL",  # Grease Pencil Edit.
    "SCULPT_GPENCIL",  # Grease Pencil Sculpt.
    "WEIGHT_GPENCIL",  # Grease Pencil Weight Paint.
    "VERTEX_GPENCIL",  # Grease Pencil Vertex Paint.
    "SCULPT_CURVES",  # Curves Sculpt.
    "PAINT_GREASE_PENCIL",  # Grease Pencil Paint.
    "SCULPT_GREASE_PENCIL",  # Grease Pencil Sculpt.
    "WEIGHT_GREASE_PENCIL",  # Grease Pencil Weight Paint.
]
type CurveFitMethodItems = typing.Literal[
    "REFIT",  # Refit.Incrementally refit the curve (high quality).
    "SPLIT",  # Split.Split the curve until the tolerance is met (fast).
]
type CurveNormalModeItems = typing.Literal[
    "MINIMUM_TWIST",  # Minimum Twist.Calculate normals with the smallest twist around the curve tangent across the whole curve.
    "Z_UP",  # Z Up.Calculate normals perpendicular to the Z axis and the curve tangent. If a series of points is vertical, the X axis is used.
    "FREE",  # Free.Use the stored custom normal attribute as the final normals.
]
type CurvesHandleTypeItems = typing.Literal[
    "FREE",  # Free.The handle can be moved anywhere, and doesn't influence the point's other handle.
    "AUTO",  # Auto.The location is automatically calculated to be smooth.
    "VECTOR",  # Vector.The location is calculated to point to the next/previous control point.
    "ALIGN",  # Align.The location is constrained to point in the opposite direction as the other handleW.
]
type CurvesTypeItems = typing.Literal[
    "CATMULL_ROM",  # Catmull Rom.
    "POLY",  # Poly.
    "BEZIER",  # Bézier.
    "NURBS",  # NURBS.
]
type DriverTargetRotationModeItems = typing.Literal[
    "AUTO",  # Auto Euler.Euler using the rotation order of the target.
    "XYZ",  # XYZ Euler.Euler using the XYZ rotation order.
    "XZY",  # XZY Euler.Euler using the XZY rotation order.
    "YXZ",  # YXZ Euler.Euler using the YXZ rotation order.
    "YZX",  # YZX Euler.Euler using the YZX rotation order.
    "ZXY",  # ZXY Euler.Euler using the ZXY rotation order.
    "ZYX",  # ZYX Euler.Euler using the ZYX rotation order.
    "QUATERNION",  # Quaternion.Quaternion rotation.
    "SWING_TWIST_X",  # Swing and X Twist.Decompose into a swing rotation to aim the X axis, followed by twist around it.
    "SWING_TWIST_Y",  # Swing and Y Twist.Decompose into a swing rotation to aim the Y axis, followed by twist around it.
    "SWING_TWIST_Z",  # Swing and Z Twist.Decompose into a swing rotation to aim the Z axis, followed by twist around it.
]
type DtLayersSelectDstItems = typing.Literal[
    "ACTIVE",  # Active Layer.Affect active data layer of all targets.
    "NAME",  # By Name.Match target data layers to affect by name.
    "INDEX",  # By Order.Match target data layers to affect by order (indices).
]
type DtLayersSelectSrcItems = typing.Literal[
    "ACTIVE",  # Active Layer.Only transfer active data layer.
    "ALL",  # All Layers.Transfer all data layers.
    "BONE_SELECT",  # Selected Pose Bones.Transfer all vertex groups used by selected pose bones.
    "BONE_DEFORM",  # Deform Pose Bones.Transfer all vertex groups used by deform bones.
]
type DtMethodEdgeItems = typing.Literal[
    "TOPOLOGY",  # Topology.Copy from identical topology meshes.
    "VERT_NEAREST",  # Nearest Vertices.Copy from most similar edge (edge which vertices are the closest of destination edge's ones).
    "NEAREST",  # Nearest Edge.Copy from closest edge (using midpoints).
    "POLY_NEAREST",  # Nearest Face Edge.Copy from closest edge of closest face (using midpoints).
    "EDGEINTERP_VNORPROJ",  # Projected Edge Interpolated.Interpolate all source edges hit by the projection of destination one along its own normal (from vertices).
]
type DtMethodLoopItems = typing.Literal[
    "TOPOLOGY",  # Topology.Copy from identical topology meshes.
    "NEAREST_NORMAL",  # Nearest Corner and Best Matching Normal.Copy from nearest corner which has the best matching normal.
    "NEAREST_POLYNOR",  # Nearest Corner and Best Matching Face Normal.Copy from nearest corner which has the face with the best matching normal to destination corner's face one.
    "NEAREST_POLY",  # Nearest Corner of Nearest Face.Copy from nearest corner of nearest face.
    "POLYINTERP_NEAREST",  # Nearest Face Interpolated.Copy from interpolated corners of the nearest source face.
    "POLYINTERP_LNORPROJ",  # Projected Face Interpolated.Copy from interpolated corners of the source face hit by corner normal projection.
]
type DtMethodPolyItems = typing.Literal[
    "TOPOLOGY",  # Topology.Copy from identical topology meshes.
    "NEAREST",  # Nearest Face.Copy from nearest face (using center points).
    "NORMAL",  # Best Normal-Matching.Copy from source face which normal is the closest to destination one.
    "POLYINTERP_PNORPROJ",  # Projected Face Interpolated.Interpolate all source polygons intersected by the projection of destination one along its own normal.
]
type DtMethodVertexItems = typing.Literal[
    "TOPOLOGY",  # Topology.Copy from identical topology meshes.
    "NEAREST",  # Nearest Vertex.Copy from closest vertex.
    "EDGE_NEAREST",  # Nearest Edge Vertex.Copy from closest vertex of closest edge.
    "EDGEINTERP_NEAREST",  # Nearest Edge Interpolated.Copy from interpolated values of vertices from closest point on closest edge.
    "POLY_NEAREST",  # Nearest Face Vertex.Copy from closest vertex of closest face.
    "POLYINTERP_NEAREST",  # Nearest Face Interpolated.Copy from interpolated values of vertices from closest point on closest face.
    "POLYINTERP_VNORPROJ",  # Projected Face Interpolated.Copy from interpolated values of vertices from point on closest face hit by normal-projection.
]
type DtMixModeItems = typing.Literal[
    "REPLACE",  # Replace.Overwrite all elements' data.
    "ABOVE_THRESHOLD",  # Above Threshold.Only replace destination elements where data is above given threshold (exact behavior depends on data type).
    "BELOW_THRESHOLD",  # Below Threshold.Only replace destination elements where data is below given threshold (exact behavior depends on data type).
    "MIX",  # Mix.Mix source value into destination one, using given threshold as factor.
    "ADD",  # Add.Add source value to destination one, using given threshold as factor.
    "SUB",  # Subtract.Subtract source value to destination one, using given threshold as factor.
    "MUL",  # Multiply.Multiply source value to destination one, using given threshold as factor.
]
type EventDirectionItems = typing.Literal[
    "ANY",  # Any.
    "NORTH",  # North.
    "NORTH_EAST",  # North-East.
    "EAST",  # East.
    "SOUTH_EAST",  # South-East.
    "SOUTH",  # South.
    "SOUTH_WEST",  # South-West.
    "WEST",  # West.
    "NORTH_WEST",  # North-West.
]
type EventTypeItems = typing.Literal[
    "NONE",
    "LEFTMOUSE",  # Left Mouse.LMB.
    "MIDDLEMOUSE",  # Middle Mouse.MMB.
    "RIGHTMOUSE",  # Right Mouse.RMB.
    "BUTTON4MOUSE",  # Button4 Mouse.MB4.
    "BUTTON5MOUSE",  # Button5 Mouse.MB5.
    "BUTTON6MOUSE",  # Button6 Mouse.MB6.
    "BUTTON7MOUSE",  # Button7 Mouse.MB7.
    "PEN",  # Pen.
    "ERASER",  # Eraser.
    "MOUSEMOVE",  # Mouse Move.MsMov.
    "INBETWEEN_MOUSEMOVE",  # In-between Move.MsSubMov.
    "TRACKPADPAN",  # Mouse/Trackpad Pan.MsPan.
    "TRACKPADZOOM",  # Mouse/Trackpad Zoom.MsZoom.
    "MOUSEROTATE",  # Mouse/Trackpad Rotate.MsRot.
    "MOUSESMARTZOOM",  # Mouse/Trackpad Smart Zoom.MsSmartZoom.
    "WHEELUPMOUSE",  # Wheel Up.WhUp.
    "WHEELDOWNMOUSE",  # Wheel Down.WhDown.
    "WHEELINMOUSE",  # Wheel In.WhIn.
    "WHEELOUTMOUSE",  # Wheel Out.WhOut.
    "A",
    "B",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "B" (ordinal 2)
    "C",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "C" (ordinal 3)
    "D",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "D" (ordinal 4)
    "E",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "E" (ordinal 5)
    "F",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "F" (ordinal 6)
    "G",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "G" (ordinal 7)
    "H",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "H" (ordinal 8)
    "I",
    "J",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "J" (ordinal 10)
    "K",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "K" (ordinal 11)
    "L",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "L" (ordinal 12)
    "M",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "M" (ordinal 13)
    "N",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "N" (ordinal 14)
    "O",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "O" (ordinal 15)
    "P",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "P" (ordinal 16)
    "Q",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "Q" (ordinal 17)
    "R",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "R" (ordinal 18)
    "S",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "S" (ordinal 19)
    "T",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "T" (ordinal 20)
    "U",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "U" (ordinal 21)
    "V",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "V" (ordinal 22)
    "W",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "W" (ordinal 23)
    "X",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "X" (ordinal 24)
    "Y",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "Y" (ordinal 25)
    "Z",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "Z" (ordinal 26)
    "ZERO",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "0" (ordinal 0)
    "ONE",
    "TWO",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "2" (ordinal 2)
    "THREE",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "3" (ordinal 3)
    "FOUR",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "4" (ordinal 4)
    "FIVE",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "5" (ordinal 5)
    "SIX",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "6" (ordinal 6)
    "SEVEN",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "7" (ordinal 7)
    "EIGHT",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "8" (ordinal 8)
    "NINE",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "9" (ordinal 9)
    "LEFT_CTRL",  # Left Ctrl.CtrlL.
    "LEFT_ALT",  # Left Alt.AltL.
    "LEFT_SHIFT",  # Left Shift.ShiftL.
    "RIGHT_ALT",  # Right Alt.AltR.
    "RIGHT_CTRL",  # Right Ctrl.CtrlR.
    "RIGHT_SHIFT",  # Right Shift.ShiftR.
    "OSKEY",  # OS Key.Cmd.
    "APP",  # Application.App.
    "GRLESS",  # Grless.
    "ESC",  # Esc.
    "TAB",  # Tab.
    "RET",  # Return.Enter.
    "SPACE",  # Spacebar.Space.
    "LINE_FEED",  # Line Feed.
    "BACK_SPACE",  # Backspace.BkSpace.
    "DEL",  # Delete.Del.
    "SEMI_COLON",  # ;.
    "PERIOD",
    "COMMA",  # ,.
    "QUOTE",  # ".
    "ACCENT_GRAVE",  # `.
    "MINUS",  # -.
    "PLUS",  # +.
    "SLASH",  # /.
    "BACK_SLASH",  # \.
    "EQUAL",  # =.
    "LEFT_BRACKET",  # [.
    "RIGHT_BRACKET",  # ].
    "LEFT_ARROW",  # Left Arrow.←.
    "DOWN_ARROW",  # Down Arrow.↓.
    "RIGHT_ARROW",  # Right Arrow.→.
    "UP_ARROW",  # Up Arrow.↑.
    "NUMPAD_2",  # Numpad 2.Pad2.
    "NUMPAD_4",  # Numpad 4.Pad4.
    "NUMPAD_6",  # Numpad 6.Pad6.
    "NUMPAD_8",  # Numpad 8.Pad8.
    "NUMPAD_1",  # Numpad 1.Pad1.
    "NUMPAD_3",  # Numpad 3.Pad3.
    "NUMPAD_5",  # Numpad 5.Pad5.
    "NUMPAD_7",  # Numpad 7.Pad7.
    "NUMPAD_9",  # Numpad 9.Pad9.
    "NUMPAD_PERIOD",  # Numpad ..Pad..
    "NUMPAD_SLASH",  # Numpad /.Pad/.
    "NUMPAD_ASTERIX",  # Numpad *.Pad*.
    "NUMPAD_0",  # Numpad 0.Pad0.
    "NUMPAD_MINUS",  # Numpad -.Pad-.
    "NUMPAD_ENTER",  # Numpad Enter.PadEnter.
    "NUMPAD_PLUS",  # Numpad +.Pad+.
    "F1",  # F1.
    "F2",  # F2.
    "F3",  # F3.
    "F4",  # F4.
    "F5",  # F5.
    "F6",  # F6.
    "F7",  # F7.
    "F8",  # F8.
    "F9",  # F9.
    "F10",  # F10.
    "F11",  # F11.
    "F12",  # F12.
    "F13",  # F13.
    "F14",  # F14.
    "F15",  # F15.
    "F16",  # F16.
    "F17",  # F17.
    "F18",  # F18.
    "F19",  # F19.
    "F20",  # F20.
    "F21",  # F21.
    "F22",  # F22.
    "F23",  # F23.
    "F24",  # F24.
    "PAUSE",  # Pause.
    "INSERT",  # Insert.Ins.
    "HOME",  # Home.
    "PAGE_UP",  # Page Up.PgUp.
    "PAGE_DOWN",  # Page Down.PgDown.
    "END",  # End.
    "MEDIA_PLAY",  # Media Play/Pause.⏯.
    "MEDIA_STOP",  # Media Stop.⏹.
    "MEDIA_FIRST",  # Media First.⏮.
    "MEDIA_LAST",  # Media Last.⏭.
    "TEXTINPUT",  # Text Input.TxtIn.
    "WINDOW_DEACTIVATE",  # Window Deactivate.
    "TIMER",  # Timer.Tmr.
    "TIMER0",  # Timer 0.Tmr0.
    "TIMER1",  # Timer 1.Tmr1.
    "TIMER2",  # Timer 2.Tmr2.
    "TIMER_JOBS",  # Timer Jobs.TmrJob.
    "TIMER_AUTOSAVE",  # Timer Autosave.TmrSave.
    "TIMER_REPORT",  # Timer Report.TmrReport.
    "TIMERREGION",  # Timer Region.TmrReg.
    "NDOF_MOTION",  # NDOF Motion.NdofMov.
    "NDOF_BUTTON_MENU",  # NDOF Menu.NdofMenu.
    "NDOF_BUTTON_FIT",  # NDOF Fit.NdofFit.
    "NDOF_BUTTON_TOP",  # NDOF Top.Ndof↑.
    "NDOF_BUTTON_BOTTOM",  # NDOF Bottom.Ndof↓.
    "NDOF_BUTTON_LEFT",  # NDOF Left.Ndof←.
    "NDOF_BUTTON_RIGHT",  # NDOF Right.Ndof→.
    "NDOF_BUTTON_FRONT",  # NDOF Front.NdofFront.
    "NDOF_BUTTON_BACK",  # NDOF Back.NdofBack.
    "NDOF_BUTTON_ISO1",  # NDOF Isometric 1.NdofIso1.
    "NDOF_BUTTON_ISO2",  # NDOF Isometric 2.NdofIso2.
    "NDOF_BUTTON_ROLL_CW",  # NDOF Roll CW.NdofRCW.
    "NDOF_BUTTON_ROLL_CCW",  # NDOF Roll CCW.NdofRCCW.
    "NDOF_BUTTON_SPIN_CW",  # NDOF Spin CW.NdofSCW.
    "NDOF_BUTTON_SPIN_CCW",  # NDOF Spin CCW.NdofSCCW.
    "NDOF_BUTTON_TILT_CW",  # NDOF Tilt CW.NdofTCW.
    "NDOF_BUTTON_TILT_CCW",  # NDOF Tilt CCW.NdofTCCW.
    "NDOF_BUTTON_ROTATE",  # NDOF Rotate.NdofRot.
    "NDOF_BUTTON_PANZOOM",  # NDOF Pan/Zoom.NdofPanZoom.
    "NDOF_BUTTON_DOMINANT",  # NDOF Dominant.NdofDom.
    "NDOF_BUTTON_PLUS",  # NDOF Plus.Ndof+.
    "NDOF_BUTTON_MINUS",  # NDOF Minus.Ndof-.
    "NDOF_BUTTON_V1",  # NDOF View 1.
    "NDOF_BUTTON_V2",  # NDOF View 2.
    "NDOF_BUTTON_V3",  # NDOF View 3.
    "NDOF_BUTTON_1",  # NDOF Button 1.NdofB1.
    "NDOF_BUTTON_2",  # NDOF Button 2.NdofB2.
    "NDOF_BUTTON_3",  # NDOF Button 3.NdofB3.
    "NDOF_BUTTON_4",  # NDOF Button 4.NdofB4.
    "NDOF_BUTTON_5",  # NDOF Button 5.NdofB5.
    "NDOF_BUTTON_6",  # NDOF Button 6.NdofB6.
    "NDOF_BUTTON_7",  # NDOF Button 7.NdofB7.
    "NDOF_BUTTON_8",  # NDOF Button 8.NdofB8.
    "NDOF_BUTTON_9",  # NDOF Button 9.NdofB9.
    "NDOF_BUTTON_10",  # NDOF Button 10.NdofB10.
    "NDOF_BUTTON_A",  # NDOF Button A.NdofBA.
    "NDOF_BUTTON_B",  # NDOF Button B.NdofBB.
    "NDOF_BUTTON_C",  # NDOF Button C.NdofBC.
    "ACTIONZONE_AREA",  # ActionZone Area.AZone Area.
    "ACTIONZONE_REGION",  # ActionZone Region.AZone Region.
    "ACTIONZONE_FULLSCREEN",  # ActionZone Fullscreen.AZone FullScr.
    "XR_ACTION",  # XR Action.
]
type EventTypeMaskItems = typing.Literal[
    "KEYBOARD_MODIFIER",  # Keyboard Modifier.
    "KEYBOARD",  # Keyboard.
    "MOUSE_WHEEL",  # Mouse Wheel.
    "MOUSE_GESTURE",  # Mouse Gesture.
    "MOUSE_BUTTON",  # Mouse Button.
    "MOUSE",  # Mouse.
    "NDOF",  # NDOF.
    "ACTIONZONE",  # Action Zone.
]
type EventValueItems = typing.Literal[
    "ANY",  # Any.
    "PRESS",  # Press.
    "RELEASE",  # Release.
    "CLICK",  # Click.
    "DOUBLE_CLICK",  # Double Click.
    "CLICK_DRAG",  # Click Drag.
    "NOTHING",  # Nothing.
]
type ExrCodecItems = typing.Literal[
    "NONE",  # None.
    "PXR24",  # Pxr24 (lossy).
    "ZIP",  # ZIP (lossless).
    "PIZ",  # PIZ (lossless).
    "RLE",  # RLE (lossless).
    "ZIPS",  # ZIPS (lossless).
    "B44",  # B44 (lossy).
    "B44A",  # B44A (lossy).
    "DWAA",  # DWAA (lossy).
    "DWAB",  # DWAB (lossy).
]
type FcurveAutoSmoothingItems = typing.Literal[
    "NONE",  # None.Automatic handles only take immediately adjacent keys into account.
    "CONT_ACCEL",  # Continuous Acceleration.Automatic handles are adjusted to avoid jumps in acceleration, resulting in smoother curves. However, key changes may affect interpolation over a larger stretch of the curve.
]
type FileselectParamsSortItems = typing.Literal[
    "FILE_SORT_ALPHA",  # Name.Sort the file list alphabetically.
    "FILE_SORT_EXTENSION",  # Extension.Sort the file list by extension/type.
    "FILE_SORT_TIME",  # Modified Date.Sort files by modification time.
    "FILE_SORT_SIZE",  # Size.Sort files by size.
]
type FmodifierTypeItems = typing.Literal[
    "NULL",  # Invalid.
    "GENERATOR",  # Generator.Generate a curve using a factorized or expanded polynomial.
    "FNGENERATOR",  # Built-In Function.Generate a curve using standard math functions such as sin and cos.
    "ENVELOPE",  # Envelope.Reshape F-Curve values, e.g. change amplitude of movements.
    "CYCLES",  # Cycles.Cyclic extend/repeat keyframe sequence.
    "NOISE",  # Noise.Add pseudo-random noise on top of F-Curves.
    "LIMITS",  # Limits.Restrict maximum and minimum values of F-Curve.
    "STEPPED",  # Stepped Interpolation.Snap values to nearest grid step, e.g. for a stop-motion look.
]
type GeometryComponentTypeItems = typing.Literal[
    "MESH",  # Mesh.Mesh component containing point, corner, edge and face data.
    "POINTCLOUD",  # Point Cloud.Point cloud component containing only point data.
    "CURVE",  # Curve.Curve component containing spline and control point data.
    "INSTANCES",  # Instances.Instances of objects or collections.
]
type GreasePencilSelectmodeItems = typing.Literal[
    "POINT",  # Point.Select only points.
    "STROKE",  # Stroke.Select all stroke points.
    "SEGMENT",  # Segment.Select all stroke points between other strokes.
]
type IconItems = typing.Literal[
    "NONE",  # NONE.
    "QUESTION",  # QUESTION.
    "ERROR",  # ERROR.
    "CANCEL",  # CANCEL.
    "TRIA_RIGHT",  # TRIA_RIGHT.
    "TRIA_DOWN",  # TRIA_DOWN.
    "TRIA_LEFT",  # TRIA_LEFT.
    "TRIA_UP",  # TRIA_UP.
    "ARROW_LEFTRIGHT",  # ARROW_LEFTRIGHT.
    "PLUS",  # PLUS.
    "DISCLOSURE_TRI_RIGHT",  # DISCLOSURE_TRI_RIGHT.
    "DISCLOSURE_TRI_DOWN",  # DISCLOSURE_TRI_DOWN.
    "RADIOBUT_OFF",  # RADIOBUT_OFF.
    "RADIOBUT_ON",  # RADIOBUT_ON.
    "MENU_PANEL",  # MENU_PANEL.
    "BLENDER",  # BLENDER.
    "GRIP",  # GRIP.
    "DOT",  # DOT.
    "COLLAPSEMENU",  # COLLAPSEMENU.
    "X",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "X" (ordinal 24)
    "DUPLICATE",  # DUPLICATE.
    "TRASH",  # TRASH.
    "COLLECTION_NEW",  # COLLECTION_NEW.
    "OPTIONS",  # OPTIONS.
    "NODE",  # NODE.
    "NODE_SEL",  # NODE_SEL.
    "WINDOW",  # WINDOW.
    "WORKSPACE",  # WORKSPACE.
    "RIGHTARROW_THIN",  # RIGHTARROW_THIN.
    "BORDERMOVE",  # BORDERMOVE.
    "VIEWZOOM",  # VIEWZOOM.
    "ADD",  # ADD.
    "REMOVE",  # REMOVE.
    "PANEL_CLOSE",  # PANEL_CLOSE.
    "COPY_ID",  # COPY_ID.
    "EYEDROPPER",  # EYEDROPPER.
    "CHECKMARK",  # CHECKMARK.
    "AUTO",  # AUTO.
    "CHECKBOX_DEHLT",  # CHECKBOX_DEHLT.
    "CHECKBOX_HLT",  # CHECKBOX_HLT.
    "UNLOCKED",  # UNLOCKED.
    "LOCKED",  # LOCKED.
    "UNPINNED",  # UNPINNED.
    "PINNED",  # PINNED.
    "SCREEN_BACK",  # SCREEN_BACK.
    "RIGHTARROW",  # RIGHTARROW.
    "DOWNARROW_HLT",  # DOWNARROW_HLT.
    "FCURVE_SNAPSHOT",  # FCURVE_SNAPSHOT.
    "OBJECT_HIDDEN",  # OBJECT_HIDDEN.
    "TOPBAR",  # TOPBAR.
    "STATUSBAR",  # STATUSBAR.
    "PLUGIN",  # PLUGIN.
    "HELP",  # HELP.
    "GHOST_ENABLED",  # GHOST_ENABLED.
    "COLOR",  # COLOR.
    "UNLINKED",  # UNLINKED.
    "LINKED",  # LINKED.
    "HAND",  # HAND.
    "ZOOM_ALL",  # ZOOM_ALL.
    "ZOOM_SELECTED",  # ZOOM_SELECTED.
    "ZOOM_PREVIOUS",  # ZOOM_PREVIOUS.
    "ZOOM_IN",  # ZOOM_IN.
    "ZOOM_OUT",  # ZOOM_OUT.
    "DRIVER_DISTANCE",  # DRIVER_DISTANCE.
    "DRIVER_ROTATIONAL_DIFFERENCE",  # DRIVER_ROTATIONAL_DIFFERENCE.
    "DRIVER_TRANSFORM",  # DRIVER_TRANSFORM.
    "FREEZE",  # FREEZE.
    "STYLUS_PRESSURE",  # STYLUS_PRESSURE.
    "GHOST_DISABLED",  # GHOST_DISABLED.
    "FILE_NEW",  # FILE_NEW.
    "FILE_TICK",  # FILE_TICK.
    "QUIT",  # QUIT.
    "URL",  # URL.
    "RECOVER_LAST",  # RECOVER_LAST.
    "THREE_DOTS",  # THREE_DOTS.
    "FULLSCREEN_ENTER",  # FULLSCREEN_ENTER.
    "FULLSCREEN_EXIT",  # FULLSCREEN_EXIT.
    "BRUSHES_ALL",  # BRUSHES_ALL.
    "LIGHT",  # LIGHT.
    "MATERIAL",  # MATERIAL.
    "TEXTURE",  # TEXTURE.
    "ANIM",  # ANIM.
    "WORLD",  # WORLD.
    "SCENE",  # SCENE.
    "OUTPUT",  # OUTPUT.
    "SCRIPT",  # SCRIPT.
    "PARTICLES",  # PARTICLES.
    "PHYSICS",  # PHYSICS.
    "SPEAKER",  # SPEAKER.
    "TOOL_SETTINGS",  # TOOL_SETTINGS.
    "SHADERFX",  # SHADERFX.
    "MODIFIER",  # MODIFIER.
    "RECORD_OFF",  # RECORD_OFF.
    "RECORD_ON",  # RECORD_ON.
    "BLANK1",  # BLANK1.
    "FAKE_USER_OFF",  # FAKE_USER_OFF.
    "FAKE_USER_ON",  # FAKE_USER_ON.
    "VIEW3D",  # VIEW3D.
    "GRAPH",  # GRAPH.
    "OUTLINER",  # OUTLINER.
    "PROPERTIES",  # PROPERTIES.
    "FILEBROWSER",  # FILEBROWSER.
    "IMAGE",  # IMAGE.
    "INFO",  # INFO.
    "SEQUENCE",  # SEQUENCE.
    "TEXT",  # TEXT.
    "SPREADSHEET",  # SPREADSHEET.
    "SOUND",  # SOUND.
    "ACTION",  # ACTION.
    "NLA",  # NLA.
    "PREFERENCES",  # PREFERENCES.
    "TIME",  # TIME.
    "NODETREE",  # NODETREE.
    "GEOMETRY_NODES",  # GEOMETRY_NODES.
    "CONSOLE",  # CONSOLE.
    "TRACKER",  # TRACKER.
    "ASSET_MANAGER",  # ASSET_MANAGER.
    "NODE_COMPOSITING",  # NODE_COMPOSITING.
    "NODE_TEXTURE",  # NODE_TEXTURE.
    "NODE_MATERIAL",  # NODE_MATERIAL.
    "UV",  # UV.
    "OBJECT_DATAMODE",  # OBJECT_DATAMODE.
    "EDITMODE_HLT",  # EDITMODE_HLT.
    "UV_DATA",  # UV_DATA.
    "VPAINT_HLT",  # VPAINT_HLT.
    "TPAINT_HLT",  # TPAINT_HLT.
    "WPAINT_HLT",  # WPAINT_HLT.
    "SCULPTMODE_HLT",  # SCULPTMODE_HLT.
    "POSE_HLT",  # POSE_HLT.
    "PARTICLEMODE",  # PARTICLEMODE.
    "TRACKING",  # TRACKING.
    "TRACKING_BACKWARDS",  # TRACKING_BACKWARDS.
    "TRACKING_FORWARDS",  # TRACKING_FORWARDS.
    "TRACKING_BACKWARDS_SINGLE",  # TRACKING_BACKWARDS_SINGLE.
    "TRACKING_FORWARDS_SINGLE",  # TRACKING_FORWARDS_SINGLE.
    "TRACKING_CLEAR_BACKWARDS",  # TRACKING_CLEAR_BACKWARDS.
    "TRACKING_CLEAR_FORWARDS",  # TRACKING_CLEAR_FORWARDS.
    "TRACKING_REFINE_BACKWARDS",  # TRACKING_REFINE_BACKWARDS.
    "TRACKING_REFINE_FORWARDS",  # TRACKING_REFINE_FORWARDS.
    "SCENE_DATA",  # SCENE_DATA.
    "RENDERLAYERS",  # RENDERLAYERS.
    "WORLD_DATA",  # WORLD_DATA.
    "OBJECT_DATA",  # OBJECT_DATA.
    "MESH_DATA",  # MESH_DATA.
    "CURVE_DATA",  # CURVE_DATA.
    "META_DATA",  # META_DATA.
    "LATTICE_DATA",  # LATTICE_DATA.
    "LIGHT_DATA",  # LIGHT_DATA.
    "MATERIAL_DATA",  # MATERIAL_DATA.
    "TEXTURE_DATA",  # TEXTURE_DATA.
    "ANIM_DATA",  # ANIM_DATA.
    "CAMERA_DATA",  # CAMERA_DATA.
    "PARTICLE_DATA",  # PARTICLE_DATA.
    "LIBRARY_DATA_DIRECT",  # LIBRARY_DATA_DIRECT.
    "GROUP",  # GROUP.
    "ARMATURE_DATA",  # ARMATURE_DATA.
    "COMMUNITY",  # COMMUNITY.
    "BONE_DATA",  # BONE_DATA.
    "CONSTRAINT",  # CONSTRAINT.
    "SHAPEKEY_DATA",  # SHAPEKEY_DATA.
    "CONSTRAINT_BONE",  # CONSTRAINT_BONE.
    "CAMERA_STEREO",  # CAMERA_STEREO.
    "PACKAGE",  # PACKAGE.
    "UGLYPACKAGE",  # UGLYPACKAGE.
    "EXPERIMENTAL",  # EXPERIMENTAL.
    "BRUSH_DATA",  # BRUSH_DATA.
    "IMAGE_DATA",  # IMAGE_DATA.
    "FILE",  # FILE.
    "FCURVE",  # FCURVE.
    "FONT_DATA",  # FONT_DATA.
    "RENDER_RESULT",  # RENDER_RESULT.
    "SURFACE_DATA",  # SURFACE_DATA.
    "EMPTY_DATA",  # EMPTY_DATA.
    "PRESET",  # PRESET.
    "RENDER_ANIMATION",  # RENDER_ANIMATION.
    "RENDER_STILL",  # RENDER_STILL.
    "LIBRARY_DATA_BROKEN",  # LIBRARY_DATA_BROKEN.
    "BOIDS",  # BOIDS.
    "STRANDS",  # STRANDS.
    "GREASEPENCIL",  # GREASEPENCIL.
    "LINE_DATA",  # LINE_DATA.
    "LIBRARY_DATA_OVERRIDE",  # LIBRARY_DATA_OVERRIDE.
    "GROUP_BONE",  # GROUP_BONE.
    "GROUP_VERTEX",  # GROUP_VERTEX.
    "GROUP_VCOL",  # GROUP_VCOL.
    "GROUP_UVS",  # GROUP_UVS.
    "FACE_MAPS",  # FACE_MAPS.
    "RNA",  # RNA.
    "RNA_ADD",  # RNA_ADD.
    "MOUSE_LMB",  # MOUSE_LMB.
    "MOUSE_MMB",  # MOUSE_MMB.
    "MOUSE_RMB",  # MOUSE_RMB.
    "MOUSE_MOVE",  # MOUSE_MOVE.
    "MOUSE_LMB_DRAG",  # MOUSE_LMB_DRAG.
    "MOUSE_MMB_DRAG",  # MOUSE_MMB_DRAG.
    "MOUSE_RMB_DRAG",  # MOUSE_RMB_DRAG.
    "MEMORY",  # MEMORY.
    "PRESET_NEW",  # PRESET_NEW.
    "DECORATE",  # DECORATE.
    "DECORATE_KEYFRAME",  # DECORATE_KEYFRAME.
    "DECORATE_ANIMATE",  # DECORATE_ANIMATE.
    "DECORATE_DRIVER",  # DECORATE_DRIVER.
    "DECORATE_LINKED",  # DECORATE_LINKED.
    "DECORATE_LIBRARY_OVERRIDE",  # DECORATE_LIBRARY_OVERRIDE.
    "DECORATE_UNLOCKED",  # DECORATE_UNLOCKED.
    "DECORATE_LOCKED",  # DECORATE_LOCKED.
    "DECORATE_OVERRIDE",  # DECORATE_OVERRIDE.
    "FUND",  # FUND.
    "TRACKER_DATA",  # TRACKER_DATA.
    "HEART",  # HEART.
    "ORPHAN_DATA",  # ORPHAN_DATA.
    "USER",  # USER.
    "SYSTEM",  # SYSTEM.
    "SETTINGS",  # SETTINGS.
    "OUTLINER_OB_EMPTY",  # OUTLINER_OB_EMPTY.
    "OUTLINER_OB_MESH",  # OUTLINER_OB_MESH.
    "OUTLINER_OB_CURVE",  # OUTLINER_OB_CURVE.
    "OUTLINER_OB_LATTICE",  # OUTLINER_OB_LATTICE.
    "OUTLINER_OB_META",  # OUTLINER_OB_META.
    "OUTLINER_OB_LIGHT",  # OUTLINER_OB_LIGHT.
    "OUTLINER_OB_CAMERA",  # OUTLINER_OB_CAMERA.
    "OUTLINER_OB_ARMATURE",  # OUTLINER_OB_ARMATURE.
    "OUTLINER_OB_FONT",  # OUTLINER_OB_FONT.
    "OUTLINER_OB_SURFACE",  # OUTLINER_OB_SURFACE.
    "OUTLINER_OB_SPEAKER",  # OUTLINER_OB_SPEAKER.
    "OUTLINER_OB_FORCE_FIELD",  # OUTLINER_OB_FORCE_FIELD.
    "OUTLINER_OB_GROUP_INSTANCE",  # OUTLINER_OB_GROUP_INSTANCE.
    "OUTLINER_OB_GREASEPENCIL",  # OUTLINER_OB_GREASEPENCIL.
    "OUTLINER_OB_LIGHTPROBE",  # OUTLINER_OB_LIGHTPROBE.
    "OUTLINER_OB_IMAGE",  # OUTLINER_OB_IMAGE.
    "OUTLINER_COLLECTION",  # OUTLINER_COLLECTION.
    "RESTRICT_COLOR_OFF",  # RESTRICT_COLOR_OFF.
    "RESTRICT_COLOR_ON",  # RESTRICT_COLOR_ON.
    "HIDE_ON",  # HIDE_ON.
    "HIDE_OFF",  # HIDE_OFF.
    "RESTRICT_SELECT_ON",  # RESTRICT_SELECT_ON.
    "RESTRICT_SELECT_OFF",  # RESTRICT_SELECT_OFF.
    "RESTRICT_RENDER_ON",  # RESTRICT_RENDER_ON.
    "RESTRICT_RENDER_OFF",  # RESTRICT_RENDER_OFF.
    "RESTRICT_INSTANCED_OFF",  # RESTRICT_INSTANCED_OFF.
    "OUTLINER_DATA_EMPTY",  # OUTLINER_DATA_EMPTY.
    "OUTLINER_DATA_MESH",  # OUTLINER_DATA_MESH.
    "OUTLINER_DATA_CURVE",  # OUTLINER_DATA_CURVE.
    "OUTLINER_DATA_LATTICE",  # OUTLINER_DATA_LATTICE.
    "OUTLINER_DATA_META",  # OUTLINER_DATA_META.
    "OUTLINER_DATA_LIGHT",  # OUTLINER_DATA_LIGHT.
    "OUTLINER_DATA_CAMERA",  # OUTLINER_DATA_CAMERA.
    "OUTLINER_DATA_ARMATURE",  # OUTLINER_DATA_ARMATURE.
    "OUTLINER_DATA_FONT",  # OUTLINER_DATA_FONT.
    "OUTLINER_DATA_SURFACE",  # OUTLINER_DATA_SURFACE.
    "OUTLINER_DATA_SPEAKER",  # OUTLINER_DATA_SPEAKER.
    "OUTLINER_DATA_LIGHTPROBE",  # OUTLINER_DATA_LIGHTPROBE.
    "OUTLINER_DATA_GP_LAYER",  # OUTLINER_DATA_GP_LAYER.
    "OUTLINER_DATA_GREASEPENCIL",  # OUTLINER_DATA_GREASEPENCIL.
    "GP_SELECT_POINTS",  # GP_SELECT_POINTS.
    "GP_SELECT_STROKES",  # GP_SELECT_STROKES.
    "GP_MULTIFRAME_EDITING",  # GP_MULTIFRAME_EDITING.
    "GP_ONLY_SELECTED",  # GP_ONLY_SELECTED.
    "GP_SELECT_BETWEEN_STROKES",  # GP_SELECT_BETWEEN_STROKES.
    "MODIFIER_OFF",  # MODIFIER_OFF.
    "MODIFIER_ON",  # MODIFIER_ON.
    "ONIONSKIN_OFF",  # ONIONSKIN_OFF.
    "ONIONSKIN_ON",  # ONIONSKIN_ON.
    "RESTRICT_VIEW_ON",  # RESTRICT_VIEW_ON.
    "RESTRICT_VIEW_OFF",  # RESTRICT_VIEW_OFF.
    "RESTRICT_INSTANCED_ON",  # RESTRICT_INSTANCED_ON.
    "MESH_PLANE",  # MESH_PLANE.
    "MESH_CUBE",  # MESH_CUBE.
    "MESH_CIRCLE",  # MESH_CIRCLE.
    "MESH_UVSPHERE",  # MESH_UVSPHERE.
    "MESH_ICOSPHERE",  # MESH_ICOSPHERE.
    "MESH_GRID",  # MESH_GRID.
    "MESH_MONKEY",  # MESH_MONKEY.
    "MESH_CYLINDER",  # MESH_CYLINDER.
    "MESH_TORUS",  # MESH_TORUS.
    "MESH_CONE",  # MESH_CONE.
    "MESH_CAPSULE",  # MESH_CAPSULE.
    "EMPTY_SINGLE_ARROW",  # EMPTY_SINGLE_ARROW.
    "LIGHT_POINT",  # LIGHT_POINT.
    "LIGHT_SUN",  # LIGHT_SUN.
    "LIGHT_SPOT",  # LIGHT_SPOT.
    "LIGHT_HEMI",  # LIGHT_HEMI.
    "LIGHT_AREA",  # LIGHT_AREA.
    "CUBE",  # CUBE.
    "SPHERE",  # SPHERE.
    "CONE",  # CONE.
    "META_PLANE",  # META_PLANE.
    "META_CUBE",  # META_CUBE.
    "META_BALL",  # META_BALL.
    "META_ELLIPSOID",  # META_ELLIPSOID.
    "META_CAPSULE",  # META_CAPSULE.
    "SURFACE_NCURVE",  # SURFACE_NCURVE.
    "SURFACE_NCIRCLE",  # SURFACE_NCIRCLE.
    "SURFACE_NSURFACE",  # SURFACE_NSURFACE.
    "SURFACE_NCYLINDER",  # SURFACE_NCYLINDER.
    "SURFACE_NSPHERE",  # SURFACE_NSPHERE.
    "SURFACE_NTORUS",  # SURFACE_NTORUS.
    "EMPTY_AXIS",  # EMPTY_AXIS.
    "STROKE",  # STROKE.
    "EMPTY_ARROWS",  # EMPTY_ARROWS.
    "CURVE_BEZCURVE",  # CURVE_BEZCURVE.
    "CURVE_BEZCIRCLE",  # CURVE_BEZCIRCLE.
    "CURVE_NCURVE",  # CURVE_NCURVE.
    "CURVE_NCIRCLE",  # CURVE_NCIRCLE.
    "CURVE_PATH",  # CURVE_PATH.
    "LIGHTPROBE_SPHERE",  # LIGHTPROBE_SPHERE.
    "LIGHTPROBE_PLANE",  # LIGHTPROBE_PLANE.
    "LIGHTPROBE_VOLUME",  # LIGHTPROBE_VOLUME.
    "COLOR_RED",  # COLOR_RED.
    "COLOR_GREEN",  # COLOR_GREEN.
    "COLOR_BLUE",  # COLOR_BLUE.
    "TRIA_RIGHT_BAR",  # TRIA_RIGHT_BAR.
    "TRIA_DOWN_BAR",  # TRIA_DOWN_BAR.
    "TRIA_LEFT_BAR",  # TRIA_LEFT_BAR.
    "TRIA_UP_BAR",  # TRIA_UP_BAR.
    "FORCE_FORCE",  # FORCE_FORCE.
    "FORCE_WIND",  # FORCE_WIND.
    "FORCE_VORTEX",  # FORCE_VORTEX.
    "FORCE_MAGNETIC",  # FORCE_MAGNETIC.
    "FORCE_HARMONIC",  # FORCE_HARMONIC.
    "FORCE_CHARGE",  # FORCE_CHARGE.
    "FORCE_LENNARDJONES",  # FORCE_LENNARDJONES.
    "FORCE_TEXTURE",  # FORCE_TEXTURE.
    "FORCE_CURVE",  # FORCE_CURVE.
    "FORCE_BOID",  # FORCE_BOID.
    "FORCE_TURBULENCE",  # FORCE_TURBULENCE.
    "FORCE_DRAG",  # FORCE_DRAG.
    "FORCE_FLUIDFLOW",  # FORCE_FLUIDFLOW.
    "RIGID_BODY",  # RIGID_BODY.
    "RIGID_BODY_CONSTRAINT",  # RIGID_BODY_CONSTRAINT.
    "AREA_JOIN",  # AREA_JOIN.
    "AREA_SWAP",  # AREA_SWAP.
    "SPLIT_HORIZONTAL",  # SPLIT_HORIZONTAL.
    "SPLIT_VERTICAL",  # SPLIT_VERTICAL.
    "IMAGE_PLANE",  # IMAGE_PLANE.
    "IMAGE_BACKGROUND",  # IMAGE_BACKGROUND.
    "IMAGE_REFERENCE",  # IMAGE_REFERENCE.
    "NODE_INSERT_ON",  # NODE_INSERT_ON.
    "NODE_INSERT_OFF",  # NODE_INSERT_OFF.
    "NODE_TOP",  # NODE_TOP.
    "NODE_SIDE",  # NODE_SIDE.
    "NODE_CORNER",  # NODE_CORNER.
    "ANCHOR_TOP",  # ANCHOR_TOP.
    "ANCHOR_BOTTOM",  # ANCHOR_BOTTOM.
    "ANCHOR_LEFT",  # ANCHOR_LEFT.
    "ANCHOR_RIGHT",  # ANCHOR_RIGHT.
    "ANCHOR_CENTER",  # ANCHOR_CENTER.
    "SELECT_SET",  # SELECT_SET.
    "SELECT_EXTEND",  # SELECT_EXTEND.
    "SELECT_SUBTRACT",  # SELECT_SUBTRACT.
    "SELECT_INTERSECT",  # SELECT_INTERSECT.
    "SELECT_DIFFERENCE",  # SELECT_DIFFERENCE.
    "ALIGN_LEFT",  # ALIGN_LEFT.
    "ALIGN_CENTER",  # ALIGN_CENTER.
    "ALIGN_RIGHT",  # ALIGN_RIGHT.
    "ALIGN_JUSTIFY",  # ALIGN_JUSTIFY.
    "ALIGN_FLUSH",  # ALIGN_FLUSH.
    "ALIGN_TOP",  # ALIGN_TOP.
    "ALIGN_MIDDLE",  # ALIGN_MIDDLE.
    "ALIGN_BOTTOM",  # ALIGN_BOTTOM.
    "BOLD",  # BOLD.
    "ITALIC",  # ITALIC.
    "UNDERLINE",  # UNDERLINE.
    "SMALL_CAPS",  # SMALL_CAPS.
    "CON_ACTION",  # CON_ACTION.
    "MOD_ENVELOPE",  # MOD_ENVELOPE.
    "MOD_OUTLINE",  # MOD_OUTLINE.
    "MOD_LENGTH",  # MOD_LENGTH.
    "MOD_DASH",  # MOD_DASH.
    "MOD_LINEART",  # MOD_LINEART.
    "HOLDOUT_OFF",  # HOLDOUT_OFF.
    "HOLDOUT_ON",  # HOLDOUT_ON.
    "INDIRECT_ONLY_OFF",  # INDIRECT_ONLY_OFF.
    "INDIRECT_ONLY_ON",  # INDIRECT_ONLY_ON.
    "CON_CAMERASOLVER",  # CON_CAMERASOLVER.
    "CON_FOLLOWTRACK",  # CON_FOLLOWTRACK.
    "CON_OBJECTSOLVER",  # CON_OBJECTSOLVER.
    "CON_LOCLIKE",  # CON_LOCLIKE.
    "CON_ROTLIKE",  # CON_ROTLIKE.
    "CON_SIZELIKE",  # CON_SIZELIKE.
    "CON_TRANSLIKE",  # CON_TRANSLIKE.
    "CON_DISTLIMIT",  # CON_DISTLIMIT.
    "CON_LOCLIMIT",  # CON_LOCLIMIT.
    "CON_ROTLIMIT",  # CON_ROTLIMIT.
    "CON_SIZELIMIT",  # CON_SIZELIMIT.
    "CON_SAMEVOL",  # CON_SAMEVOL.
    "CON_TRANSFORM",  # CON_TRANSFORM.
    "CON_TRANSFORM_CACHE",  # CON_TRANSFORM_CACHE.
    "CON_CLAMPTO",  # CON_CLAMPTO.
    "CON_KINEMATIC",  # CON_KINEMATIC.
    "CON_LOCKTRACK",  # CON_LOCKTRACK.
    "CON_SPLINEIK",  # CON_SPLINEIK.
    "CON_STRETCHTO",  # CON_STRETCHTO.
    "CON_TRACKTO",  # CON_TRACKTO.
    "CON_ARMATURE",  # CON_ARMATURE.
    "CON_CHILDOF",  # CON_CHILDOF.
    "CON_FLOOR",  # CON_FLOOR.
    "CON_FOLLOWPATH",  # CON_FOLLOWPATH.
    "CON_PIVOT",  # CON_PIVOT.
    "CON_SHRINKWRAP",  # CON_SHRINKWRAP.
    "MODIFIER_DATA",  # MODIFIER_DATA.
    "MOD_WAVE",  # MOD_WAVE.
    "MOD_BUILD",  # MOD_BUILD.
    "MOD_DECIM",  # MOD_DECIM.
    "MOD_MIRROR",  # MOD_MIRROR.
    "MOD_SOFT",  # MOD_SOFT.
    "MOD_SUBSURF",  # MOD_SUBSURF.
    "HOOK",  # HOOK.
    "MOD_PHYSICS",  # MOD_PHYSICS.
    "MOD_PARTICLES",  # MOD_PARTICLES.
    "MOD_BOOLEAN",  # MOD_BOOLEAN.
    "MOD_EDGESPLIT",  # MOD_EDGESPLIT.
    "MOD_ARRAY",  # MOD_ARRAY.
    "MOD_UVPROJECT",  # MOD_UVPROJECT.
    "MOD_DISPLACE",  # MOD_DISPLACE.
    "MOD_CURVE",  # MOD_CURVE.
    "MOD_LATTICE",  # MOD_LATTICE.
    "MOD_TINT",  # MOD_TINT.
    "MOD_ARMATURE",  # MOD_ARMATURE.
    "MOD_SHRINKWRAP",  # MOD_SHRINKWRAP.
    "MOD_CAST",  # MOD_CAST.
    "MOD_MESHDEFORM",  # MOD_MESHDEFORM.
    "MOD_BEVEL",  # MOD_BEVEL.
    "MOD_SMOOTH",  # MOD_SMOOTH.
    "MOD_SIMPLEDEFORM",  # MOD_SIMPLEDEFORM.
    "MOD_MASK",  # MOD_MASK.
    "MOD_CLOTH",  # MOD_CLOTH.
    "MOD_EXPLODE",  # MOD_EXPLODE.
    "MOD_FLUIDSIM",  # MOD_FLUIDSIM.
    "MOD_MULTIRES",  # MOD_MULTIRES.
    "MOD_FLUID",  # MOD_FLUID.
    "MOD_SOLIDIFY",  # MOD_SOLIDIFY.
    "MOD_SCREW",  # MOD_SCREW.
    "MOD_VERTEX_WEIGHT",  # MOD_VERTEX_WEIGHT.
    "MOD_DYNAMICPAINT",  # MOD_DYNAMICPAINT.
    "MOD_REMESH",  # MOD_REMESH.
    "MOD_OCEAN",  # MOD_OCEAN.
    "MOD_WARP",  # MOD_WARP.
    "MOD_SKIN",  # MOD_SKIN.
    "MOD_TRIANGULATE",  # MOD_TRIANGULATE.
    "MOD_WIREFRAME",  # MOD_WIREFRAME.
    "MOD_DATA_TRANSFER",  # MOD_DATA_TRANSFER.
    "MOD_NORMALEDIT",  # MOD_NORMALEDIT.
    "MOD_PARTICLE_INSTANCE",  # MOD_PARTICLE_INSTANCE.
    "MOD_HUE_SATURATION",  # MOD_HUE_SATURATION.
    "MOD_NOISE",  # MOD_NOISE.
    "MOD_OFFSET",  # MOD_OFFSET.
    "MOD_SIMPLIFY",  # MOD_SIMPLIFY.
    "MOD_THICKNESS",  # MOD_THICKNESS.
    "MOD_INSTANCE",  # MOD_INSTANCE.
    "MOD_TIME",  # MOD_TIME.
    "MOD_OPACITY",  # MOD_OPACITY.
    "REC",  # REC.
    "PLAY",  # PLAY.
    "FF",  # FF.
    "REW",  # REW.
    "PAUSE",  # PAUSE.
    "PREV_KEYFRAME",  # PREV_KEYFRAME.
    "NEXT_KEYFRAME",  # NEXT_KEYFRAME.
    "PLAY_SOUND",  # PLAY_SOUND.
    "PLAY_REVERSE",  # PLAY_REVERSE.
    "PREVIEW_RANGE",  # PREVIEW_RANGE.
    "ACTION_TWEAK",  # ACTION_TWEAK.
    "PMARKER_ACT",  # PMARKER_ACT.
    "PMARKER_SEL",  # PMARKER_SEL.
    "PMARKER",  # PMARKER.
    "MARKER_HLT",  # MARKER_HLT.
    "MARKER",  # MARKER.
    "KEYFRAME_HLT",  # KEYFRAME_HLT.
    "KEYFRAME",  # KEYFRAME.
    "KEYINGSET",  # KEYINGSET.
    "KEY_DEHLT",  # KEY_DEHLT.
    "KEY_HLT",  # KEY_HLT.
    "MUTE_IPO_OFF",  # MUTE_IPO_OFF.
    "MUTE_IPO_ON",  # MUTE_IPO_ON.
    "DRIVER",  # DRIVER.
    "SOLO_OFF",  # SOLO_OFF.
    "SOLO_ON",  # SOLO_ON.
    "FRAME_PREV",  # FRAME_PREV.
    "FRAME_NEXT",  # FRAME_NEXT.
    "NLA_PUSHDOWN",  # NLA_PUSHDOWN.
    "IPO_CONSTANT",  # IPO_CONSTANT.
    "IPO_LINEAR",  # IPO_LINEAR.
    "IPO_BEZIER",  # IPO_BEZIER.
    "IPO_SINE",  # IPO_SINE.
    "IPO_QUAD",  # IPO_QUAD.
    "IPO_CUBIC",  # IPO_CUBIC.
    "IPO_QUART",  # IPO_QUART.
    "IPO_QUINT",  # IPO_QUINT.
    "IPO_EXPO",  # IPO_EXPO.
    "IPO_CIRC",  # IPO_CIRC.
    "IPO_BOUNCE",  # IPO_BOUNCE.
    "IPO_ELASTIC",  # IPO_ELASTIC.
    "IPO_BACK",  # IPO_BACK.
    "IPO_EASE_IN",  # IPO_EASE_IN.
    "IPO_EASE_OUT",  # IPO_EASE_OUT.
    "IPO_EASE_IN_OUT",  # IPO_EASE_IN_OUT.
    "NORMALIZE_FCURVES",  # NORMALIZE_FCURVES.
    "ORIENTATION_PARENT",  # ORIENTATION_PARENT.
    "FACE_CORNER",  # FACE_CORNER.
    "VERTEXSEL",  # VERTEXSEL.
    "EDGESEL",  # EDGESEL.
    "FACESEL",  # FACESEL.
    "CURSOR",  # CURSOR.
    "PIVOT_BOUNDBOX",  # PIVOT_BOUNDBOX.
    "PIVOT_CURSOR",  # PIVOT_CURSOR.
    "PIVOT_INDIVIDUAL",  # PIVOT_INDIVIDUAL.
    "PIVOT_MEDIAN",  # PIVOT_MEDIAN.
    "PIVOT_ACTIVE",  # PIVOT_ACTIVE.
    "CENTER_ONLY",  # CENTER_ONLY.
    "ROOTCURVE",  # ROOTCURVE.
    "SMOOTHCURVE",  # SMOOTHCURVE.
    "SPHERECURVE",  # SPHERECURVE.
    "INVERSESQUARECURVE",  # INVERSESQUARECURVE.
    "SHARPCURVE",  # SHARPCURVE.
    "LINCURVE",  # LINCURVE.
    "NOCURVE",  # NOCURVE.
    "RNDCURVE",  # RNDCURVE.
    "PROP_OFF",  # PROP_OFF.
    "PROP_ON",  # PROP_ON.
    "PROP_CON",  # PROP_CON.
    "PROP_PROJECTED",  # PROP_PROJECTED.
    "PARTICLE_POINT",  # PARTICLE_POINT.
    "PARTICLE_TIP",  # PARTICLE_TIP.
    "PARTICLE_PATH",  # PARTICLE_PATH.
    "SNAP_FACE_NEAREST",  # SNAP_FACE_NEAREST.
    "SNAP_FACE_CENTER",  # SNAP_FACE_CENTER.
    "SNAP_PERPENDICULAR",  # SNAP_PERPENDICULAR.
    "SNAP_MIDPOINT",  # SNAP_MIDPOINT.
    "SNAP_OFF",  # SNAP_OFF.
    "SNAP_ON",  # SNAP_ON.
    "SNAP_NORMAL",  # SNAP_NORMAL.
    "SNAP_GRID",  # SNAP_GRID.
    "SNAP_VERTEX",  # SNAP_VERTEX.
    "SNAP_EDGE",  # SNAP_EDGE.
    "SNAP_FACE",  # SNAP_FACE.
    "SNAP_VOLUME",  # SNAP_VOLUME.
    "SNAP_INCREMENT",  # SNAP_INCREMENT.
    "STICKY_UVS_LOC",  # STICKY_UVS_LOC.
    "STICKY_UVS_DISABLE",  # STICKY_UVS_DISABLE.
    "STICKY_UVS_VERT",  # STICKY_UVS_VERT.
    "CLIPUV_DEHLT",  # CLIPUV_DEHLT.
    "CLIPUV_HLT",  # CLIPUV_HLT.
    "SNAP_PEEL_OBJECT",  # SNAP_PEEL_OBJECT.
    "GRID",  # GRID.
    "OBJECT_ORIGIN",  # OBJECT_ORIGIN.
    "ORIENTATION_GLOBAL",  # ORIENTATION_GLOBAL.
    "ORIENTATION_GIMBAL",  # ORIENTATION_GIMBAL.
    "ORIENTATION_LOCAL",  # ORIENTATION_LOCAL.
    "ORIENTATION_NORMAL",  # ORIENTATION_NORMAL.
    "ORIENTATION_VIEW",  # ORIENTATION_VIEW.
    "COPYDOWN",  # COPYDOWN.
    "PASTEDOWN",  # PASTEDOWN.
    "PASTEFLIPUP",  # PASTEFLIPUP.
    "PASTEFLIPDOWN",  # PASTEFLIPDOWN.
    "VIS_SEL_11",  # VIS_SEL_11.
    "VIS_SEL_10",  # VIS_SEL_10.
    "VIS_SEL_01",  # VIS_SEL_01.
    "VIS_SEL_00",  # VIS_SEL_00.
    "AUTOMERGE_OFF",  # AUTOMERGE_OFF.
    "AUTOMERGE_ON",  # AUTOMERGE_ON.
    "UV_VERTEXSEL",  # UV_VERTEXSEL.
    "UV_EDGESEL",  # UV_EDGESEL.
    "UV_FACESEL",  # UV_FACESEL.
    "UV_ISLANDSEL",  # UV_ISLANDSEL.
    "UV_SYNC_SELECT",  # UV_SYNC_SELECT.
    "GP_CAPS_FLAT",  # GP_CAPS_FLAT.
    "GP_CAPS_ROUND",  # GP_CAPS_ROUND.
    "FIXED_SIZE",  # FIXED_SIZE.
    "TRANSFORM_ORIGINS",  # TRANSFORM_ORIGINS.
    "GIZMO",  # GIZMO.
    "ORIENTATION_CURSOR",  # ORIENTATION_CURSOR.
    "NORMALS_VERTEX",  # NORMALS_VERTEX.
    "NORMALS_FACE",  # NORMALS_FACE.
    "NORMALS_VERTEX_FACE",  # NORMALS_VERTEX_FACE.
    "SHADING_BBOX",  # SHADING_BBOX.
    "SHADING_WIRE",  # SHADING_WIRE.
    "SHADING_SOLID",  # SHADING_SOLID.
    "SHADING_RENDERED",  # SHADING_RENDERED.
    "SHADING_TEXTURE",  # SHADING_TEXTURE.
    "OVERLAY",  # OVERLAY.
    "XRAY",  # XRAY.
    "LOCKVIEW_OFF",  # LOCKVIEW_OFF.
    "LOCKVIEW_ON",  # LOCKVIEW_ON.
    "AXIS_SIDE",  # AXIS_SIDE.
    "AXIS_FRONT",  # AXIS_FRONT.
    "AXIS_TOP",  # AXIS_TOP.
    "LAYER_USED",  # LAYER_USED.
    "LAYER_ACTIVE",  # LAYER_ACTIVE.
    "OUTLINER_OB_CURVES",  # OUTLINER_OB_CURVES.
    "OUTLINER_DATA_CURVES",  # OUTLINER_DATA_CURVES.
    "CURVES_DATA",  # CURVES_DATA.
    "OUTLINER_OB_POINTCLOUD",  # OUTLINER_OB_POINTCLOUD.
    "OUTLINER_DATA_POINTCLOUD",  # OUTLINER_DATA_POINTCLOUD.
    "POINTCLOUD_DATA",  # POINTCLOUD_DATA.
    "OUTLINER_OB_VOLUME",  # OUTLINER_OB_VOLUME.
    "OUTLINER_DATA_VOLUME",  # OUTLINER_DATA_VOLUME.
    "VOLUME_DATA",  # VOLUME_DATA.
    "POINTCLOUD_POINT",  # POINTCLOUD_POINT.
    "INTERNET_OFFLINE",  # INTERNET_OFFLINE.
    "INTERNET",  # INTERNET.
    "CURRENT_FILE",  # CURRENT_FILE.
    "HOME",  # HOME.
    "DOCUMENTS",  # DOCUMENTS.
    "TEMP",  # TEMP.
    "SORTALPHA",  # SORTALPHA.
    "SORTBYEXT",  # SORTBYEXT.
    "SORTTIME",  # SORTTIME.
    "SORTSIZE",  # SORTSIZE.
    "SHORTDISPLAY",  # SHORTDISPLAY.
    "LONGDISPLAY",  # LONGDISPLAY.
    "IMGDISPLAY",  # IMGDISPLAY.
    "TAG",  # TAG.
    "BOOKMARKS",  # BOOKMARKS.
    "FONTPREVIEW",  # FONTPREVIEW.
    "FILTER",  # FILTER.
    "NEWFOLDER",  # NEWFOLDER.
    "FOLDER_REDIRECT",  # FOLDER_REDIRECT.
    "FILE_PARENT",  # FILE_PARENT.
    "FILE_REFRESH",  # FILE_REFRESH.
    "FILE_FOLDER",  # FILE_FOLDER.
    "FILE_BLANK",  # FILE_BLANK.
    "FILE_BLEND",  # FILE_BLEND.
    "FILE_IMAGE",  # FILE_IMAGE.
    "FILE_MOVIE",  # FILE_MOVIE.
    "FILE_SCRIPT",  # FILE_SCRIPT.
    "FILE_SOUND",  # FILE_SOUND.
    "FILE_FONT",  # FILE_FONT.
    "FILE_TEXT",  # FILE_TEXT.
    "SORT_DESC",  # SORT_DESC.
    "SORT_ASC",  # SORT_ASC.
    "LINK_BLEND",  # LINK_BLEND.
    "APPEND_BLEND",  # APPEND_BLEND.
    "IMPORT",  # IMPORT.
    "EXPORT",  # EXPORT.
    "LOOP_BACK",  # LOOP_BACK.
    "LOOP_FORWARDS",  # LOOP_FORWARDS.
    "BACK",  # BACK.
    "FORWARD",  # FORWARD.
    "FILE_ARCHIVE",  # FILE_ARCHIVE.
    "FILE_CACHE",  # FILE_CACHE.
    "FILE_VOLUME",  # FILE_VOLUME.
    "FILE_3D",  # FILE_3D.
    "FILE_HIDDEN",  # FILE_HIDDEN.
    "FILE_BACKUP",  # FILE_BACKUP.
    "DISK_DRIVE",  # DISK_DRIVE.
    "MATPLANE",  # MATPLANE.
    "MATSPHERE",  # MATSPHERE.
    "MATCUBE",  # MATCUBE.
    "MONKEY",  # MONKEY.
    "CURVES",  # CURVES.
    "ALIASED",  # ALIASED.
    "ANTIALIASED",  # ANTIALIASED.
    "MAT_SPHERE_SKY",  # MAT_SPHERE_SKY.
    "MATSHADERBALL",  # MATSHADERBALL.
    "MATCLOTH",  # MATCLOTH.
    "MATFLUID",  # MATFLUID.
    "WORDWRAP_OFF",  # WORDWRAP_OFF.
    "WORDWRAP_ON",  # WORDWRAP_ON.
    "SYNTAX_OFF",  # SYNTAX_OFF.
    "SYNTAX_ON",  # SYNTAX_ON.
    "LINENUMBERS_OFF",  # LINENUMBERS_OFF.
    "LINENUMBERS_ON",  # LINENUMBERS_ON.
    "SCRIPTPLUGINS",  # SCRIPTPLUGINS.
    "DISC",  # DISC.
    "DESKTOP",  # DESKTOP.
    "EXTERNAL_DRIVE",  # EXTERNAL_DRIVE.
    "NETWORK_DRIVE",  # NETWORK_DRIVE.
    "SEQ_SEQUENCER",  # SEQ_SEQUENCER.
    "SEQ_PREVIEW",  # SEQ_PREVIEW.
    "SEQ_LUMA_WAVEFORM",  # SEQ_LUMA_WAVEFORM.
    "SEQ_CHROMA_SCOPE",  # SEQ_CHROMA_SCOPE.
    "SEQ_HISTOGRAM",  # SEQ_HISTOGRAM.
    "SEQ_SPLITVIEW",  # SEQ_SPLITVIEW.
    "SEQ_STRIP_META",  # SEQ_STRIP_META.
    "SEQ_STRIP_DUPLICATE",  # SEQ_STRIP_DUPLICATE.
    "IMAGE_RGB",  # IMAGE_RGB.
    "IMAGE_RGB_ALPHA",  # IMAGE_RGB_ALPHA.
    "IMAGE_ALPHA",  # IMAGE_ALPHA.
    "IMAGE_ZDEPTH",  # IMAGE_ZDEPTH.
    "HANDLE_AUTOCLAMPED",  # HANDLE_AUTOCLAMPED.
    "HANDLE_AUTO",  # HANDLE_AUTO.
    "HANDLE_ALIGNED",  # HANDLE_ALIGNED.
    "HANDLE_VECTOR",  # HANDLE_VECTOR.
    "HANDLE_FREE",  # HANDLE_FREE.
    "VIEW_CAMERA_UNSELECTED",  # VIEW_CAMERA_UNSELECTED.
    "VIEW_UNLOCKED",  # VIEW_UNLOCKED.
    "VIEW_LOCKED",  # VIEW_LOCKED.
    "VIEW_PERSPECTIVE",  # VIEW_PERSPECTIVE.
    "VIEW_ORTHO",  # VIEW_ORTHO.
    "VIEW_CAMERA",  # VIEW_CAMERA.
    "VIEW_PAN",  # VIEW_PAN.
    "VIEW_ZOOM",  # VIEW_ZOOM.
    "BRUSH_BLOB",  # BRUSH_BLOB.
    "BRUSH_BLUR",  # BRUSH_BLUR.
    "BRUSH_CLAY",  # BRUSH_CLAY.
    "BRUSH_CLAY_STRIPS",  # BRUSH_CLAY_STRIPS.
    "BRUSH_CLONE",  # BRUSH_CLONE.
    "BRUSH_CREASE",  # BRUSH_CREASE.
    "BRUSH_FILL",  # BRUSH_FILL.
    "BRUSH_FLATTEN",  # BRUSH_FLATTEN.
    "BRUSH_GRAB",  # BRUSH_GRAB.
    "BRUSH_INFLATE",  # BRUSH_INFLATE.
    "BRUSH_LAYER",  # BRUSH_LAYER.
    "BRUSH_MASK",  # BRUSH_MASK.
    "BRUSH_MIX",  # BRUSH_MIX.
    "BRUSH_NUDGE",  # BRUSH_NUDGE.
    "BRUSH_PAINT_SELECT",  # BRUSH_PAINT_SELECT.
    "BRUSH_PINCH",  # BRUSH_PINCH.
    "BRUSH_SCRAPE",  # BRUSH_SCRAPE.
    "BRUSH_SCULPT_DRAW",  # BRUSH_SCULPT_DRAW.
    "BRUSH_SMEAR",  # BRUSH_SMEAR.
    "BRUSH_SMOOTH",  # BRUSH_SMOOTH.
    "BRUSH_SNAKE_HOOK",  # BRUSH_SNAKE_HOOK.
    "BRUSH_SOFTEN",  # BRUSH_SOFTEN.
    "BRUSH_TEXDRAW",  # BRUSH_TEXDRAW.
    "BRUSH_TEXFILL",  # BRUSH_TEXFILL.
    "BRUSH_TEXMASK",  # BRUSH_TEXMASK.
    "BRUSH_THUMB",  # BRUSH_THUMB.
    "BRUSH_ROTATE",  # BRUSH_ROTATE.
    "GPBRUSH_SMOOTH",  # GPBRUSH_SMOOTH.
    "GPBRUSH_THICKNESS",  # GPBRUSH_THICKNESS.
    "GPBRUSH_STRENGTH",  # GPBRUSH_STRENGTH.
    "GPBRUSH_GRAB",  # GPBRUSH_GRAB.
    "GPBRUSH_PUSH",  # GPBRUSH_PUSH.
    "GPBRUSH_TWIST",  # GPBRUSH_TWIST.
    "GPBRUSH_PINCH",  # GPBRUSH_PINCH.
    "GPBRUSH_RANDOMIZE",  # GPBRUSH_RANDOMIZE.
    "GPBRUSH_CLONE",  # GPBRUSH_CLONE.
    "GPBRUSH_WEIGHT",  # GPBRUSH_WEIGHT.
    "GPBRUSH_PENCIL",  # GPBRUSH_PENCIL.
    "GPBRUSH_PEN",  # GPBRUSH_PEN.
    "GPBRUSH_INK",  # GPBRUSH_INK.
    "GPBRUSH_INKNOISE",  # GPBRUSH_INKNOISE.
    "GPBRUSH_BLOCK",  # GPBRUSH_BLOCK.
    "GPBRUSH_MARKER",  # GPBRUSH_MARKER.
    "GPBRUSH_FILL",  # GPBRUSH_FILL.
    "GPBRUSH_AIRBRUSH",  # GPBRUSH_AIRBRUSH.
    "GPBRUSH_CHISEL",  # GPBRUSH_CHISEL.
    "GPBRUSH_ERASE_SOFT",  # GPBRUSH_ERASE_SOFT.
    "GPBRUSH_ERASE_HARD",  # GPBRUSH_ERASE_HARD.
    "GPBRUSH_ERASE_STROKE",  # GPBRUSH_ERASE_STROKE.
    "BRUSH_CURVES_ADD",  # BRUSH_CURVES_ADD.
    "BRUSH_CURVES_COMB",  # BRUSH_CURVES_COMB.
    "BRUSH_CURVES_CUT",  # BRUSH_CURVES_CUT.
    "BRUSH_CURVES_DELETE",  # BRUSH_CURVES_DELETE.
    "BRUSH_CURVES_DENSITY",  # BRUSH_CURVES_DENSITY.
    "BRUSH_CURVES_GROW_SHRINK",  # BRUSH_CURVES_GROW_SHRINK.
    "BRUSH_CURVES_PINCH",  # BRUSH_CURVES_PINCH.
    "BRUSH_CURVES_PUFF",  # BRUSH_CURVES_PUFF.
    "BRUSH_CURVES_SLIDE",  # BRUSH_CURVES_SLIDE.
    "BRUSH_CURVES_SMOOTH",  # BRUSH_CURVES_SMOOTH.
    "BRUSH_CURVES_SNAKE_HOOK",  # BRUSH_CURVES_SNAKE_HOOK.
    "KEYTYPE_KEYFRAME_VEC",  # KEYTYPE_KEYFRAME_VEC.
    "KEYTYPE_BREAKDOWN_VEC",  # KEYTYPE_BREAKDOWN_VEC.
    "KEYTYPE_EXTREME_VEC",  # KEYTYPE_EXTREME_VEC.
    "KEYTYPE_JITTER_VEC",  # KEYTYPE_JITTER_VEC.
    "KEYTYPE_MOVING_HOLD_VEC",  # KEYTYPE_MOVING_HOLD_VEC.
    "KEYTYPE_GENERATED_VEC",  # KEYTYPE_GENERATED_VEC.
    "HANDLETYPE_FREE_VEC",  # HANDLETYPE_FREE_VEC.
    "HANDLETYPE_ALIGNED_VEC",  # HANDLETYPE_ALIGNED_VEC.
    "HANDLETYPE_VECTOR_VEC",  # HANDLETYPE_VECTOR_VEC.
    "HANDLETYPE_AUTO_VEC",  # HANDLETYPE_AUTO_VEC.
    "HANDLETYPE_AUTO_CLAMP_VEC",  # HANDLETYPE_AUTO_CLAMP_VEC.
    "COLORSET_01_VEC",  # COLORSET_01_VEC.
    "COLORSET_02_VEC",  # COLORSET_02_VEC.
    "COLORSET_03_VEC",  # COLORSET_03_VEC.
    "COLORSET_04_VEC",  # COLORSET_04_VEC.
    "COLORSET_05_VEC",  # COLORSET_05_VEC.
    "COLORSET_06_VEC",  # COLORSET_06_VEC.
    "COLORSET_07_VEC",  # COLORSET_07_VEC.
    "COLORSET_08_VEC",  # COLORSET_08_VEC.
    "COLORSET_09_VEC",  # COLORSET_09_VEC.
    "COLORSET_10_VEC",  # COLORSET_10_VEC.
    "COLORSET_11_VEC",  # COLORSET_11_VEC.
    "COLORSET_12_VEC",  # COLORSET_12_VEC.
    "COLORSET_13_VEC",  # COLORSET_13_VEC.
    "COLORSET_14_VEC",  # COLORSET_14_VEC.
    "COLORSET_15_VEC",  # COLORSET_15_VEC.
    "COLORSET_16_VEC",  # COLORSET_16_VEC.
    "COLORSET_17_VEC",  # COLORSET_17_VEC.
    "COLORSET_18_VEC",  # COLORSET_18_VEC.
    "COLORSET_19_VEC",  # COLORSET_19_VEC.
    "COLORSET_20_VEC",  # COLORSET_20_VEC.
    "COLLECTION_COLOR_01",  # COLLECTION_COLOR_01.
    "COLLECTION_COLOR_02",  # COLLECTION_COLOR_02.
    "COLLECTION_COLOR_03",  # COLLECTION_COLOR_03.
    "COLLECTION_COLOR_04",  # COLLECTION_COLOR_04.
    "COLLECTION_COLOR_05",  # COLLECTION_COLOR_05.
    "COLLECTION_COLOR_06",  # COLLECTION_COLOR_06.
    "COLLECTION_COLOR_07",  # COLLECTION_COLOR_07.
    "COLLECTION_COLOR_08",  # COLLECTION_COLOR_08.
    "SEQUENCE_COLOR_01",  # SEQUENCE_COLOR_01.
    "SEQUENCE_COLOR_02",  # SEQUENCE_COLOR_02.
    "SEQUENCE_COLOR_03",  # SEQUENCE_COLOR_03.
    "SEQUENCE_COLOR_04",  # SEQUENCE_COLOR_04.
    "SEQUENCE_COLOR_05",  # SEQUENCE_COLOR_05.
    "SEQUENCE_COLOR_06",  # SEQUENCE_COLOR_06.
    "SEQUENCE_COLOR_07",  # SEQUENCE_COLOR_07.
    "SEQUENCE_COLOR_08",  # SEQUENCE_COLOR_08.
    "SEQUENCE_COLOR_09",  # SEQUENCE_COLOR_09.
    "LIBRARY_DATA_INDIRECT",  # LIBRARY_DATA_INDIRECT.
    "LIBRARY_DATA_OVERRIDE_NONEDITABLE",  # LIBRARY_DATA_OVERRIDE_NONEDITABLE.
    "EVENT_A",  # EVENT_A.
    "EVENT_B",  # EVENT_B.
    "EVENT_C",  # EVENT_C.
    "EVENT_D",  # EVENT_D.
    "EVENT_E",  # EVENT_E.
    "EVENT_F",  # EVENT_F.
    "EVENT_G",  # EVENT_G.
    "EVENT_H",  # EVENT_H.
    "EVENT_I",  # EVENT_I.
    "EVENT_J",  # EVENT_J.
    "EVENT_K",  # EVENT_K.
    "EVENT_L",  # EVENT_L.
    "EVENT_M",  # EVENT_M.
    "EVENT_N",  # EVENT_N.
    "EVENT_O",  # EVENT_O.
    "EVENT_P",  # EVENT_P.
    "EVENT_Q",  # EVENT_Q.
    "EVENT_R",  # EVENT_R.
    "EVENT_S",  # EVENT_S.
    "EVENT_T",  # EVENT_T.
    "EVENT_U",  # EVENT_U.
    "EVENT_V",  # EVENT_V.
    "EVENT_W",  # EVENT_W.
    "EVENT_X",  # EVENT_X.
    "EVENT_Y",  # EVENT_Y.
    "EVENT_Z",  # EVENT_Z.
    "EVENT_SHIFT",  # EVENT_SHIFT.
    "EVENT_CTRL",  # EVENT_CTRL.
    "EVENT_ALT",  # EVENT_ALT.
    "EVENT_OS",  # EVENT_OS.
    "EVENT_F1",  # EVENT_F1.
    "EVENT_F2",  # EVENT_F2.
    "EVENT_F3",  # EVENT_F3.
    "EVENT_F4",  # EVENT_F4.
    "EVENT_F5",  # EVENT_F5.
    "EVENT_F6",  # EVENT_F6.
    "EVENT_F7",  # EVENT_F7.
    "EVENT_F8",  # EVENT_F8.
    "EVENT_F9",  # EVENT_F9.
    "EVENT_F10",  # EVENT_F10.
    "EVENT_F11",  # EVENT_F11.
    "EVENT_F12",  # EVENT_F12.
    "EVENT_ESC",  # EVENT_ESC.
    "EVENT_TAB",  # EVENT_TAB.
    "EVENT_PAGEUP",  # EVENT_PAGEUP.
    "EVENT_PAGEDOWN",  # EVENT_PAGEDOWN.
    "EVENT_RETURN",  # EVENT_RETURN.
    "EVENT_SPACEKEY",  # EVENT_SPACEKEY.
    "EVENT_ZEROKEY",  # EVENT_ZEROKEY.
    "EVENT_ONEKEY",  # EVENT_ONEKEY.
    "EVENT_TWOKEY",  # EVENT_TWOKEY.
    "EVENT_THREEKEY",  # EVENT_THREEKEY.
    "EVENT_FOURKEY",  # EVENT_FOURKEY.
    "EVENT_FIVEKEY",  # EVENT_FIVEKEY.
    "EVENT_SIXKEY",  # EVENT_SIXKEY.
    "EVENT_SEVENKEY",  # EVENT_SEVENKEY.
    "EVENT_EIGHTKEY",  # EVENT_EIGHTKEY.
    "EVENT_NINEKEY",  # EVENT_NINEKEY.
    "EVENT_PAD0",  # EVENT_PAD0.
    "EVENT_PAD1",  # EVENT_PAD1.
    "EVENT_PAD2",  # EVENT_PAD2.
    "EVENT_PAD3",  # EVENT_PAD3.
    "EVENT_PAD4",  # EVENT_PAD4.
    "EVENT_PAD5",  # EVENT_PAD5.
    "EVENT_PAD6",  # EVENT_PAD6.
    "EVENT_PAD7",  # EVENT_PAD7.
    "EVENT_PAD8",  # EVENT_PAD8.
    "EVENT_PAD9",  # EVENT_PAD9.
    "EVENT_PADASTER",  # EVENT_PADASTER.
    "EVENT_PADSLASH",  # EVENT_PADSLASH.
    "EVENT_PADMINUS",  # EVENT_PADMINUS.
    "EVENT_PADENTER",  # EVENT_PADENTER.
    "EVENT_PADPLUS",  # EVENT_PADPLUS.
    "EVENT_PADPERIOD",  # EVENT_PADPERIOD.
    "EVENT_MOUSE_4",  # EVENT_MOUSE_4.
    "EVENT_MOUSE_5",  # EVENT_MOUSE_5.
    "EVENT_MOUSE_6",  # EVENT_MOUSE_6.
    "EVENT_MOUSE_7",  # EVENT_MOUSE_7.
    "EVENT_TABLET_STYLUS",  # EVENT_TABLET_STYLUS.
    "EVENT_TABLET_ERASER",  # EVENT_TABLET_ERASER.
    "EVENT_LEFT_ARROW",  # EVENT_LEFT_ARROW.
    "EVENT_DOWN_ARROW",  # EVENT_DOWN_ARROW.
    "EVENT_RIGHT_ARROW",  # EVENT_RIGHT_ARROW.
    "EVENT_UP_ARROW",  # EVENT_UP_ARROW.
    "EVENT_PAUSE",  # EVENT_PAUSE.
    "EVENT_INSERT",  # EVENT_INSERT.
    "EVENT_HOME",  # EVENT_HOME.
    "EVENT_END",  # EVENT_END.
    "EVENT_UNKNOWN",  # EVENT_UNKNOWN.
    "EVENT_GRLESS",  # EVENT_GRLESS.
    "EVENT_MEDIAPLAY",  # EVENT_MEDIAPLAY.
    "EVENT_MEDIASTOP",  # EVENT_MEDIASTOP.
    "EVENT_MEDIAFIRST",  # EVENT_MEDIAFIRST.
    "EVENT_MEDIALAST",  # EVENT_MEDIALAST.
    "EVENT_APP",  # EVENT_APP.
    "EVENT_CAPSLOCK",  # EVENT_CAPSLOCK.
    "EVENT_BACKSPACE",  # EVENT_BACKSPACE.
    "EVENT_DEL",  # EVENT_DEL.
    "EVENT_SEMICOLON",  # EVENT_SEMICOLON.
    "EVENT_PERIOD",  # EVENT_PERIOD.
    "EVENT_COMMA",  # EVENT_COMMA.
    "EVENT_QUOTE",  # EVENT_QUOTE.
    "EVENT_ACCENTGRAVE",  # EVENT_ACCENTGRAVE.
    "EVENT_MINUS",  # EVENT_MINUS.
    "EVENT_PLUS",  # EVENT_PLUS.
    "EVENT_SLASH",  # EVENT_SLASH.
    "EVENT_BACKSLASH",  # EVENT_BACKSLASH.
    "EVENT_EQUAL",  # EVENT_EQUAL.
    "EVENT_LEFTBRACKET",  # EVENT_LEFTBRACKET.
    "EVENT_RIGHTBRACKET",  # EVENT_RIGHTBRACKET.
    "EVENT_F13",  # EVENT_F13.
    "EVENT_F14",  # EVENT_F14.
    "EVENT_F15",  # EVENT_F15.
    "EVENT_F16",  # EVENT_F16.
    "EVENT_F17",  # EVENT_F17.
    "EVENT_F18",  # EVENT_F18.
    "EVENT_F19",  # EVENT_F19.
    "EVENT_F20",  # EVENT_F20.
    "EVENT_F21",  # EVENT_F21.
    "EVENT_F22",  # EVENT_F22.
    "EVENT_F23",  # EVENT_F23.
    "EVENT_F24",  # EVENT_F24.
    "EVENT_NDOF_BUTTON_V1",  # EVENT_NDOF_BUTTON_V1.
    "EVENT_NDOF_BUTTON_V2",  # EVENT_NDOF_BUTTON_V2.
    "EVENT_NDOF_BUTTON_V3",  # EVENT_NDOF_BUTTON_V3.
    "EVENT_NDOF_BUTTON_1",  # EVENT_NDOF_BUTTON_1.
    "EVENT_NDOF_BUTTON_2",  # EVENT_NDOF_BUTTON_2.
    "EVENT_NDOF_BUTTON_3",  # EVENT_NDOF_BUTTON_3.
    "EVENT_NDOF_BUTTON_4",  # EVENT_NDOF_BUTTON_4.
    "EVENT_NDOF_BUTTON_5",  # EVENT_NDOF_BUTTON_5.
    "EVENT_NDOF_BUTTON_6",  # EVENT_NDOF_BUTTON_6.
    "EVENT_NDOF_BUTTON_7",  # EVENT_NDOF_BUTTON_7.
    "EVENT_NDOF_BUTTON_8",  # EVENT_NDOF_BUTTON_8.
    "EVENT_NDOF_BUTTON_9",  # EVENT_NDOF_BUTTON_9.
    "EVENT_NDOF_BUTTON_10",  # EVENT_NDOF_BUTTON_10.
    "EVENT_NDOF_BUTTON_A",  # EVENT_NDOF_BUTTON_A.
    "EVENT_NDOF_BUTTON_B",  # EVENT_NDOF_BUTTON_B.
    "EVENT_NDOF_BUTTON_C",  # EVENT_NDOF_BUTTON_C.
    "EVENT_NDOF_BUTTON_MENU",  # EVENT_NDOF_BUTTON_MENU.
    "EVENT_NDOF_BUTTON_FIT",  # EVENT_NDOF_BUTTON_FIT.
    "EVENT_NDOF_BUTTON_TOP",  # EVENT_NDOF_BUTTON_TOP.
    "EVENT_NDOF_BUTTON_BOTTOM",  # EVENT_NDOF_BUTTON_BOTTOM.
    "EVENT_NDOF_BUTTON_LEFT",  # EVENT_NDOF_BUTTON_LEFT.
    "EVENT_NDOF_BUTTON_RIGHT",  # EVENT_NDOF_BUTTON_RIGHT.
    "EVENT_NDOF_BUTTON_FRONT",  # EVENT_NDOF_BUTTON_FRONT.
    "EVENT_NDOF_BUTTON_BACK",  # EVENT_NDOF_BUTTON_BACK.
    "EVENT_NDOF_BUTTON_ISO1",  # EVENT_NDOF_BUTTON_ISO1.
    "EVENT_NDOF_BUTTON_ISO2",  # EVENT_NDOF_BUTTON_ISO2.
    "EVENT_NDOF_BUTTON_ROLL_CW",  # EVENT_NDOF_BUTTON_ROLL_CW.
    "EVENT_NDOF_BUTTON_ROLL_CCW",  # EVENT_NDOF_BUTTON_ROLL_CCW.
    "EVENT_NDOF_BUTTON_SPIN_CW",  # EVENT_NDOF_BUTTON_SPIN_CW.
    "EVENT_NDOF_BUTTON_SPIN_CCW",  # EVENT_NDOF_BUTTON_SPIN_CCW.
    "EVENT_NDOF_BUTTON_TILT_CW",  # EVENT_NDOF_BUTTON_TILT_CW.
    "EVENT_NDOF_BUTTON_TILT_CCW",  # EVENT_NDOF_BUTTON_TILT_CCW.
    "EVENT_NDOF_BUTTON_ROTATE",  # EVENT_NDOF_BUTTON_ROTATE.
    "EVENT_NDOF_BUTTON_PANZOOM",  # EVENT_NDOF_BUTTON_PANZOOM.
    "EVENT_NDOF_BUTTON_DOMINANT",  # EVENT_NDOF_BUTTON_DOMINANT.
    "EVENT_NDOF_BUTTON_PLUS",  # EVENT_NDOF_BUTTON_PLUS.
    "EVENT_NDOF_BUTTON_MINUS",  # EVENT_NDOF_BUTTON_MINUS.
]
type IdTypeItems = typing.Literal[
    "ACTION",  # Action.
    "ARMATURE",  # Armature.
    "BRUSH",  # Brush.
    "CACHEFILE",  # Cache File.
    "CAMERA",  # Camera.
    "COLLECTION",  # Collection.
    "CURVE",  # Curve.
    "CURVES",  # Curves.
    "FONT",  # Font.
    "GREASEPENCIL",  # Grease Pencil.
    "GREASEPENCIL_V3",  # Grease Pencil v3.
    "IMAGE",  # Image.
    "KEY",  # Key.
    "LATTICE",  # Lattice.
    "LIBRARY",  # Library.
    "LIGHT",  # Light.
    "LIGHT_PROBE",  # Light Probe.
    "LINESTYLE",  # Line Style.
    "MASK",  # Mask.
    "MATERIAL",  # Material.
    "MESH",  # Mesh.
    "META",  # Metaball.
    "MOVIECLIP",  # Movie Clip.
    "NODETREE",  # Node Tree.
    "OBJECT",  # Object.
    "PAINTCURVE",  # Paint Curve.
    "PALETTE",  # Palette.
    "PARTICLE",  # Particle.
    "POINTCLOUD",  # Point Cloud.
    "SCENE",  # Scene.
    "SCREEN",  # Screen.
    "SOUND",  # Sound.
    "SPEAKER",  # Speaker.
    "TEXT",  # Text.
    "TEXTURE",  # Texture.
    "VOLUME",  # Volume.
    "WINDOWMANAGER",  # Window Manager.
    "WORKSPACE",  # Workspace.
    "WORLD",  # World.
]
type ImageColorDepthItems = typing.Literal[
    "8",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "8" (ordinal 8)8-bit color channels.
    "10",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "10" (ordinal 10)10-bit color channels.
    "12",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "12" (ordinal 12)12-bit color channels.
    "16",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "16" (ordinal 16)16-bit color channels.
    "32",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "32" (ordinal 32)32-bit color channels.
]
type ImageColorModeItems = typing.Literal[
    "BW",  # BW.Images get saved in 8-bit grayscale (only PNG, JPEG, TGA, TIF).
    "RGB",  # RGB.Images are saved with RGB (color) data.
    "RGBA",  # RGBA.Images are saved with RGB and Alpha data (if supported).
]
type ImageGeneratedTypeItems = typing.Literal[
    "BLANK",  # Blank.Generate a blank image.
    "UV_GRID",  # UV Grid.Generated grid to test UV mappings.
    "COLOR_GRID",  # Color Grid.Generated improved UV grid to test UV mappings.
]
type ImageTypeItems = typing.Literal[
    "BMP",  # BMP.Output image in bitmap format.
    "IRIS",  # Iris.Output image in SGI IRIS format.
    "PNG",  # PNG.Output image in PNG format.
    "JPEG",  # JPEG.Output image in JPEG format.
    "JPEG2000",  # JPEG 2000.Output image in JPEG 2000 format.
    "TARGA",  # Targa.Output image in Targa format.
    "TARGA_RAW",  # Targa Raw.Output image in uncompressed Targa format.
    "CINEON",  # Cineon.Output image in Cineon format.
    "DPX",  # DPX.Output image in DPX format.
    "OPEN_EXR_MULTILAYER",  # OpenEXR MultiLayer.Output image in multilayer OpenEXR format.
    "OPEN_EXR",  # OpenEXR.Output image in OpenEXR format.
    "HDR",  # Radiance HDR.Output image in Radiance HDR format.
    "TIFF",  # TIFF.Output image in TIFF format.
    "WEBP",  # WebP.Output image in WebP format.
    "FFMPEG",  # FFmpeg Video.
]
type KeyblockTypeItems = typing.Literal[
    "KEY_LINEAR",  # Linear.
    "KEY_CARDINAL",  # Cardinal.
    "KEY_CATMULL_ROM",  # Catmull-Rom.
    "KEY_BSPLINE",  # BSpline.
]
type KeyframeHandleTypeItems = typing.Literal[
    "FREE",  # Free.Completely independent manually set handle.
    "ALIGNED",  # Aligned.Manually set handle with rotation locked together with its pair.
    "VECTOR",  # Vector.Automatic handles that create straight lines.
    "AUTO",  # Automatic.Automatic handles that create smooth curves.
    "AUTO_CLAMPED",  # Auto Clamped.Automatic handles that create smooth curves which only change direction at keyframes.
]
type KeyframePasteMergeItems = typing.Literal[
    "MIX",  # Mix.Overlay existing with new keys.
    "OVER_ALL",  # Overwrite All.Replace all keys.
    "OVER_RANGE",  # Overwrite Range.Overwrite keys in pasted range.
    "OVER_RANGE_ALL",  # Overwrite Entire Range.Overwrite keys in pasted range, using the range of all copied keys.
]
type KeyframePasteOffsetItems = typing.Literal[
    "START",  # Frame Start.Paste keys starting at current frame.
    "END",  # Frame End.Paste keys ending at current frame.
    "RELATIVE",  # Frame Relative.Paste keys relative to the current frame when copying.
    "NONE",  # No Offset.Paste keys from original time.
]
type KeyframePasteOffsetValueItems = typing.Literal[
    "LEFT_KEY",  # Left Key.Paste keys with the first key matching the key left of the cursor.
    "RIGHT_KEY",  # Right Key.Paste keys with the last key matching the key right of the cursor.
    "CURRENT_FRAME",  # Current Frame Value.Paste keys relative to the value of the curve under the cursor.
    "CURSOR_VALUE",  # Cursor Value.Paste keys relative to the Y-Position of the cursor.
    "NONE",  # No Offset.Paste keys with the same value as they were copied.
]
type KeyingFlagApiItems = typing.Literal[
    "INSERTKEY_NEEDED",  # Only Needed.Only insert keyframes where they're needed in the relevant F-Curves.
    "INSERTKEY_VISUAL",  # Visual Keying.Insert keyframes based on 'visual transforms'.
    "INSERTKEY_XYZ_TO_RGB",  # XYZ=RGB Colors (ignored).This flag is no longer in use, and is here so that code that uses it doesn't break. The XYZ=RGB coloring is determined by the animation preferences.
    "INSERTKEY_REPLACE",  # Replace Existing.Only replace existing keyframes.
    "INSERTKEY_AVAILABLE",  # Only Available.Don't create F-Curves when they don't already exist.
    "INSERTKEY_CYCLE_AWARE",  # Cycle Aware Keying.When inserting into a curve with cyclic extrapolation, remap the keyframe inside the cycle time range, and if changing an end key, also update the other one.
]
type KeyingFlagItems = typing.Literal[
    "INSERTKEY_NEEDED",  # Only Needed.Only insert keyframes where they're needed in the relevant F-Curves.
    "INSERTKEY_VISUAL",  # Visual Keying.Insert keyframes based on 'visual transforms'.
    "INSERTKEY_XYZ_TO_RGB",  # XYZ=RGB Colors (ignored).This flag is no longer in use, and is here so that code that uses it doesn't break. The XYZ=RGB coloring is determined by the animation preferences.
]
type KeyingsetPathGroupingItems = typing.Literal[
    "NAMED",  # Named Group.
    "NONE",  # None.
    "KEYINGSET",  # Keying Set Name.
]
type KeymapPropvalueItems = typing.Literal["NONE",]
type LightTypeItems = typing.Literal[
    "POINT",  # Point.Omnidirectional point light source.
    "SUN",  # Sun.Constant direction parallel ray light source.
    "SPOT",  # Spot.Directional cone light source.
    "AREA",  # Area.Directional area light source.
]
type LightprobesTypeItems = typing.Literal[
    "SPHERE",  # Sphere.
    "PLANE",  # Plane.
    "VOLUME",  # Volume.
]
type LinestyleAlphaModifierTypeItems = typing.Literal[
    "ALONG_STROKE",  # Along Stroke.
    "CREASE_ANGLE",  # Crease Angle.
    "CURVATURE_3D",  # Curvature 3D.
    "DISTANCE_FROM_CAMERA",  # Distance from Camera.
    "DISTANCE_FROM_OBJECT",  # Distance from Object.
    "MATERIAL",  # Material.
    "NOISE",  # Noise.
    "TANGENT",  # Tangent.
]
type LinestyleColorModifierTypeItems = typing.Literal[
    "ALONG_STROKE",  # Along Stroke.
    "CREASE_ANGLE",  # Crease Angle.
    "CURVATURE_3D",  # Curvature 3D.
    "DISTANCE_FROM_CAMERA",  # Distance from Camera.
    "DISTANCE_FROM_OBJECT",  # Distance from Object.
    "MATERIAL",  # Material.
    "NOISE",  # Noise.
    "TANGENT",  # Tangent.
]
type LinestyleGeometryModifierTypeItems = typing.Literal[
    "2D_OFFSET",  # 2D Offset.
    "2D_TRANSFORM",  # 2D Transform.
    "BACKBONE_STRETCHER",  # Backbone Stretcher.
    "BEZIER_CURVE",  # Bézier Curve.
    "BLUEPRINT",  # Blueprint.
    "GUIDING_LINES",  # Guiding Lines.
    "PERLIN_NOISE_1D",  # Perlin Noise 1D.
    "PERLIN_NOISE_2D",  # Perlin Noise 2D.
    "POLYGONIZATION",  # Polygonization.
    "SAMPLING",  # Sampling.
    "SIMPLIFICATION",  # Simplification.
    "SINUS_DISPLACEMENT",  # Sinus Displacement.
    "SPATIAL_NOISE",  # Spatial Noise.
    "TIP_REMOVER",  # Tip Remover.
]
type LinestyleThicknessModifierTypeItems = typing.Literal[
    "ALONG_STROKE",  # Along Stroke.
    "CALLIGRAPHY",  # Calligraphy.
    "CREASE_ANGLE",  # Crease Angle.
    "CURVATURE_3D",  # Curvature 3D.
    "DISTANCE_FROM_CAMERA",  # Distance from Camera.
    "DISTANCE_FROM_OBJECT",  # Distance from Object.
    "MATERIAL",  # Material.
    "NOISE",  # Noise.
    "TANGENT",  # Tangent.
]
type MappingTypeItems = typing.Literal[
    "POINT",  # Point.Transform a point.
    "TEXTURE",  # Texture.Transform a texture by inverse mapping the texture coordinate.
    "VECTOR",  # Vector.Transform a direction vector. Location is ignored.
    "NORMAL",  # Normal.Transform a unit normal vector. Location is ignored.
]
type MeshDelimitModeItems = typing.Literal[
    "NORMAL",  # Normal.Delimit by face directions.
    "MATERIAL",  # Material.Delimit by face material.
    "SEAM",  # Seam.Delimit by edge seams.
    "SHARP",  # Sharp.Delimit by sharp edges.
    "UV",  # UVs.Delimit by UV coordinates.
]
type MeshSelectModeItems = typing.Literal[
    "VERT",  # Vertex.Vertex selection mode.
    "EDGE",  # Edge.Edge selection mode.
    "FACE",  # Face.Face selection mode.
]
type MeshSelectModeUvItems = typing.Literal[
    "VERTEX",  # Vertex.Vertex selection mode.
    "EDGE",  # Edge.Edge selection mode.
    "FACE",  # Face.Face selection mode.
    "ISLAND",  # Island.Island selection mode.
]
type MetaelemTypeItems = typing.Literal[
    "BALL",  # Ball.
    "CAPSULE",  # Capsule.
    "PLANE",  # Plane.
    "ELLIPSOID",  # Ellipsoid.
    "CUBE",  # Cube.
]
type ModifierShrinkwrapModeItems = typing.Literal[
    "ON_SURFACE",  # On Surface.The point is constrained to the surface of the target object, with distance offset towards the original point location.
    "INSIDE",  # Inside.The point is constrained to be inside the target object.
    "OUTSIDE",  # Outside.The point is constrained to be outside the target object.
    "OUTSIDE_SURFACE",  # Outside Surface.The point is constrained to the surface of the target object, with distance offset always to the outside, towards or away from the original location.
    "ABOVE_SURFACE",  # Above Surface.The point is constrained to the surface of the target object, with distance offset applied exactly along the target normal.
]
type ModifierTriangulateNgonMethodItems = typing.Literal[
    "BEAUTY",  # Beauty.Arrange the new triangles evenly (slow).
    "CLIP",  # Clip.Split the polygons with an ear clipping algorithm.
]
type ModifierTriangulateQuadMethodItems = typing.Literal[
    "BEAUTY",  # Beauty.Split the quads in nice triangles, slower method.
    "FIXED",  # Fixed.Split the quads on the first and third vertices.
    "FIXED_ALTERNATE",  # Fixed Alternate.Split the quads on the 2nd and 4th vertices.
    "SHORTEST_DIAGONAL",  # Shortest Diagonal.Split the quads along their shortest diagonal.
    "LONGEST_DIAGONAL",  # Longest Diagonal.Split the quads along their longest diagonal.
]
type MotionpathBakeLocationItems = typing.Literal[
    "HEADS",  # Heads.Calculate bone paths from heads.
    "TAILS",  # Tails.Calculate bone paths from tails.
]
type MotionpathDisplayTypeItems = typing.Literal[
    "CURRENT_FRAME",  # Around Frame.Display Paths of poses within a fixed number of frames around the current frame.
    "RANGE",  # In Range.Display Paths of poses within specified range.
]
type MotionpathRangeItems = typing.Literal[
    "KEYS_ALL",  # All Keys.From the first keyframe to the last.
    "KEYS_SELECTED",  # Selected Keys.From the first selected keyframe to the last.
    "SCENE",  # Scene Frame Range.The entire Scene / Preview range.
    "MANUAL",  # Manual Range.Manually determined frame range.
]
type NavigationModeItems = typing.Literal[
    "WALK",  # Walk.Interactively walk or free navigate around the scene.
    "FLY",  # Fly.Use fly dynamics to navigate the scene.
]
type NlaModeBlendItems = typing.Literal[
    "REPLACE",  # Replace.The strip values replace the accumulated results by amount specified by influence.
    "COMBINE",  # Combine.The strip values are combined with accumulated results by appropriately using addition, multiplication, or quaternion math, based on channel type.
    "ADD",  # Add.Weighted result of strip is added to the accumulated results.
    "SUBTRACT",  # Subtract.Weighted result of strip is removed from the accumulated results.
    "MULTIPLY",  # Multiply.Weighted result of strip is multiplied with the accumulated results.
]
type NlaModeExtendItems = typing.Literal[
    "NOTHING",  # Nothing.Strip has no influence past its extents.
    "HOLD",  # Hold.Hold the first frame if no previous strips in track, and always hold last frame.
    "HOLD_FORWARD",  # Hold Forward.Only hold last frame.
]
type NodeBooleanMathItems = typing.Literal[
    "AND",  # And.True when both inputs are true.
    "OR",  # Or.True when at least one input is true.
    "NOT",  # Not.Opposite of the input.
    "NAND",  # Not And.True when at least one input is false.
    "NOR",  # Nor.True when both inputs are false.
    "XNOR",  # Equal.True when both inputs are equal (exclusive nor).
    "XOR",  # Not Equal.True when both inputs are different (exclusive or).
    "IMPLY",  # Imply.True unless the first input is true and the second is false.
    "NIMPLY",  # Subtract.True when the first input is true and the second is false (not imply).
]
type NodeClampItems = typing.Literal[
    "MINMAX",  # Min Max.Constrain value between min and max.
    "RANGE",  # Range.Constrain value between min and max, swapping arguments when min > max.
]
type NodeCombsepColorItems = typing.Literal[
    "RGB",  # RGB.Use RGB color processing.
    "HSV",  # HSV.Use HSV color processing.
    "HSL",  # HSL.Use HSL color processing.
]
type NodeCompareOperationItems = typing.Literal[
    "LESS_THAN",  # Less Than.True when the first input is smaller than second input.
    "LESS_EQUAL",  # Less Than or Equal.True when the first input is smaller than the second input or equal.
    "GREATER_THAN",  # Greater Than.True when the first input is greater than the second input.
    "GREATER_EQUAL",  # Greater Than or Equal.True when the first input is greater than the second input or equal.
    "EQUAL",  # Equal.True when both inputs are approximately equal.
    "NOT_EQUAL",  # Not Equal.True when both inputs are not approximately equal.
    "BRIGHTER",  # Brighter.True when the first input is brighter.
    "DARKER",  # Darker.True when the first input is darker.
]
type NodeFilterItems = typing.Literal[
    "SOFTEN",  # Soften.
    "SHARPEN",  # Box Sharpen.An aggressive sharpening filter.
    "SHARPEN_DIAMOND",  # Diamond Sharpen.A moderate sharpening filter.
    "LAPLACE",  # Laplace.
    "SOBEL",  # Sobel.
    "PREWITT",  # Prewitt.
    "KIRSCH",  # Kirsch.
    "SHADOW",  # Shadow.
]
type NodeFloatCompareItems = typing.Literal[
    "LESS_THAN",  # Less Than.True when the first input is smaller than second input.
    "LESS_EQUAL",  # Less Than or Equal.True when the first input is smaller than the second input or equal.
    "GREATER_THAN",  # Greater Than.True when the first input is greater than the second input.
    "GREATER_EQUAL",  # Greater Than or Equal.True when the first input is greater than the second input or equal.
    "EQUAL",  # Equal.True when both inputs are approximately equal.
    "NOT_EQUAL",  # Not Equal.True when both inputs are not approximately equal.
]
type NodeFloatToIntItems = typing.Literal[
    "ROUND",  # Round.Round the float up or down to the nearest integer.
    "FLOOR",  # Floor.Round the float down to the next smallest integer.
    "CEILING",  # Ceiling.Round the float up to the next largest integer.
    "TRUNCATE",  # Truncate.Round the float to the closest integer in the direction of zero (floor if positive; ceiling if negative).
]
type NodeGeometryCurveHandleSideItems = typing.Literal[
    "LEFT",  # Left.Use the left handles.
    "RIGHT",  # Right.Use the right handles.
]
type NodeGeometryMeshCircleFillTypeItems = typing.Literal[
    "NONE",  # None.
    "NGON",  # N-Gon.
    "TRIANGLE_FAN",  # Triangles.
]
type NodeMapRangeItems = typing.Literal[
    "LINEAR",  # Linear.Linear interpolation between From Min and From Max values.
    "STEPPED",  # Stepped Linear.Stepped linear interpolation between From Min and From Max values.
    "SMOOTHSTEP",  # Smooth Step.Smooth Hermite edge interpolation between From Min and From Max values.
    "SMOOTHERSTEP",  # Smoother Step.Smoother Hermite edge interpolation between From Min and From Max values.
]
type NodeMathItems = typing.Literal[
    "ADD",  # Add.A + B.
    "SUBTRACT",  # Subtract.A - B.
    "MULTIPLY",  # Multiply.A * B.
    "DIVIDE",  # Divide.A / B.
    "MULTIPLY_ADD",  # Multiply Add.A * B + C.
    "POWER",  # Power.A power B.
    "LOGARITHM",  # Logarithm.Logarithm A base B.
    "SQRT",  # Square Root.Square root of A.
    "INVERSE_SQRT",  # Inverse Square Root.1 / Square root of A.
    "ABSOLUTE",  # Absolute.Magnitude of A.
    "EXPONENT",  # Exponent.exp(A).
    "MINIMUM",  # Minimum.The minimum from A and B.
    "MAXIMUM",  # Maximum.The maximum from A and B.
    "LESS_THAN",  # Less Than.1 if A < B else 0.
    "GREATER_THAN",  # Greater Than.1 if A > B else 0.
    "SIGN",  # Sign.Returns the sign of A.
    "COMPARE",  # Compare.1 if (A == B) within tolerance C else 0.
    "SMOOTH_MIN",  # Smooth Minimum.The minimum from A and B with smoothing C.
    "SMOOTH_MAX",  # Smooth Maximum.The maximum from A and B with smoothing C.
    "ROUND",  # Round.Round A to the nearest integer. Round upward if the fraction part is 0.5.
    "FLOOR",  # Floor.The largest integer smaller than or equal A.
    "CEIL",  # Ceil.The smallest integer greater than or equal A.
    "TRUNC",  # Truncate.The integer part of A, removing fractional digits.
    "FRACT",  # Fraction.The fraction part of A.
    "MODULO",  # Truncated Modulo.The remainder of truncated division using fmod(A,B).
    "FLOORED_MODULO",  # Floored Modulo.The remainder of floored division.
    "WRAP",  # Wrap.Wrap value to range, wrap(A,B).
    "SNAP",  # Snap.Snap to increment, snap(A,B).
    "PINGPONG",  # Ping-Pong.Wraps a value and reverses every other cycle (A,B).
    "SINE",  # Sine.sin(A).
    "COSINE",  # Cosine.cos(A).
    "TANGENT",  # Tangent.tan(A).
    "ARCSINE",  # Arcsine.arcsin(A).
    "ARCCOSINE",  # Arccosine.arccos(A).
    "ARCTANGENT",  # Arctangent.arctan(A).
    "ARCTAN2",  # Arctan2.The signed angle arctan(A / B).
    "SINH",  # Hyperbolic Sine.sinh(A).
    "COSH",  # Hyperbolic Cosine.cosh(A).
    "TANH",  # Hyperbolic Tangent.tanh(A).
    "RADIANS",  # To Radians.Convert from degrees to radians.
    "DEGREES",  # To Degrees.Convert from radians to degrees.
]
type NodeSocketDataTypeItems = typing.Literal[
    "FLOAT",  # Float.
    "INT",  # Integer.
    "BOOLEAN",  # Boolean.
    "VECTOR",  # Vector.
    "ROTATION",  # Rotation.
    "MATRIX",  # Matrix.
    "STRING",  # String.
    "MENU",  # Menu.
    "RGBA",  # Color.
    "OBJECT",  # Object.
    "IMAGE",  # Image.
    "GEOMETRY",  # Geometry.
    "COLLECTION",  # Collection.
    "TEXTURE",  # Texture.
    "MATERIAL",  # Material.
]
type NodeSocketInOutItems = typing.Literal[
    "IN",  # Input.
    "OUT",  # Output.
]
type NodeSocketTypeItems = typing.Literal[
    "CUSTOM",  # Custom.
    "VALUE",  # Value.
    "INT",  # Integer.
    "BOOLEAN",  # Boolean.
    "VECTOR",  # Vector.
    "ROTATION",  # Rotation.
    "MATRIX",  # Matrix.
    "STRING",  # String.
    "RGBA",  # RGBA.
    "SHADER",  # Shader.
    "OBJECT",  # Object.
    "IMAGE",  # Image.
    "GEOMETRY",  # Geometry.
    "COLLECTION",  # Collection.
    "TEXTURE",  # Texture.
    "MATERIAL",  # Material.
    "MENU",  # Menu.
]
type NodeTreeInterfaceItemTypeItems = typing.Literal[
    "SOCKET",  # Socket.
    "PANEL",  # Panel.
]
type NodeVecMathItems = typing.Literal[
    "ADD",  # Add.A + B.
    "SUBTRACT",  # Subtract.A - B.
    "MULTIPLY",  # Multiply.Entry-wise multiply.
    "DIVIDE",  # Divide.Entry-wise divide.
    "MULTIPLY_ADD",  # Multiply Add.A * B + C.
    "CROSS_PRODUCT",  # Cross Product.A cross B.
    "PROJECT",  # Project.Project A onto B.
    "REFLECT",  # Reflect.Reflect A around the normal B. B doesn't need to be normalized.
    "REFRACT",  # Refract.For a given incident vector A, surface normal B and ratio of indices of refraction, Ior, refract returns the refraction vector, R.
    "FACEFORWARD",  # Faceforward.Orients a vector A to point away from a surface B as defined by its normal C. Returns (dot(B, C) < 0) ? A : -A.
    "DOT_PRODUCT",  # Dot Product.A dot B.
    "DISTANCE",  # Distance.Distance between A and B.
    "LENGTH",  # Length.Length of A.
    "SCALE",  # Scale.A multiplied by Scale.
    "NORMALIZE",  # Normalize.Normalize A.
    "ABSOLUTE",  # Absolute.Entry-wise absolute.
    "MINIMUM",  # Minimum.Entry-wise minimum.
    "MAXIMUM",  # Maximum.Entry-wise maximum.
    "FLOOR",  # Floor.Entry-wise floor.
    "CEIL",  # Ceil.Entry-wise ceil.
    "FRACTION",  # Fraction.The fraction part of A entry-wise.
    "MODULO",  # Modulo.Entry-wise modulo using fmod(A,B).
    "WRAP",  # Wrap.Entry-wise wrap(A,B).
    "SNAP",  # Snap.Round A to the largest integer multiple of B less than or equal A.
    "SINE",  # Sine.Entry-wise sin(A).
    "COSINE",  # Cosine.Entry-wise cos(A).
    "TANGENT",  # Tangent.Entry-wise tan(A).
]
type NormalSpaceItems = typing.Literal[
    "OBJECT",  # Object.Bake the normals in object space.
    "TANGENT",  # Tangent.Bake the normals in tangent space.
]
type NormalSwizzleItems = typing.Literal[
    "POS_X",  # +X.
    "POS_Y",  # +Y.
    "POS_Z",  # +Z.
    "NEG_X",  # -X.
    "NEG_Y",  # -Y.
    "NEG_Z",  # -Z.
]
type ObjectAxisItems = typing.Literal[
    "POS_X",  # +X.
    "POS_Y",  # +Y.
    "POS_Z",  # +Z.
    "NEG_X",  # -X.
    "NEG_Y",  # -Y.
    "NEG_Z",  # -Z.
]
type ObjectEmptyDrawtypeItems = typing.Literal[
    "PLAIN_AXES",  # Plain Axes.
    "ARROWS",  # Arrows.
    "SINGLE_ARROW",  # Single Arrow.
    "CIRCLE",  # Circle.
    "CUBE",  # Cube.
    "SPHERE",  # Sphere.
    "CONE",  # Cone.
    "IMAGE",  # Image.
]
type ObjectGpencilTypeItems = typing.Literal[
    "EMPTY",  # Blank.Create an empty grease pencil object.
    "STROKE",  # Stroke.Create a simple stroke with basic colors.
    "MONKEY",  # Monkey.Construct a Suzanne grease pencil object.
    "LINEART_SCENE",  # Scene Line Art.Quickly set up Line Art for the entire scene.
    "LINEART_COLLECTION",  # Collection Line Art.Quickly set up Line Art for the active collection.
    "LINEART_OBJECT",  # Object Line Art.Quickly set up Line Art for the active object.
]
type ObjectGreasepencilModifierTypeItems = typing.Literal[
    "GP_TEXTURE",  # Texture Mapping.Change stroke UV texture values.
    "GP_TIME",  # Time Offset.Offset keyframes.
    "GP_WEIGHT_ANGLE",  # Vertex Weight Angle.Generate vertex weights based on stroke angle.
    "GP_WEIGHT_PROXIMITY",  # Vertex Weight Proximity.Generate vertex weights based on distance to object.
    "GP_ARRAY",  # Array.Create array of duplicate instances.
    "GP_BUILD",  # Build.Create duplication of strokes.
    "GP_DASH",  # Dot Dash.Generate dot-dash styled strokes.
    "GP_ENVELOPE",  # Envelope.Create an envelope shape.
    "GP_LENGTH",  # Length.Extend or shrink strokes.
    "GP_LINEART",  # Line Art.Generate Line Art strokes from selected source.
    "GP_MIRROR",  # Mirror.Duplicate strokes like a mirror.
    "GP_MULTIPLY",  # Multiple Strokes.Produce multiple strokes along one stroke.
    "GP_OUTLINE",  # Outline.Convert stroke to perimeter.
    "GP_SIMPLIFY",  # Simplify.Simplify stroke reducing number of points.
    "GP_SUBDIV",  # Subdivide.Subdivide stroke adding more control points.
    "GP_ARMATURE",  # Armature.Deform stroke points using armature object.
    "GP_HOOK",  # Hook.Deform stroke points using objects.
    "GP_LATTICE",  # Lattice.Deform strokes using lattice.
    "GP_NOISE",  # Noise.Add noise to strokes.
    "GP_OFFSET",  # Offset.Change stroke location, rotation or scale.
    "SHRINKWRAP",  # Shrinkwrap.Project the shape onto another object.
    "GP_SMOOTH",  # Smooth.Smooth stroke.
    "GP_THICK",  # Thickness.Change stroke thickness.
    "GP_COLOR",  # Hue/Saturation.Apply changes to stroke colors.
    "GP_OPACITY",  # Opacity.Opacity of the strokes.
    "GP_TINT",  # Tint.Tint strokes with new color.
]
type ObjectModeItems = typing.Literal[
    "OBJECT",  # Object Mode.
    "EDIT",  # Edit Mode.
    "POSE",  # Pose Mode.
    "SCULPT",  # Sculpt Mode.
    "VERTEX_PAINT",  # Vertex Paint.
    "WEIGHT_PAINT",  # Weight Paint.
    "TEXTURE_PAINT",  # Texture Paint.
    "PARTICLE_EDIT",  # Particle Edit.
    "EDIT_GPENCIL",  # Edit Mode.Edit Grease Pencil Strokes.
    "SCULPT_GPENCIL",  # Sculpt Mode.Sculpt Grease Pencil Strokes.
    "PAINT_GPENCIL",  # Draw Mode.Paint Grease Pencil Strokes.
    "WEIGHT_GPENCIL",  # Weight Paint.Grease Pencil Weight Paint Strokes.
    "VERTEX_GPENCIL",  # Vertex Paint.Grease Pencil Vertex Paint Strokes.
    "SCULPT_CURVES",  # Sculpt Mode.
]
type ObjectModifierTypeItems = typing.Literal[
    "GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY",  # Vertex Weight Proximity.Generate vertex weights based on distance to object.
    "DATA_TRANSFER",  # Data Transfer.Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another.
    "MESH_CACHE",  # Mesh Cache.Deform the mesh using an external frame-by-frame vertex transform cache.
    "MESH_SEQUENCE_CACHE",  # Mesh Sequence Cache.Deform the mesh or curve using an external mesh cache in Alembic format.
    "NORMAL_EDIT",  # Normal Edit.Modify the direction of the surface normals.
    "WEIGHTED_NORMAL",  # Weighted Normal.Modify the direction of the surface normals using a weighting method.
    "UV_PROJECT",  # UV Project.Project the UV map coordinates from the negative Z axis of another object.
    "UV_WARP",  # UV Warp.Transform the UV map using the difference between two objects.
    "VERTEX_WEIGHT_EDIT",  # Vertex Weight Edit.Modify of the weights of a vertex group.
    "VERTEX_WEIGHT_MIX",  # Vertex Weight Mix.Mix the weights of two vertex groups.
    "VERTEX_WEIGHT_PROXIMITY",  # Vertex Weight Proximity.Set the vertex group weights based on the distance to another target object.
    "GREASE_PENCIL_COLOR",  # Hue/Saturation.Change hue/saturation/value of the strokes.
    "GREASE_PENCIL_TINT",  # Tint.Tint the color of the strokes.
    "GREASE_PENCIL_OPACITY",  # Opacity.Change the opacity of the strokes.
    "GREASE_PENCIL_VERTEX_WEIGHT_ANGLE",  # Vertex Weight Angle.Generate vertex weights based on stroke angle.
    "GREASE_PENCIL_TIME",  # Time Offset.Offset keyframes.
    "GREASE_PENCIL_TEXTURE",  # Texture Mapping.Change stroke UV texture values.
    "ARRAY",  # Array.Create copies of the shape with offsets.
    "BEVEL",  # Bevel.Generate sloped corners by adding geometry to the mesh's edges or vertices.
    "BOOLEAN",  # Boolean.Use another shape to cut, combine or perform a difference operation.
    "BUILD",  # Build.Cause the faces of the mesh object to appear or disappear one after the other over time.
    "DECIMATE",  # Decimate.Reduce the geometry density.
    "EDGE_SPLIT",  # Edge Split.Split away joined faces at the edges.
    "NODES",  # Geometry Nodes.
    "MASK",  # Mask.Dynamically hide vertices based on a vertex group or armature.
    "MIRROR",  # Mirror.Mirror along the local X, Y and/or Z axes, over the object origin.
    "MESH_TO_VOLUME",  # Mesh to Volume.
    "MULTIRES",  # Multiresolution.Subdivide the mesh in a way that allows editing the higher subdivision levels.
    "REMESH",  # Remesh.Generate new mesh topology based on the current shape.
    "SCREW",  # Screw.Lathe around an axis, treating the input mesh as a profile.
    "SKIN",  # Skin.Create a solid shape from vertices and edges, using the vertex radius to define the thickness.
    "SOLIDIFY",  # Solidify.Make the surface thick.
    "SUBSURF",  # Subdivision Surface.Split the faces into smaller parts, giving it a smoother appearance.
    "TRIANGULATE",  # Triangulate.Convert all polygons to triangles.
    "VOLUME_TO_MESH",  # Volume to Mesh.
    "WELD",  # Weld.Find groups of vertices closer than dist and merge them together.
    "WIREFRAME",  # Wireframe.Convert faces into thickened edges.
    "GREASE_PENCIL_ARRAY",  # Array strokes.Duplicate strokes into an array.
    "GREASE_PENCIL_BUILD",  # Build.Grease Pencil build modifier.
    "GREASE_PENCIL_LENGTH",  # Length.Grease Pencil length modifier.
    "LINEART",  # Line Art.Generate Line Art from scene geometries.
    "GREASE_PENCIL_MIRROR",  # Mirror strokes.Duplicate strokes like a mirror.
    "GREASE_PENCIL_MULTIPLY",  # Multiple Strokes.Generate multiple strokes around original strokes.
    "GREASE_PENCIL_SIMPLIFY",  # Simplify.Simplify stroke reducing number of points.
    "GREASE_PENCIL_SUBDIV",  # Subdivide strokes.Grease Pencil subdivide modifier.
    "GREASE_PENCIL_ENVELOPE",  # Envelope.Create an envelope shape.
    "GREASE_PENCIL_OUTLINE",  # Outline.Convert stroke to perimeter.
    "ARMATURE",  # Armature.Deform the shape using an armature object.
    "CAST",  # Cast.Shift the shape towards a predefined primitive.
    "CURVE",  # Curve.Bend the mesh using a curve object.
    "DISPLACE",  # Displace.Offset vertices based on a texture.
    "HOOK",  # Hook.Deform specific points using another object.
    "LAPLACIANDEFORM",  # Laplacian Deform.Deform based a series of anchor points.
    "LATTICE",  # Lattice.Deform using the shape of a lattice object.
    "MESH_DEFORM",  # Mesh Deform.Deform using a different mesh, which acts as a deformation cage.
    "SHRINKWRAP",  # Shrinkwrap.Project the shape onto another object.
    "SIMPLE_DEFORM",  # Simple Deform.Deform the shape by twisting, bending, tapering or stretching.
    "SMOOTH",  # Smooth.Smooth the mesh by flattening the angles between adjacent faces.
    "CORRECTIVE_SMOOTH",  # Smooth Corrective.Smooth the mesh while still preserving the volume.
    "LAPLACIANSMOOTH",  # Smooth Laplacian.Reduce the noise on a mesh surface with minimal changes to its shape.
    "SURFACE_DEFORM",  # Surface Deform.Transfer motion from another mesh.
    "WARP",  # Warp.Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects.
    "WAVE",  # Wave.Adds a ripple-like motion to an object's geometry.
    "VOLUME_DISPLACE",  # Volume Displace.Deform volume based on noise or other vector fields.
    "GREASE_PENCIL_HOOK",  # Hook.Deform stroke points using objects.
    "GREASE_PENCIL_NOISE",  # Noise.Generate noise wobble in grease pencil strokes.
    "GREASE_PENCIL_OFFSET",  # Offset.Change stroke location, rotation, or scale.
    "GREASE_PENCIL_SMOOTH",  # Smooth.Smooth grease pencil strokes.
    "GREASE_PENCIL_THICKNESS",  # Thickness.Change stroke thickness.
    "GREASE_PENCIL_LATTICE",  # Lattice.Deform strokes using a lattice object.
    "GREASE_PENCIL_DASH",  # Dot Dash.Generate dot-dash styled strokes.
    "GREASE_PENCIL_ARMATURE",  # Armature.Deform stroke points using armature object.
    "GREASE_PENCIL_SHRINKWRAP",  # Shrinkwrap.Project the shape onto another object.
    "CLOTH",  # Cloth.Physic simulation for cloth.
    "COLLISION",  # Collision.For colliders participating in physics simulation, control which level in the modifier stack is used as the collision surface.
    "DYNAMIC_PAINT",  # Dynamic Paint.Turn objects into paint canvases and brushes, creating color attributes, image sequences, or displacement.
    "EXPLODE",  # Explode.Break apart the mesh faces and let them follow particles.
    "FLUID",  # Fluid.Physics simulation for fluids, like water, oil and smoke.
    "OCEAN",  # Ocean.Generate a moving ocean surface.
    "PARTICLE_INSTANCE",  # Particle Instance.Duplicate mesh at the location of particles.
    "PARTICLE_SYSTEM",  # Particle System.Spawn particles from the shape.
    "SOFT_BODY",  # Soft Body.Simulate soft deformable objects.
    "SURFACE",  # Surface.
]
type ObjectRotationModeItems = typing.Literal[
    "QUATERNION",  # Quaternion (WXYZ).No Gimbal Lock.
    "XYZ",  # XYZ Euler.XYZ Rotation Order - prone to Gimbal Lock (default).
    "XZY",  # XZY Euler.XZY Rotation Order - prone to Gimbal Lock.
    "YXZ",  # YXZ Euler.YXZ Rotation Order - prone to Gimbal Lock.
    "YZX",  # YZX Euler.YZX Rotation Order - prone to Gimbal Lock.
    "ZXY",  # ZXY Euler.ZXY Rotation Order - prone to Gimbal Lock.
    "ZYX",  # ZYX Euler.ZYX Rotation Order - prone to Gimbal Lock.
    "AXIS_ANGLE",  # Axis Angle.Axis Angle (W+XYZ), defines a rotation around some axis defined by 3D-Vector.
]
type ObjectShaderfxTypeItems = typing.Literal[
    "FX_BLUR",  # Blur.Apply Gaussian Blur to object.
    "FX_COLORIZE",  # Colorize.Apply different tint effects.
    "FX_FLIP",  # Flip.Flip image.
    "FX_GLOW",  # Glow.Create a glow effect.
    "FX_PIXEL",  # Pixelate.Pixelate image.
    "FX_RIM",  # Rim.Add a rim to the image.
    "FX_SHADOW",  # Shadow.Create a shadow effect.
    "FX_SWIRL",  # Swirl.Create a rotation distortion.
    "FX_WAVE",  # Wave Distortion.Apply sinusoidal deformation.
]
type ObjectTypeCurveItems = typing.Literal[
    "CURVE",  # Curve.
    "SURFACE",  # Surface.
    "FONT",  # Text.
]
type ObjectTypeItems = typing.Literal[
    "MESH",  # Mesh.
    "CURVE",  # Curve.
    "SURFACE",  # Surface.
    "META",  # Metaball.
    "FONT",  # Text.
    "CURVES",  # Hair Curves.
    "POINTCLOUD",  # Point Cloud.
    "VOLUME",  # Volume.
    "GPENCIL",  # Grease Pencil.
    "GREASEPENCIL",  # Grease Pencil v3.
    "ARMATURE",  # Armature.
    "LATTICE",  # Lattice.
    "EMPTY",  # Empty.
    "LIGHT",  # Light.
    "LIGHT_PROBE",  # Light Probe.
    "CAMERA",  # Camera.
    "SPEAKER",  # Speaker.
]
type OperatorContextItems = typing.Literal[
    "INVOKE_DEFAULT",  # Invoke Default.
    "INVOKE_REGION_WIN",  # Invoke Region Window.
    "INVOKE_REGION_CHANNELS",  # Invoke Region Channels.
    "INVOKE_REGION_PREVIEW",  # Invoke Region Preview.
    "INVOKE_AREA",  # Invoke Area.
    "INVOKE_SCREEN",  # Invoke Screen.
    "EXEC_DEFAULT",  # Exec Default.
    "EXEC_REGION_WIN",  # Exec Region Window.
    "EXEC_REGION_CHANNELS",  # Exec Region Channels.
    "EXEC_REGION_PREVIEW",  # Exec Region Preview.
    "EXEC_AREA",  # Exec Area.
    "EXEC_SCREEN",  # Exec Screen.
]
type OperatorPropertyTagItems = typing.Literal[
    "ADVANCED",  # Advanced.The property is advanced so UI is suggested to hide it.
]
type OperatorReturnItems = typing.Literal[
    "RUNNING_MODAL",  # Running Modal.Keep the operator running with blender.
    "CANCELLED",  # Cancelled.The operator exited without doing anything, so no undo entry should be pushed.
    "FINISHED",  # Finished.The operator exited after completing its action.
    "PASS_THROUGH",  # Pass Through.Do nothing and pass the event on.
    "INTERFACE",  # Interface.Handled but not executed (popup menus).
]
type OperatorTypeFlagItems = typing.Literal[
    "REGISTER",  # Register.Display in the info window and support the redo toolbar panel.
    "UNDO",  # Undo.Push an undo event (needed for operator redo).
    "UNDO_GROUPED",  # Grouped Undo.Push a single undo event for repeated instances of this operator.
    "BLOCKING",  # Blocking.Block anything else from using the cursor.
    "MACRO",  # Macro.Use to check if an operator is a macro.
    "GRAB_CURSOR",  # Grab Pointer.Use so the operator grabs the mouse focus, enables wrapping when continuous grab is enabled.
    "GRAB_CURSOR_X",  # Grab Pointer X.Grab, only warping the X axis.
    "GRAB_CURSOR_Y",  # Grab Pointer Y.Grab, only warping the Y axis.
    "DEPENDS_ON_CURSOR",  # Depends on Cursor.The initial cursor location is used, when running from a menus or buttons the user is prompted to place the cursor before beginning the operation.
    "PRESET",  # Preset.Display a preset button with the operators settings.
    "INTERNAL",  # Internal.Removes the operator from search results.
    "MODAL_PRIORITY",  # Modal Priority.Handle events before other modal operators without this option. Use with caution, do not modify data that other modal operators assume is unchanged during their operation.
]
type ParticleEditDisconnectedHairBrushItems = typing.Literal[
    "COMB",  # Comb.Comb hairs.
    "SMOOTH",  # Smooth.Smooth hairs.
    "LENGTH",  # Length.Make hairs longer or shorter.
    "CUT",  # Cut.Cut hairs.
    "WEIGHT",  # Weight.Weight hair particles.
]
type ParticleEditHairBrushItems = typing.Literal[
    "COMB",  # Comb.Comb hairs.
    "SMOOTH",  # Smooth.Smooth hairs.
    "ADD",  # Add.Add hairs.
    "LENGTH",  # Length.Make hairs longer or shorter.
    "PUFF",  # Puff.Make hairs stand up.
    "CUT",  # Cut.Cut hairs.
    "WEIGHT",  # Weight.Weight hair particles.
]
type PreferenceSectionItems = typing.Literal[
    "INTERFACE",  # Interface.
    "VIEWPORT",  # Viewport.
    "LIGHTS",  # Lights.
    "EDITING",  # Editing.
    "ANIMATION",  # Animation.
    "EXTENSIONS",  # Get Extensions.Browse, install and manage extensions from remote and local repositories.
    "ADDONS",  # Add-ons.Manage add-ons installed via Extensions.
    "THEMES",  # Themes.Edit and save themes installed via Extensions.
    "INPUT",  # Input.
    "NAVIGATION",  # Navigation.
    "KEYMAP",  # Keymap.
    "SYSTEM",  # System.
    "SAVE_LOAD",  # Save & Load.
    "FILE_PATHS",  # File Paths.
    "EXPERIMENTAL",  # Experimental.
]
type PropDynamicpaintTypeItems = typing.Literal[
    "CANVAS",  # Canvas.
    "BRUSH",  # Brush.
]
type PropertyFlagEnumItems = typing.Literal[
    "HIDDEN",  # Hidden.For operators: hide from places in the user interface where Blender would add the property automatically, like Adjust Last Operation. Also this property is not written to presets.
    "SKIP_SAVE",  # Skip Save.For operators: the value of this property will not be remembered between invocations of the operator; instead, each invocation will start by using the default value. Also this property is not written to presets.
    "ANIMATABLE",  # Animatable.
    "LIBRARY_EDITABLE",  # Library Editable.This property can be edited, even when it is used on linked data (which normally is read-only). Note that edits to the property will not be saved to the blend file.
    "ENUM_FLAG",  # Enum Flag.
]
type PropertyFlagItems = typing.Literal[
    "HIDDEN",  # Hidden.For operators: hide from places in the user interface where Blender would add the property automatically, like Adjust Last Operation. Also this property is not written to presets.
    "SKIP_SAVE",  # Skip Save.For operators: the value of this property will not be remembered between invocations of the operator; instead, each invocation will start by using the default value. Also this property is not written to presets.
    "SKIP_PRESET",  # Skip Preset.Do not write in presets.
    "ANIMATABLE",  # Animatable.
    "LIBRARY_EDITABLE",  # Library Editable.This property can be edited, even when it is used on linked data (which normally is read-only). Note that edits to the property will not be saved to the blend file.
    "PROPORTIONAL",  # Adjust values proportionally to each other.
    "TEXTEDIT_UPDATE",  # Update on every keystroke in textedit 'mode'.
    "OUTPUT_PATH",  # Output Path.
]
type PropertyOverrideFlagCollectionItems = typing.Literal[
    "LIBRARY_OVERRIDABLE",  # Library Overridable.Make that property editable in library overrides of linked data-blocks.
    "NO_PROPERTY_NAME",  # No Name.Do not use the names of the items, only their indices in the collection.
    "USE_INSERTION",  # Use Insertion.Allow users to add new items in that collection in library overrides.
]
type PropertyOverrideFlagItems = typing.Literal[
    "LIBRARY_OVERRIDABLE",  # Library Overridable.Make that property editable in library overrides of linked data-blocks.
]
type PropertyStringSearchFlagItems = typing.Literal[
    "SORT",  # Sort Search Results.
    "SUGGESTION",  # Suggestion.Search results are suggestions (other values may be entered).
]
type PropertySubtypeItems = typing.Literal[
    "NONE",  # None.
    "FILE_PATH",  # File Path.
    "DIR_PATH",  # Directory Path.
    "FILE_NAME",  # File Name.
    "BYTE_STRING",  # Byte String.
    "PASSWORD",  # Password.A string that is displayed hidden ('********').
    "PIXEL",  # Pixel.
    "UNSIGNED",  # Unsigned.
    "PERCENTAGE",  # Percentage.
    "FACTOR",  # Factor.
    "ANGLE",  # Angle.
    "TIME",  # Time (Scene Relative).Time specified in frames, converted to seconds based on scene frame rate.
    "TIME_ABSOLUTE",  # Time (Absolute).Time specified in seconds, independent of the scene.
    "DISTANCE",  # Distance.
    "DISTANCE_CAMERA",  # Camera Distance.
    "POWER",  # Power.
    "TEMPERATURE",  # Temperature.
    "WAVELENGTH",  # Wavelength.
    "COLOR",  # Color.
    "TRANSLATION",  # Translation.
    "DIRECTION",  # Direction.
    "VELOCITY",  # Velocity.
    "ACCELERATION",  # Acceleration.
    "MATRIX",  # Matrix.
    "EULER",  # Euler Angles.
    "QUATERNION",  # Quaternion.
    "AXISANGLE",  # Axis-Angle.
    "XYZ",  # XYZ.
    "XYZ_LENGTH",  # XYZ Length.
    "COLOR_GAMMA",  # Color.
    "COORDINATES",  # Coordinates.
    "LAYER",  # Layer.
    "LAYER_MEMBER",  # Layer Member.
]
type PropertySubtypeNumberArrayItems = typing.Literal[
    "COLOR",  # Color.
    "TRANSLATION",  # Translation.
    "DIRECTION",  # Direction.
    "VELOCITY",  # Velocity.
    "ACCELERATION",  # Acceleration.
    "MATRIX",  # Matrix.
    "EULER",  # Euler Angles.
    "QUATERNION",  # Quaternion.
    "AXISANGLE",  # Axis-Angle.
    "XYZ",  # XYZ.
    "XYZ_LENGTH",  # XYZ Length.
    "COLOR_GAMMA",  # Color.
    "COORDINATES",  # Coordinates.
    "LAYER",  # Layer.
    "LAYER_MEMBER",  # Layer Member.
    "NONE",  # None.
]
type PropertySubtypeNumberItems = typing.Literal[
    "PIXEL",  # Pixel.
    "UNSIGNED",  # Unsigned.
    "PERCENTAGE",  # Percentage.
    "FACTOR",  # Factor.
    "ANGLE",  # Angle.
    "TIME",  # Time (Scene Relative).Time specified in frames, converted to seconds based on scene frame rate.
    "TIME_ABSOLUTE",  # Time (Absolute).Time specified in seconds, independent of the scene.
    "DISTANCE",  # Distance.
    "DISTANCE_CAMERA",  # Camera Distance.
    "POWER",  # Power.
    "TEMPERATURE",  # Temperature.
    "WAVELENGTH",  # Wavelength.
    "NONE",  # None.
]
type PropertySubtypeStringItems = typing.Literal[
    "FILE_PATH",  # File Path.
    "DIR_PATH",  # Directory Path.
    "FILE_NAME",  # File Name.
    "BYTE_STRING",  # Byte String.
    "PASSWORD",  # Password.A string that is displayed hidden ('********').
    "NONE",  # None.
]
type PropertyTypeItems = typing.Literal[
    "BOOLEAN",  # Boolean.
    "INT",  # Integer.
    "FLOAT",  # Float.
    "STRING",  # String.
    "ENUM",  # Enumeration.
    "POINTER",  # Pointer.
    "COLLECTION",  # Collection.
]
type PropertyUnitItems = typing.Literal[
    "NONE",  # None.
    "LENGTH",  # Length.
    "AREA",  # Area.
    "VOLUME",  # Volume.
    "ROTATION",  # Rotation.
    "TIME",  # Time (Scene Relative).
    "TIME_ABSOLUTE",  # Time (Absolute).
    "VELOCITY",  # Velocity.
    "ACCELERATION",  # Acceleration.
    "MASS",  # Mass.
    "CAMERA",  # Camera.
    "POWER",  # Power.
    "TEMPERATURE",  # Temperature.
    "WAVELENGTH",  # Wavelength.
]
type ProportionalFalloffCurveOnlyItems = typing.Literal[
    "SMOOTH",  # Smooth.Smooth falloff.
    "SPHERE",  # Sphere.Spherical falloff.
    "ROOT",  # Root.Root falloff.
    "INVERSE_SQUARE",  # Inverse Square.Inverse Square falloff.
    "SHARP",  # Sharp.Sharp falloff.
    "LINEAR",  # Linear.Linear falloff.
]
type ProportionalFalloffItems = typing.Literal[
    "SMOOTH",  # Smooth.Smooth falloff.
    "SPHERE",  # Sphere.Spherical falloff.
    "ROOT",  # Root.Root falloff.
    "INVERSE_SQUARE",  # Inverse Square.Inverse Square falloff.
    "SHARP",  # Sharp.Sharp falloff.
    "LINEAR",  # Linear.Linear falloff.
    "CONSTANT",  # Constant.Constant falloff.
    "RANDOM",  # Random.Random falloff.
]
type RampBlendItems = typing.Literal[
    "MIX",  # Mix.
    "DARKEN",  # Darken.
    "MULTIPLY",  # Multiply.
    "BURN",  # Color Burn.
    "LIGHTEN",  # Lighten.
    "SCREEN",  # Screen.
    "DODGE",  # Color Dodge.
    "ADD",  # Add.
    "OVERLAY",  # Overlay.
    "SOFT_LIGHT",  # Soft Light.
    "LINEAR_LIGHT",  # Linear Light.
    "DIFFERENCE",  # Difference.
    "EXCLUSION",  # Exclusion.
    "SUBTRACT",  # Subtract.
    "DIVIDE",  # Divide.
    "HUE",  # Hue.
    "SATURATION",  # Saturation.
    "COLOR",  # Color.
    "VALUE",  # Value.
]
type RegionTypeItems = typing.Literal[
    "WINDOW",  # Window.
    "HEADER",  # Header.
    "CHANNELS",  # Channels.
    "TEMPORARY",  # Temporary.
    "UI",  # Sidebar.
    "TOOLS",  # Tools.
    "TOOL_PROPS",  # Tool Properties.
    "ASSET_SHELF",  # Asset Shelf.
    "ASSET_SHELF_HEADER",  # Asset Shelf Header.
    "PREVIEW",  # Preview.
    "HUD",  # Floating Region.
    "NAVIGATION_BAR",  # Navigation Bar.
    "EXECUTE",  # Execute Buttons.
    "FOOTER",  # Footer.
    "TOOL_HEADER",  # Tool Header.
    "XR",  # XR.
]
type RenderPassTypeItems = typing.Literal[
    "COMBINED",  # Combined.
    "Z",  # <string>:4: (INFO/1) Enumerated list start value not ordinal-1: "Z" (ordinal 26)
    "SHADOW",  # Shadow.
    "AO",  # Ambient Occlusion.
    "POSITION",  # Position.
    "NORMAL",  # Normal.
    "VECTOR",  # Vector.
    "OBJECT_INDEX",  # Object Index.
    "UV",  # UV.
    "MIST",  # Mist.
    "EMIT",  # Emit.
    "ENVIRONMENT",  # Environment.
    "MATERIAL_INDEX",  # Material Index.
    "DIFFUSE_DIRECT",  # Diffuse Direct.
    "DIFFUSE_INDIRECT",  # Diffuse Indirect.
    "DIFFUSE_COLOR",  # Diffuse Color.
    "GLOSSY_DIRECT",  # Glossy Direct.
    "GLOSSY_INDIRECT",  # Glossy Indirect.
    "GLOSSY_COLOR",  # Glossy Color.
    "TRANSMISSION_DIRECT",  # Transmission Direct.
    "TRANSMISSION_INDIRECT",  # Transmission Indirect.
    "TRANSMISSION_COLOR",  # Transmission Color.
    "SUBSURFACE_DIRECT",  # Subsurface Direct.
    "SUBSURFACE_INDIRECT",  # Subsurface Indirect.
    "SUBSURFACE_COLOR",  # Subsurface Color.
]
type RigidbodyConstraintTypeItems = typing.Literal[
    "FIXED",  # Fixed.Glue rigid bodies together.
    "POINT",  # Point.Constrain rigid bodies to move around common pivot point.
    "HINGE",  # Hinge.Restrict rigid body rotation to one axis.
    "SLIDER",  # Slider.Restrict rigid body translation to one axis.
    "PISTON",  # Piston.Restrict rigid body translation and rotation to one axis.
    "GENERIC",  # Generic.Restrict translation and rotation to specified axes.
    "GENERIC_SPRING",  # Generic Spring.Restrict translation and rotation to specified axes with springs.
    "MOTOR",  # Motor.Drive rigid body around or along an axis.
]
type RigidbodyObjectShapeItems = typing.Literal[
    "BOX",  # Box.Box-like shapes (i.e. cubes), including planes (i.e. ground planes).
    "SPHERE",  # Sphere.
    "CAPSULE",  # Capsule.
    "CYLINDER",  # Cylinder.
    "CONE",  # Cone.
    "CONVEX_HULL",  # Convex Hull.A mesh-like surface encompassing (i.e. shrinkwrap over) all vertices (best results with fewer vertices).
    "MESH",  # Mesh.Mesh consisting of triangles only, allowing for more detailed interactions than convex hulls.
    "COMPOUND",  # Compound Parent.Combines all of its direct rigid body children into one rigid object.
]
type RigidbodyObjectTypeItems = typing.Literal[
    "ACTIVE",  # Active.Object is directly controlled by simulation results.
    "PASSIVE",  # Passive.Object is directly controlled by animation system.
]
type SequenceModifierTypeItems = typing.Literal[
    "BRIGHT_CONTRAST",  # Brightness/Contrast.
    "COLOR_BALANCE",  # Color Balance.
    "CURVES",  # Curves.
    "HUE_CORRECT",  # Hue Correct.
    "MASK",  # Mask.
    "TONEMAP",  # Tone Map.
    "WHITE_BALANCE",  # White Balance.
    "SOUND_EQUALIZER",  # Sound Equalizer.
]
type SequenceSoundModifierTypeItems = typing.Literal[
    "SOUND_EQUALIZER",  # Sound Equalizer.
]
type SequenceVideoModifierTypeItems = typing.Literal[
    "BRIGHT_CONTRAST",  # Brightness/Contrast.
    "COLOR_BALANCE",  # Color Balance.
    "CURVES",  # Curves.
    "HUE_CORRECT",  # Hue Correct.
    "MASK",  # Mask.
    "TONEMAP",  # Tone Map.
    "WHITE_BALANCE",  # White Balance.
]
type ShadingTypeItems = typing.Literal[
    "WIREFRAME",  # Wireframe.Display the object as wire edges.
    "SOLID",  # Solid.Display in solid mode.
    "MATERIAL",  # Material Preview.Display in Material Preview mode.
    "RENDERED",  # Rendered.Display render preview.
]
type ShrinkwrapFaceCullItems = typing.Literal[
    "OFF",  # Off.No culling.
    "FRONT",  # Front.No projection when in front of the face.
    "BACK",  # Back.No projection when behind the face.
]
type ShrinkwrapTypeItems = typing.Literal[
    "NEAREST_SURFACEPOINT",  # Nearest Surface Point.Shrink the mesh to the nearest target surface.
    "PROJECT",  # Project.Shrink the mesh to the nearest target surface along a given axis.
    "NEAREST_VERTEX",  # Nearest Vertex.Shrink the mesh to the nearest target vertex.
    "TARGET_PROJECT",  # Target Normal Project.Shrink the mesh to the nearest target surface along the interpolated vertex normals of the target.
]
type SnapAnimationElementItems = typing.Literal[
    "FRAME",  # Frame.Snap to frame.
    "SECOND",  # Second.Snap to seconds.
    "MARKER",  # Nearest Marker.Snap to nearest marker.
]
type SnapElementItems = typing.Literal[
    "INCREMENT",  # Increment.Snap to increments.
    "GRID",  # Grid.Snap to grid.
    "VERTEX",  # Vertex.Snap to vertices.
    "EDGE",  # Edge.Snap to edges.
    "FACE",  # Face.Snap by projecting onto faces.
    "VOLUME",  # Volume.Snap to volume.
    "EDGE_MIDPOINT",  # Edge Center.Snap to the middle of edges.
    "EDGE_PERPENDICULAR",  # Edge Perpendicular.Snap to the nearest point on an edge.
    "FACE_PROJECT",  # Face Project.Snap by projecting onto faces.
    "FACE_NEAREST",  # Face Nearest.Snap to nearest point on faces.
]
type SnapNodeElementItems = typing.Literal[
    "GRID",  # Grid.Snap to grid.
    "NODE_X",  # Node X.Snap to left/right node border.
    "NODE_Y",  # Node Y.Snap to top/bottom node border.
    "NODE_XY",  # Node X / Y.Snap to any node border.
]
type SnapSourceItems = typing.Literal[
    "CLOSEST",  # Closest.Snap closest point onto target.
    "CENTER",  # Center.Snap transformation center onto target.
    "MEDIAN",  # Median.Snap median onto target.
    "ACTIVE",  # Active.Snap active onto target.
]
type SpaceActionModeItems = typing.Literal[
    "DOPESHEET",  # Dope Sheet.Edit all keyframes in scene.
    "TIMELINE",  # Timeline.Timeline and playback controls.
]
type SpaceFileBrowseModeItems = typing.Literal[
    "FILES",  # File Browser.
    "ASSETS",  # Asset Browser.
]
type SpaceGraphModeItems = typing.Literal[
    "FCURVES",  # Graph Editor.Edit animation/keyframes displayed as 2D curves.
    "DRIVERS",  # Drivers.Edit drivers.
]
type SpaceImageModeAllItems = typing.Literal[
    "VIEW",  # View.View the image.
    "UV",  # UV Editor.UV edit in mesh editmode.
    "PAINT",  # Paint.2D image painting mode.
    "MASK",  # Mask.Mask editing.
]
type SpaceImageModeItems = typing.Literal[
    "IMAGE_EDITOR",  # Image Editor.View the image.
    "UV",  # UV Editor.UV edit in mesh editmode.
]
type SpaceSequencerViewTypeItems = typing.Literal[
    "SEQUENCER",  # Sequencer.
    "PREVIEW",  # Preview.
    "SEQUENCER_PREVIEW",  # Sequencer & Preview.
]
type SpaceTypeItems = typing.Literal[
    "EMPTY",  # Empty.
    "VIEW_3D",  # 3D Viewport.Manipulate objects in a 3D environment.
    "IMAGE_EDITOR",  # UV/Image Editor.View and edit images and UV Maps.
    "NODE_EDITOR",  # Node Editor.Editor for node-based shading and compositing tools.
    "SEQUENCE_EDITOR",  # Video Sequencer.Video editing tools.
    "CLIP_EDITOR",  # Movie Clip Editor.Motion tracking tools.
    "DOPESHEET_EDITOR",  # Dope Sheet.Adjust timing of keyframes.
    "GRAPH_EDITOR",  # Graph Editor.Edit drivers and keyframe interpolation.
    "NLA_EDITOR",  # Nonlinear Animation.Combine and layer Actions.
    "TEXT_EDITOR",  # Text Editor.Edit scripts and in-file documentation.
    "CONSOLE",  # Python Console.Interactive programmatic console for advanced editing and script development.
    "INFO",  # Info.Log of operations, warnings and error messages.
    "TOPBAR",  # Top Bar.Global bar at the top of the screen for global per-window settings.
    "STATUSBAR",  # Status Bar.Global bar at the bottom of the screen for general status information.
    "OUTLINER",  # Outliner.Overview of scene graph and all available data-blocks.
    "PROPERTIES",  # Properties.Edit properties of active object and related data-blocks.
    "FILE_BROWSER",  # File Browser.Browse for files and assets.
    "SPREADSHEET",  # Spreadsheet.Explore geometry data in a table.
    "PREFERENCES",  # Preferences.Edit persistent configuration settings.
]
type Stereo3DAnaglyphTypeItems = typing.Literal[
    "RED_CYAN",  # Red-Cyan.
    "GREEN_MAGENTA",  # Green-Magenta.
    "YELLOW_BLUE",  # Yellow-Blue.
]
type Stereo3DDisplayItems = typing.Literal[
    "ANAGLYPH",  # Anaglyph.Render views for left and right eyes as two differently filtered colors in a single image (anaglyph glasses are required).
    "INTERLACE",  # Interlace.Render views for left and right eyes interlaced in a single image (3D-ready monitor is required).
    "TIMESEQUENTIAL",  # Time Sequential.Render alternate eyes (also known as page flip, quad buffer support in the graphic card is required).
    "SIDEBYSIDE",  # Side-by-Side.Render views for left and right eyes side-by-side.
    "TOPBOTTOM",  # Top-Bottom.Render views for left and right eyes one above another.
]
type Stereo3DInterlaceTypeItems = typing.Literal[
    "ROW_INTERLEAVED",  # Row Interleaved.
    "COLUMN_INTERLEAVED",  # Column Interleaved.
    "CHECKERBOARD_INTERLEAVED",  # Checkerboard Interleaved.
]
type StripColorItems = typing.Literal[
    "NONE",  # None.Assign no color tag to the collection.
    "COLOR_01",  # Color 01.
    "COLOR_02",  # Color 02.
    "COLOR_03",  # Color 03.
    "COLOR_04",  # Color 04.
    "COLOR_05",  # Color 05.
    "COLOR_06",  # Color 06.
    "COLOR_07",  # Color 07.
    "COLOR_08",  # Color 08.
    "COLOR_09",  # Color 09.
]
type SubdivisionBoundarySmoothItems = typing.Literal[
    "PRESERVE_CORNERS",  # Keep Corners.Smooth boundaries, but corners are kept sharp.
    "ALL",  # All.Smooth boundaries, including corners.
]
type SubdivisionUvSmoothItems = typing.Literal[
    "NONE",  # None.UVs are not smoothed, boundaries are kept sharp.
    "PRESERVE_CORNERS",  # Keep Corners.UVs are smoothed, corners on discontinuous boundary are kept sharp.
    "PRESERVE_CORNERS_AND_JUNCTIONS",  # Keep Corners, Junctions.UVs are smoothed, corners on discontinuous boundary and junctions of 3 or more regions are kept sharp.
    "PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE",  # Keep Corners, Junctions, Concave.UVs are smoothed, corners on discontinuous boundary, junctions of 3 or more regions and darts and concave corners are kept sharp.
    "PRESERVE_BOUNDARIES",  # Keep Boundaries.UVs are smoothed, boundaries are kept sharp.
    "SMOOTH_ALL",  # All.UVs and boundaries are smoothed.
]
type SymmetrizeDirectionItems = typing.Literal[
    "NEGATIVE_X",  # -X to +X.
    "POSITIVE_X",  # +X to -X.
    "NEGATIVE_Y",  # -Y to +Y.
    "POSITIVE_Y",  # +Y to -Y.
    "NEGATIVE_Z",  # -Z to +Z.
    "POSITIVE_Z",  # +Z to -Z.
]
type TextureTypeItems = typing.Literal[
    "NONE",  # None.
    "BLEND",  # Blend.Procedural - create a ramp texture.
    "CLOUDS",  # Clouds.Procedural - create a cloud-like fractal noise texture.
    "DISTORTED_NOISE",  # Distorted Noise.Procedural - noise texture distorted by two noise algorithms.
    "IMAGE",  # Image or Movie.Allow for images or movies to be used as textures.
    "MAGIC",  # Magic.Procedural - color texture based on trigonometric functions.
    "MARBLE",  # Marble.Procedural - marble-like noise texture with wave generated bands.
    "MUSGRAVE",  # Musgrave.Procedural - highly flexible fractal noise texture.
    "NOISE",  # Noise.Procedural - random noise, gives a different result every time, for every frame, for every pixel.
    "STUCCI",  # Stucci.Procedural - create a fractal noise texture.
    "VORONOI",  # Voronoi.Procedural - create cell-like patterns based on Worley noise.
    "WOOD",  # Wood.Procedural - wave generated bands or rings, with optional noise.
]
type TransformModeTypeItems = typing.Literal[
    "INIT",  # Init.
    "DUMMY",  # Dummy.
    "TRANSLATION",  # Translation.
    "ROTATION",  # Rotation.
    "RESIZE",  # Resize.
    "SKIN_RESIZE",  # Skin Resize.
    "TOSPHERE",  # To Sphere.
    "SHEAR",  # Shear.
    "BEND",  # Bend.
    "SHRINKFATTEN",  # Shrink/Fatten.
    "TILT",  # Tilt.
    "TRACKBALL",  # Trackball.
    "PUSHPULL",  # Push/Pull.
    "CREASE",  # Crease.
    "VERTEX_CREASE",  # Vertex Crease.
    "MIRROR",  # Mirror.
    "BONE_SIZE",  # Bone Size.
    "BONE_ENVELOPE",  # Bone Envelope.
    "BONE_ENVELOPE_DIST",  # Bone Envelope Distance.
    "CURVE_SHRINKFATTEN",  # Curve Shrink/Fatten.
    "MASK_SHRINKFATTEN",  # Mask Shrink/Fatten.
    "GPENCIL_SHRINKFATTEN",  # Grease Pencil Shrink/Fatten.
    "BONE_ROLL",  # Bone Roll.
    "TIME_TRANSLATE",  # Time Translate.
    "TIME_SLIDE",  # Time Slide.
    "TIME_SCALE",  # Time Scale.
    "TIME_EXTEND",  # Time Extend.
    "BAKE_TIME",  # Bake Time.
    "BWEIGHT",  # Bevel Weight.
    "ALIGN",  # Align.
    "EDGESLIDE",  # Edge Slide.
    "SEQSLIDE",  # Sequence Slide.
    "GPENCIL_OPACITY",  # Grease Pencil Opacity.
]
type TransformOrientationItems = typing.Literal[
    "GLOBAL",  # Global.Align the transformation axes to world space.
    "LOCAL",  # Local.Align the transformation axes to the selected objects' local space.
    "NORMAL",  # Normal.Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).
    "GIMBAL",  # Gimbal.Align each axis to the Euler rotation axis as used for input.
    "VIEW",  # View.Align the transformation axes to the window.
    "CURSOR",  # Cursor.Align the transformation axes to the 3D cursor.
    "PARENT",  # Parent.Align the transformation axes to the object's parent space.
]
type TransformPivotFullItems = typing.Literal[
    "BOUNDING_BOX_CENTER",  # Bounding Box Center.Pivot around bounding box center of selected object(s).
    "CURSOR",  # 3D Cursor.Pivot around the 3D cursor.
    "INDIVIDUAL_ORIGINS",  # Individual Origins.Pivot around each object's own origin.
    "MEDIAN_POINT",  # Median Point.Pivot around the median point of selected objects.
    "ACTIVE_ELEMENT",  # Active Element.Pivot around active object.
]
type UilistLayoutTypeItems = typing.Literal[
    "DEFAULT",  # Default Layout.Use the default, multi-rows layout.
    "COMPACT",  # Compact Layout.Use the compact, single-row layout.
    "GRID",  # Grid Layout.Use the grid-based layout.
]
type UnpackMethodItems = typing.Literal[
    "REMOVE",  # Remove Pack.
    "USE_LOCAL",  # Use Local File.
    "WRITE_LOCAL",  # Write Local File (overwrite existing).
    "USE_ORIGINAL",  # Use Original File.
    "WRITE_ORIGINAL",  # Write Original File (overwrite existing).
]
type VelocityUnitItems = typing.Literal[
    "SECOND",  # Second.
    "FRAME",  # Frame.
]
type ViewsFormatItems = typing.Literal[
    "INDIVIDUAL",  # Individual.Individual files for each view with the prefix as defined by the scene views.
    "STEREO_3D",  # Stereo 3D.Single file with an encoded stereo pair.
]
type ViewsFormatMultilayerItems = typing.Literal[
    "INDIVIDUAL",  # Individual.Individual files for each view with the prefix as defined by the scene views.
    "MULTIVIEW",  # Multi-View.Single file with all the views.
]
type ViewsFormatMultiviewItems = typing.Literal[
    "INDIVIDUAL",  # Individual.Individual files for each view with the prefix as defined by the scene views.
    "STEREO_3D",  # Stereo 3D.Single file with an encoded stereo pair.
    "MULTIVIEW",  # Multi-View.Single file with all the views.
]
type VolumeGridDataTypeItems = typing.Literal[
    "BOOLEAN",  # Boolean.Boolean.
    "FLOAT",  # Float.Single precision float.
    "DOUBLE",  # Double.Double precision.
    "INT",  # Integer.32-bit integer.
    "INT64",  # Integer 64-bit.64-bit integer.
    "MASK",  # Mask.No data, boolean mask of active voxels.
    "VECTOR_FLOAT",  # Float Vector.3D float vector.
    "VECTOR_DOUBLE",  # Double Vector.3D double vector.
    "VECTOR_INT",  # Integer Vector.3D integer vector.
    "POINTS",  # Points (Unsupported).Points grid, currently unsupported by volume objects.
    "UNKNOWN",  # Unknown.Unsupported data type.
]
type WindowCursorItems = typing.Literal[
    "DEFAULT",  # Default.
    "NONE",  # None.
    "WAIT",  # Wait.
    "CROSSHAIR",  # Crosshair.
    "MOVE_X",  # Move-X.
    "MOVE_Y",  # Move-Y.
    "KNIFE",  # Knife.
    "TEXT",  # Text.
    "PAINT_BRUSH",  # Paint Brush.
    "PAINT_CROSS",  # Paint Cross.
    "DOT",  # Dot Cursor.
    "ERASER",  # Eraser.
    "HAND",  # Hand.
    "SCROLL_X",  # Scroll-X.
    "SCROLL_Y",  # Scroll-Y.
    "SCROLL_XY",  # Scroll-XY.
    "EYEDROPPER",  # Eyedropper.
    "PICK_AREA",  # Pick Area.
    "STOP",  # Stop.
    "COPY",  # Copy.
    "CROSS",  # Cross.
    "MUTE",  # Mute.
    "ZOOM_IN",  # Zoom In.
    "ZOOM_OUT",  # Zoom Out.
]
type WmJobTypeItems = typing.Literal[
    "RENDER",  # Regular rendering.
    "RENDER_PREVIEW",  # Rendering previews.
    "OBJECT_BAKE",  # Object Baking.
    "COMPOSITE",  # Compositing.
    "SHADER_COMPILATION",  # Shader compilation.
]
type WmReportItems = typing.Literal[
    "DEBUG",  # Debug.
    "INFO",  # Info.
    "OPERATOR",  # Operator.
    "PROPERTY",  # Property.
    "WARNING",  # Warning.
    "ERROR",  # Error.
    "ERROR_INVALID_INPUT",  # Invalid Input.
    "ERROR_INVALID_CONTEXT",  # Invalid Context.
    "ERROR_OUT_OF_MEMORY",  # Out of Memory.
]
type WorkspaceObjectModeItems = typing.Literal[
    "OBJECT",  # Object Mode.
    "EDIT",  # Edit Mode.
    "POSE",  # Pose Mode.
    "SCULPT",  # Sculpt Mode.
    "VERTEX_PAINT",  # Vertex Paint.
    "WEIGHT_PAINT",  # Weight Paint.
    "TEXTURE_PAINT",  # Texture Paint.
    "PARTICLE_EDIT",  # Particle Edit.
    "EDIT_GPENCIL",  # Grease Pencil Edit Mode.Edit Grease Pencil Strokes.
    "SCULPT_GPENCIL",  # Grease Pencil Sculpt Mode.Sculpt Grease Pencil Strokes.
    "PAINT_GPENCIL",  # Grease Pencil Draw.Paint Grease Pencil Strokes.
    "VERTEX_GPENCIL",  # Grease Pencil Vertex Paint.Grease Pencil Vertex Paint Strokes.
    "WEIGHT_GPENCIL",  # Grease Pencil Weight Paint.Grease Pencil Weight Paint Strokes.
]
