# moments_gray_plane (Operator)

## Name

`moments_gray_plane` — Calculate gray value moments and approximation by a plane.

## Signature

`def moments_gray_plane(regions: HObject, image: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def moments_gray_plane_s(regions: HObject, image: HObject) -> Tuple[float, float, float, float, float]`

## Description

The operator `moments_gray_plane` calculates the gray value
moments and the parameters of the approximation of the gray values
by a plane. The calculation is carried out according to the
following formula:
$$MRow = \frac{1}{F^2} \sum_{(r,c)\in Regions} (r-\bar r)(Image(r,c)-Mean) \\ MCOL = \frac{1}{F^2} \sum_{(r,c)\in Regions} (c-\bar c)(Image(r,c)-Mean) \\ Alpha = \frac{MRowF_{m02} - m_{11}MCOL}{F} \quad - \quad m_{20}m_{02} - m_{11}^2 \\ Beta = \frac{m_{20}MCOLF - MRowFm_{11}}{m_{20}m_{02} - m_{11}^2}$$ ![figure](../assets/e4cc0d3f73143502.svg)
where $F$ is the plane, $\overline{r}$ ![figure](../assets/89e9b8268e46ca07.svg), $\overline{c}$ ![figure](../assets/4a7cfdbd248fc874.svg)
the center, and $m_{11}$, $m_{20}$, and $m_{02}$
the scaled moments of *`regions`*.

The parameters *`alpha`*, *`beta`* and
*`mean`* describe a plane above the region:
$$Image'(r,c) = Alpha(r - \bar{r}) + Beta(c - \bar{c}) + Mean$$ ![figure](../assets/a84bcb5b18508fff.svg)
Thus *`alpha`* indicates the gradient in the direction of the
line axis (“down”), *`beta`* the gradient in the direction
of the column axis (to the “right”).

## Attention

Note that the operator `moments_gray_plane` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions to be checked.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / direction / cyclic / uint2 / real)

Corresponding gray values.

**`mrow`** (output_control)  real(-array) `→` Sequence[float]

Mixed moments along a line.

**`mcol`** (output_control)  real(-array) `→` Sequence[float]

Mixed moments along a column.

**`alpha`** (output_control)  real(-array) `→` Sequence[float]

Parameter Alpha of the approximating plane.

**`beta`** (output_control)  real(-array) `→` Sequence[float]

Parameter Beta of the approximating plane.

**`mean`** (output_control)  real(-array) `→` Sequence[float]

Mean gray value.

## Result

The operator `moments_gray_plane` returns the value 2 (
H_MSG_TRUE)
if an
image with the defined gray values (byte) is entered and
the parameters are correct. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`, the behavior
in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Predecessors

`draw_region`,
`gen_circle`,
`gen_ellipse`,
`gen_rectangle1`,
`gen_rectangle2`,
`threshold`,
`regiongrowing`

## See also

`intensity`,
`moments_region_2nd`

## References

R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, pp 75-76

## Module

Foundation
