# gen_random_regions (Operator)

## Name

`gen_random_regions` — Create random regions like circles, rectangles and ellipses.

## Signature

`gen_random_regions( : Regions : Type, WidthMin, WidthMax, HeightMin, HeightMax, PhiMin, PhiMax, NumRegions, Width, Height : )`

## Description

The operator `gen_random_regions` generates regions,
whose parameters are determined at random within the given limits,
and returns them in *`Regions`*.

The parameter *`NumRegions`* determines how many regions are created.

The position is always random and cannot be determined by parameters,
but the center of every region lies in the pixel area
[0...*`Width`*-1]
[0...*`Height`*-1].

The parameter *`Type`* defines the type of the regions.
The meaning of the lower and upper limits depends on *`Type`*:

- *'rectangle1'*: Minimum/maximum width/height.

  *`PhiMin`* and *`PhiMax`* are without further significance.
- *'rectangle2'*: Minimum/maximum half edge lengths,
  minimum/maximum rotation angle.
  Thereby the larger value is used for the first half edge length.
  The parameters correspond to the parameters `Length1`,
  `Length2`, and `Phi` of [`gen_rectangle2`](gen_rectangle2.md).
- *'circle'*: *`WidthMin`* and *`WidthMax`* determine
  the minimum and maximum radii.
  The parameters correspond to the parameter `Radius` in
  [`gen_circle`](gen_circle.md).

  *`HeightMin`* and *`HeightMax`* as well as
  *`PhiMin`* and *`PhiMax`* are without further significance.
- *'ellipse'*: Minimum/maximum half-radii and minimal/maximum
  rotation angle.
  Thereby the larger value is used for the first half-radius.
  The parameters correspond to the parameters `Radius1`,
  `Radius2`, and `Phi` in [`gen_ellipse`](gen_ellipse.md).
- *'ring'*: Minimum/maximum radii, whereby the larger one
  determines the radius of the larger circle and the smaller one the radius
  of the hole.

  *`PhiMin`* and *`PhiMax`* are without further significance.

The random parameters are generated using the C function “nrand48()”.
See the parameter *'seed_rand'* of [`set_system`](set_system.md) for
information on the used random seed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Regions`** (output_object)  region-array `→` object

Created regions.

**`Type`** (input_control)  string `→`  (string)

Type of regions to be created.

Default:
'circle'

List of values:
'circle', 'ellipse', 'rectangle1', 'rectangle2', 'ring'

**`WidthMin`** (input_control)  number `→`  (real / integer)

Minimum object characteristic, depending on type and value.

Default:
10.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`0
≤
WidthMin` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`WidthMax`** (input_control)  number `→`  (real / integer)

Maximum object characteristic, depending on type and value.

Default:
20.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`WidthMax` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`WidthMin <= WidthMax`

**`HeightMin`** (input_control)  number `→`  (real / integer)

Minimum object characteristic, depending on type and value.

Default:
10.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`0
≤
HeightMin` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`HeightMax`** (input_control)  number `→`  (real / integer)

Maximum object characteristic, depending on type and value.

Default:
30.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`HeightMax` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`HeightMin <= HeightMax`

**`PhiMin`** (input_control)  number `→`  (real / integer)

Minimum rotation angle of the region.

Default:
-0.7854

Suggested values:
0.0, 0.1, 0.3, 0.6, 0.9, 1.2, 1.5

Value range:
`0.0
≤
PhiMin
≤
6.28` (lin)

Restriction:
`PhiMin > 0`

**`PhiMax`** (input_control)  number `→`  (real / integer)

Maximum rotation angle of the region.

Default:
0.7854

Suggested values:
0.0, 0.1, 0.3, 0.6, 0.9, 1.2, 1.5

Value range:
`0.0
≤
PhiMax
≤
6.28` (lin)

Restriction:
`PhiMax > 0`

**`NumRegions`** (input_control)  integer `→`  (integer)

Number of regions.

Default:
100

Suggested values:
1, 5, 20, 100, 200, 500, 1000, 2000

Value range:
`1
≤
NumRegions` (lin)

Minimum increment:
1

Recommended increment:
10

**`Width`** (input_control)  integer `→`  (integer)

Maximum horizontal expansion of the centers.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
Width` (lin)

Minimum increment:
1

Recommended increment:
10

**`Height`** (input_control)  integer `→`  (integer)

Maximum vertical expansion of the centers.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
Height` (lin)

Minimum increment:
1

Recommended increment:
10

## Result

If the parameter values are correct `gen_random_regions` returns
the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is determined by
the operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`paint_region`

## Module

Foundation
