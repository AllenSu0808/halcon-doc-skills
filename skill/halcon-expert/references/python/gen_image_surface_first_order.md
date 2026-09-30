# gen_image_surface_first_order (Operator)

## Name

`gen_image_surface_first_order` — Create a tilted gray surface with first order polynomial.

## Signature

`def gen_image_surface_first_order(type: str, alpha: float, beta: float, gamma: float, row: float, column: float, width: int, height: int) -> HObject`

## Description

The operator `gen_image_surface_first_order` creates a tilted
gray value surface according to the following equation:
$$\text{ImageSurface}(r,c) = \Alpha(r-Row) \\\n+ \Beta(c-Column) \\\n+ \Gamma$$ ![figure](../assets/5c7896e434c4cc64.svg)
The size of the image is determined by *`width`* and *`height`*.
The parameters *`row`* and *`column`* define the reference point
of the created gray surface. If [`fit_surface_first_order`](fit_surface_first_order.md) was used to
determine the parameters of the gray surface, this reference point should
correspond to the center of gravity that is used in the surface equation
(see [`fit_surface_first_order`](fit_surface_first_order.md)). Its coordinates can be computed as
follows:

|  |
| --- |
| [`intersection(ROI, Image, RegionIntersection)`](intersection.md) |
| `fit_surface_first_order(RegionIntersection, Image, Algorithm, Iterations, ClippingFactor, Alpha, Beta, Gamma)` |
| [`area_center(RegionIntersection, Area, Row, Column)`](area_center.md) |
| `gen_image_surface_first_order(ImageSurface, Type, Alpha, Beta, Gamma, Row, Column, Width, Height)` |

The gray values are of the type *`type`* (see [`gen_image_const`](gen_image_const.md)
for a detailed description of the pixel types).
Gray values outside the valid area are clipped.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_surface`** (output_object)  image `→` HObject (byte / uint2 / real)

Created image with new image matrix.

**`type`** (input_control)  string `→` str

Pixel type.

Default:
"byte"

List of values:
"byte", "real", "uint2"

**`alpha`** (input_control)  number `→` float

First order coefficient in vertical direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`beta`** (input_control)  number `→` float

First order coefficient in horizontal direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`gamma`** (input_control)  number `→` float

Zero order coefficient.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`row`** (input_control)  number `→` float

Row coordinate of the reference point of the surface.

Default:
256.0

Suggested values:
0.0, 128.0, 256.0, 512.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`column`** (input_control)  number `→` float

Column coordinate of the reference point of the surface.

Default:
256.0

Suggested values:
0.0, 128.0, 256.0, 512.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`width`** (input_control)  extent.x `→` int

Width of image.

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

**`height`** (input_control)  extent.y `→` int

Height of image.

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

If the parameter values are correct `gen_image_surface_first_order`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`fit_surface_first_order`

## Possible Successors

`sub_image`

## See also

`gen_image_gray_ramp`,
`gen_image_surface_second_order`,
`gen_image_const`

## Module

Foundation
