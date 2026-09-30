# polar_trans_region_inv (Operator)

## Name

`polar_trans_region_inv` — Transform a region in polar coordinates back to Cartesian
coordinates.

## Signature

`polar_trans_region_inv(PolarRegion : XYTransRegion : Row, Column, AngleStart, AngleEnd, RadiusStart, RadiusEnd, WidthIn, HeightIn, Width, Height, Interpolation : )`

## Description

`polar_trans_region_inv` transforms the polar coordinate
representation of a region, stored in *`PolarRegion`*, back
onto an annular arc in Cartesian coordinates, described by the radii
*`RadiusStart`* and *`RadiusEnd`* and the angles
*`AngleStart`* and *`AngleEnd`* with the center point
located at (*`Row`*, *`Column`*). All of these values can
be chosen as real numbers. In addition, the dimensions of the
virtual image containing the region *`PolarRegion`* must be
given in *`WidthIn`* and
*`HeightIn`*. *`WidthIn`*-1 is the column coordinate
corresponding to *`AngleEnd`* and *`HeightIn`*-1 is the
row coordinate corresponding to
*`RadiusEnd`*. *`AngleStart`* and *`RadiusStart`*
correspond to column and row coordinate *0*. Furthermore,
the dimensions *`Width`* and *`Height`* of the virtual
output image containing the transformed region
*`XYTransRegion`* are required.

The angles and radii are inclusive, which means that the row
coordinate *0* in *`PolarRegion`* will be mapped onto a
a circle with a distance of *`RadiusStart`* pixels from the
specified center and the row with the coordinate
*`HeightIn`*-1 will be mapped onto a circle of radius
*`RadiusEnd`*. This applies to *`AngleStart`*,
*`AngleEnd`*, and *`WidthIn`* in an analogous way.

The parameter *`Interpolation`* is used to select the
interpolation method *'bilinear'* or
*'nearest_neighbor'*. Setting *`Interpolation`* to
*'bilinear'* leads to smoother region boundaries, especially
if regions are enlarged. However, the runtime increases
significantly.

`polar_trans_region_inv` is the inverse function of
[`polar_trans_region`](polar_trans_region.md).

The call sequence:

|  |
| --- |
| `polar_trans_region(Region, PolarRegion, Row, Column, rad(360), 0, 0 Radius, Width, Height, 'nearest_neighbor')` |
| `polar_trans_region_inv(PolarRegion, XYTransRegion, Row, Column, rad(360), 0, 0, Radius, Width, Height, Width, Height, 'nearest_neighbor')` |

returns the region `Region`, restricted to the circle around
(`Row`, `Column`) with radius `Radius`, as its
output region *`XYTransRegion`*.

If more than one region is passed in *`PolarRegion`*, their
Cartesian transformations are computed individually and stored as a
tuple in *`XYTransRegion`*. Please note that the indices of an
input region and its transformation only correspond if the system
variable *'store_empty_regions'* is set to *'false'*
(see [`set_system`](set_system.md)). Otherwise empty output regions are
discarded and the length of the input tuple *`PolarRegion`* is
most likely not equal to the length of the output tuple
*`XYTransRegion`*.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

If *`Width`* or *`Height`* are chosen greater than the
dimensions of the current image, the system variable
*'clip_region'* should be set to *'false'* (see
[`set_system`](set_system.md)). Otherwise, an output region that does not lie
within the dimensions of the current image can produce an error
message.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`PolarRegion`** (input_object)  region(-array) `→` object

Input region.

**`XYTransRegion`** (output_object)  region(-array) `→` object

Output region.

**`Row`** (input_control)  number `→`  (real / integer)

Row coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 240, 256, 480, 512

Value range:
`-131068
≤
Row
≤
131068`

**`Column`** (input_control)  number `→`  (real / integer)

Column coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 256, 320, 512, 640

Value range:
`-131068
≤
Column
≤
131068`

**`AngleStart`** (input_control)  angle.rad `→`  (real)

Angle of the ray to map the column coordinate *0*
of *`PolarRegion`* to.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

Value range:
`-6.2831853
≤
AngleStart
≤
6.2831853`

**`AngleEnd`** (input_control)  angle.rad `→`  (real)

Angle of the ray to map the column coordinate
*`WidthIn`*-1 of *`PolarRegion`* to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

Value range:
`-6.2831853
≤
AngleEnd
≤
6.2831853`

**`RadiusStart`** (input_control)  number `→`  (real / integer)

Radius of the circle to map the row coordinate
*0* of *`PolarRegion`* to.

Default:
0

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
RadiusStart
≤
32767`

**`RadiusEnd`** (input_control)  number `→`  (real / integer)

Radius of the circle to map the row coordinate
*`HeightIn`*-1 of *`PolarRegion`* to.

Default:
100

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
RadiusEnd
≤
32767`

**`WidthIn`** (input_control)  extent.x `→`  (integer)

Width of the virtual input image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`2
≤
WidthIn
≤
32767`

**`HeightIn`** (input_control)  extent.y `→`  (integer)

Height of the virtual input image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`2
≤
HeightIn
≤
32767`

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the virtual output image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`1
≤
Width
≤
32767`

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the virtual output image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`1
≤
Height
≤
32767`

**`Interpolation`** (input_control)  string `→`  (string)

Interpolation method for the transformation.

Default:
'nearest_neighbor'

List of values:
'bilinear', 'nearest_neighbor'

## See also

`polar_trans_image_ext`,
`polar_trans_image_inv`,
`polar_trans_region`,
`polar_trans_contour_xld`,
`polar_trans_contour_xld_inv`

## Module

Foundation
