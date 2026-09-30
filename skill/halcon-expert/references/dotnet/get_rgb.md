# GetRgb (Operator)

## Name

`GetRgb` — Get the current color in RGB-coding.

## Signature

`static void HOperatorSet.GetRgb(HTuple windowHandle, out HTuple red, out HTuple green, out HTuple blue)`

`void HWindow.GetRgb(out HTuple red, out HTuple green, out HTuple blue)`

## Description

`GetRgb` returns the output colors or gray values, respectively, for
the output window. They are defined by the three color
components red, green and blue.

The values returned by `GetRgb` can be set with
[`SetRgb`](set_rgb.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`red`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

The current color's red value.

**`green`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

The current color's green value.

**`blue`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

The current color's blue value.

## Result

`GetRgb` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetRgb`,
`DispRegion`,
`DispImage`

## See also

`SetRgb`

## Module

Foundation
