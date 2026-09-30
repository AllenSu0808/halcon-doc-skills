# GetImageTime (Operator)

## Name

`GetImageTime` — Request time at which the image was created.

## Signature

`static void HOperatorSet.GetImageTime(HObject image, out HTuple MSecond, out HTuple second, out HTuple minute, out HTuple hour, out HTuple day, out HTuple YDay, out HTuple month, out HTuple year)`

`int HImage.GetImageTime(out int second, out int minute, out int hour, out int day, out int YDay, out int month, out int year)`

## Description

The operator `GetImageTime` returns the time at which the image was
created internally in HALCON. This time doesn't necessarily correlate with
the time the image was acquired.

For some image acquisition interfaces, the time of the acquisition can be
queried with [`GetFramegrabberParam`](get_framegrabber_param.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`MSecond`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Milliseconds (0..999).

**`second`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Seconds (0..59).

**`minute`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minutes (0..59).

**`hour`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Hours (0..23).

**`day`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Day of the month (1..31).

**`YDay`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Day of the year (1..366).

**`month`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Month (1..12).

**`year`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Year (xxxx).

## Result

The operator `GetImageTime` returns the value 2 (
H_MSG_TRUE)
if
exactly one image was passed.
The behavior in case of empty input (no input images available) is set via
the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`ReadImage`,
`GrabImage`

## See also

`CountSeconds`

## Module

Foundation
