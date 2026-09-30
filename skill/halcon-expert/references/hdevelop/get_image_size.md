# get_image_size (Operator)

## Name

`get_image_size` — Return the size of an image.

## Signature

`get_image_size(Image : : : Width, Height)`

## Description

The operator `get_image_size` returns the image
size (width and height) of the input image.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`Width`** (output_control)  extent.x(-array) `→`  (integer)

Width of image.

**`Height`** (output_control)  extent.y(-array) `→`  (integer)

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
