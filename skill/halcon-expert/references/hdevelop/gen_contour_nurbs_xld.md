# gen_contour_nurbs_xld (Operator)

## Name

`gen_contour_nurbs_xld` — Transform a NURBS curve into an XLD contour.

## Signature

`gen_contour_nurbs_xld( : Contour : Rows, Cols, Knots, Weights, Degree, MaxError, MaxDistance : )`

## Description

`gen_contour_nurbs_xld` generates an XLD *`Contour`* that
approximates a
NURBS curve (non-uniform rational B-Spline curve). The NURBS curve is
specified by its *`Degree`*, a control polygon (via *`Rows`* and
*`Cols`*), a *`Weights`* vector and a *`Knots`*
vector.

The *`Degree`* of the curve determines the grade of differentiability of
the curve. The curve lies within the convex hull of its control
polygon (*`Rows`*,*`Cols`*). The weights in *`Weights`*
determine how much the curve is
attracted by the individual control points (*`Rows`*,*`Cols`*).
A *`Weights`* vector with equal weights for all
control points is generated if *'auto'* is chosen.
The *`Knots`* vector describes the domain of the curve.
Typically, this parameter can be set to *'auto'*.

The accuracy of the generated *`Contour`* depends on the two parameters
*`MaxDistance`* and *`MaxError`*. *`MaxDistance`* limits the
maximum distance of two subsequent *`Contour`* points. The maximum
distance between the generated *`Contour`* and the actual NURBS curve
is limited to *`MaxError`*. By default the approximation must fulfill
both constraints, but it is possible to set one of these parameters to
*'omit'*. The lower *`MaxError`* and *`MaxDistance`* are chosen
the better is the approximation of the curve. Note that all *`Contour`*
points lie exactly on the curve (except for numerical inaccuracies).

**Definition**

A NURBS curve $C$ of degree $p$ is given by
$$C(u)=\frac{\sum_{i=0}^{n} N_{i,p}(u)w_{i}P_{i}}{\sum_{i=0}^{n} N_{i,p}(u)w_{i}},\quad u\in [u_{p},u_{n}].$$ ![figure](../assets/7221a3c8b32df73f.svg)
The basis functions $N_{i,p}$ are defined by
$$N_{i,0}(u)=\begin{cases}1&\text{if }u_i\le u<u_{i+1}\\0&\text{otherwise}\end{cases}\quad N_{i,p}(u)=\frac{u-u_i}{u_{i+p}-u_i}N_{i,p-1}(u)+\frac{u_{i+p+1}-u}{u_{i+p+1}-u_{i+1}}N_{i+1,p-1}(u)$$ ![figure](../assets/7a0913369165554b.svg)
Thus, each NURBS curve is determined by its *`Degree`* $p$,
its control Polygon
$P_{0},...,P_{n-1}$ (*`Rows`* and
*`Cols`*), its weight vector
$w=(w_{0},...,w_{n-1})$
(*`Weights`*), and its knot vector
$u=(u_{0},...,u_{n+p})$ (*`Knots`*).

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
and *`Knots`* is set to *'auto'*, the curve is closed
automatically such that all knots feature multiplicity one.
Note that in this case the length of *`Weights`* is required to be
$n-1$.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (output_object)  xld_cont `→` object

The contour that approximates the NURBS curve.

**`Rows`** (input_control)  coordinates.y-array `→`  (real)

Row coordinates of the control polygon.

Number of elements:
Rows == Cols && Rows >= Degree + 1

**`Cols`** (input_control)  coordinates.x-array `→`  (real)

Column coordinates of the control polygon.

Number of elements:
Cols == Rows && Cols >= Degree + 1

**`Knots`** (input_control)  string(-array) `→`  (string / real)

The knot vector $u$.

Default:
'auto'

Suggested values:
'auto'

**`Weights`** (input_control)  string(-array) `→`  (string / real)

The weight vector $w$.

Number of elements:
Weights == Rows

Default:
'auto'

Suggested values:
'auto'

Restriction:
`Weights > 0.0`

**`Degree`** (input_control)  integer `→`  (integer)

The degree $p$ of the NURBS curve.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2`

**`MaxError`** (input_control)  real `→`  (real / string)

Maximum distance between the NURBS
curve and its approximation.

Default:
1.0

Suggested values:
'omit', 1.0, 2.0, 3.0, 4.0, 5.0

Restriction:
`MaxError > 0.0`

**`MaxDistance`** (input_control)  real `→`  (real / string)

Maximum distance between two subsequent
*`Contour`* points.

Default:
5.0

Suggested values:
'omit', 1.0, 2.0, 3.0, 4.0, 5.0

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

`gen_nurbs_interp`

## Possible Successors

`gen_polygons_xld`

## References

L. Piegl, W. Tiller: ”The NURBS Book”, 2nd Edition, Springer, 1997.

## Module

Foundation
