# get_lut (Operator)

## Name

`get_lut` — Get current look-up-table (lut).

## Signature

`def get_lut(window_handle: HHandle) -> Sequence[Union[int, str]]`

## Description

`get_lut` returns the name or the values of the look-up-table
(lut) of the window, currently used by [`disp_image`](disp_image.md) (or indirectly
by [`disp_region`](disp_region.md), etc.) for output.
To set a look-up-table use [`set_lut`](set_lut.md). If the current table is a
system table without any modification ( by [`set_fix`](set_fix.md) ), the name
of the table is returned.
If it is a modified table, a table read from a file or a table for
output with pseudo real colors, the RGB-values of the table are returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`look_up_table`** (output_control)  string-array `→` Sequence[Union[int, str]]

Name of look-up-table or tuple of RGB-values.

## Result

`get_lut` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_lut`

## See also

`set_lut`

## Module

Foundation
