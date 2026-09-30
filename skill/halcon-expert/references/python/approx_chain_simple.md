# approx_chain_simple (Operator)

## Name

`approx_chain_simple` — Approximate a contour by arcs and lines.

## Warning

**`approx_chain_simple` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def approx_chain_simple(row: Sequence[int], column: Sequence[int]) -> Tuple[Sequence[int], Sequence[int], Sequence[float], Sequence[int], Sequence[int], Sequence[int], Sequence[int], Sequence[int], Sequence[int], Sequence[int]]`

## Description

The contour of a curve is approximated by a sequence of
lines and arcs.

The result of the procedure is returned separately as arcs and
lines. If one is interested in the sequence of the segments the
individual resulting elements can be read successively from the
resulting tuples. The sequence can be taken from the return
parameter order (0: next element is next line segment, 1: next
element is next arc segment).

The operator `approx_chain_simple` behaves similarly as
[`approx_chain`](approx_chain.md) except that in the case of
`approx_chain_simple` the missing parameters are internally
allocated as follows: MinWidthCoord = 1.0, MaxWidthCoord = 3.0,
ThreshStart = 0.5, ThreshEnd = 0.9, ThreshStep = 0.3, MinWidthSmooth
= 1.0, MaxWidthSmooth = 3.0, MinWidthCurve = 2, MaxWidthCurve = 9,
Weight1 = 1.0, Weight2 = 1.0, Weight3 = 1.0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`row`** (input_control)  point.y-array `→` Sequence[int]

Row of the contour.

Default:
32

**`column`** (input_control)  point.x-array `→` Sequence[int]

Column of the contour.

Default:
32

**`arc_center_row`** (output_control)  arc.center.y-array `→` Sequence[int]

Row of the center of an arc.

**`arc_center_col`** (output_control)  arc.center.x-array `→` Sequence[int]

Column of the center of an arc.

**`arc_angle`** (output_control)  arc.angle.rad-array `→` Sequence[float]

Angle of an arc.

**`arc_begin_row`** (output_control)  arc.begin.y-array `→` Sequence[int]

Row of the starting point of an arc.

**`arc_begin_col`** (output_control)  arc.begin.x-array `→` Sequence[int]

Column of the starting point of an arc.

**`line_begin_row`** (output_control)  line.begin.y-array `→` Sequence[int]

Row of the starting point of a line segment.

**`line_begin_col`** (output_control)  line.begin.x-array `→` Sequence[int]

Column of the starting point of a line segment.

**`line_end_row`** (output_control)  line.end.y-array `→` Sequence[int]

Row of the ending point of a line segment.

**`line_end_col`** (output_control)  line.end.x-array `→` Sequence[int]

Column of the ending point of a line segment.

**`order`** (output_control)  integer-array `→` Sequence[int]

Sequence of line (value 0) and arc segments (value 1).

## Example (C)

```
/* read edge image */
read_image(&Image,"fig1_kan");
/* construct edge region */
hysteresis_threshold(Image,&RK1,64,255,40,1);
connection(RK1,&Rand);
/* fetch chain code */
T_get_region_contour(Rand,&Rows,&Columns);
firstline = get_i(Tline,0);
firstcol = get_i(Tcol,0);
/* approximation with lines and circular arcs */
T_approx_chain_simple(Rows,Columns,
                &Bzl,&Bzc,&Br,&Bwl,&Bwc,&Ll0,&Lc0,&Ll1,&Lc1,&order);
nob = length_tuple(Bzl);
nol = length_tuple(Ll0);
/* draw lines and arcs */
set_i(WindowHandleTuple,WindowHandle,0);
set_line_width(WindowHandle,4);
if (nob>0) T_disp_arc(Bzl,Bzc,Br,Bwl,Bwc);
set_line_width(WindowHandle,1);
if (nol>0) T_disp_line(WindowHandleTuple,Ll0,Lc0,Ll1,Lc1);
```

## Result

The operator `approx_chain_simple` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. Otherwise an exception is raised.

## Possible Predecessors

`sobel_amp`,
`edges_image`,
`get_region_contour`,
`threshold`,
`hysteresis_threshold`

## Possible Successors

`set_line_width`,
`disp_arc`,
`disp_line`

## Alternatives

`get_region_polygon`,
`approx_chain`

## See also

`get_region_chain`,
`smallest_circle`,
`disp_circle`,
`disp_line`

## Module

Foundation
