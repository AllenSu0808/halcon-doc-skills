# get_image_time (Operator)

## Name

`get_image_time` — Request time at which the image was created.

## Signature

`def get_image_time(image: HObject) -> Tuple[int, int, int, int, int, int, int, int]`

## Description

The operator `get_image_time` returns the time at which the image was
created internally in HALCON. This time doesn't necessarily correlate with
the time the image was acquired.

For some image acquisition interfaces, the time of the acquisition can be
queried with [`get_framegrabber_param`](get_framegrabber_param.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`msecond`** (output_control)  integer `→` int

Milliseconds (0..999).

**`second`** (output_control)  integer `→` int

Seconds (0..59).

**`minute`** (output_control)  integer `→` int

Minutes (0..59).

**`hour`** (output_control)  integer `→` int

Hours (0..23).

**`day`** (output_control)  integer `→` int

Day of the month (1..31).

**`yday`** (output_control)  integer `→` int

Day of the year (1..366).

**`month`** (output_control)  integer `→` int

Month (1..12).

**`year`** (output_control)  integer `→` int

Year (xxxx).

## Result

The operator `get_image_time` returns the value 2 (
H_MSG_TRUE)
if
exactly one image was passed.
The behavior in case of empty input (no input images available) is set via
the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`read_image`,
`grab_image`

## See also

`count_seconds`

## Module

Foundation
