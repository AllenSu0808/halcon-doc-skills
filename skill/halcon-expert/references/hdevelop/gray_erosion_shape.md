# gray_erosion_shape (Operator)

## Name

`gray_erosion_shape` — Determine the minimum gray value within a selected mask.

## Signature

`gray_erosion_shape(Image : ImageMin : MaskHeight, MaskWidth, MaskShape : )`

## Description

`gray_erosion_shape` calculates the minimum gray value of the input
image *`Image`* within a mask of shape *`MaskShape`*,
vertical size *`MaskHeight`* and horizontal size *`MaskWidth`*
for each image point.
The resulting image is returned in *`ImageMin`*.

If the parameters *`MaskHeight`* or *`MaskWidth`* are of the
type integer and are even, they are changed to the next larger odd value.
In contrast, if at least one of the two parameters is of the type float, the
input image *`Image`* is transformed with both the next larger and
the next smaller odd mask size, and the output image *`ImageMin`* is
interpolated from the two intermediate images. Therefore, note that
`gray_erosion_shape` returns different results for mask sizes of,
e.g., *4* and *4.0*!

In case of the values
'rhombus' and 'octagon' for the *`MaskShape`* control parameter,
*`MaskHeight`* and *`MaskWidth`* must be equal. The parameter
value 'octagon' for *`MaskShape`* denotes an equilateral octagonal
mask which is a suitable approximation for a circular structure.
At the border of the image the gray values are mirrored.

## Attention

Note that `gray_erosion_shape` requires considerably more time for
mask sizes of type float than for mask sizes of type integer. This is
especially true for rectangular masks with different width and height!

`gray_erosion_shape` can be executed on OpenCL devices. In case of
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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte* / uint2*) **allowed for compute devices*

Image for which the minimum gray values are to
be calculated.

**`ImageMin`** (output_object)  (multichannel-)image(-array) `→` object (byte / uint2)

Image containing the minimum gray values.

**`MaskHeight`** (input_control)  extent.y `→`  (real / integer)

Height of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`1.0
≤
MaskHeight`

**`MaskWidth`** (input_control)  extent.x `→`  (real / integer)

Width of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`1.0
≤
MaskWidth`

**`MaskShape`** (input_control)  string `→`  (string)

Shape of the mask.

Default:
'octagon'

List of values:
'octagon', 'rectangle', 'rhombus'

## Result

`gray_erosion_shape` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Alternatives

`gray_erosion`,
`gray_erosion_rect`

## See also

`gray_opening_shape`,
`gray_closing_shape`,
`gray_skeleton`

## Module

Foundation
