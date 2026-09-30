# ApproxChain (Operator)

## Name

`ApproxChain` — Approximate a contour by arcs and lines.

## Warning

**`ApproxChain` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.ApproxChain(HTuple row, HTuple column, HTuple minWidthCoord, HTuple maxWidthCoord, HTuple threshStart, HTuple threshEnd, HTuple threshStep, HTuple minWidthSmooth, HTuple maxWidthSmooth, HTuple minWidthCurve, HTuple maxWidthCurve, HTuple weight1, HTuple weight2, HTuple weight3, out HTuple arcCenterRow, out HTuple arcCenterCol, out HTuple arcAngle, out HTuple arcBeginRow, out HTuple arcBeginCol, out HTuple lineBeginRow, out HTuple lineBeginCol, out HTuple lineEndRow, out HTuple lineEndCol, out HTuple order)`

`static void HMisc.ApproxChain(HTuple row, HTuple column, double minWidthCoord, double maxWidthCoord, double threshStart, double threshEnd, double threshStep, double minWidthSmooth, double maxWidthSmooth, int minWidthCurve, int maxWidthCurve, double weight1, double weight2, double weight3, out HTuple arcCenterRow, out HTuple arcCenterCol, out HTuple arcAngle, out HTuple arcBeginRow, out HTuple arcBeginCol, out HTuple lineBeginRow, out HTuple lineBeginCol, out HTuple lineEndRow, out HTuple lineEndCol, out HTuple order)`

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

**`row`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row of the contour.

Default:
32

**`column`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column of the contour.

Default:
32

**`minWidthCoord`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Minimum width of Gauss operator for coordinate
smoothing (> 0.4).

Default:
0.5

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
minWidthCoord
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`maxWidthCoord`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum width of Gauss operator for coordinate
smoothing (> 0.4).

Default:
2.4

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
maxWidthCoord
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`threshStart`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Minimum threshold value of the curvature for accepting
a corner (relative to the largest curvature present).

Default:
0.3

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8

Value range:
`0.1
≤
threshStart
≤
0.9` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`threshEnd`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum threshold value of the curvature for accepting
a corner (relative to the largest curvature present).

Default:
0.9

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8

Value range:
`0.1
≤
threshEnd
≤
0.9` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`threshStep`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Step width for threshold increase.

Default:
0.2

Suggested values:
0.3, 0.4, 0.5

Value range:
`0.1
≤
threshStep
≤
0.9` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`minWidthSmooth`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Minimum width of Gauss operator for smoothing
the curvature function (> 0.4).

Default:
0.5

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
minWidthSmooth
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`maxWidthSmooth`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum width of Gauss operator for smoothing
the curvature function.

Default:
2.4

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
maxWidthSmooth
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`minWidthCurve`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum width of curve area for curvature
determination (> 0.4).

Default:
2

Suggested values:
2, 5, 7

Value range:
`1
≤
minWidthCurve
≤
12` (lin)

Minimum increment:
1

Recommended increment:
2

**`maxWidthCurve`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum width of curve area for curvature
determination.

Default:
12

Suggested values:
2, 5, 7

Value range:
`1
≤
maxWidthCurve
≤
20` (lin)

Minimum increment:
1

Recommended increment:
2

**`weight1`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Weighting factor for approximation precision.

Default:
1.0

Suggested values:
0.0, 0.5, 1.0

Value range:
`0.0
≤
weight1
≤
1.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

**`weight2`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Weighting factor for large segments.

Default:
1.0

Suggested values:
0.0, 0.5, 1.0

Value range:
`0.0
≤
weight2
≤
1.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

**`weight3`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Weighting factor for small segments.

Default:
1.0

Suggested values:
0.0, 0.5, 1.0

Value range:
`0.0
≤
weight3
≤
1.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

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

The operator `ApproxChain` returns the value 2 (
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
`ApproxChainSimple`

## See also

`GetRegionChain`,
`SmallestCircle`,
`DispCircle`,
`DispLine`

## Module

Foundation
