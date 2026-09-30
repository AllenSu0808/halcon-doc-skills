# gen_random_regions (Operator)

## Name

`gen_random_regions` — Create random regions like circles, rectangles and ellipses.

## Signature

`def gen_random_regions(type: str, width_min: Union[float, int], width_max: Union[float, int], height_min: Union[float, int], height_max: Union[float, int], phi_min: Union[float, int], phi_max: Union[float, int], num_regions: int, width: int, height: int) -> HObject`

## Description

The operator `gen_random_regions` generates regions,
whose parameters are determined at random within the given limits,
and returns them in *`regions`*.

The parameter *`num_regions`* determines how many regions are created.

The position is always random and cannot be determined by parameters,
but the center of every region lies in the pixel area
[0...*`width`*-1]
[0...*`height`*-1].

The parameter *`type`* defines the type of the regions.
The meaning of the lower and upper limits depends on *`type`*:

- *"rectangle1"*: Minimum/maximum width/height.

  *`phi_min`* and *`phi_max`* are without further significance.
- *"rectangle2"*: Minimum/maximum half edge lengths,
  minimum/maximum rotation angle.
  Thereby the larger value is used for the first half edge length.
  The parameters correspond to the parameters `length_1`,
  `length_2`, and `phi` of [`gen_rectangle2`](gen_rectangle2.md).
- *"circle"*: *`width_min`* and *`width_max`* determine
  the minimum and maximum radii.
  The parameters correspond to the parameter `radius` in
  [`gen_circle`](gen_circle.md).

  *`height_min`* and *`height_max`* as well as
  *`phi_min`* and *`phi_max`* are without further significance.
- *"ellipse"*: Minimum/maximum half-radii and minimal/maximum
  rotation angle.
  Thereby the larger value is used for the first half-radius.
  The parameters correspond to the parameters `radius_1`,
  `radius_2`, and `phi` in [`gen_ellipse`](gen_ellipse.md).
- *"ring"*: Minimum/maximum radii, whereby the larger one
  determines the radius of the larger circle and the smaller one the radius
  of the hole.

  *`phi_min`* and *`phi_max`* are without further significance.

The random parameters are generated using the C function “nrand48()”.
See the parameter *"seed_rand"* of [`set_system`](set_system.md) for
information on the used random seed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (output_object)  region-array `→` HObject

Created regions.

**`type`** (input_control)  string `→` str

Type of regions to be created.

Default:
"circle"

List of values:
"circle", "ellipse", "rectangle1", "rectangle2", "ring"

**`width_min`** (input_control)  number `→` Union[float, int]

Minimum object characteristic, depending on type and value.

Default:
10.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`0
≤
width_min` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`width_max`** (input_control)  number `→` Union[float, int]

Maximum object characteristic, depending on type and value.

Default:
20.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`width_max` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`WidthMin <= WidthMax`

**`height_min`** (input_control)  number `→` Union[float, int]

Minimum object characteristic, depending on type and value.

Default:
10.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`0
≤
height_min` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`height_max`** (input_control)  number `→` Union[float, int]

Maximum object characteristic, depending on type and value.

Default:
30.0

Suggested values:
1.0, 3.0, 5.0, 10.0, 20.0, 40.0, 80.0

Value range:
`height_max` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`HeightMin <= HeightMax`

**`phi_min`** (input_control)  number `→` Union[float, int]

Minimum rotation angle of the region.

Default:
-0.7854

Suggested values:
0.0, 0.1, 0.3, 0.6, 0.9, 1.2, 1.5

Value range:
`0.0
≤
phi_min
≤
6.28` (lin)

Restriction:
`PhiMin > 0`

**`phi_max`** (input_control)  number `→` Union[float, int]

Maximum rotation angle of the region.

Default:
0.7854

Suggested values:
0.0, 0.1, 0.3, 0.6, 0.9, 1.2, 1.5

Value range:
`0.0
≤
phi_max
≤
6.28` (lin)

Restriction:
`PhiMax > 0`

**`num_regions`** (input_control)  integer `→` int

Number of regions.

Default:
100

Suggested values:
1, 5, 20, 100, 200, 500, 1000, 2000

Value range:
`1
≤
num_regions` (lin)

Minimum increment:
1

Recommended increment:
10

**`width`** (input_control)  integer `→` int

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

**`height`** (input_control)  integer `→` int

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
