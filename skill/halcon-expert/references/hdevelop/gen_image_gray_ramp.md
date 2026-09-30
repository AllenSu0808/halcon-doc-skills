# gen_image_gray_ramp (Operator)

## Name

`gen_image_gray_ramp` — Create a gray value ramp.

## Signature

`gen_image_gray_ramp( : ImageGrayRamp : Alpha, Beta, Mean, Row, Column, Width, Height : )`

## Description

The operator `gen_image_gray_ramp` creates a gray value
ramp according to the following equation:
*`ImageGrayRamp`*(r,c) = *`Alpha`*(r-*`Row`*) + *`Beta`*(c-*`Column`*) + *`Mean`*
The size of the image is determined by *`Width`* and *`Height`*
The gray values are of the type byte.
Gray values outside the valid area are clipped.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageGrayRamp`** (output_object)  image `→` object (byte)

Created image with new image matrix.

**`Alpha`** (input_control)  real `→`  (real)

Gradient in line direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`Beta`** (input_control)  real `→`  (real)

Gradient in column direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`Mean`** (input_control)  real `→`  (real)

Mean gray value.

Default:
128

Suggested values:
0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 255.0

Minimum increment:
1

Recommended increment:
10

**`Row`** (input_control)  point.y `→`  (integer)

Line index of reference point.

Default:
256

Suggested values:
128, 256, 512, 1024

Minimum increment:
1

Recommended increment:
10

**`Column`** (input_control)  point.x `→`  (integer)

Column index of reference point.

Default:
256

Suggested values:
128, 256, 512, 1024

Minimum increment:
1

Recommended increment:
10

**`Width`** (input_control)  extent.x `→`  (integer)

Width of image.

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

**`Height`** (input_control)  extent.y `→`  (integer)

Height of image.

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
