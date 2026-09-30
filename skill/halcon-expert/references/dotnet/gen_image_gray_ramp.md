# GenImageGrayRamp (Operator)

## Name

`GenImageGrayRamp` — Create a gray value ramp.

## Signature

`static void HOperatorSet.GenImageGrayRamp(out HObject imageGrayRamp, HTuple alpha, HTuple beta, HTuple mean, HTuple row, HTuple column, HTuple width, HTuple height)`

`void HImage.GenImageGrayRamp(double alpha, double beta, double mean, int row, int column, int width, int height)`

## Description

The operator `GenImageGrayRamp` creates a gray value
ramp according to the following equation:
*`imageGrayRamp`*(r,c) = *`alpha`*(r-*`row`*) + *`beta`*(c-*`column`*) + *`mean`*
The size of the image is determined by *`width`* and *`height`*
The gray values are of the type byte.
Gray values outside the valid area are clipped.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageGrayRamp`** (output_object)  image `→` [HImage](HImage.md) (byte)

Created image with new image matrix.

**`alpha`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Gradient in line direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`beta`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Gradient in column direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`mean`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Mean gray value.

Default:
128

Suggested values:
0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 255.0

Minimum increment:
1

Recommended increment:
10

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Line index of reference point.

Default:
256

Suggested values:
128, 256, 512, 1024

Minimum increment:
1

Recommended increment:
10

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column index of reference point.

Default:
256

Suggested values:
128, 256, 512, 1024

Minimum increment:
1

Recommended increment:
10

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

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

If the parameter values are correct `GenImageGrayRamp`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`MomentsGrayPlane`

## Possible Successors

`PaintRegion`,
`ReduceDomain`,
`GetImagePointer1`,
`CopyObj`

## Alternatives

`GenImage1`

## See also

`ReduceDomain`,
`PaintGray`,
`GenImageConst`

## Module

Foundation
