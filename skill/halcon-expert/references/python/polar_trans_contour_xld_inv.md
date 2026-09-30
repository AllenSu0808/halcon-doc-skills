# polar_trans_contour_xld_inv (Operator)

## Name

`polar_trans_contour_xld_inv` — Transform a contour in polar coordinates back to Cartesian coordinates

## Signature

`def polar_trans_contour_xld_inv(polar_contour: HObject, row: Union[int, float], column: Union[int, float], angle_start: float, angle_end: float, radius_start: Union[int, float], radius_end: Union[int, float], width_in: int, height_in: int, width: int, height: int) -> HObject`

## Description

`polar_trans_contour_xld_inv` transforms the polar coordinate
representation of a contour, stored in *`polar_contour`*, back
onto an annular arc in Cartesian coordinates, described by the radii
*`radius_start`* and *`radius_end`* and the angles
*`angle_start`* and *`angle_end`* with the center point
located at (*`row`*, *`column`*). All of these values can
be chosen as real numbers. In addition, the dimensions of the
virtual image containing the contour *`polar_contour`* must be
given in *`width_in`* and
*`height_in`*. *`width_in`*-1 is the column coordinate
corresponding to *`angle_end`* and *`height_in`*-1 is the
row coordinate corresponding to
*`radius_end`*. *`angle_start`* and *`radius_start`*
correspond to column and row coordinate *0*. Furthermore, the
dimensions *`width`* and *`height`* of the virtual output
image containing the transformed contour *`xytrans_contour`* are
required. The output contour is cropped at the borders of this
virtual output image.

`polar_trans_contour_xld_inv` is the inverse function of
[`polar_trans_contour_xld`](polar_trans_contour_xld.md).

The call sequence:

|  |
| --- |
| `polar_trans_contour_xld(Contour, PolarContour, Row, Column, rad(360), 0, 0, Radius, Width, Height)` |
| `polar_trans_contour_xld_inv(PolarContour, XYTransContour, Row, Column, rad(360), 0, 0, Radius, Width, Height, WidthOut, HeightOut)` |

returns the contour `contour`, restricted to the circle
around (`row`, `column`) with radius `radius`,
as its output contour *`xytrans_contour`*.

Note that *`xytrans_contour`* can consist of more than one
contour because *`polar_contour`* may be cropped at the borders
of the virtual output image given by *`width`* and
*`height`*.

If more than one contour is passed in *`polar_contour`*, their
transformations are computed individually and stored as a tuple in
*`xytrans_contour`*. However, since one contour may be
transformed into several contours, there is no relation between the
indices of the contours in the input tuple *`polar_contour`* and
the indices in the output tuple *`xytrans_contour`*.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

Only the contour points are transformed. As the polar transformation
is not affine, `polar_trans_contour_xld_inv` only produces
reliable results if the spacing of the contour points is
small. Existing attributes are not transformed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`polar_contour`** (input_object)  xld_cont(-array) `→` HObject

Input contour.

**`xytrans_contour`** (output_object)  xld_cont(-array) `→` HObject

Output contour.

**`row`** (input_control)  number `→` Union[int, float]

Row coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 240, 256, 480, 512

**`column`** (input_control)  number `→` Union[int, float]

Column coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 256, 320, 512, 640

**`angle_start`** (input_control)  angle.rad `→` float

Angle of the ray to map the column coordinate *0*
of *`polar_contour`* to.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

Value range:
`-6.2831853
≤
angle_start
≤
6.2831853`

**`angle_end`** (input_control)  angle.rad `→` float

Angle of the ray to map the column coordinate
*`width_in`*-1 of *`polar_contour`* to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

Value range:
`-6.2831853
≤
angle_end
≤
6.2831853`

**`radius_start`** (input_control)  number `→` Union[int, float]

Radius of the circle to map the row coordinate
*0* of *`polar_contour`* to.

Default:
0

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radius_start
≤
32767`

**`radius_end`** (input_control)  number `→` Union[int, float]

Radius of the circle to map the row coordinate
*`height_in`*-1 of *`polar_contour`* to.

Default:
100

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radius_end
≤
32767`

**`width_in`** (input_control)  extent.x `→` int

Width of the virtual input image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`0
≤
width_in
≤
32767`

**`height_in`** (input_control)  extent.y `→` int

Height of the virtual input image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`0
≤
height_in
≤
32767`

**`width`** (input_control)  extent.x `→` int

Width of the virtual output image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`0
≤
width
≤
32767`

**`height`** (input_control)  extent.y `→` int

Height of the virtual output image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`0
≤
height
≤
32767`

## See also

`polar_trans_image_ext`,
`polar_trans_image_inv`,
`polar_trans_region`,
`polar_trans_region_inv`,
`polar_trans_contour_xld`

## Module

Foundation
