# approx_chain (Operator)

## Name

`approx_chain` — Approximate a contour by arcs and lines.

## Warning

**`approx_chain` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`approx_chain( : : Row, Column, MinWidthCoord, MaxWidthCoord, ThreshStart, ThreshEnd, ThreshStep, MinWidthSmooth, MaxWidthSmooth, MinWidthCurve, MaxWidthCurve, Weight1, Weight2, Weight3 : ArcCenterRow, ArcCenterCol, ArcAngle, ArcBeginRow, ArcBeginCol, LineBeginRow, LineBeginCol, LineEndRow, LineEndCol, Order)`

## Description

The coordinates of a curve are approximated by a row of lines
and arcs. The procedure tries values from a user-definable range
for certain parameters. The limits of these ranges are explicitly
stated in the parameter list of the function
(MinWidthCoord ... MaxWidthCoord, ThreshStart ... ThreshEnd,
MinWidthSmooth ... MaxWidthSmooth, MinWidthCurve ... MaxWidthCurve).
Additionally, the step width for the parameter area of the threshold
value for pointed corners has to be indicated (ThreshStep). By
narrowing the covered areas the runtime of the calculation can be
shortened, but the result may deteriorate.

The parameters Weight1, Weight2 and Weight3 indicate whether the
desired weighting is placed more on precision of the approximation,
obtaining as much large segments as possible or as few small
segments as possible. Thus, for (Weight1,Weight2,Weight3) (1,0,0)
creates a very precise approximation and (0,1,1) an approximation
with as few large segments as possible.

The result of the procedure is returned separately as arcs and
lines. If one is interested in the sequence of the segments the
individual resulting elements can be read successively from the
resulting tuples; the sequence can be taken from the return
parameter order (0: next element is next line segment, 1: next
element is next arc segment).

## Attention

Contours which can possibly consist of only one segment should also
be examined with a threshold maximum (ThreshEnd) > 1.0, because
otherwise at least one “corner point” is determined in any case.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Row`** (input_control)  point.y-array `→`  (integer)

Row of the contour.

Default:
32

**`Column`** (input_control)  point.x-array `→`  (integer)

Column of the contour.

Default:
32

**`MinWidthCoord`** (input_control)  real `→`  (real)

Minimum width of Gauss operator for coordinate
smoothing (> 0.4).

Default:
0.5

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
MinWidthCoord
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`MaxWidthCoord`** (input_control)  real `→`  (real)

Maximum width of Gauss operator for coordinate
smoothing (> 0.4).

Default:
2.4

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
MaxWidthCoord
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`ThreshStart`** (input_control)  real `→`  (real)

Minimum threshold value of the curvature for accepting
a corner (relative to the largest curvature present).

Default:
0.3

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8

Value range:
`0.1
≤
ThreshStart
≤
0.9` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`ThreshEnd`** (input_control)  real `→`  (real)

Maximum threshold value of the curvature for accepting
a corner (relative to the largest curvature present).

Default:
0.9

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8

Value range:
`0.1
≤
ThreshEnd
≤
0.9` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`ThreshStep`** (input_control)  real `→`  (real)

Step width for threshold increase.

Default:
0.2

Suggested values:
0.3, 0.4, 0.5

Value range:
`0.1
≤
ThreshStep
≤
0.9` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`MinWidthSmooth`** (input_control)  real `→`  (real)

Minimum width of Gauss operator for smoothing
the curvature function (> 0.4).

Default:
0.5

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
MinWidthSmooth
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`MaxWidthSmooth`** (input_control)  real `→`  (real)

Maximum width of Gauss operator for smoothing
the curvature function.

Default:
2.4

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
MaxWidthSmooth
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`MinWidthCurve`** (input_control)  integer `→`  (integer)

Minimum width of curve area for curvature
determination (> 0.4).

Default:
2

Suggested values:
2, 5, 7

Value range:
`1
≤
MinWidthCurve
≤
12` (lin)

Minimum increment:
1

Recommended increment:
2

**`MaxWidthCurve`** (input_control)  integer `→`  (integer)

Maximum width of curve area for curvature
determination.

Default:
12

Suggested values:
2, 5, 7

Value range:
`1
≤
MaxWidthCurve
≤
20` (lin)

Minimum increment:
1

Recommended increment:
2

**`Weight1`** (input_control)  real `→`  (real)

Weighting factor for approximation precision.

Default:
1.0

Suggested values:
0.0, 0.5, 1.0

Value range:
`0.0
≤
Weight1
≤
1.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

**`Weight2`** (input_control)  real `→`  (real)

Weighting factor for large segments.

Default:
1.0

Suggested values:
0.0, 0.5, 1.0

Value range:
`0.0
≤
Weight2
≤
1.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

**`Weight3`** (input_control)  real `→`  (real)

Weighting factor for small segments.

Default:
1.0

Suggested values:
0.0, 0.5, 1.0

Value range:
`0.0
≤
Weight3
≤
1.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

**`ArcCenterRow`** (output_control)  arc.center.y-array `→`  (integer)

Row of the center of an arc.

**`ArcCenterCol`** (output_control)  arc.center.x-array `→`  (integer)

Column of the center of an arc.

**`ArcAngle`** (output_control)  arc.angle.rad-array `→`  (real)

Angle of an arc.

**`ArcBeginRow`** (output_control)  arc.begin.y-array `→`  (integer)

Row of the starting point of an arc.

**`ArcBeginCol`** (output_control)  arc.begin.x-array `→`  (integer)

Column of the starting point of an arc.

**`LineBeginRow`** (output_control)  line.begin.y-array `→`  (integer)

Row of the starting point of a line segment.

**`LineBeginCol`** (output_control)  line.begin.x-array `→`  (integer)

Column of the starting point of a line segment.

**`LineEndRow`** (output_control)  line.end.y-array `→`  (integer)

Row of the ending point of a line segment.

**`LineEndCol`** (output_control)  line.end.x-array `→`  (integer)

Column of the ending point of a line segment.

**`Order`** (output_control)  integer-array `→`  (integer)

Sequence of line (value 0) and arc segments (value 1).

## Example (C)

```
/* read edge image  */
read_image(&Image,"fig1_kan");
/* construct edge region  */
hysteresis_threshold(Image,&RK1,64,255,40,1);
connection(RK1,&Rand);
/* fetch chain code  */
T_get_region_contour(Rand,&Rows,&Columns);
firstline = get_i(Tline,0);
firstcol = get_i(Tcol,0);
/* approximation with lines and circular arcs */
set_d(t1,0.4,0);
set_d(t2,2.4,0);

set_d(t3,0.3,0);
set_d(t4,0.9,0);

set_d(t5,0.2,0);

set_d(t6,0.4,0);
set_d(t7,2.4,0);

set_i(t8,2,0);
set_i(t9,12,0);

set_d(t10,1.0,0);
set_d(t11,1.0,0);
set_d(t12,1.0,0);

T_approx_chain(Rows,Columns,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,
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

The operator `approx_chain` returns the value 2 (
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
`approx_chain_simple`

## See also

`get_region_chain`,
`smallest_circle`,
`disp_circle`,
`disp_line`

## Module

Foundation
