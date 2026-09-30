# GetPartStyle (Operator)

## Name

`GetPartStyle` — Get the current interpolation mode for gray value display.

## Signature

`static void HOperatorSet.GetPartStyle(HTuple windowHandle, out HTuple style)`

`int HWindow.GetPartStyle()`

## Description

`GetPartStyle` returns the interpolation mode used for
displaying an image part in the window. An interpolation
takes place if the output window is larger than the image format or
the image output format (see [`SetPart`](set_part.md)). HALCON supports
three interpolation modes:

- **0** —

  no interpolation (low quality, very fast).
- **1** —

  unweighted interpolation (average quality and computation time)
- **2** —

  weighted interpolation (high quality, slow)

The current mode can be changed with [`SetPartStyle`](set_part_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`style`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Interpolation mode for image display:
0 (fast, low quality) to 2 (slow, high quality).

List of values:
0, 1, 2

## Result

`GetPartStyle` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetPartStyle`,
`DispRegion`,
`DispImage`

## See also

`SetPartStyle`,
`SetPart`,
`DispImage`,
`DispColor`

## Module

Foundation
