# GrabImageStart (Operator)

## Name

`GrabImageStart` — Start an asynchronous grab from the specified image acquisition device.

## Signature

`static void HOperatorSet.GrabImageStart(HTuple acqHandle, HTuple maxDelay)`

`void HFramegrabber.GrabImageStart(double maxDelay)`

## Description

The operator `GrabImageStart` starts the asynchronous grab of
an image via the image acquisition device specified by *`acqHandle`*.
The desired operational mode of the image acquisition device as well as a
suitable image part and additional interface-specific settings can be
specified using the operators [`OpenFramegrabber`](open_framegrabber.md) and
[`SetFramegrabberParam`](set_framegrabber_param.md).

The grab is finished via [`GrabImageAsync`](grab_image_async.md) or
[`GrabDataAsync`](grab_data_async.md). The *`maxDelay`* parameter is obsolete and
does not effect the new asynchronous grab. Note that you can check for a
too old image by using the *`maxDelay`* parameter of the operator
[`GrabImageAsync`](grab_image_async.md) or [`GrabDataAsync`](grab_data_async.md), respectively.

Please note that the operator `GrabImageStart` makes sense only when
used together with [`GrabImageAsync`](grab_image_async.md) or [`GrabDataAsync`](grab_data_async.md). If
you call the operators [`GrabImage`](grab_image.md) or [`GrabData`](grab_data.md) instead, the
asynchronous grab started by `GrabImageStart` is aborted and a new
synchronous grab is started.

To abort the grab, the operator [`SetFramegrabberParam`](set_framegrabber_param.md) with the
parameter `'do_abort_grab'` can be used if the specific image
acquisition interface supports it. Note that as an exception from
the description of the concurrent usage in multiple threads (see below)
`'do_abort_grab'` can also be used from another thread.

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively.

`GrabImageStart` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`acqHandle`** (input_control)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the acquisition device to be used.

**`maxDelay`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

This parameter is obsolete and has no effect.

Default:
-1.0

Suggested values:
-1.0, 20.0, 33.3, 40.0, 66.6, 80.0, 99.9

## Example (HDevelop)

```
* Select a suitable image acquisition interface named AcqName.
open_framegrabber('AcqName', 1, 1, 0, 0, 0, 0, 'default', -1, 'default', \
                  -1.0, 'default', 'default', 'default', -1, -1, AcqHandle)
* Start asynchronous grabbing.
grab_image_start(AcqHandle, -1)
* Run acquisition loop.
while (true)
    * Get image, start next grab.
    grab_image_async(Image, AcqHandle, -1.0)
    * Next: Do something with the grabbed image.
endwhile
close_framegrabber(AcqHandle)
```

## Result

If the image acquisition device is open and supports asynchronous grabbing
the operator `GrabImageStart` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`OpenFramegrabber`,
`SetFramegrabberParam`

## Possible Successors

`GrabImageAsync`,
`GrabDataAsync`,
`SetFramegrabberParam`,
`CloseFramegrabber`

## See also

`OpenFramegrabber`,
`InfoFramegrabber`,
`SetFramegrabberParam`

## Module

Foundation
