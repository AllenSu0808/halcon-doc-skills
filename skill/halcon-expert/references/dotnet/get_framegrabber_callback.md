# GetFramegrabberCallback (Operator)

## Name

`GetFramegrabberCallback` — Query callback function of an image acquisition device.

## Signature

`static void HOperatorSet.GetFramegrabberCallback(HTuple acqHandle, HTuple callbackType, out HTuple callbackFunction, out HTuple userContext)`

`IntPtr HFramegrabber.GetFramegrabberCallback(string callbackType, out IntPtr userContext)`

## Description

The operator `GetFramegrabberCallback` queries a callback function
for the image acquisition device specified by *`acqHandle`*. If the
callback function was registered via [`SetFramegrabberCallback`](set_framegrabber_callback.md)
before, *`callbackFunction`* contains a pointer to it, otherwise
NULL. Furthermore, *`userContext`* contains a pointer to the
user-specific context data that was set via
[`SetFramegrabberCallback`](set_framegrabber_callback.md) (or NULL).

With the parameter *`callbackType`*, you can select different callback
types. Suggested values are:

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

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively.

`GetFramegrabberCallback` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`acqHandle`** (input_control)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the acquisition device to be used.

**`callbackType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Callback type.

Default:
"transfer_end"

Suggested values:
"exception", "exposure_end", "exposure_start", "transfer_end"

**`callbackFunction`** (output_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the callback function.

**`userContext`** (output_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to user-specific context data.

## Result

If the image acquisition device is open and the specified callback type
is supported, the operator `GetFramegrabberCallback` returns the
value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`OpenFramegrabber`,
`SetFramegrabberCallback`

## Possible Successors

`GrabImage`,
`GrabData`,
`GrabImageStart`,
`GrabImageAsync`,
`GrabDataAsync`,
`SetFramegrabberParam`,
`CloseFramegrabber`

## See also

`OpenFramegrabber`,
`InfoFramegrabber`,
`SetFramegrabberCallback`

## Module

Foundation
