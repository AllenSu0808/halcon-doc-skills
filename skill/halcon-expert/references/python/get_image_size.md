# get_image_size (Operator)

## Name

`get_image_size` — Return the size of an image.

## Signature

`def get_image_size(image: HObject) -> Tuple[Sequence[int], Sequence[int]]`

`def get_image_size_s(image: HObject) -> Tuple[int, int]`

## Description

The operator `get_image_size` returns the image
size (width and height) of the input image.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`width`** (output_control)  extent.x(-array) `→` Sequence[int]

Width of image.

**`height`** (output_control)  extent.y(-array) `→` Sequence[int]

Height of image.

## Result

The operator `get_image_size` returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) is set via
the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`read_image`

## Alternatives

`get_image_pointer1`

## See also

`get_image_type`

## Module

Foundation
