# disp_xld (Operator)

## Name

`disp_xld` — Display an XLD object.

## Signature

`disp_xld(XLDObject : : WindowHandle : )`

## Description

`disp_xld` serves to display an XLD object of arbitrary
type.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLDObject`** (input_object)  xld-array `→` object

XLD object to display.

**`WindowHandle`** (input_control)  window `→`  (handle)

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
