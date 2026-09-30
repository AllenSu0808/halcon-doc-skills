# ApplyColorTransLut (Operator)

## Name

`ApplyColorTransLut` — Color space transformation using pre-generated look-up-table.

## Signature

`static void HOperatorSet.ApplyColorTransLut(HObject image1, HObject image2, HObject image3, out HObject imageResult1, out HObject imageResult2, out HObject imageResult3, HTuple colorTransLUTHandle)`

`HImage HImage.ApplyColorTransLut(HImage image2, HImage image3, out HImage imageResult2, out HImage imageResult3, HColorTransLUT colorTransLUTHandle)`

`HImage HColorTransLUT.ApplyColorTransLut(HImage image1, HImage image2, HImage image3, out HImage imageResult2, out HImage imageResult3)`

## Description

`ApplyColorTransLut` transforms an 3-channel image from the
RGB color space to further color spaces and vice versa using a
pre-generated look-up-table. The three channels of the image are
passed as three separate images on input and output.

For further information about the color space transformations see
operators [`TransFromRgb`](trans_from_rgb.md) and [`TransToRgb`](trans_to_rgb.md)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`image1`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Input image (channel 1).

**`image2`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Input image (channel 2).

**`image3`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Input image (channel 3).

**`imageResult1`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Color-transformed output image (channel 1).

**`imageResult2`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Color-transformed output image (channel 2).

**`imageResult3`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Color-transformed output image (channel 3).

**`colorTransLUTHandle`** (input_control)  color_trans_lut `→` [HColorTransLUT](HColorTransLUT.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the look-up-table for the color space
transformation.

## Result

The operator `ApplyColorTransLut` returns the value 2 (
H_MSG_TRUE)
if
the given parameters are correct and the input images could be
successfully transformed. Otherwise, an exception will be raised.

## Possible Predecessors

`CreateColorTransLut`

## Possible Successors

`ClearColorTransLut`

## Alternatives

`TransFromRgb`,
`TransToRgb`

## See also

`CreateColorTransLut`,
`ClearColorTransLut`

## Module

Foundation
