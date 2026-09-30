# SetFramegrabberLut (Operator)

## Name

`SetFramegrabberLut` — Set look-up table of the image acquisition device.

## Signature

`static void HOperatorSet.SetFramegrabberLut(HTuple acqHandle, HTuple imageRed, HTuple imageGreen, HTuple imageBlue)`

`void HFramegrabber.SetFramegrabberLut(HTuple imageRed, HTuple imageGreen, HTuple imageBlue)`

## Description

The operator `SetFramegrabberLut` sets the look-up table (LUT) of
the image acquisition device specified by *`acqHandle`*. Note that
this operation is not supported for all kinds of image acquisition devices.

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively.

`SetFramegrabberLut` runs in parallel with all non-exclusive
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

**`imageRed`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Red level of the LUT entries.

**`imageGreen`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Green level of the LUT entries.

**`imageBlue`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Blue level of the LUT entries.

## Result

The operator `SetFramegrabberLut` returns the value 2 (
H_MSG_TRUE)
if the specified LUT is correct and the image acquisition device is open.

## Possible Predecessors

`OpenFramegrabber`,
`GetFramegrabberLut`

## Possible Successors

`GrabImage`,
`GrabData`,
`GrabImageStart`,
`GrabImageAsync`,
`GrabDataAsync`

## See also

`GetFramegrabberLut`,
`OpenFramegrabber`

## Module

Foundation
