# DistancePp (Operator)

## Name

`DistancePp` — Calculate the distance between two points.

## Signature

`static void HOperatorSet.DistancePp(HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distance)`

`static HTuple HMisc.DistancePp(HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`static double HMisc.DistancePp(double row1, double column1, double row2, double column2)`

## Description

The operator `DistancePp` calculates the distance between pairs
of points
according to the following formula:
$$\text{Distance} = \sqrt{(\text{Row1} - \text{Row2})^{2} + (\text{Column1} - \text{Column2})^{2}}$$ ![figure](../assets/b6cc3cc605b60bc7.svg)
The result is returned in *`distance`*.

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

**`row1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point.

**`column1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point.

**`row2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point.

**`column2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point.

**`distance`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

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

`DistancePp` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistancePs`

## See also

`DistancePl`,
`DistancePr`

## Module

Foundation
