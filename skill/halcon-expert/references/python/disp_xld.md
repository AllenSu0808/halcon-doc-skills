# disp_xld (Operator)

## Name

`disp_xld` — Display an XLD object.

## Signature

`def disp_xld(xldobject: HObject, window_handle: HHandle) -> None`

## Description

`disp_xld` serves to display an XLD object of arbitrary
type.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`xldobject`** (input_object)  xld-array `→` HObject

XLD object to display.

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

## See also

`disp_image`,
`disp_region`,
`disp_channel`,
`disp_color`,
`disp_line`,
`disp_arc`

## Module

Foundation
