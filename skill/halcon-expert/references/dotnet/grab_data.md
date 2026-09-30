# GrabData (Operator)

## Name

`GrabData` — Synchronous grab of images and preprocessed image data from the specified
image acquisition device.

## Signature

`static void HOperatorSet.GrabData(out HObject image, out HObject region, out HObject contours, HTuple acqHandle, out HTuple data)`

`HRegion HImage.GrabData(out HXLDCont contours, HFramegrabber acqHandle, out HTuple data)`

`HRegion HImage.GrabData(out HXLDCont contours, HFramegrabber acqHandle, out string data)`

`HImage HRegion.GrabData(out HXLDCont contours, HFramegrabber acqHandle, out HTuple data)`

`HImage HRegion.GrabData(out HXLDCont contours, HFramegrabber acqHandle, out string data)`

`HImage HFramegrabber.GrabData(out HRegion region, out HXLDCont contours, out HTuple data)`

`HImage HFramegrabber.GrabData(out HRegion region, out HXLDCont contours, out string data)`

## Description

The operator `GrabData` grabs images and preprocessed image data via
the image acquisition device specified by *`acqHandle`*. The desired
operational mode of the image acquisition device as well as a suitable
image part and additional interface-specific settings can be specified
using the operators [`OpenFramegrabber`](open_framegrabber.md) and
[`SetFramegrabberParam`](set_framegrabber_param.md). Depending on the current
configuration of the image acquisition device, the preprocessed
image data can be returned in terms of images (*`image`*),
regions (*`region`*), XLD contours (*`contours`*), and
control data (*`data`*).

To abort the grab, the operator [`SetFramegrabberParam`](set_framegrabber_param.md) with the
parameter `'do_abort_grab'` can be used if the specific image
acquisition interface supports it. Note that as an exception from
the description of the concurrent usage in multiple threads (see below)
`'do_abort_grab'` can also be used from another thread.

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively.

`GrabData` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / real / uint2)

Grabbed image data.

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Preprocessed image regions.

**`contours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Preprocessed XLD contours.

**`acqHandle`** (input_control)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the acquisition device to be used.

**`data`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Preprocessed control data.

## Example (HDevelop)

```
* Select a suitable image acquisition interface name AcqName
info_framegrabber(AcqName,'port',Information,Values)
* Open image acquisition device using the default settings, see
* documentation of the actually used interface for more details
open_framegrabber(AcqName,1,1,0,0,0,0,'default',-1,'default',-1.0, \
                  'default','default','default',-1,-1,AcqHandle)
* Grab and segment image
grab_data (Image, Region, Contours, AcqHandle, Data)
* Process Region...
close_framegrabber(AcqHandle)
```

## Result

If the image acquisition device is open and supports the image
acquisition via `GrabData`, the operator `GrabData`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`OpenFramegrabber`,
`GrabImageStart`,
`SetFramegrabberParam`

## Possible Successors

`GrabDataAsync`,
`GrabImageStart`,
`GrabImage`,
`GrabImageAsync`,
`SetFramegrabberParam`,
`CloseFramegrabber`

## See also

`OpenFramegrabber`,
`InfoFramegrabber`,
`SetFramegrabberParam`

## Module

Foundation
