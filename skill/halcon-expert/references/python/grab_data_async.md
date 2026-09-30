# grab_data_async (Operator)

## Name

`grab_data_async` — Asynchronous grab of images and preprocessed image data from the specified
image acquisition device.

## Signature

`def grab_data_async(acq_handle: HHandle, max_delay: float) -> Tuple[HObject, HObject, HObject, Sequence[HTupleElementType]]`

`def grab_data_async_s(acq_handle: HHandle, max_delay: float) -> Tuple[HObject, HObject, HObject, HTupleElementType]`

## Description

The operator `grab_data_async` requests asynchronously grabbed images
and preprocessed image data from the image acquisition device specified by
*`acq_handle`*.
By default, `grab_data_async` also starts the next asynchronous grab
before the operator returns.
More information about the behavior of a specific image acquisition device
can be found in the corresponding interface documentation in the directory
`doc/html/reference/acquisition`.
The desired operational mode of the image acquisition device as well as a
suitable image part and additional interface-specific settings can be
specified using the operators [`open_framegrabber`](open_framegrabber.md) and
[`set_framegrabber_param`](set_framegrabber_param.md).
Depending on the current configuration of the image acquisition device, the
preprocessed image data can be returned in terms of images
(*`image`*), regions (*`region`*), XLD contours
(*`contours`*), and control data (*`data`*).

The grab of the next image is finished by calling
`grab_data_async` or [`grab_image_async`](grab_image_async.md). If more than
*`max_delay`* ms have passed since the asynchronous grab was
started, the asynchronously grabbed image is considered as too old
and a new image is grabbed, if necessary. If a negative value is assigned to
*`max_delay`*, this control mechanism is deactivated.

To abort the grab, the operator [`set_framegrabber_param`](set_framegrabber_param.md) with the
parameter `'do_abort_grab'` can be used if the specific image
acquisition interface supports it. Note that as an exception from
the description of the concurrent usage in multiple threads (see below)
`'do_abort_grab'` can also be used from another thread.

Please note that if you call the operators [`grab_image`](grab_image.md) or
[`grab_data`](grab_data.md) after `grab_data_async`, the asynchronous
grab started by `grab_data_async` is aborted and a new
synchronous grab is started.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`grab_data_async` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image(-array) `→` HObject (byte / real / uint2)

Grabbed image data.

**`region`** (output_object)  region(-array) `→` HObject

Pre-processed image regions.

**`contours`** (output_object)  xld_cont(-array) `→` HObject

Pre-processed XLD contours.

**`acq_handle`** (input_control)  framegrabber `→` HHandle

Handle of the acquisition device to be used.

**`max_delay`** (input_control)  number `→` float

Maximum tolerated delay between the start of the
asynchronous grab and the delivery of the image [ms].

Default:
-1.0

Suggested values:
-1.0, 20.0, 33.3, 40.0, 66.6, 80.0, 99.9

**`data`** (output_control)  string(-array) `→` Sequence[HTupleElementType]

Pre-processed control data.

## Example (HDevelop)

```
* Select a suitable image acquisition interface name AcqName
open_framegrabber(AcqName,1,1,0,0,0,0,'default',-1,'default',-1.0, \
                  'default','default','default',-1,-1,AcqHandle)
* Grab image, segment it, and start next grab
grab_data_async (Image1, Region1, Contours1, AcqHandle, -1.0, Data1)
* Process data 1...
* Finish asynchronous grab, segment this image, and start next grab
grab_data_async (Image2, Region2, Contours2, AcqHandle, -1.0, Data2)
* Process data 2...
close_framegrabber(AcqHandle)
```

## Result

If the image acquisition device is open and supports the image
acquisition via `grab_data_async`, the operator
`grab_data_async` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`open_framegrabber`,
`grab_image_start`,
`set_framegrabber_param`

## Possible Successors

`grab_image_async`,
`set_framegrabber_param`,
`close_framegrabber`

## See also

`open_framegrabber`,
`info_framegrabber`,
`set_framegrabber_param`

## Module

Foundation
