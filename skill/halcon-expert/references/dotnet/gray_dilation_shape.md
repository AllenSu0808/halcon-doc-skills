# GrayDilationShape (Operator)

## Name

`GrayDilationShape` — Determine the maximum gray value within a selected mask.

## Signature

`static void HOperatorSet.GrayDilationShape(HObject image, out HObject imageMax, HTuple maskHeight, HTuple maskWidth, HTuple maskShape)`

`HImage HImage.GrayDilationShape(HTuple maskHeight, HTuple maskWidth, string maskShape)`

`HImage HImage.GrayDilationShape(double maskHeight, double maskWidth, string maskShape)`

## Description

`GrayDilationShape` calculates the maximum gray value of the input
image *`image`* within a mask of shape *`maskShape`*,
vertical size *`maskHeight`* and horizontal size *`maskWidth`*
for each image point.
The resulting image is returned in *`imageMax`*.

If the parameters *`maskHeight`* or *`maskWidth`* are of the
type integer and are even, they are changed to the next larger odd value.
In contrast, if at least one of the two parameters is of the type float, the
input image *`image`* is transformed with both the next larger and
the next smaller odd mask size, and the output image *`imageMax`* is
interpolated from the two intermediate images. Therefore, note that
`GrayDilationShape` returns different results for mask sizes of,
e.g., *4* and *4.0*!

In case of the values
'rhombus' and 'octagon' for the *`maskShape`* control parameter,
*`maskHeight`* and *`maskWidth`* must be equal. The parameter
value 'octagon' for *`maskShape`* denotes an equilateral octagonal
mask which is a suitable approximation for a circular structure.
At the border of the image the gray values are mirrored.

## Attention

Note that `GrayDilationShape` requires considerably more time for
mask sizes of type float than for mask sizes of type integer. This is
especially true for rectangular masks with different width and height!

`GrayDilationShape` can be executed on OpenCL devices. In case of
mask sizes of type float the result can vary slightly from the CPU as the
interpolation is calculated in single precision on the OpenCL device.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / uint2*) **allowed for compute devices*

Image for which the maximum gray values are to
be calculated.

**`imageMax`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Image containing the maximum gray values.

**`maskHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*double* / int / long)

Height of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`1.0
≤
maskHeight`

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*double* / int / long)

Width of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`1.0
≤
maskWidth`

**`maskShape`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Shape of the mask.

Default:
"octagon"

List of values:
"octagon", "rectangle", "rhombus"

## Result

`GrayDilationShape` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Alternatives

`GrayDilation`,
`GrayDilationRect`

## See also

`GrayOpeningShape`,
`GrayClosingShape`,
`GraySkeleton`

## Module

Foundation
