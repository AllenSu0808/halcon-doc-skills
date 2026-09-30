# get_image_type (Operator)

## Name

`get_image_type` — Return the type of an image.

## Signature

`get_image_type(Image : : : Type)`

## Description

The operator `get_image_type` returns the image type
(*`Type`* = 'byte', 'int2', 'uint2', etc.).

## Attention

For multi-channel input images the type of the first channel is returned.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`Type`** (output_control)  string(-array) `→`  (string)

Type of image.

List of values:
'byte', 'complex', 'cyclic', 'direction', 'int1', 'int2', 'int4', 'int8', 'real', 'uint2', 'vector_field_absolute', 'vector_field_relative'

## Result

The operator `get_image_type` returns the value 2 (
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

`get_image_size`

## Module

Foundation
