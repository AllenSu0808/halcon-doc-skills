# gen_nurbs_interp (Operator)

## Name

`gen_nurbs_interp` — Create control data of a NURBS curve that interpolates given points.

## Signature

`gen_nurbs_interp( : : Rows, Cols, Tangents, Degree : CtrlRows, CtrlCols, Knots)`

## Description

`gen_nurbs_interp` creates the NURBS control data
*`CtrlRows`*, *`CtrlCols`*, and *`Knots`* of a NURBS
curve that interpolates the input points (*`Rows`*, *`Cols`*).
If the input point list is not closed (i.e., the first point is identical to
the last point), the tangents of the first and last point must be given
in *`Tangents`* in the order [drow_{0},dcol_{0},drow_{n-1},dcol_{n-1}]
(for closed point lists, *`Tangents`* must be an empty tuple).
Furthermore the *`Degree`* of the NURBS curve must be specified.

The output of `gen_nurbs_interp` can be used directly with
[`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md) with the weights vector set to
*'auto'*.

See the documentation of [`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md) for more information
on NURBS curves.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Rows`** (input_control)  coordinates.y-array `→`  (real)

Row coordinates of input point list.

Number of elements:
Rows == Cols

**`Cols`** (input_control)  coordinates.x-array `→`  (real)

Column coordinates of input point list.

Number of elements:
Cols == Rows

**`Tangents`** (input_control)  real-array `→`  (real)

Tangents at first and last point.

Default:
[]

**`Degree`** (input_control)  integer `→`  (integer)

Order of the output curve.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2`

**`CtrlRows`** (output_control)  coordinates.y-array `→`  (real)

Row coordinates of the control polygon.

**`CtrlCols`** (output_control)  coordinates.x-array `→`  (real)

Column coordinates of the control polygon.

Number of elements:
Cols == Rows

**`Knots`** (output_control)  real-array `→`  (real)

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
