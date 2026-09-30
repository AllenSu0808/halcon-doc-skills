# SetFramegrabberParam (Operator)

## Name

`SetFramegrabberParam` — Set specific parameters of an image acquisition device.

## Signature

`static void HOperatorSet.SetFramegrabberParam(HTuple acqHandle, HTuple param, HTuple value)`

`void HFramegrabber.SetFramegrabberParam(HTuple param, HTuple value)`

`void HFramegrabber.SetFramegrabberParam(string param, string value)`

## Description

The operator `SetFramegrabberParam` sets specific parameters
for the image acquisition device specified by *`acqHandle`*.
Additional information for a specific image acquisition device is
available via [`InfoFramegrabber`](info_framegrabber.md). A comprehensive documentation
of all image acquisition device-specific parameters can be found in the
corresponding interface documentation in the directory
`doc/html/reference/acquisition`.

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively.

`SetFramegrabberParam` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- acqHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`acqHandle`** (input_control, state is modified)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the acquisition device to be used.

**`param`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter name.

Suggested values:
"color_space", "continuous_grabbing", "external_trigger", "grab_timeout", "image_height", "image_width", "port", "start_column", "start_row", "volatile"

**`value`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Parameter value to be set.

## Result

If the image acquisition device is open and the specified parameter /
parameter value is supported, the operator `SetFramegrabberParam`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`OpenFramegrabber`

## Possible Successors

`GrabImage`,
`GrabData`,
`GrabImageStart`,
`GrabImageAsync`,
`GrabDataAsync`,
`GetFramegrabberParam`

## See also

`OpenFramegrabber`,
`InfoFramegrabber`,
`GetFramegrabberParam`

## Module

Foundation
