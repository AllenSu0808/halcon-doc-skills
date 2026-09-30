# GrabDataAsync (Operator)

## Name

`GrabDataAsync` — Asynchronous grab of images and preprocessed image data from the specified
image acquisition device.

## Signature

`static void HOperatorSet.GrabDataAsync(out HObject image, out HObject region, out HObject contours, HTuple acqHandle, HTuple maxDelay, out HTuple data)`

`HRegion HImage.GrabDataAsync(out HXLDCont contours, HFramegrabber acqHandle, double maxDelay, out HTuple data)`

`HRegion HImage.GrabDataAsync(out HXLDCont contours, HFramegrabber acqHandle, double maxDelay, out string data)`

`HImage HRegion.GrabDataAsync(out HXLDCont contours, HFramegrabber acqHandle, double maxDelay, out HTuple data)`

`HImage HRegion.GrabDataAsync(out HXLDCont contours, HFramegrabber acqHandle, double maxDelay, out string data)`

`HImage HFramegrabber.GrabDataAsync(out HRegion region, out HXLDCont contours, double maxDelay, out HTuple data)`

`HImage HFramegrabber.GrabDataAsync(out HRegion region, out HXLDCont contours, double maxDelay, out string data)`

## Description

The operator `GrabDataAsync` requests asynchronously grabbed images
and preprocessed image data from the image acquisition device specified by
*`acqHandle`*.
By default, `GrabDataAsync` also starts the next asynchronous grab
before the operator returns.
More information about the behavior of a specific image acquisition device
can be found in the corresponding interface documentation in the directory
`doc/html/reference/acquisition`.
The desired operational mode of the image acquisition device as well as a
suitable image part and additional interface-specific settings can be
specified using the operators [`OpenFramegrabber`](open_framegrabber.md) and
[`SetFramegrabberParam`](set_framegrabber_param.md).
Depending on the current configuration of the image acquisition device, the
preprocessed image data can be returned in terms of images
(*`image`*), regions (*`region`*), XLD contours
(*`contours`*), and control data (*`data`*).

The grab of the next image is finished by calling
`GrabDataAsync` or [`GrabImageAsync`](grab_image_async.md). If more than
*`maxDelay`* ms have passed since the asynchronous grab was
started, the asynchronously grabbed image is considered as too old
and a new image is grabbed, if necessary. If a negative value is assigned to
*`maxDelay`*, this control mechanism is deactivated.

To abort the grab, the operator [`SetFramegrabberParam`](set_framegrabber_param.md) with the
parameter `'do_abort_grab'` can be used if the specific image
acquisition interface supports it. Note that as an exception from
the description of the concurrent usage in multiple threads (see below)
`'do_abort_grab'` can also be used from another thread.

Please note that if you call the operators [`GrabImage`](grab_image.md) or
[`GrabData`](grab_data.md) after `GrabDataAsync`, the asynchronous
grab started by `GrabDataAsync` is aborted and a new
synchronous grab is started.

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively.

`GrabDataAsync` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / real / uint2)

Grabbed image data.

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Pre-processed image regions.

**`contours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Pre-processed XLD contours.

**`acqHandle`** (input_control)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the acquisition device to be used.

**`maxDelay`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Maximum tolerated delay between the start of the
asynchronous grab and the delivery of the image [ms].

Default:
-1.0

Suggested values:
-1.0, 20.0, 33.3, 40.0, 66.6, 80.0, 99.9

**`data`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

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
acquisition via `GrabDataAsync`, the operator
`GrabDataAsync` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`OpenFramegrabber`,
`GrabImageStart`,
`SetFramegrabberParam`

## Possible Successors

`GrabImageAsync`,
`SetFramegrabberParam`,
`CloseFramegrabber`

## See also

`OpenFramegrabber`,
`InfoFramegrabber`,
`SetFramegrabberParam`

## Module

Foundation
