# AddNoiseWhiteContourXld (Operator)

## Name

`AddNoiseWhiteContourXld` — Add noise to XLD contours.

## Signature

`static void HOperatorSet.AddNoiseWhiteContourXld(HObject contours, out HObject noisyContours, HTuple numRegrPoints, HTuple amp)`

`HXLDCont HXLDCont.AddNoiseWhiteContourXld(int numRegrPoints, double amp)`

## Description

`AddNoiseWhiteContourXld` adds noise to the input XLD contours
*`contours`* and returns the noisy contours in
*`noisyContours`*. For each point along the original contours
the local regression line (i.e., a least-squares approximating line)
based on *`numRegrPoints`* neighboring points is determined.
Then the point is shifted perpendicular to this line. The length
of the shifts corresponds to white noise, equally distributed in the
interval [-*`amp`*,*`amp`*].

The random noise is generated using the C function “drand48()”.
See the parameter *"seed_rand"* of [`SetSystem`](set_system.md) for
information on the used random seed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Original contours.

**`noisyContours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Noisy contours.

**`numRegrPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of points used to calculate the regression
line.

Default:
5

Suggested values:
3, 5, 7, 9

Restriction:
`NumRegrPoints >= 3 && odd(NumRegrPoints)`

**`amp`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum amplitude of the added noise (equally
distributed in [-Amp,Amp]).

Default:
1.0

Suggested values:
0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 10.0

Restriction:
`Amp > 0`

## Example (HDevelop)

```
draw_ellipse(WindowHandle,Row,Column,Phi,Radius1,Radius2)
gen_ellipse_contour_xld(Ellipse,Row,Column,Phi,Radius1,Radius2,0,6.28319, \
                        'positive', 1.5)
add_noise_white_contour_xld(Ellipse,NoisyEllipse,5,0.5)
fit_ellipse_contour_xld (NoisyEllipse, 'fitzgibbon', -1, 2, 0, 200, 3, 2.0, \
                         ERow, EColumn, EPhi, ERadius1, ERadius2, \
                         EStartPhi, EEndPhi, EPointOrder)
```

## Result

`AddNoiseWhiteContourXld` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`,
`GenEllipseContourXld`

## Possible Successors

`SmoothContoursXld`

## See also

`SmoothContoursXld`,
`AddNoiseWhite`

## Module

Foundation
