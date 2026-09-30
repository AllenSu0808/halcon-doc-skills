# QueryAllColors (Operator)

## Name

`QueryAllColors` — Query all color names.

## Signature

`static void HOperatorSet.QueryAllColors(HTuple windowHandle, out HTuple colors)`

`HTuple HWindow.QueryAllColors()`

## Description

`QueryAllColors` returns the names of all colors that
are known to HALCON. That doesn't mean that these colors are
available for specific screens. On some screens there may only be a
subset of colors available (see [`QueryColor`](query_color.md)). The HALCON colors
are used to display regions ([`DispRegion`](disp_region.md),
[`DispPolygon`](disp_polygon.md), [`DispCircle`](disp_circle.md), etc.). They can
be defined with [`SetColor`](set_color.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`colors`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Color names.

## Result

`QueryAllColors` always returns 2 (
H_MSG_TRUE)

## Possible Successors

`SetSystem`,
`SetColor`,
`DispRegion`

## See also

`QueryColor`,
`SetSystem`,
`SetColor`,
`DispRegion`,
`OpenWindow`

## Module

Foundation
