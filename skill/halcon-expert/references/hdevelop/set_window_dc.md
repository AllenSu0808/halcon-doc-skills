# set_window_dc (Operator)

## Name

`set_window_dc` — Set the device context of a virtual graphics window (Windows NT).

## Signature

`set_window_dc( : : WindowHandle, WINHDC : )`

## Description

`set_window_dc` sets the device context of a window previously
opened with [`new_extern_window`](new_extern_window.md). All output
([`disp_region`](disp_region.md), [`disp_image`](disp_image.md), etc.) is done in the
window with this device context.

The parameter *`WINHDC`* contains the device context of the
window in which HALCON should output its data. This device context
is used in all output routines of HALCON.

## Attention

The window *`WindowHandle`* has to be created with
[`new_extern_window`](new_extern_window.md) beforehand.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`WINHDC`** (input_control)  pointer `→`  (integer)

device context of WINHWnd.

Restriction:
`WINHDC != 0`

## Result

If the values of the specified parameters are correct,
`set_window_dc` returns 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`new_extern_window`

## Possible Successors

`disp_image`,
`disp_region`

## See also

`new_extern_window`,
`disp_region`,
`disp_image`,
`disp_color`,
`set_lut`,
`query_color`,
`set_color`,
`set_rgb`,
`set_hsi`,
`set_pixel`,
`set_gray`,
`set_part`,
`set_part_style`,
`query_window_type`,
`get_window_type`,
`set_window_type`,
`get_mposition`,
`set_tposition`,
`set_window_extents`,
`get_window_extents`,
`set_window_attr`,
`set_check`,
`set_system`

## Module

Foundation
