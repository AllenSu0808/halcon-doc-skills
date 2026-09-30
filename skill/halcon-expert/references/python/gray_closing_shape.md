# gray_closing_shape (Operator)

## Name

`gray_closing_shape` — Perform a gray value closing with a selected mask.

## Signature

`def gray_closing_shape(image: HObject, mask_height: Union[int, float], mask_width: Union[int, float], mask_shape: str) -> HObject`

## Description

`gray_closing_shape` applies a gray value closing to the input image
*`image`* with the structuring element of shape *`mask_shape`*.
The mask's offset values are 0 and its horizontal and vertical size is
defined by *`mask_height`* and *`mask_width`*. The resulting image
is returned in *`image_closing`*.

If the parameters *`mask_height`* or *`mask_width`* are of the
type integer and are even, they are changed to the next larger odd value.
In contrast, if at least one of the two parameters is of the type float, the
input image *`image`* is transformed with both the next larger and
the next smaller odd mask size, and the output image *`image_closing`*
is interpolated from the two intermediate images. Therefore, note that
`gray_closing_shape` returns different results for mask sizes of,
e.g., *4* and *4.0*!

In case of the values
'rhombus' and 'octagon' for the *`mask_shape`* control parameter,
*`mask_height`* and *`mask_width`* must be equal. The parameter
value 'octagon' for *`mask_shape`* denotes an equilateral octagonal
mask which is a suitable approximation for a circular structure.
At the border of the image the gray values are mirrored.

The gray value closing of an image i with a structuring element
s is defined as
$$i\cdot s = (i\oplus s) \ominus s$$ ![figure](../assets/96c1630e17b95b14.svg)
i.e., a dilation of the image with s followed by an erosion with
s (see [`gray_dilation_shape`](gray_dilation_shape.md) and [`gray_erosion_shape`](gray_erosion_shape.md)).

## Attention

Note that `gray_closing_shape` requires considerably more time for
mask sizes of type float than for mask sizes of type integer. This is
especially true for rectangular masks with different width and height!

`gray_closing_shape` can be executed on OpenCL devices. In case of
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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / uint2*) **allowed for compute devices*

Image for which the minimum gray values are to
be calculated.

**`image_closing`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Image containing the minimum gray values.

**`mask_height`** (input_control)  extent.y `→` Union[int, float]

Height of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`1.0
≤
mask_height
≤
511.0`

**`mask_width`** (input_control)  extent.x `→` Union[int, float]

Width of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`1.0
≤
mask_width
≤
511.0`

**`mask_shape`** (input_control)  string `→` str

Shape of the mask.

Default:
"octagon"

List of values:
"octagon", "rectangle", "rhombus"

## Result

`gray_closing_shape` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Alternatives

`gray_closing`

## See also

`gray_dilation_shape`,
`gray_erosion_shape`,
`closing`

## Module

Foundation
