# grab_data (Operator)

## Name

`grab_data` — Synchronous grab of images and preprocessed image data from the specified
image acquisition device.

## Signature

`def grab_data(acq_handle: HHandle) -> Tuple[HObject, HObject, HObject, Sequence[HTupleElementType]]`

`def grab_data_s(acq_handle: HHandle) -> Tuple[HObject, HObject, HObject, HTupleElementType]`

## Description

The operator `grab_data` grabs images and preprocessed image data via
the image acquisition device specified by *`acq_handle`*. The desired
operational mode of the image acquisition device as well as a suitable
image part and additional interface-specific settings can be specified
using the operators [`open_framegrabber`](open_framegrabber.md) and
[`set_framegrabber_param`](set_framegrabber_param.md). Depending on the current
configuration of the image acquisition device, the preprocessed
image data can be returned in terms of images (*`image`*),
regions (*`region`*), XLD contours (*`contours`*), and
control data (*`data`*).

To abort the grab, the operator [`set_framegrabber_param`](set_framegrabber_param.md) with the
parameter `'do_abort_grab'` can be used if the specific image
acquisition interface supports it. Note that as an exception from
the description of the concurrent usage in multiple threads (see below)
`'do_abort_grab'` can also be used from another thread.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`grab_data` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image(-array) `→` HObject (byte / real / uint2)

Grabbed image data.

**`region`** (output_object)  region(-array) `→` HObject

Preprocessed image regions.

**`contours`** (output_object)  xld_cont(-array) `→` HObject

Preprocessed XLD contours.

**`acq_handle`** (input_control)  framegrabber `→` HHandle

Handle of the acquisition device to be used.

**`data`** (output_control)  string(-array) `→` Sequence[HTupleElementType]

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
acquisition via `grab_data`, the operator `grab_data`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_framegrabber`,
`grab_image_start`,
`set_framegrabber_param`

## Possible Successors

`grab_data_async`,
`grab_image_start`,
`grab_image`,
`grab_image_async`,
`set_framegrabber_param`,
`close_framegrabber`

## See also

`open_framegrabber`,
`info_framegrabber`,
`set_framegrabber_param`

## Module

Foundation
