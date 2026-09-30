# GetFix (Operator)

## Name

`GetFix` — Get mode of fixing of current look-up-table (lut).

## Warning

**`GetFix` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.GetFix(HTuple windowHandle, out HTuple mode)`

`string HWindow.GetFix()`

## Description

Use `GetFix` to get mode of fixing of current look-up-table
(look-up-table of valid window) set before by [`SetFix`](set_fix.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`mode`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Current Mode of fixing.

## Result

`GetFix` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetFix`,
`SetPixel`,
`SetRgb`

## See also

`SetFix`

## Module

Foundation
