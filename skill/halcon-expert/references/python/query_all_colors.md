# query_all_colors (Operator)

## Name

`query_all_colors` — Query all color names.

## Signature

`def query_all_colors(window_handle: HHandle) -> Sequence[str]`

## Description

`query_all_colors` returns the names of all colors that
are known to HALCON. That doesn't mean that these colors are
available for specific screens. On some screens there may only be a
subset of colors available (see [`query_color`](query_color.md)). The HALCON colors
are used to display regions ([`disp_region`](disp_region.md),
[`disp_polygon`](disp_polygon.md), [`disp_circle`](disp_circle.md), etc.). They can
be defined with [`set_color`](set_color.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`colors`** (output_control)  string-array `→` Sequence[str]

Color names.

## Result

`query_all_colors` always returns 2 (
H_MSG_TRUE)

## Possible Successors

`set_system`,
`set_color`,
`disp_region`

## See also

`query_color`,
`set_system`,
`set_color`,
`disp_region`,
`open_window`

## Module

Foundation
