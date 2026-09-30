# get_framegrabber_callback (Operator)

## Name

`get_framegrabber_callback` — Query callback function of an image acquisition device.

## Signature

`get_framegrabber_callback( : : AcqHandle, CallbackType : CallbackFunction, UserContext)`

## Description

The operator `get_framegrabber_callback` queries a callback function
for the image acquisition device specified by *`AcqHandle`*. If the
callback function was registered via [`set_framegrabber_callback`](set_framegrabber_callback.md)
before, *`CallbackFunction`* contains a pointer to it, otherwise
NULL. Furthermore, *`UserContext`* contains a pointer to the
user-specific context data that was set via
[`set_framegrabber_callback`](set_framegrabber_callback.md) (or NULL).

With the parameter *`CallbackType`*, you can select different callback
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
for *`CallbackType`* are possible. All actually supported callback
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

**`AcqHandle`** (input_control)  framegrabber `→`  (handle)

Handle of the acquisition device to be used.

**`CallbackType`** (input_control)  string `→`  (string)

Callback type.

Default:
'transfer_end'

Suggested values:
'exception', 'exposure_end', 'exposure_start', 'transfer_end'

**`CallbackFunction`** (output_control)  pointer `→`  (integer)

Pointer to the callback function.

**`UserContext`** (output_control)  pointer `→`  (integer)

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
