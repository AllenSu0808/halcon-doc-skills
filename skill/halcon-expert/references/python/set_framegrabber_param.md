# set_framegrabber_param (Operator)

## Name

`set_framegrabber_param` — Set specific parameters of an image acquisition device.

## Signature

`def set_framegrabber_param(acq_handle: HHandle, param: MaybeSequence[str], value: HTupleType) -> None`

## Description

The operator `set_framegrabber_param` sets specific parameters
for the image acquisition device specified by *`acq_handle`*.
Additional information for a specific image acquisition device is
available via [`info_framegrabber`](info_framegrabber.md). A comprehensive documentation
of all image acquisition device-specific parameters can be found in the
corresponding interface documentation in the directory
`doc/html/reference/acquisition`.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`set_framegrabber_param` runs in parallel with all non-exclusive
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

**`param`** (input_control)  string(-array) `→` MaybeSequence[str]

Parameter name.

Suggested values:
"color_space", "continuous_grabbing", "external_trigger", "grab_timeout", "image_height", "image_width", "port", "start_column", "start_row", "volatile"

**`value`** (input_control)  string(-array) `→` HTupleType

Parameter value to be set.

## Result

If the image acquisition device is open and the specified parameter /
parameter value is supported, the operator `set_framegrabber_param`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_framegrabber`

## Possible Successors

`grab_image`,
`grab_data`,
`grab_image_start`,
`grab_image_async`,
`grab_data_async`,
`get_framegrabber_param`

## See also

`open_framegrabber`,
`info_framegrabber`,
`get_framegrabber_param`

## Module

Foundation
