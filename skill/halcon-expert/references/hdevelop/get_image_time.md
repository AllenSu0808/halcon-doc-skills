# get_image_time (Operator)

## Name

`get_image_time` — Request time at which the image was created.

## Signature

`get_image_time(Image : : : MSecond, Second, Minute, Hour, Day, YDay, Month, Year)`

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

**`Image`** (input_object)  (multichannel-)image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`MSecond`** (output_control)  integer `→`  (integer)

Milliseconds (0..999).

**`Second`** (output_control)  integer `→`  (integer)

Seconds (0..59).

**`Minute`** (output_control)  integer `→`  (integer)

Minutes (0..59).

**`Hour`** (output_control)  integer `→`  (integer)

Hours (0..23).

**`Day`** (output_control)  integer `→`  (integer)

Day of the month (1..31).

**`YDay`** (output_control)  integer `→`  (integer)

Day of the year (1..366).

**`Month`** (output_control)  integer `→`  (integer)

Month (1..12).

**`Year`** (output_control)  integer `→`  (integer)

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
