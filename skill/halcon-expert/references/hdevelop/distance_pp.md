# distance_pp (Operator)

## Name

`distance_pp` — Calculate the distance between two points.

## Signature

`distance_pp( : : Row1, Column1, Row2, Column2 : Distance)`

## Description

The operator `distance_pp` calculates the distance between pairs
of points
according to the following formula:
$$\text{Distance} = \sqrt{(\text{Row1} - \text{Row2})^{2} + (\text{Column1} - \text{Column2})^{2}}$$ ![figure](../assets/b6cc3cc605b60bc7.svg)
The result is returned in *`Distance`*.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of computed distances is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Row1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point.

**`Column1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point.

**`Row2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point.

**`Column2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point.

**`Distance`** (output_control)  real(-array) `→`  (real)

Distance between the points.

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
draw_point (WindowHandle, Row1, Column1)
gen_cross_contour_xld (Cross, Row1, Column1, 15, 0)
draw_point (WindowHandle, Row2, Column2)
gen_cross_contour_xld (Cross, Row2, Column2, 15, 0)
distance_pp (Row1, Column1, Row2, Column2, Distance)
```

## Result

`distance_pp` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_ps`

## See also

`distance_pl`,
`distance_pr`

## Module

Foundation
