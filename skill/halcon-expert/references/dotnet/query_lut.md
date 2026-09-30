# QueryLut (Operator)

## Name

`QueryLut` — Query all available look-up-tables (lut).

## Signature

`static void HOperatorSet.QueryLut(HTuple windowHandle, out HTuple lookUpTable)`

`HTuple HWindow.QueryLut()`

## Description

`QueryLut` returns the names of all look-up-tables available on
the current used device. These tables can be set with [`SetLut`](set_lut.md).
An table named 'default' is always available.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`lookUpTable`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of look-up-tables.

## Result

`QueryLut` returns 2 (
H_MSG_TRUE)
if a window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetLut`,
`DispLut`

## See also

`SetLut`

## Module

Foundation
