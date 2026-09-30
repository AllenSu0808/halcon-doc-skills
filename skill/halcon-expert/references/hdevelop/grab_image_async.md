# grab_image_async (Operator)

## Name

`grab_image_async` — Asynchronous grab of an image from the specified image acquisition device.

## Signature

`grab_image_async( : Image : AcqHandle, MaxDelay : )`

## Description

The operator `grab_image_async` requests an asynchronously grabbed
image from the image acquisition device specified by *`AcqHandle`*.
By default, `grab_image_async` also starts the next asynchronous grab
before the operator returns.
More information about the behavior of a specific image acquisition device
can be found in the corresponding interface documentation in the directory
`doc/html/reference/acquisition`.
The desired operational mode of the image acquisition device as well as a
suitable image part and additional interface-specific settings can be
specified using the operators [`open_framegrabber`](open_framegrabber.md) and
[`set_framegrabber_param`](set_framegrabber_param.md).

The grab is finished by calling `grab_image_async` or
[`grab_data_async`](grab_data_async.md). If more than *`MaxDelay`* ms have passed
since the asynchronous grab was started, the asynchronously grabbed image
is considered as too old and a new image is grabbed, if necessary. If a
negative value is assigned to *`MaxDelay`*, this control mechanism is
deactivated.

To abort the grab, the operator [`set_framegrabber_param`](set_framegrabber_param.md) with the
parameter `'do_abort_grab'` can be used if the specific image
acquisition interface supports it. Note that as an exception from
the description of the concurrent usage in multiple threads (see below)
`'do_abort_grab'` can also be used from another thread.

Please note that if you call the operators [`grab_image`](grab_image.md) or
[`grab_data`](grab_data.md) after `grab_image_async`, the asynchronous grab
started by `grab_image_async` is aborted and a new
synchronous grab is started.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`grab_image_async` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (output_object)  image `→` object (byte / int2)

Grabbed image.

**`AcqHandle`** (input_control)  framegrabber `→`  (handle)

Handle of the acquisition device to be used.

**`MaxDelay`** (input_control)  number `→`  (real)

Maximum tolerated delay between the start of the
asynchronous grab and the delivery of the image [ms].

Default:
-1.0

Suggested values:
-1.0, 20.0, 33.3, 40.0, 66.6, 80.0, 99.9

## Example (HDevelop)

```
* Select a suitable image acquisition interface named AcqName
open_framegrabber('AcqName', 1, 1, 0, 0, 0, 0, 'default' ,-1 , \
                  'default' ,-1.0, 'default', 'default', 'default', -1, \
                  -1, AcqHandle)
* Grab image + start next grab
grab_image_async(Image1, AcqHandle, -1.0)
* Process Image1 ...
* Finish asynchronous grab + start next grab
grab_image_async(Image2, AcqHandle, -1.0)
* Process Image2 ...
close_framegrabber(AcqHandle)
```

## Result

If the image acquisition device is open and supports asynchronous grabbing
the operator `grab_image_async` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`grab_image_start`,
`open_framegrabber`,
`set_framegrabber_param`

## Possible Successors

`grab_data_async`,
`set_framegrabber_param`,
`close_framegrabber`

## See also

`grab_image_start`,
`open_framegrabber`,
`info_framegrabber`,
`set_framegrabber_param`

## Module

Foundation
