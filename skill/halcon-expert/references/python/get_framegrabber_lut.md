# get_framegrabber_lut (Operator)

## Name

`get_framegrabber_lut` — Query look-up table of the image acquisition device.

## Signature

`def get_framegrabber_lut(acq_handle: HHandle) -> Tuple[Sequence[int], Sequence[int], Sequence[int]]`

## Description

The operator `get_framegrabber_lut` queries the look-up table (LUT) of
the image acquisition device specified by *`acq_handle`*. Note that
this operation is not supported for all kinds of image acquisition devices.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`get_framegrabber_lut` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`acq_handle`** (input_control)  framegrabber `→` HHandle

Handle of the acquisition device to be used.

**`image_red`** (output_control)  integer-array `→` Sequence[int]

Red level of the LUT entries.

**`image_green`** (output_control)  integer-array `→` Sequence[int]

Green level of the LUT entries.

**`image_blue`** (output_control)  integer-array `→` Sequence[int]

Blue level of the LUT entries.

## Result

The operator `get_framegrabber_lut` returns the value 2 (
H_MSG_TRUE)
if the image acquisition device is open.

## Possible Predecessors

`open_framegrabber`

## Possible Successors

`set_framegrabber_lut`

## See also

`set_framegrabber_lut`,
`open_framegrabber`

## Module

Foundation
