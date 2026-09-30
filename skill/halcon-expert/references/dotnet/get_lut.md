# GetLut (Operator)

## Name

`GetLut` — Get current look-up-table (lut).

## Signature

`static void HOperatorSet.GetLut(HTuple windowHandle, out HTuple lookUpTable)`

`HTuple HWindow.GetLut()`

## Description

`GetLut` returns the name or the values of the look-up-table
(lut) of the window, currently used by [`DispImage`](disp_image.md) (or indirectly
by [`DispRegion`](disp_region.md), etc.) for output.
To set a look-up-table use [`SetLut`](set_lut.md). If the current table is a
system table without any modification ( by [`SetFix`](set_fix.md) ), the name
of the table is returned.
If it is a modified table, a table read from a file or a table for
output with pseudo real colors, the RGB-values of the table are returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`lookUpTable`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long)

Name of look-up-table or tuple of RGB-values.

## Result

`GetLut` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetLut`

## See also

`SetLut`

## Module

Foundation
