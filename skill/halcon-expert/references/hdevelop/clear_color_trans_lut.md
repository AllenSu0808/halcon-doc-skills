# clear_color_trans_lut (Operator)

## Name

`clear_color_trans_lut` — Release the look-up-table needed for color space transformation.

## Signature

`clear_color_trans_lut( : : ColorTransLUTHandle : )`

## Description

The operator `clear_color_trans_lut` frees the memory of the
look-up-table created by [`create_color_trans_lut`](create_color_trans_lut.md). After calling
`clear_color_trans_lut` the handle *`ColorTransLUTHandle`*
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ColorTransLUTHandle`** (input_control)  color_trans_lut `→`  (handle)

Handle of the look-up-table handle for the
color space transformation.

## Result

The operator `clear_color_trans_lut` returns the value 2 (
H_MSG_TRUE)
if the
look-up-table was successfully released. Otherwise, an exception will be
raised.

## Possible Predecessors

`create_color_trans_lut`,
`apply_color_trans_lut`

## See also

`create_color_trans_lut`,
`apply_color_trans_lut`

## Module

Foundation
