# query_lut (Operator)

## Name

`query_lut` — Query all available look-up-tables (lut).

## Signature

`def query_lut(window_handle: HHandle) -> Sequence[str]`

## Description

`query_lut` returns the names of all look-up-tables available on
the current used device. These tables can be set with [`set_lut`](set_lut.md).
An table named 'default' is always available.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`look_up_table`** (output_control)  string-array `→` Sequence[str]

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
