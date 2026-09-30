# apply_color_trans_lut (Operator)

## Name

`apply_color_trans_lut` — Color space transformation using pre-generated look-up-table.

## Signature

`def apply_color_trans_lut(image_1: HObject, image_2: HObject, image_3: HObject, color_trans_luthandle: HHandle) -> Tuple[HObject, HObject, HObject]`

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

**`image_1`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Input image (channel 1).

**`image_2`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Input image (channel 2).

**`image_3`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Input image (channel 3).

**`image_result_1`** (output_object)  singlechannelimage(-array) `→` HObject (byte)

Color-transformed output image (channel 1).

**`image_result_2`** (output_object)  singlechannelimage(-array) `→` HObject (byte)

Color-transformed output image (channel 2).

**`image_result_3`** (output_object)  singlechannelimage(-array) `→` HObject (byte)

Color-transformed output image (channel 3).

**`color_trans_luthandle`** (input_control)  color_trans_lut `→` HHandle

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
