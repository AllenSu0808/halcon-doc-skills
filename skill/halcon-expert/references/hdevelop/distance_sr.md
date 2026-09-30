# distance_sr (Operator)

## Name

`distance_sr` — Calculate the distance between a line segment and one region.

## Signature

`distance_sr(Region : : Row1, Column1, Row2, Column2 : DistanceMin, DistanceMax)`

## Description

The operator `distance_sr` calculates the distance between
a line segment and a region.
*`Row1`*, *`Column1`*, *`Row2`*, *`Column2`*
are the start and end coordinates of a line segment.
The parameters *`DistanceMin`* and *`DistanceMax`*
contain the resulting distances.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of distances is always *N*.

## Attention

To enhance `distance_sr`,
holes are ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Input region.

**`Row1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point of the line segment.

**`Column1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point of the line segment.

**`Row2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the line segment.

**`Column2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the line segment.

**`DistanceMin`** (output_control)  real(-array) `→`  (real)

Minimum distance between the line segment and
the region.

**`DistanceMax`** (output_control)  real(-array) `→`  (real)

Maximum distance between the line segment and
the region.

## Example (HDevelop)

```
gen_circle (Circle, 200, 200, 100.5)
Column1 := 300
Column2 := 400
for Row := 50 to 350 by 50
  gen_contour_polygon_xld (Line, [Row,Row], [Column1,Column2])
  distance_sr (Circle, Row, Column1, Row, Column2, DistanceMin, DistanceMax)
endfor
```

## Result

`distance_sr` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_sc`,
`distance_lr`,
`distance_pr`,
`diameter_region`

## See also

`hamming_distance`,
`select_region_point`,
`test_region_point`,
`smallest_rectangle2`

## Module

Foundation
