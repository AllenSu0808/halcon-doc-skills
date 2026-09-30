# create_color_trans_lut (Operator)

## Name

`create_color_trans_lut` — Creates the look-up-table for transformation of an image from the
RGB color space to an arbitrary color space.

## Signature

`create_color_trans_lut( : : ColorSpace, TransDirection, NumBits : ColorTransLUTHandle)`

## Description

The operator `create_color_trans_lut` returns a look-up table
(LUT) for color space transformation of a 8 bit RGB image to a
different color space and vice versa. That means, this operator is
only valid for three channel images, where each channel has pixels
of type `byte`. If the input images have different domains, only the
intersection of the three input images is used for the
transformation.

The parameter *`ColorSpace`* identifies the initial or the target
color space transformation and the direction of the transformation is set
by *`TransDirection`*. *`ColorTransLUTHandle`* contains the
handle of the created look-up-table.

Using a LUT significantly speeds up the process of transformation a
RGB image to another color space and vice versa with exception of
the *'yiq'*, *'yuv'*, *'argyb'*, *'ciexyz'*,
and *'i1i2i3'* color spaces.
Be aware that the LUT already needs 48MB of memory space.

For further information about the possible color space
transformations see the description of the operators
[`trans_from_rgb`](trans_from_rgb.md) and [`trans_to_rgb`](trans_to_rgb.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`ColorSpace`** (input_control)  string `→`  (string)

Color space of the output image.

Default:
'hsv'

List of values:
'argyb', 'cielab', 'cielchab', 'cielchuv', 'cieluv', 'ciexyz', 'ciexyz3', 'ciexyz4', 'ciexyz4', 'hls', 'hls', 'hsi', 'hsv', 'i1i2i3', 'ihs', 'lms', 'yiq', 'yuv'

**`TransDirection`** (input_control)  string `→`  (string)

Direction of color space transformation.

Default:
'from_rgb'

List of values:
'from_rgb', 'to_rgb'

**`NumBits`** (input_control)  integer `→`  (integer)

Number of bits of the input image.

Default:
8

List of values:
8

**`ColorTransLUTHandle`** (output_control)  color_trans_lut `→`  (handle)

Handle of the look-up-table for color space
transformation.

## Result

The operator `create_color_trans_lut` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct and the look-up-table is
generated. Otherwise, an exception will be raised.

## Possible Successors

`apply_color_trans_lut`

## See also

`apply_color_trans_lut`,
`clear_color_trans_lut`

## Module

Foundation
