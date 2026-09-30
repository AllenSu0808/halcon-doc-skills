# PolarTransRegionInv (Operator)

## Name

`PolarTransRegionInv` — Transform a region in polar coordinates back to Cartesian
coordinates.

## Signature

`static void HOperatorSet.PolarTransRegionInv(HObject polarRegion, out HObject XYTransRegion, HTuple row, HTuple column, HTuple angleStart, HTuple angleEnd, HTuple radiusStart, HTuple radiusEnd, HTuple widthIn, HTuple heightIn, HTuple width, HTuple height, HTuple interpolation)`

`HRegion HRegion.PolarTransRegionInv(HTuple row, HTuple column, double angleStart, double angleEnd, HTuple radiusStart, HTuple radiusEnd, int widthIn, int heightIn, int width, int height, string interpolation)`

`HRegion HRegion.PolarTransRegionInv(double row, double column, double angleStart, double angleEnd, double radiusStart, double radiusEnd, int widthIn, int heightIn, int width, int height, string interpolation)`

## Description

`PolarTransRegionInv` transforms the polar coordinate
representation of a region, stored in *`polarRegion`*, back
onto an annular arc in Cartesian coordinates, described by the radii
*`radiusStart`* and *`radiusEnd`* and the angles
*`angleStart`* and *`angleEnd`* with the center point
located at (*`row`*, *`column`*). All of these values can
be chosen as real numbers. In addition, the dimensions of the
virtual image containing the region *`polarRegion`* must be
given in *`widthIn`* and
*`heightIn`*. *`widthIn`*-1 is the column coordinate
corresponding to *`angleEnd`* and *`heightIn`*-1 is the
row coordinate corresponding to
*`radiusEnd`*. *`angleStart`* and *`radiusStart`*
correspond to column and row coordinate *0*. Furthermore,
the dimensions *`width`* and *`height`* of the virtual
output image containing the transformed region
*`XYTransRegion`* are required.

The angles and radii are inclusive, which means that the row
coordinate *0* in *`polarRegion`* will be mapped onto a
a circle with a distance of *`radiusStart`* pixels from the
specified center and the row with the coordinate
*`heightIn`*-1 will be mapped onto a circle of radius
*`radiusEnd`*. This applies to *`angleStart`*,
*`angleEnd`*, and *`widthIn`* in an analogous way.

The parameter *`interpolation`* is used to select the
interpolation method *"bilinear"* or
*"nearest_neighbor"*. Setting *`interpolation`* to
*"bilinear"* leads to smoother region boundaries, especially
if regions are enlarged. However, the runtime increases
significantly.

`PolarTransRegionInv` is the inverse function of
[`PolarTransRegion`](polar_trans_region.md).

The call sequence:

|  |
| --- |
| `polar_trans_region(Region, PolarRegion, Row, Column, rad(360), 0, 0 Radius, Width, Height, 'nearest_neighbor')` |
| `polar_trans_region_inv(PolarRegion, XYTransRegion, Row, Column, rad(360), 0, 0, Radius, Width, Height, Width, Height, 'nearest_neighbor')` |

returns the region `region`, restricted to the circle around
(`row`, `column`) with radius `radius`, as its
output region *`XYTransRegion`*.

If more than one region is passed in *`polarRegion`*, their
Cartesian transformations are computed individually and stored as a
tuple in *`XYTransRegion`*. Please note that the indices of an
input region and its transformation only correspond if the system
variable *"store_empty_regions"* is set to *"false"*
(see [`SetSystem`](set_system.md)). Otherwise empty output regions are
discarded and the length of the input tuple *`polarRegion`* is
most likely not equal to the length of the output tuple
*`XYTransRegion`*.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

If *`width`* or *`height`* are chosen greater than the
dimensions of the current image, the system variable
*"clip_region"* should be set to *"false"* (see
[`SetSystem`](set_system.md)). Otherwise, an output region that does not lie
within the dimensions of the current image can produce an error
message.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`polarRegion`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input region.

**`XYTransRegion`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Output region.

**`row`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`column`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the ray to map the column coordinate *0*
of *`polarRegion`* to.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

Value range:
`-6.2831853
≤
angleStart
≤
6.2831853`

**`angleEnd`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the ray to map the column coordinate
*`widthIn`*-1 of *`polarRegion`* to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

Value range:
`-6.2831853
≤
angleEnd
≤
6.2831853`

**`radiusStart`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circle to map the row coordinate
*0* of *`polarRegion`* to.

Default:
0

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radiusStart
≤
32767`

**`radiusEnd`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circle to map the row coordinate
*`heightIn`*-1 of *`polarRegion`* to.

Default:
100

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radiusEnd
≤
32767`

**`widthIn`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the virtual input image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`2
≤
widthIn
≤
32767`

**`heightIn`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the virtual input image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`2
≤
heightIn
≤
32767`

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

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

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Interpolation method for the transformation.

Default:
"nearest_neighbor"

List of values:
"bilinear", "nearest_neighbor"

## See also

`PolarTransImageExt`,
`PolarTransImageInv`,
`PolarTransRegion`,
`PolarTransContourXld`,
`PolarTransContourXldInv`

## Module

Foundation
