# SetPartStyle (Operator)

## Name

`SetPartStyle` — Define an interpolation method for gray value output.

## Signature

`static void HOperatorSet.SetPartStyle(HTuple windowHandle, HTuple style)`

`void HWindow.SetPartStyle(int style)`

## Description

`SetPartStyle` defines the interpolation method to
zoom an image part which is displayed in the window. Interpolation
takes place, if the output window has different size than the image
to display (e.g., after a call to [`SetPart`](set_part.md) or a
window resize). Three modes are supported:

- **0** —

  no interpolation (low quality, very fast).
- **1** —

  unweighted interpolation (medium quality and run time)
- **2** —

  weighted interpolation (high quality, slow)

The current value can be queried with [`GetPartStyle`](get_part_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`style`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Interpolation method for image output:
0 (fast, low quality) to 2 (slow, high quality).

Default:
0

List of values:
0, 1, 2

## Result

`SetPartStyle` returns 2 (
H_MSG_TRUE)
if the parameter is correct
and the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`GetPartStyle`

## Possible Successors

`SetPart`,
`DispImage`,
`DispRegion`

## Alternatives

`AffineTransImage`

## See also

`GetPartStyle`,
`SetPart`,
`DispImage`,
`DispColor`

## Module

Foundation
