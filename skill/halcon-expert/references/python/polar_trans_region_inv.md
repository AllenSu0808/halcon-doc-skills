# polar_trans_region_inv (Operator)

## Name

`polar_trans_region_inv` — Transform a region in polar coordinates back to Cartesian
coordinates.

## Signature

`def polar_trans_region_inv(polar_region: HObject, row: Union[int, float], column: Union[int, float], angle_start: float, angle_end: float, radius_start: Union[int, float], radius_end: Union[int, float], width_in: int, height_in: int, width: int, height: int, interpolation: str) -> HObject`

## Description

`polar_trans_region_inv` transforms the polar coordinate
representation of a region, stored in *`polar_region`*, back
onto an annular arc in Cartesian coordinates, described by the radii
*`radius_start`* and *`radius_end`* and the angles
*`angle_start`* and *`angle_end`* with the center point
located at (*`row`*, *`column`*). All of these values can
be chosen as real numbers. In addition, the dimensions of the
virtual image containing the region *`polar_region`* must be
given in *`width_in`* and
*`height_in`*. *`width_in`*-1 is the column coordinate
corresponding to *`angle_end`* and *`height_in`*-1 is the
row coordinate corresponding to
*`radius_end`*. *`angle_start`* and *`radius_start`*
correspond to column and row coordinate *0*. Furthermore,
the dimensions *`width`* and *`height`* of the virtual
output image containing the transformed region
*`xytrans_region`* are required.

The angles and radii are inclusive, which means that the row
coordinate *0* in *`polar_region`* will be mapped onto a
a circle with a distance of *`radius_start`* pixels from the
specified center and the row with the coordinate
*`height_in`*-1 will be mapped onto a circle of radius
*`radius_end`*. This applies to *`angle_start`*,
*`angle_end`*, and *`width_in`* in an analogous way.

The parameter *`interpolation`* is used to select the
interpolation method *"bilinear"* or
*"nearest_neighbor"*. Setting *`interpolation`* to
*"bilinear"* leads to smoother region boundaries, especially
if regions are enlarged. However, the runtime increases
significantly.

`polar_trans_region_inv` is the inverse function of
[`polar_trans_region`](polar_trans_region.md).

The call sequence:

|  |
| --- |
| `polar_trans_region(Region, PolarRegion, Row, Column, rad(360), 0, 0 Radius, Width, Height, 'nearest_neighbor')` |
| `polar_trans_region_inv(PolarRegion, XYTransRegion, Row, Column, rad(360), 0, 0, Radius, Width, Height, Width, Height, 'nearest_neighbor')` |

returns the region `region`, restricted to the circle around
(`row`, `column`) with radius `radius`, as its
output region *`xytrans_region`*.

If more than one region is passed in *`polar_region`*, their
Cartesian transformations are computed individually and stored as a
tuple in *`xytrans_region`*. Please note that the indices of an
input region and its transformation only correspond if the system
variable *"store_empty_regions"* is set to *"false"*
(see [`set_system`](set_system.md)). Otherwise empty output regions are
discarded and the length of the input tuple *`polar_region`* is
most likely not equal to the length of the output tuple
*`xytrans_region`*.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

If *`width`* or *`height`* are chosen greater than the
dimensions of the current image, the system variable
*"clip_region"* should be set to *"false"* (see
[`set_system`](set_system.md)). Otherwise, an output region that does not lie
within the dimensions of the current image can produce an error
message.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`polar_region`** (input_object)  region(-array) `→` HObject

Input region.

**`xytrans_region`** (output_object)  region(-array) `→` HObject

Output region.

**`row`** (input_control)  number `→` Union[int, float]

Row coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 240, 256, 480, 512

Value range:
`-131068
≤
row
≤
131068`

**`column`** (input_control)  number `→` Union[int, float]

Column coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 256, 320, 512, 640

Value range:
`-131068
≤
column
≤
131068`

**`angle_start`** (input_control)  angle.rad `→` float

Angle of the ray to map the column coordinate *0*
of *`polar_region`* to.

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
*`width_in`*-1 of *`polar_region`* to.

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
*0* of *`polar_region`* to.

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
*`height_in`*-1 of *`polar_region`* to.

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
`2
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
`2
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
`1
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
`1
≤
height
≤
32767`

**`interpolation`** (input_control)  string `→` str

Interpolation method for the transformation.

Default:
"nearest_neighbor"

List of values:
"bilinear", "nearest_neighbor"

## See also

`polar_trans_image_ext`,
`polar_trans_image_inv`,
`polar_trans_region`,
`polar_trans_contour_xld`,
`polar_trans_contour_xld_inv`

## Module

Foundation
