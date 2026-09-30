# SetWindowDc (Operator)

## Name

`SetWindowDc` — Set the device context of a virtual graphics window (Windows NT).

## Signature

`static void HOperatorSet.SetWindowDc(HTuple windowHandle, HTuple WINHDC)`

`void HWindow.SetWindowDc(IntPtr WINHDC)`

## Description

`SetWindowDc` sets the device context of a window previously
opened with [`NewExternWindow`](new_extern_window.md). All output
([`DispRegion`](disp_region.md), [`DispImage`](disp_image.md), etc.) is done in the
window with this device context.

The parameter *`WINHDC`* contains the device context of the
window in which HALCON should output its data. This device context
is used in all output routines of HALCON.

## Attention

The window *`windowHandle`* has to be created with
[`NewExternWindow`](new_extern_window.md) beforehand.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`WINHDC`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

device context of WINHWnd.

Restriction:
`WINHDC != 0`

## Result

If the values of the specified parameters are correct,
`SetWindowDc` returns 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`NewExternWindow`

## Possible Successors

`DispImage`,
`DispRegion`

## See also

`NewExternWindow`,
`DispRegion`,
`DispImage`,
`DispColor`,
`SetLut`,
`QueryColor`,
`SetColor`,
`SetRgb`,
`SetHsi`,
`SetPixel`,
`SetGray`,
`SetPart`,
`SetPartStyle`,
`QueryWindowType`,
`GetWindowType`,
`SetWindowType`,
`GetMposition`,
`SetTposition`,
`SetWindowExtents`,
`GetWindowExtents`,
`SetWindowAttr`,
`SetCheck`,
`SetSystem`

## Module

Foundation
