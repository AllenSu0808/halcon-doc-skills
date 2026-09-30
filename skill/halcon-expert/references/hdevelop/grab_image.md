# grab_image (Operator)

## Name

`grab_image` — Synchronous grab of an image from the specified image acquisition device.

## Signature

`grab_image( : Image : AcqHandle : )`

## Description

The operator `grab_image` grabs an image via the image acquisition
device specified by *`AcqHandle`*. The desired operational mode of the
image acquisition device as well as a suitable image part and additional
interface-specific settings can be specified using the operators
[`open_framegrabber`](open_framegrabber.md) and [`set_framegrabber_param`](set_framegrabber_param.md).

To abort the grab, the operator [`set_framegrabber_param`](set_framegrabber_param.md) with the
parameter `'do_abort_grab'` can be used if the specific image
acquisition interface supports it. Note that as an exception from
the description of the concurrent usage in multiple threads (see below)
`'do_abort_grab'` can also be used from another thread.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`grab_image` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (output_object)  image `→` object (byte / uint2)

Grabbed image.

**`AcqHandle`** (input_control)  framegrabber `→`  (handle)

Handle of the acquisition device to be used.

## Example (HDevelop)

```
* Select a suitable image acquisition interface name AcqName
info_framegrabber(AcqName,'port',Information,Values)
* Open image acquisition device using the default settings, see
* documentation of the actually used interface for more details
open_framegrabber(AcqName,1,1,0,0,0,0,'default',-1,'default',-1.0, \
                  'default','default','default',-1,-1,AcqHandle)
grab_image(Image,AcqHandle)
close_framegrabber(AcqHandle)
```

## Result

If the image could be acquired successfully, the operator `grab_image`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_framegrabber`,
`set_framegrabber_param`

## Possible Successors

`grab_image_start`,
`grab_image_async`,
`close_framegrabber`

## See also

`open_framegrabber`,
`info_framegrabber`,
`set_framegrabber_param`

## Module

Foundation
