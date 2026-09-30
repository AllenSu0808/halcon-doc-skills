# get_framegrabber_callback (Operator)

## Name

`get_framegrabber_callback` — Query callback function of an image acquisition device.

## Signature

`def get_framegrabber_callback(acq_handle: HHandle, callback_type: str) -> Tuple[int, int]`

## Description

The operator `get_framegrabber_callback` queries a callback function
for the image acquisition device specified by *`acq_handle`*. If the
callback function was registered via [`set_framegrabber_callback`](set_framegrabber_callback.md)
before, *`callback_function`* contains a pointer to it, otherwise
NULL. Furthermore, *`user_context`* contains a pointer to the
user-specific context data that was set via
[`set_framegrabber_callback`](set_framegrabber_callback.md) (or NULL).

With the parameter *`callback_type`*, you can select different callback
types. Suggested values are:

- **'exception':** —

  The image acquisition has raised an exception.
- **'exposure_end':** —

  The exposure of the next image has been finished.
- **'exposure_start':** —

  The exposure of the next image has been started.
- **'transfer_end':** —

  A new image is ready to be fetched
  by [`grab_image_async`](grab_image_async.md).

Depending on the functionality of the underlying API, additional values
for *`callback_type`* are possible. All actually supported callback
types of a specific image acquisition device can be queried by
calling [`get_framegrabber_param`](get_framegrabber_param.md) with the parameter
`'available_callback_types'`. For more details see the
documentation of the specific image acquisition interface.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`get_framegrabber_callback` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`acq_handle`** (input_control)  framegrabber `→` HHandle

Handle of the acquisition device to be used.

**`callback_type`** (input_control)  string `→` str

Callback type.

Default:
"transfer_end"

Suggested values:
"exception", "exposure_end", "exposure_start", "transfer_end"

**`callback_function`** (output_control)  pointer `→` int

Pointer to the callback function.

**`user_context`** (output_control)  pointer `→` int

Pointer to user-specific context data.

## Result

If the image acquisition device is open and the specified callback type
is supported, the operator `get_framegrabber_callback` returns the
value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_framegrabber`,
`set_framegrabber_callback`

## Possible Successors

`grab_image`,
`grab_data`,
`grab_image_start`,
`grab_image_async`,
`grab_data_async`,
`set_framegrabber_param`,
`close_framegrabber`

## See also

`open_framegrabber`,
`info_framegrabber`,
`set_framegrabber_callback`

## Module

Foundation
