# query_lut (Operator)

## Name

`query_lut` — Query all available look-up-tables (lut).

## Signature

`query_lut( : : WindowHandle : LookUpTable)`

## Description

`query_lut` returns the names of all look-up-tables available on
the current used device. These tables can be set with [`set_lut`](set_lut.md).
An table named 'default' is always available.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`LookUpTable`** (output_control)  string-array `→`  (string)

Names of look-up-tables.

## Result

`query_lut` returns 2 (
H_MSG_TRUE)
if a window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_lut`,
`disp_lut`

## See also

`set_lut`

## Module

Foundation
