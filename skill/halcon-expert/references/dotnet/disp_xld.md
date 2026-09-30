# DispXld (Operator)

## Name

`DispXld` — Display an XLD object.

## Signature

`static void HOperatorSet.DispXld(HObject XLDObject, HTuple windowHandle)`

`void HXLD.DispXld(HWindow windowHandle)`

`void HWindow.DispXld(HXLD XLDObject)`

## Description

`DispXld` serves to display an XLD object of arbitrary
type.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLDObject`** (input_object)  xld-array `→` [HXLD](HXLD.md)

XLD object to display.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## See also

`DispImage`,
`DispRegion`,
`DispChannel`,
`DispColor`,
`DispLine`,
`DispArc`

## Module

Foundation
