# set_framegrabber_lut (Operator)

## Name

`set_framegrabber_lut` — Set look-up table of the image acquisition device.

## Signature

`def set_framegrabber_lut(acq_handle: HHandle, image_red: Sequence[int], image_green: Sequence[int], image_blue: Sequence[int]) -> None`

## Description

The operator `set_framegrabber_lut` sets the look-up table (LUT) of
the image acquisition device specified by *`acq_handle`*. Note that
this operation is not supported for all kinds of image acquisition devices.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`set_framegrabber_lut` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- acq_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`acq_handle`** (input_control, state is modified)  framegrabber `→` HHandle

Handle of the acquisition device to be used.

**`image_red`** (input_control)  integer-array `→` Sequence[int]

Red level of the LUT entries.

**`image_green`** (input_control)  integer-array `→` Sequence[int]

Green level of the LUT entries.

**`image_blue`** (input_control)  integer-array `→` Sequence[int]

Blue level of the LUT entries.

## Result

The operator `set_framegrabber_lut` returns the value 2 (
H_MSG_TRUE)
if the specified LUT is correct and the image acquisition device is open.

## Possible Predecessors

`open_framegrabber`,
`get_framegrabber_lut`

## Possible Successors

`grab_image`,
`grab_data`,
`grab_image_start`,
`grab_image_async`,
`grab_data_async`

## See also

`get_framegrabber_lut`,
`open_framegrabber`

## Module

Foundation
