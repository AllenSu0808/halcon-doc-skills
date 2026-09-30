# set_framegrabber_callback (Operator)

## Name

`set_framegrabber_callback` — Register a callback function for an image acquisition device.

## Signature

`def set_framegrabber_callback(acq_handle: HHandle, callback_type: str, callback_function: int, user_context: int) -> None`

## Description

The operator `set_framegrabber_callback` registers a callback function
for the image acquisition device specified by *`acq_handle`*. The
parameter *`callback_function`* contains a pointer to the function to
register, while *`callback_type`* specifies to which
function of the underlying API the callback should be connected.

Suggested values for *`callback_type`* are:

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

Once the callback is registered, on every occurrence of the underlying event
(e.g., the notification that the exposure has finished) the specified
callback function *`callback_function`* will be called. If
*`callback_function`* is set to NULL, the corresponding callback will be
unregistered.

The signature of the callback function is the following:
Herror HAcqCallback(void *AcqHandle, void *Context, void *UserContext)

The first parameter of the callback function contains the handle to the image
acquisition device passed in *`acq_handle`*, the second one provides a
pointer to interface-specific context data, and the third parameter is a
user-specific pointer that is specified in *`user_context`*.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`set_framegrabber_callback` runs in parallel with all non-exclusive
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

**`callback_type`** (input_control)  string `→` str

Callback type.

Default:
"transfer_end"

Suggested values:
"exception", "exposure_end", "exposure_start", "transfer_end"

**`callback_function`** (input_control)  pointer `→` int

Pointer to the callback function to be set.

**`user_context`** (input_control)  pointer `→` int

Pointer to user-specific context data.

## Result

If the image acquisition device is open and the specified callback
was registered successfully, the operator `set_framegrabber_callback`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_framegrabber`,
`set_framegrabber_param`

## Possible Successors

`grab_image`,
`grab_data`,
`grab_image_start`,
`grab_image_async`,
`grab_data_async`,
`get_framegrabber_param`

## See also

`open_framegrabber`,
`get_framegrabber_callback`

## Module

Foundation
