# ClearColorTransLut (Operator)

## Name

`ClearColorTransLut` — Release the look-up-table needed for color space transformation.

## Signature

`static void HOperatorSet.ClearColorTransLut(HTuple colorTransLUTHandle)`

`static void HImage.ClearColorTransLut(HColorTransLUT colorTransLUTHandle)`

`void HColorTransLUT.ClearColorTransLut()`

## Description

The operator `ClearColorTransLut` frees the memory of the
look-up-table created by [`CreateColorTransLut`](create_color_trans_lut.md). After calling
`ClearColorTransLut` the handle *`colorTransLUTHandle`*
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`colorTransLUTHandle`** (input_control)  color_trans_lut `→` [HColorTransLUT](HColorTransLUT.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the look-up-table handle for the
color space transformation.

## Result

The operator `ClearColorTransLut` returns the value 2 (
H_MSG_TRUE)
if the
look-up-table was successfully released. Otherwise, an exception will be
raised.

## Possible Predecessors

`CreateColorTransLut`,
`ApplyColorTransLut`

## See also

`CreateColorTransLut`,
`ApplyColorTransLut`

## Module

Foundation
