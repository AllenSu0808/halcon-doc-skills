# GrabImage (Operator)

## Name

`GrabImage` — Synchronous grab of an image from the specified image acquisition device.

## Signature

`static void HOperatorSet.GrabImage(out HObject image, HTuple acqHandle)`

`void HImage.GrabImage(HFramegrabber acqHandle)`

`HImage HFramegrabber.GrabImage()`

## Description

The operator `GrabImage` grabs an image via the image acquisition
device specified by *`acqHandle`*. The desired operational mode of the
image acquisition device as well as a suitable image part and additional
interface-specific settings can be specified using the operators
[`OpenFramegrabber`](open_framegrabber.md) and [`SetFramegrabberParam`](set_framegrabber_param.md).

To abort the grab, the operator [`SetFramegrabberParam`](set_framegrabber_param.md) with the
parameter `'do_abort_grab'` can be used if the specific image
acquisition interface supports it. Note that as an exception from
the description of the concurrent usage in multiple threads (see below)
`'do_abort_grab'` can also be used from another thread.

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively.

`GrabImage` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` [HImage](HImage.md) (byte / uint2)

Grabbed image.

**`acqHandle`** (input_control)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

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

If the image could be acquired successfully, the operator `GrabImage`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`OpenFramegrabber`,
`SetFramegrabberParam`

## Possible Successors

`GrabImageStart`,
`GrabImageAsync`,
`CloseFramegrabber`

## See also

`OpenFramegrabber`,
`InfoFramegrabber`,
`SetFramegrabberParam`

## Module

Foundation
