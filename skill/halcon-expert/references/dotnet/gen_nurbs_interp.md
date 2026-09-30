# GenNurbsInterp (Operator)

## Name

`GenNurbsInterp` — Create control data of a NURBS curve that interpolates given points.

## Signature

`static void HOperatorSet.GenNurbsInterp(HTuple rows, HTuple cols, HTuple tangents, HTuple degree, out HTuple ctrlRows, out HTuple ctrlCols, out HTuple knots)`

## Description

`GenNurbsInterp` creates the NURBS control data
*`ctrlRows`*, *`ctrlCols`*, and *`knots`* of a NURBS
curve that interpolates the input points (*`rows`*, *`cols`*).
If the input point list is not closed (i.e., the first point is identical to
the last point), the tangents of the first and last point must be given
in *`tangents`* in the order [drow_{0},dcol_{0},drow_{n-1},dcol_{n-1}]
(for closed point lists, *`tangents`* must be an empty tuple).
Furthermore the *`degree`* of the NURBS curve must be specified.

The output of `GenNurbsInterp` can be used directly with
[`GenContourNurbsXld`](gen_contour_nurbs_xld.md) with the weights vector set to
*"auto"*.

See the documentation of [`GenContourNurbsXld`](gen_contour_nurbs_xld.md) for more information
on NURBS curves.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rows`** (input_control)  coordinates.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of input point list.

Number of elements:
Rows == Cols

**`cols`** (input_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of input point list.

Number of elements:
Cols == Rows

**`tangents`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tangents at first and last point.

Default:
[]

**`degree`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Order of the output curve.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2`

**`ctrlRows`** (output_control)  coordinates.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the control polygon.

**`ctrlCols`** (output_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the control polygon.

Number of elements:
Cols == Rows

**`knots`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

The knot vector of the output curve.

## Result

If all input parameters are correct `GenNurbsInterp` returns the
value 2 (
H_MSG_TRUE)
.

## Possible Successors

`GenContourNurbsXld`

## See also

`DrawNurbsInterp`,
`DrawNurbsInterpMod`

## References

L. Piegl, W. Tiller: ”The NURBS Book”, 2nd Edition, Springer, 1997.

## Module

Foundation
