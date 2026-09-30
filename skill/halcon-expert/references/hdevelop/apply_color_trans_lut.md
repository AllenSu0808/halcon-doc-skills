# apply_color_trans_lut (Operator)

## Name

`apply_color_trans_lut` — Color space transformation using pre-generated look-up-table.

## Signature

`apply_color_trans_lut(Image1, Image2, Image3 : ImageResult1, ImageResult2, ImageResult3 : ColorTransLUTHandle : )`

## Description

`apply_color_trans_lut` transforms an 3-channel image from the
RGB color space to further color spaces and vice versa using a
pre-generated look-up-table. The three channels of the image are
passed as three separate images on input and output.

For further information about the color space transformations see
operators [`trans_from_rgb`](trans_from_rgb.md) and [`trans_to_rgb`](trans_to_rgb.md)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`Image1`** (input_object)  singlechannelimage(-array) `→` object (byte)

Input image (channel 1).

**`Image2`** (input_object)  singlechannelimage(-array) `→` object (byte)

Input image (channel 2).

**`Image3`** (input_object)  singlechannelimage(-array) `→` object (byte)

Input image (channel 3).

**`ImageResult1`** (output_object)  singlechannelimage(-array) `→` object (byte)

Color-transformed output image (channel 1).

**`ImageResult2`** (output_object)  singlechannelimage(-array) `→` object (byte)

Color-transformed output image (channel 2).

**`ImageResult3`** (output_object)  singlechannelimage(-array) `→` object (byte)

Color-transformed output image (channel 3).

**`ColorTransLUTHandle`** (input_control)  color_trans_lut `→`  (handle)

Handle of the look-up-table for the color space
transformation.

## Result

The operator `apply_color_trans_lut` returns the value 2 (
H_MSG_TRUE)
if
the given parameters are correct and the input images could be
successfully transformed. Otherwise, an exception will be raised.

## Possible Predecessors

`create_color_trans_lut`

## Possible Successors

`clear_color_trans_lut`

## Alternatives

`trans_from_rgb`,
`trans_to_rgb`

## See also

`create_color_trans_lut`,
`clear_color_trans_lut`

## Module

Foundation
