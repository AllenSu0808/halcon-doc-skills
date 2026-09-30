# set_framegrabber_lut (Operator)

## Name

`set_framegrabber_lut` — Set look-up table of the image acquisition device.

## Signature

`set_framegrabber_lut( : : AcqHandle, ImageRed, ImageGreen, ImageBlue : )`

## Description

The operator `set_framegrabber_lut` sets the look-up table (LUT) of
the image acquisition device specified by *`AcqHandle`*. Note that
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

- AcqHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`AcqHandle`** (input_control, state is modified)  framegrabber `→`  (handle)

Handle of the acquisition device to be used.

**`ImageRed`** (input_control)  integer-array `→`  (integer)

Red level of the LUT entries.

**`ImageGreen`** (input_control)  integer-array `→`  (integer)

Green level of the LUT entries.

**`ImageBlue`** (input_control)  integer-array `→`  (integer)

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
