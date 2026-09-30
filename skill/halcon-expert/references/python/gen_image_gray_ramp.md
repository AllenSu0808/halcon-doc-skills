# gen_image_gray_ramp (Operator)

## Name

`gen_image_gray_ramp` — Create a gray value ramp.

## Signature

`def gen_image_gray_ramp(alpha: float, beta: float, mean: float, row: int, column: int, width: int, height: int) -> HObject`

## Description

The operator `gen_image_gray_ramp` creates a gray value
ramp according to the following equation:
*`image_gray_ramp`*(r,c) = *`alpha`*(r-*`row`*) + *`beta`*(c-*`column`*) + *`mean`*
The size of the image is determined by *`width`* and *`height`*
The gray values are of the type byte.
Gray values outside the valid area are clipped.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_gray_ramp`** (output_object)  image `→` HObject (byte)

Created image with new image matrix.

**`alpha`** (input_control)  real `→` float

Gradient in line direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`beta`** (input_control)  real `→` float

Gradient in column direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`mean`** (input_control)  real `→` float

Mean gray value.

Default:
128

Suggested values:
0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 255.0

Minimum increment:
1

Recommended increment:
10

**`row`** (input_control)  point.y `→` int

Line index of reference point.

Default:
256

Suggested values:
128, 256, 512, 1024

Minimum increment:
1

Recommended increment:
10

**`column`** (input_control)  point.x `→` int

Column index of reference point.

Default:
256

Suggested values:
128, 256, 512, 1024

Minimum increment:
1

Recommended increment:
10

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

If the parameter values are correct `gen_image_gray_ramp`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`moments_gray_plane`

## Possible Successors

`paint_region`,
`reduce_domain`,
`get_image_pointer1`,
`copy_obj`

## Alternatives

`gen_image1`

## See also

`reduce_domain`,
`paint_gray`,
`gen_image_const`

## Module

Foundation
