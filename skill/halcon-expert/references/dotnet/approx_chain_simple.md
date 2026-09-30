# ApproxChainSimple (Operator)

## Name

`ApproxChainSimple` — Approximate a contour by arcs and lines.

## Warning

**`ApproxChainSimple` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.ApproxChainSimple(HTuple row, HTuple column, out HTuple arcCenterRow, out HTuple arcCenterCol, out HTuple arcAngle, out HTuple arcBeginRow, out HTuple arcBeginCol, out HTuple lineBeginRow, out HTuple lineBeginCol, out HTuple lineEndRow, out HTuple lineEndCol, out HTuple order)`

`static void HMisc.ApproxChainSimple(HTuple row, HTuple column, out HTuple arcCenterRow, out HTuple arcCenterCol, out HTuple arcAngle, out HTuple arcBeginRow, out HTuple arcBeginCol, out HTuple lineBeginRow, out HTuple lineBeginCol, out HTuple lineEndRow, out HTuple lineEndCol, out HTuple order)`

## Description

The contour of a curve is approximated by a sequence of
lines and arcs.

The result of the procedure is returned separately as arcs and
lines. If one is interested in the sequence of the segments the
individual resulting elements can be read successively from the
resulting tuples. The sequence can be taken from the return
parameter order (0: next element is next line segment, 1: next
element is next arc segment).

The operator `ApproxChainSimple` behaves similarly as
[`ApproxChain`](approx_chain.md) except that in the case of
`ApproxChainSimple` the missing parameters are internally
allocated as follows: MinWidthCoord = 1.0, MaxWidthCoord = 3.0,
ThreshStart = 0.5, ThreshEnd = 0.9, ThreshStep = 0.3, MinWidthSmooth
= 1.0, MaxWidthSmooth = 3.0, MinWidthCurve = 2, MaxWidthCurve = 9,
Weight1 = 1.0, Weight2 = 1.0, Weight3 = 1.0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`row`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row of the contour.

Default:
32

**`column`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column of the contour.

Default:
32

**`arcCenterRow`** (output_control)  arc.center.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row of the center of an arc.

**`arcCenterCol`** (output_control)  arc.center.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column of the center of an arc.

**`arcAngle`** (output_control)  arc.angle.rad-array `→` [HTuple](HTuple.md) (*double*)

Angle of an arc.

**`arcBeginRow`** (output_control)  arc.begin.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row of the starting point of an arc.

**`arcBeginCol`** (output_control)  arc.begin.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column of the starting point of an arc.

**`lineBeginRow`** (output_control)  line.begin.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row of the starting point of a line segment.

**`lineBeginCol`** (output_control)  line.begin.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column of the starting point of a line segment.

**`lineEndRow`** (output_control)  line.end.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row of the ending point of a line segment.

**`lineEndCol`** (output_control)  line.end.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column of the ending point of a line segment.

**`order`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

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

The operator `ApproxChainSimple` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. Otherwise an exception is raised.

## Possible Predecessors

`SobelAmp`,
`EdgesImage`,
`GetRegionContour`,
`Threshold`,
`HysteresisThreshold`

## Possible Successors

`SetLineWidth`,
`DispArc`,
`DispLine`

## Alternatives

`GetRegionPolygon`,
`ApproxChain`

## See also

`GetRegionChain`,
`SmallestCircle`,
`DispCircle`,
`DispLine`

## Module

Foundation
