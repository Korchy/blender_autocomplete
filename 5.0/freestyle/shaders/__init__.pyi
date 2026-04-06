"""
This module contains stroke shaders used for creation of stylized
strokes.  It is also intended to be a collection of examples for
shader definition in Python.

User-defined stroke shaders inherit the
freestyle.types.StrokeShader class.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types
import freestyle.types
import mathutils

class BackboneStretcherShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `BackboneStretcherShader`[Geometry shader]"""

    def __init__(self, amount: float = 2.0) -> None:
        """Builds a BackboneStretcherShader object.

        :param amount: The stretching amount value.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Stretches the stroke at its two extremities and following the
        respective directions: v(1)v(0) and v(n-1)v(n).

                :param stroke: A Stroke object.
        """

class BezierCurveShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `BezierCurveShader`[Geometry shader]"""

    def __init__(self, error: float = 4.0) -> None:
        """Builds a BezierCurveShader object.

                :param error: The error were allowing for the approximation. This
        error is the max distance allowed between the new curve and the
        original geometry.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Transforms the stroke backbone geometry so that it corresponds to a
        Bezier Curve approximation of the original backbone geometry.

                :param stroke: A Stroke object.
        """

class BlenderTextureShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `BlenderTextureShader`[Texture shader]"""

    def __init__(
        self, texture: bpy.types.LineStyleTextureSlot | bpy.types.ShaderNodeTree
    ) -> None:
        """Builds a BlenderTextureShader object.

        :param texture: A line style texture slot or a shader node tree to define a set of textures.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Assigns a blender texture slot to the stroke  shading in order to
        simulate marks.

                :param stroke: A Stroke object.
        """

class CalligraphicShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `CalligraphicShader`[Thickness Shader]"""

    def __init__(
        self,
        thickness_min: float,
        thickness_max: float,
        orientation: collections.abc.Sequence[float] | mathutils.Vector,
        clamp: bool,
    ) -> None:
        """Builds a CalligraphicShader object.

                :param thickness_min: The minimum thickness in the direction
        perpendicular to the main direction.
                :param thickness_max: The maximum thickness in the main direction.
                :param orientation: The 2D vector giving the main direction.
                :param clamp: If true, the strokes are drawn in black when the stroke
        direction is between -90 and 90 degrees with respect to the main
        direction and drawn in white otherwise. If false, the strokes
        are always drawn in black.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Assigns thicknesses to the stroke vertices so that the stroke looks
        like made with a calligraphic tool, i.e. the stroke will be the
        thickest in a main direction, and the thinnest in the direction
        perpendicular to this one, and an interpolation in between.

                :param stroke: A Stroke object.
        """

class ColorNoiseShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `ColorNoiseShader`[Color shader]"""

    def __init__(self, amplitude: float, period: float) -> None:
        """Builds a ColorNoiseShader object.

        :param amplitude: The amplitude of the noise signal.
        :param period: The period of the noise signal.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Shader to add noise to the stroke colors.

        :param stroke: A Stroke object.
        """

class ConstantColorShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `ConstantColorShader`[Color shader]"""

    def __init__(
        self, red: float, green: float, blue: float, alpha: float = 1.0
    ) -> None:
        """Builds a ConstantColorShader object.

        :param red: The red component.
        :param green: The green component.
        :param blue: The blue component.
        :param alpha: The alpha value.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Assigns a constant color to every vertex of the Stroke.

        :param stroke: A Stroke object.
        """

class ConstantThicknessShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `ConstantThicknessShader`[Thickness shader]"""

    def __init__(self, thickness: float) -> None:
        """Builds a ConstantThicknessShader object.

        :param thickness: The thickness that must be assigned to the stroke.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Assigns an absolute constant thickness to every vertex of the Stroke.

        :param stroke: A Stroke object.
        """

class ConstrainedIncreasingThicknessShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `ConstrainedIncreasingThicknessShader`[Thickness shader]"""

    def __init__(
        self, thickness_min: float, thickness_max: float, ratio: float
    ) -> None:
        """Builds a ConstrainedIncreasingThicknessShader object.

        :param thickness_min: The minimum thickness.
        :param thickness_max: The maximum thickness.
        :param ratio: The thickness/length ratio that we dont want to exceed.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Same as the `IncreasingThicknessShader`, but here we allow
        the user to control the thickness/length ratio so that we dont get
        fat short lines.

                :param stroke: A Stroke object.
        """

class GuidingLinesShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `GuidingLinesShader`[Geometry shader]"""

    def __init__(self, offset: float) -> None:
        """Builds a GuidingLinesShader object.

                :param offset: The line that replaces the stroke is initially in the
        middle of the initial stroke bounding box. offset is the value
        of the displacement which is applied to this line along its
        normal.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Shader to modify the Stroke geometry so that it corresponds to its
        main direction line. This shader must be used together with the
        splitting operator using the curvature criterion. Indeed, the
        precision of the approximation will depend on the size of the
        strokes pieces. The bigger the pieces are, the rougher the
        approximation is.

                :param stroke: A Stroke object.
        """

class IncreasingColorShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `IncreasingColorShader`[Color shader]"""

    def __init__(
        self,
        red_min: float,
        green_min: float,
        blue_min: float,
        alpha_min: float,
        red_max: float,
        green_max: float,
        blue_max: float,
        alpha_max: float,
    ) -> None:
        """Builds an IncreasingColorShader object.

        :param red_min: The first color red component.
        :param green_min: The first color green component.
        :param blue_min: The first color blue component.
        :param alpha_min: The first color alpha value.
        :param red_max: The second color red component.
        :param green_max: The second color green component.
        :param blue_max: The second color blue component.
        :param alpha_max: The second color alpha value.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Assigns a varying color to the stroke. The user specifies two
        colors A and B. The stroke color will change linearly from A to B
        between the first and the last vertex.

                :param stroke: A Stroke object.
        """

class IncreasingThicknessShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `IncreasingThicknessShader`[Thickness shader]"""

    def __init__(self, thickness_A: float, thickness_B: float) -> None:
        """Builds an IncreasingThicknessShader object.

        :param thickness_A: The first thickness value.
        :param thickness_B: The second thickness value.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Assigns thicknesses values such as the thickness increases from a
        thickness value A to a thickness value B between the first vertex
        to the midpoint vertex and then decreases from B to a A between
        this midpoint vertex and the last vertex. The thickness is
        linearly interpolated from A to B.

                :param stroke: A Stroke object.
        """

class PolygonalizationShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `PolygonalizationShader`[Geometry shader]"""

    def __init__(self, error: float) -> None:
        """Builds a PolygonalizationShader object.

                :param error: The error we want our polygonal approximation to have
        with respect to the original geometry. The smaller, the closer
        the new stroke is to the original one. This error corresponds to
        the maximum distance between the new stroke and the old one.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Modifies the Stroke geometry so that it looks more "polygonal".
        The basic idea is to start from the minimal stroke approximation
        consisting in a line joining the first vertex to the last one and
        to subdivide using the original stroke vertices until a certain
        error is reached.

                :param stroke: A Stroke object.
        """

class RoundCapShader:
    def round_cap_thickness(self, x) -> None:
        """

        :param x:
        """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class SamplingShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `SamplingShader`[Geometry shader]"""

    def __init__(self, sampling: float) -> None:
        """Builds a SamplingShader object.

        :param sampling: The sampling to use for the stroke resampling.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Resamples the stroke.

        :param stroke: A Stroke object.
        """

class SmoothingShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `SmoothingShader`[Geometry shader]"""

    def __init__(
        self,
        num_iterations: int = 100,
        factor_point: float = 0.1,
        factor_curvature: float = 0.0,
        factor_curvature_difference: float = 0.2,
        aniso_point: float = 0.0,
        aniso_normal: float = 0.0,
        aniso_curvature: float = 0.0,
        carricature_factor: float = 1.0,
    ) -> None:
        """Builds a SmoothingShader object.

        :param num_iterations: The number of iterations.
        :param factor_point: 0.1
        :param factor_curvature: 0.0
        :param factor_curvature_difference: 0.2
        :param aniso_point: 0.0
        :param aniso_normal: 0.0
        :param aniso_curvature: 0.0
        :param carricature_factor: 1.0
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Smooths the stroke by moving the vertices to make the stroke
        smoother. Uses curvature flow to converge towards a curve of
        constant curvature. The diffusion method we use is anisotropic to
        prevent the diffusion across corners.

                :param stroke: A Stroke object.
        """

class SpatialNoiseShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `SpatialNoiseShader`[Geometry shader]"""

    def __init__(
        self,
        amount: float,
        scale: float,
        num_octaves: int,
        smooth: bool,
        pure_random: bool,
    ) -> None:
        """Builds a SpatialNoiseShader object.

        :param amount: The amplitude of the noise.
        :param scale: The noise frequency.
        :param num_octaves: The number of octaves
        :param smooth: True if you want the noise to be smooth.
        :param pure_random: True if you dont want any coherence.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Spatial Noise stroke shader. Moves the vertices to make the stroke
        more noisy.

                :param stroke: A Stroke object.
        """

class SquareCapShader:
    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class StrokeTextureStepShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `StrokeTextureStepShader`[Texture shader]"""

    def __init__(self, step: float) -> None:
        """Builds a StrokeTextureStepShader object.

        :param step: The spacing along the stroke.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Assigns a spacing factor to the texture coordinates of the Stroke.

        :param stroke: A Stroke object.
        """

class ThicknessNoiseShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `ThicknessNoiseShader`[Thickness shader]"""

    def __init__(self, amplitude: float, period: float) -> None:
        """Builds a ThicknessNoiseShader object.

        :param amplitude: The amplitude of the noise signal.
        :param period: The period of the noise signal.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Adds some noise to the stroke thickness.

        :param stroke: A Stroke object.
        """

class TipRemoverShader:
    """Class hierarchy: `freestyle.types.StrokeShader` > `TipRemoverShader`[Geometry shader]"""

    def __init__(self, tip_length: float) -> None:
        """Builds a TipRemoverShader object.

                :param tip_length: The length of the piece of stroke we want to remove
        at each extremity.
        """

    def shade(self, stroke: freestyle.types.Stroke) -> None:
        """Removes the strokes extremities.

        :param stroke: A Stroke object.
        """

class py2DCurvatureColorShader:
    """Assigns a color (grayscale) to the stroke based on the curvature.
    A higher curvature will yield a brighter color.
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyBackboneStretcherNoCuspShader:
    """Stretches the strokes backbone, excluding cusp vertices (end junctions)."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyBackboneStretcherShader:
    """Stretches the strokes backbone by a given length (in pixels)."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyBluePrintCirclesShader:
    """Draws the silhouette of the object as a circle."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyBluePrintDirectedSquaresShader:
    """Replaces the stroke with a directed square."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyBluePrintEllipsesShader:
    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyBluePrintSquaresShader:
    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyConstantColorShader:
    """Assigns a constant color to the stroke."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyConstantThicknessShader:
    """Assigns a constant thickness along the stroke."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyConstrainedIncreasingThicknessShader:
    """Increasingly thickens the stroke, constrained by a ratio of the
    strokes length.
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyDecreasingThicknessShader:
    """Inverse of pyIncreasingThicknessShader, decreasingly thickens the stroke."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyDepthDiscontinuityThicknessShader:
    """Assigns a thickness to the stroke based on the strokes distance
    to the camera (Z-value).
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyDiffusion2Shader:
    """Iteratively adds an offset to the position of each stroke vertex
    in the direction perpendicular to the stroke direction at the
    point. The offset is scaled by the 2D curvature (i.e. how quickly
    the stroke curve is) at the point.
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyFXSVaryingThicknessWithDensityShader:
    """Assigns thickness to a stroke based on the density of the diffuse map."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyGuidingLineShader:
    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyHLRShader:
    """Controls visibility based upon the quantitative invisibility (QI)
    based on hidden line removal (HLR).
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyImportance2DThicknessShader:
    """Assigns thickness based on distance to a given point in 2D space.
    the thickness is inverted, so the vertices closest to the
    specified point have the lowest thickness.
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyImportance3DThicknessShader:
    """Assigns thickness based on distance to a given point in 3D space."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyIncreasingColorShader:
    """Fades from one color to another along the stroke."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyIncreasingThicknessShader:
    """Increasingly thickens the stroke."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyInterpolateColorShader:
    """Fades from one color to another and back."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyLengthDependingBackboneStretcherShader:
    """Stretches the strokes backbone proportional to the strokes length
    NOTE: youll probably want an l somewhere between (0.5 - 0). A value that
    is too high may yield unexpected results.
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyMaterialColorShader:
    """Assigns the color of the underlying material to the stroke."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyModulateAlphaShader:
    """Limits the strokes alpha between a min and max value."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyNonLinearVaryingThicknessShader:
    """Assigns thickness to a stroke based on an exponential function."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyPerlinNoise1DShader:
    """Displaces the stroke using the curvilinear abscissa.  This means
    that lines with the same length and sampling interval will be
    identically distorted.
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyPerlinNoise2DShader:
    """Displaces the stroke using the strokes coordinates.  This means
    that in a scene no strokes will be distorted identically.More information on the noise shaders can be found at:
    https://freestyleintegration.wordpress.com/2011/09/25/development-updates-on-september-25/
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyRandomColorShader:
    """Assigns a color to the stroke based on given seed."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pySLERPThicknessShader:
    """Assigns thickness to a stroke based on spherical linear interpolation."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pySamplingShader:
    """Resamples the stroke, which gives the stroke the amount of
    vertices specified.
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pySinusDisplacementShader:
    """Displaces the stroke in the shape of a sine wave."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyTVertexRemoverShader:
    """Removes t-vertices from the stroke."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyTVertexThickenerShader:
    """Thickens TVertices (visual intersections between two edges)."""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyTimeColorShader:
    """Assigns a grayscale value that increases for every vertex.
    The brightness will increase along the stroke.
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyTipRemoverShader:
    """Removes the tips of the stroke.Undocumented"""

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """

class pyZDependingThicknessShader:
    """Assigns thickness based on an objects local Z depth (point
    closest to camera is 1, point furthest from camera is zero).
    """

    def shade(self, stroke) -> None:
        """

        :param stroke:
        """
