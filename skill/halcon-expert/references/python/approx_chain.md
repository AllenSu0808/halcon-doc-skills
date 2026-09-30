# approx_chain (Operator)

## Name

`approx_chain` — Approximate a contour by arcs and lines.

## Warning

**`approx_chain` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def approx_chain(row: Sequence[int], column: Sequence[int], min_width_coord: float, max_width_coord: float, thresh_start: float, thresh_end: float, thresh_step: float, min_width_smooth: float, max_width_smooth: float, min_width_curve: int, max_width_curve: int, weight_1: float, weight_2: float, weight_3: float) -> Tuple[Sequence[int], Sequence[int], Sequence[float], Sequence[int], Sequence[int], Sequence[int], Sequence[int], Sequence[int], Sequence[int], Sequence[int]]`

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

**`row`** (input_control)  point.y-array `→` Sequence[int]

Row of the contour.

Default:
32

**`column`** (input_control)  point.x-array `→` Sequence[int]

Column of the contour.

Default:
32

**`min_width_coord`** (input_control)  real `→` float

Minimum width of Gauss operator for coordinate
smoothing (> 0.4).

Default:
0.5

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
min_width_coord
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`max_width_coord`** (input_control)  real `→` float

Maximum width of Gauss operator for coordinate
smoothing (> 0.4).

Default:
2.4

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
max_width_coord
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`thresh_start`** (input_control)  real `→` float

Minimum threshold value of the curvature for accepting
a corner (relative to the largest curvature present).

Default:
0.3

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8

Value range:
`0.1
≤
thresh_start
≤
0.9` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`thresh_end`** (input_control)  real `→` float

Maximum threshold value of the curvature for accepting
a corner (relative to the largest curvature present).

Default:
0.9

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8

Value range:
`0.1
≤
thresh_end
≤
0.9` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`thresh_step`** (input_control)  real `→` float

Step width for threshold increase.

Default:
0.2

Suggested values:
0.3, 0.4, 0.5

Value range:
`0.1
≤
thresh_step
≤
0.9` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`min_width_smooth`** (input_control)  real `→` float

Minimum width of Gauss operator for smoothing
the curvature function (> 0.4).

Default:
0.5

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
min_width_smooth
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`max_width_smooth`** (input_control)  real `→` float

Maximum width of Gauss operator for smoothing
the curvature function.

Default:
2.4

Suggested values:
0.5, 0.7, 1.0, 1.2, 1.5, 1.7

Value range:
`0.4
≤
max_width_smooth
≤
3.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`min_width_curve`** (input_control)  integer `→` int

Minimum width of curve area for curvature
determination (> 0.4).

Default:
2

Suggested values:
2, 5, 7

Value range:
`1
≤
min_width_curve
≤
12` (lin)

Minimum increment:
1

Recommended increment:
2

**`max_width_curve`** (input_control)  integer `→` int

Maximum width of curve area for curvature
determination.

Default:
12

Suggested values:
2, 5, 7

Value range:
`1
≤
max_width_curve
≤
20` (lin)

Minimum increment:
1

Recommended increment:
2

**`weight_1`** (input_control)  real `→` float

Weighting factor for approximation precision.

Default:
1.0

Suggested values:
0.0, 0.5, 1.0

Value range:
`0.0
≤
weight_1
≤
1.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

**`weight_2`** (input_control)  real `→` float

Weighting factor for large segments.

Default:
1.0

Suggested values:
0.0, 0.5, 1.0

Value range:
`0.0
≤
weight_2
≤
1.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

**`weight_3`** (input_control)  real `→` float

Weighting factor for small segments.

Default:
1.0

Suggested values:
0.0, 0.5, 1.0

Value range:
`0.0
≤
weight_3
≤
1.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

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
