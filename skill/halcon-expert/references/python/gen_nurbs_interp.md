# gen_nurbs_interp (Operator)

## Name

`gen_nurbs_interp` — Create control data of a NURBS curve that interpolates given points.

## Signature

`def gen_nurbs_interp(rows: Sequence[float], cols: Sequence[float], tangents: Sequence[float], degree: int) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

## Description

`gen_nurbs_interp` creates the NURBS control data
*`ctrl_rows`*, *`ctrl_cols`*, and *`knots`* of a NURBS
curve that interpolates the input points (*`rows`*, *`cols`*).
If the input point list is not closed (i.e., the first point is identical to
the last point), the tangents of the first and last point must be given
in *`tangents`* in the order [drow_{0},dcol_{0},drow_{n-1},dcol_{n-1}]
(for closed point lists, *`tangents`* must be an empty tuple).
Furthermore the *`degree`* of the NURBS curve must be specified.

The output of `gen_nurbs_interp` can be used directly with
[`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md) with the weights vector set to
*"auto"*.

See the documentation of [`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md) for more information
on NURBS curves.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rows`** (input_control)  coordinates.y-array `→` Sequence[float]

Row coordinates of input point list.

Number of elements:
Rows == Cols

**`cols`** (input_control)  coordinates.x-array `→` Sequence[float]

Column coordinates of input point list.

Number of elements:
Cols == Rows

**`tangents`** (input_control)  real-array `→` Sequence[float]

Tangents at first and last point.

Default:
[]

**`degree`** (input_control)  integer `→` int

Order of the output curve.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2`

**`ctrl_rows`** (output_control)  coordinates.y-array `→` Sequence[float]

Row coordinates of the control polygon.

**`ctrl_cols`** (output_control)  coordinates.x-array `→` Sequence[float]

Column coordinates of the control polygon.

Number of elements:
Cols == Rows

**`knots`** (output_control)  real-array `→` Sequence[float]

The knot vector of the output curve.

## Result

If all input parameters are correct `gen_nurbs_interp` returns the
value 2 (
H_MSG_TRUE)
.

## Possible Successors

`gen_contour_nurbs_xld`

## See also

`draw_nurbs_interp`,
`draw_nurbs_interp_mod`

## References

L. Piegl, W. Tiller: ”The NURBS Book”, 2nd Edition, Springer, 1997.

## Module

Foundation
