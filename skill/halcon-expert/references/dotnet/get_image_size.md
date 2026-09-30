# GetImageSize (Operator)

## Name

`GetImageSize` — Return the size of an image.

## Signature

`static void HOperatorSet.GetImageSize(HObject image, out HTuple width, out HTuple height)`

`void HImage.GetImageSize(out HTuple width, out HTuple height)`

`void HImage.GetImageSize(out int width, out int height)`

## Description

The operator `GetImageSize` returns the image
size (width and height) of the input image.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`width`** (output_control)  extent.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Width of image.

**`height`** (output_control)  extent.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Height of image.

## Result

The operator `GetImageSize` returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) is set via
the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`ReadImage`

## Alternatives

`GetImagePointer1`

## See also

`GetImageType`

## Module

Foundation
