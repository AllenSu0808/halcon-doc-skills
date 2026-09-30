# GenContourNurbsXld (Operator)

## Name

`GenContourNurbsXld` — Transform a NURBS curve into an XLD contour.

## Signature

`static void HOperatorSet.GenContourNurbsXld(out HObject contour, HTuple rows, HTuple cols, HTuple knots, HTuple weights, HTuple degree, HTuple maxError, HTuple maxDistance)`

`void HXLDCont.GenContourNurbsXld(HTuple rows, HTuple cols, HTuple knots, HTuple weights, int degree, HTuple maxError, HTuple maxDistance)`

`void HXLDCont.GenContourNurbsXld(HTuple rows, HTuple cols, string knots, string weights, int degree, double maxError, double maxDistance)`

## Description

`GenContourNurbsXld` generates an XLD *`contour`* that
approximates a
NURBS curve (non-uniform rational B-Spline curve). The NURBS curve is
specified by its *`degree`*, a control polygon (via *`rows`* and
*`cols`*), a *`weights`* vector and a *`knots`*
vector.

The *`degree`* of the curve determines the grade of differentiability of
the curve. The curve lies within the convex hull of its control
polygon (*`rows`*,*`cols`*). The weights in *`weights`*
determine how much the curve is
attracted by the individual control points (*`rows`*,*`cols`*).
A *`weights`* vector with equal weights for all
control points is generated if *"auto"* is chosen.
The *`knots`* vector describes the domain of the curve.
Typically, this parameter can be set to *"auto"*.

The accuracy of the generated *`contour`* depends on the two parameters
*`maxDistance`* and *`maxError`*. *`maxDistance`* limits the
maximum distance of two subsequent *`contour`* points. The maximum
distance between the generated *`contour`* and the actual NURBS curve
is limited to *`maxError`*. By default the approximation must fulfill
both constraints, but it is possible to set one of these parameters to
*"omit"*. The lower *`maxError`* and *`maxDistance`* are chosen
the better is the approximation of the curve. Note that all *`contour`*
points lie exactly on the curve (except for numerical inaccuracies).

**Definition**

A NURBS curve $C$ of degree $p$ is given by
$$C(u)=\frac{\sum_{i=0}^{n} N_{i,p}(u)w_{i}P_{i}}{\sum_{i=0}^{n} N_{i,p}(u)w_{i}},\quad u\in [u_{p},u_{n}].$$ ![figure](../assets/7221a3c8b32df73f.svg)
The basis functions $N_{i,p}$ are defined by
$$N_{i,0}(u)=\begin{cases}1&\text{if }u_i\le u<u_{i+1}\\0&\text{otherwise}\end{cases}\quad N_{i,p}(u)=\frac{u-u_i}{u_{i+p}-u_i}N_{i,p-1}(u)+\frac{u_{i+p+1}-u}{u_{i+p+1}-u_{i+1}}N_{i+1,p-1}(u)$$ ![figure](../assets/7a0913369165554b.svg)
Thus, each NURBS curve is determined by its *`degree`* $p$,
its control Polygon
$P_{0},...,P_{n-1}$ (*`rows`* and
*`cols`*), its weight vector
$w=(w_{0},...,w_{n-1})$
(*`weights`*), and its knot vector
$u=(u_{0},...,u_{n+p})$ (*`knots`*).

The grade of differentiability of the curve is set via the degree $p$.
At least $p+1$ control points $P_{i}$ are required to form
a valid curve.
The knot vector $u$ describes the domain of the curve.
Its length must be $n+p+1$ and its entries must be monotonically
increasing.
Every entry $u_{i}$ stands for a knot between the curve segments
$[u_{i-1},u_{i})$ and
$[u_{i},u_{i+1})$.
Each curve segment $[u_{i},u_{i+1})$ lies within the
convex hull of the control points $P_{i-p},..,P_{i}$.
For every curve segment of length zero, the differentiability at knot
$k$ decreases.
The number of occurrences of each knot in the knot vector is called
multiplicity. The maximum multiplicity of one knot is $p$.
Only the start and the end point's multiplicity can be $p+1$
(which in fact is the case for most curves, because in this case start and
end point of the curve correspond to the first respectively last point of
the control polygon).
If start and/or end point do not have full multiplicity, the domain of
the curve is restricted to $[u_{p},u_{n}]$.
The weights $w_{i}$ determine the influence of the individual
control points $P_{i}$ on the curve.

**Closed Curves:** If start and end point are equal
($P_{0}=P_{n-1}$)
and *`knots`* is set to *"auto"*, the curve is closed
automatically such that all knots feature multiplicity one.
Note that in this case the length of *`weights`* is required to be
$n-1$.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (output_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

The contour that approximates the NURBS curve.

**`rows`** (input_control)  coordinates.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the control polygon.

Number of elements:
Rows == Cols && Rows >= Degree + 1

**`cols`** (input_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the control polygon.

Number of elements:
Cols == Rows && Cols >= Degree + 1

**`knots`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double)

The knot vector $u$.

Default:
"auto"

Suggested values:
"auto"

**`weights`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double)

The weight vector $w$.

Number of elements:
Weights == Rows

Default:
"auto"

Suggested values:
"auto"

Restriction:
`Weights > 0.0`

**`degree`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

The degree $p$ of the NURBS curve.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2`

**`maxError`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / string)

Maximum distance between the NURBS
curve and its approximation.

Default:
1.0

Suggested values:
"omit", 1.0, 2.0, 3.0, 4.0, 5.0

Restriction:
`MaxError > 0.0`

**`maxDistance`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / string)

Maximum distance between two subsequent
*`contour`* points.

Default:
5.0

Suggested values:
"omit", 1.0, 2.0, 3.0, 4.0, 5.0

Restriction:
`MaxDistance > 0.0`

## Example (HDevelop)

```
* use a polygon XLD contour as control polygon and approximate
* the NURBS curve as contour

get_contour_xld(Polygon, Row, Col)
gen_contour_nurbs_xld(NURBSContour, Row, Col, 'auto', 'auto', 3, 1.0, 10.0)
```

## Possible Predecessors

`GenNurbsInterp`

## Possible Successors

`GenPolygonsXld`

## References

L. Piegl, W. Tiller: ”The NURBS Book”, 2nd Edition, Springer, 1997.

## Module

Foundation
