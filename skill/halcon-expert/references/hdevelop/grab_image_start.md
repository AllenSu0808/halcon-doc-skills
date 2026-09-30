# grab_image_start (Operator)

## Name

`grab_image_start` — Start an asynchronous grab from the specified image acquisition device.

## Signature

`grab_image_start( : : AcqHandle, MaxDelay : )`

## Description

The operator `grab_image_start` starts the asynchronous grab of
an image via the image acquisition device specified by *`AcqHandle`*.
The desired operational mode of the image acquisition device as well as a
suitable image part and additional interface-specific settings can be
specified using the operators [`open_framegrabber`](open_framegrabber.md) and
[`set_framegrabber_param`](set_framegrabber_param.md).

The grab is finished via [`grab_image_async`](grab_image_async.md) or
[`grab_data_async`](grab_data_async.md). The *`MaxDelay`* parameter is obsolete and
does not effect the new asynchronous grab. Note that you can check for a
too old image by using the *`MaxDelay`* parameter of the operator
[`grab_image_async`](grab_image_async.md) or [`grab_data_async`](grab_data_async.md), respectively.

Please note that the operator `grab_image_start` makes sense only when
used together with [`grab_image_async`](grab_image_async.md) or [`grab_data_async`](grab_data_async.md). If
you call the operators [`grab_image`](grab_image.md) or [`grab_data`](grab_data.md) instead, the
asynchronous grab started by `grab_image_start` is aborted and a new
synchronous grab is started.

To abort the grab, the operator [`set_framegrabber_param`](set_framegrabber_param.md) with the
parameter `'do_abort_grab'` can be used if the specific image
acquisition interface supports it. Note that as an exception from
the description of the concurrent usage in multiple threads (see below)
`'do_abort_grab'` can also be used from another thread.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`grab_image_start` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`AcqHandle`** (input_control)  framegrabber `→`  (handle)

Handle of the acquisition device to be used.

**`MaxDelay`** (input_control)  number `→`  (real)

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
the operator `grab_image_start` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`open_framegrabber`,
`set_framegrabber_param`

## Possible Successors

`grab_image_async`,
`grab_data_async`,
`set_framegrabber_param`,
`close_framegrabber`

## See also

`open_framegrabber`,
`info_framegrabber`,
`set_framegrabber_param`

## Module

Foundation
