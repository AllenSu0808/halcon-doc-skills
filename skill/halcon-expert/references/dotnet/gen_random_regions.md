# GenRandomRegions (Operator)

## Name

`GenRandomRegions` — Create random regions like circles, rectangles and ellipses.

## Signature

`static void HOperatorSet.GenRandomRegions(out HObject regions, HTuple type, HTuple widthMin, HTuple widthMax, HTuple heightMin, HTuple heightMax, HTuple phiMin, HTuple phiMax, HTuple numRegions, HTuple width, HTuple height)`

`void HRegion.GenRandomRegions(string type, HTuple widthMin, HTuple widthMax, HTuple heightMin, HTuple heightMax, HTuple phiMin, HTuple phiMax, int numRegions, int width, int height)`

`void HRegion.GenRandomRegions(string type, double widthMin, double widthMax, double heightMin, double heightMax, double phiMin, double phiMax, int numRegions, int width, int height)`

## Description

The operator `GenRandomRegions` generates regions,
whose parameters are determined at random within the given limits,
and returns them in *`regions`*.

The parameter *`numRegions`* determines how many regions are created.

The position is always random and cannot be determined by parameters,
but the center of every region lies in the pixel area
[0...*`width`*-1]
[0...*`height`*-1].

The parameter *`type`* defines the type of the regions.
The meaning of the lower and upper limits depends on *`type`*:

- *"rectangle1"*: Minimum/maximum width/height.

  *`phiMin`* and *`phiMax`* are without further significance.
- *"rectangle2"*: Minimum/maximum half edge lengths,
  minimum/maximum rotation angle.
  Thereby the larger value is used for the first half edge length.
  The parameters correspond to the parameters `length1`,
  `length2`, and `phi` of [`GenRectangle2`](gen_rectangle2.md).
- *"circle"*: *`widthMin`* and *`widthMax`* determine
  the minimum and maximum radii.
  The parameters correspond to the parameter `radius` in
  [`GenCircle`](gen_circle.md).

  *`heightMin`* and *`heightMax`* as well as
  *`phiMin`* and *`phiMax`* are without further significance.
- *"ellipse"*: Minimum/maximum half-radii and minimal/maximum
  rotation angle.
  Thereby the larger value is used for the first half-radius.
  The parameters correspond to the parameters `radius1`,
  `radius2`, and `phi` in [`GenEllipse`](gen_ellipse.md).
- *"ring"*: Minimum/maximum radii, whereby the larger one
  determines the radius of the larger circle and the smaller one the radius
  of the hole.

  *`phiMin`* and *`phiMax`* are without further significance.

The random parameters are generated using the C function “nrand48()”.
See the parameter *"seed_rand"* of [`SetSystem`](set_system.md) for
information on the used random seed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Created regions.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of regions to be created.

Default:
"circle"

List of values:
"circle", "ellipse", "rectangle1", "rectangle2", "ring"

**`widthMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum object characteristic, depending on type and value.

Default:
10.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`0
≤
widthMin` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`widthMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum object characteristic, depending on type and value.

Default:
20.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`widthMax` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`WidthMin <= WidthMax`

**`heightMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum object characteristic, depending on type and value.

Default:
10.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`0
≤
heightMin` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`heightMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum object characteristic, depending on type and value.

Default:
30.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`heightMax` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`HeightMin <= HeightMax`

**`phiMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum rotation angle of the region.

Default:
-0.7854

Suggested values:
0.0, 0.1, 0.3, 0.6, 0.9, 1.2, 1.5

Value range:
`0.0
≤
phiMin
≤
6.28` (lin)

Restriction:
`PhiMin > 0`

**`phiMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum rotation angle of the region.

Default:
0.7854

Suggested values:
0.0, 0.1, 0.3, 0.6, 0.9, 1.2, 1.5

Value range:
`0.0
≤
phiMax
≤
6.28` (lin)

Restriction:
`PhiMax > 0`

**`numRegions`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of regions.

Default:
100

Suggested values:
1, 5, 20, 100, 200, 500, 1000, 2000

Value range:
`1
≤
numRegions` (lin)

Minimum increment:
1

Recommended increment:
10

**`width`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum horizontal expansion of the centers.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
width` (lin)

Minimum increment:
1

Recommended increment:
10

**`height`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum vertical expansion of the centers.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
height` (lin)

Minimum increment:
1

Recommended increment:
10

## Result

If the parameter values are correct `GenRandomRegions` returns
the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is determined by
the operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`PaintRegion`

## Module

Foundation
