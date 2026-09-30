# GrayClosingShape (Operator)

## Name

`GrayClosingShape` — Perform a gray value closing with a selected mask.

## Signature

`static void HOperatorSet.GrayClosingShape(HObject image, out HObject imageClosing, HTuple maskHeight, HTuple maskWidth, HTuple maskShape)`

`HImage HImage.GrayClosingShape(HTuple maskHeight, HTuple maskWidth, string maskShape)`

`HImage HImage.GrayClosingShape(double maskHeight, double maskWidth, string maskShape)`

## Description

`GrayClosingShape` applies a gray value closing to the input image
*`image`* with the structuring element of shape *`maskShape`*.
The mask's offset values are 0 and its horizontal and vertical size is
defined by *`maskHeight`* and *`maskWidth`*. The resulting image
is returned in *`imageClosing`*.

If the parameters *`maskHeight`* or *`maskWidth`* are of the
type integer and are even, they are changed to the next larger odd value.
In contrast, if at least one of the two parameters is of the type float, the
input image *`image`* is transformed with both the next larger and
the next smaller odd mask size, and the output image *`imageClosing`*
is interpolated from the two intermediate images. Therefore, note that
`GrayClosingShape` returns different results for mask sizes of,
e.g., *4* and *4.0*!

In case of the values
'rhombus' and 'octagon' for the *`maskShape`* control parameter,
*`maskHeight`* and *`maskWidth`* must be equal. The parameter
value 'octagon' for *`maskShape`* denotes an equilateral octagonal
mask which is a suitable approximation for a circular structure.
At the border of the image the gray values are mirrored.

The gray value closing of an image i with a structuring element
s is defined as
$$i\cdot s = (i\oplus s) \ominus s$$ ![figure](../assets/96c1630e17b95b14.svg)
i.e., a dilation of the image with s followed by an erosion with
s (see [`GrayDilationShape`](gray_dilation_shape.md) and [`GrayErosionShape`](gray_erosion_shape.md)).

## Attention

Note that `GrayClosingShape` requires considerably more time for
mask sizes of type float than for mask sizes of type integer. This is
especially true for rectangular masks with different width and height!

`GrayClosingShape` can be executed on OpenCL devices. In case of
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

Image for which the minimum gray values are to
be calculated.

**`imageClosing`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Image containing the minimum gray values.

**`maskHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*double* / int / long)

Height of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`1.0
≤
maskHeight
≤
511.0`

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*double* / int / long)

Width of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`1.0
≤
maskWidth
≤
511.0`

**`maskShape`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Shape of the mask.

Default:
"octagon"

List of values:
"octagon", "rectangle", "rhombus"

## Result

`GrayClosingShape` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Alternatives

`GrayClosing`

## See also

`GrayDilationShape`,
`GrayErosionShape`,
`Closing`

## Module

Foundation
