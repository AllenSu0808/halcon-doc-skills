# SetFramegrabberCallback (Operator)

## Name

`SetFramegrabberCallback` — Register a callback function for an image acquisition device.

## Signature

`static void HOperatorSet.SetFramegrabberCallback(HTuple acqHandle, HTuple callbackType, HTuple callbackFunction, HTuple userContext)`

`void HFramegrabber.SetFramegrabberCallback(string callbackType, IntPtr callbackFunction, IntPtr userContext)`

## Description

The operator `SetFramegrabberCallback` registers a callback function
for the image acquisition device specified by *`acqHandle`*. The
parameter *`callbackFunction`* contains a pointer to the function to
register, while *`callbackType`* specifies to which
function of the underlying API the callback should be connected.

Suggested values for *`callbackType`* are:

- **'exception':** —

  The image acquisition has raised an exception.
- **'exposure_end':** —

  The exposure of the next image has been finished.
- **'exposure_start':** —

  The exposure of the next image has been started.
- **'transfer_end':** —

  A new image is ready to be fetched
  by [`GrabImageAsync`](grab_image_async.md).

Depending on the functionality of the underlying API, additional values
for *`callbackType`* are possible. All actually supported callback
types of a specific image acquisition device can be queried by
calling [`GetFramegrabberParam`](get_framegrabber_param.md) with the parameter
`'available_callback_types'`. For more details see the
documentation of the specific image acquisition interface.

Once the callback is registered, on every occurrence of the underlying event
(e.g., the notification that the exposure has finished) the specified
callback function *`callbackFunction`* will be called. If
*`callbackFunction`* is set to NULL, the corresponding callback will be
unregistered.

The signature of the callback function is the following:
Herror HAcqCallback(void *AcqHandle, void *Context, void *UserContext)

The first parameter of the callback function contains the handle to the image
acquisition device passed in *`acqHandle`*, the second one provides a
pointer to interface-specific context data, and the third parameter is a
user-specific pointer that is specified in *`userContext`*.

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively.

`SetFramegrabberCallback` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- acqHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`acqHandle`** (input_control, state is modified)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the acquisition device to be used.

**`callbackType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Callback type.

Default:
"transfer_end"

Suggested values:
"exception", "exposure_end", "exposure_start", "transfer_end"

**`callbackFunction`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the callback function to be set.

**`userContext`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to user-specific context data.

## Result

If the image acquisition device is open and the specified callback
was registered successfully, the operator `SetFramegrabberCallback`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`OpenFramegrabber`,
`SetFramegrabberParam`

## Possible Successors

`GrabImage`,
`GrabData`,
`GrabImageStart`,
`GrabImageAsync`,
`GrabDataAsync`,
`GetFramegrabberParam`

## See also

`OpenFramegrabber`,
`GetFramegrabberCallback`

## Module

Foundation
