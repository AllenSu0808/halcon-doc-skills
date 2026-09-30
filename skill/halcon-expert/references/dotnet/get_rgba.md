# GetRgba (Operator)

## Name

`GetRgba` — Get the current color in RGBA-coding.

## Signature

`static void HOperatorSet.GetRgba(HTuple windowHandle, out HTuple red, out HTuple green, out HTuple blue, out HTuple alpha)`

`void HWindow.GetRgba(out HTuple red, out HTuple green, out HTuple blue, out HTuple alpha)`

## Description

`GetRgba` returns the output colors or gray values, respectively, for
the output window. They are defined by the four color components red, green,
blue and alpha.

The values returned by `GetRgba` can be set with
[`SetRgba`](set_rgba.md).

## Attention

`GetRgba` depends on the library libcanvas, which might not be
available on embedded systems.

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

**`alpha`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

The current color's alpha value.

## Result

`GetRgba` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetRgba`,
`DispObj`

## See also

`SetRgba`

## Module

Foundation
