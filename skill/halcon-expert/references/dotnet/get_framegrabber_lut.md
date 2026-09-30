# GetFramegrabberLut (Operator)

## Name

`GetFramegrabberLut` — Query look-up table of the image acquisition device.

## Signature

`static void HOperatorSet.GetFramegrabberLut(HTuple acqHandle, out HTuple imageRed, out HTuple imageGreen, out HTuple imageBlue)`

`void HFramegrabber.GetFramegrabberLut(out HTuple imageRed, out HTuple imageGreen, out HTuple imageBlue)`

## Description

The operator `GetFramegrabberLut` queries the look-up table (LUT) of
the image acquisition device specified by *`acqHandle`*. Note that
this operation is not supported for all kinds of image acquisition devices.

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively.

`GetFramegrabberLut` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`acqHandle`** (input_control)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the acquisition device to be used.

**`imageRed`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Red level of the LUT entries.

**`imageGreen`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Green level of the LUT entries.

**`imageBlue`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Blue level of the LUT entries.

## Result

The operator `GetFramegrabberLut` returns the value 2 (
H_MSG_TRUE)
if the image acquisition device is open.

## Possible Predecessors

`OpenFramegrabber`

## Possible Successors

`SetFramegrabberLut`

## See also

`SetFramegrabberLut`,
`OpenFramegrabber`

## Module

Foundation
