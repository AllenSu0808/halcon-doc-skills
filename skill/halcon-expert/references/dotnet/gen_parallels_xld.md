# GenParallelsXld (Operator)

## Name

`GenParallelsXld` — Extract parallel XLD polygons.

## Signature

`static void HOperatorSet.GenParallelsXld(HObject polygons, out HObject parallels, HTuple len, HTuple dist, HTuple alpha, HTuple merge)`

`HXLDPara HXLDPoly.GenParallelsXld(HTuple len, HTuple dist, HTuple alpha, string merge)`

`HXLDPara HXLDPoly.GenParallelsXld(double len, double dist, double alpha, string merge)`

## Description

`GenParallelsXld` examines the XLD polygons passed in
*`polygons`* for parallelism. The resulting parallel
polygons are returned in *`parallels`*. If the parameter
*`merge`* is set to *"true"*, adjacent parallel polygons
are returned in a single parallel relation. Otherwise, one parallel
relation is returned for each pair of parallel line segments.

Only polygon segments longer than *`len`* are taken into account.
Whether two polygon segments are parallel depends on a maximum allowed
angle difference *`alpha`* (in radians).
Furthermore, the projections of the two segments onto their angle bisector
have to overlap.
Finally, the overlap on the angle bisector is reprojected onto the two
segments. If the maximal distance of the reprojections is smaller than
*`dist`*, the segments are stored in *`parallels`*.

As a side effect, a quality factor is calculated for each pair of
parallels, compare [`ModParallelsXld`](mod_parallels_xld.md). It is based on the
normalized angular difference and the
normalized length of the overlap:
$$q = \frac{\pi/2 - \delta \alpha}{\pi/2} \; \frac{2\overlap}{l_{n1} + l_{n2}} \\ \text{with } 0 \leq q \leq 1$$ ![figure](../assets/ad2f2906e0dccb5d.svg)
Here, $\delta\alpha$ is the angle difference of the
polygon segments, $overlap$ is the length of the overlap,
$len_{1}$ and $len_{2}$ the lengths of the polygon
segments, and $q$ the resulting quality factor.
The quality factor is a measure of parallelism (the larger its
value, the “more parallel” the polygons). Finally, the quality
factors of all parallel polygon segments contained in a single
polygon are added, weighted with their length of the overlapping
area. Note that you can query the range for the quality
factor with [`InfoParallelsXld`](info_parallels_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`polygons`** (input_object)  xld_poly-array `→` [HXLDPoly](HXLDPoly.md)

Input polygons.

**`parallels`** (output_object)  xld_para-array `→` [HXLDPara](HXLDPara.md)

Parallel polygons.

**`len`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum length of the individual polygon segments.

Default:
10.0

Suggested values:
5.0, 10.0, 15.0, 20.0

Restriction:
`Len > 0.0`

**`dist`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum distance between the polygon segments.

Default:
30.0

Suggested values:
20.0, 25.0, 30.0, 40.0, 50.0, 75.0

Restriction:
`Dist > 0.0`

**`alpha`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum angle difference of the polygon segments.

Default:
0.15

Suggested values:
0.05, 0.10, 0.15, 0.20, 0.30

Restriction:
`0 <= Alpha && Alpha <= pi / 2`

**`merge`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Should adjacent parallel relations be merged?

Default:
"true"

List of values:
"false", "true"

## Possible Predecessors

`GenPolygonsXld`

## Possible Successors

`ModParallelsXld`,
`GetParallelsXld`,
`InfoParallelsXld`

## Module

Foundation
