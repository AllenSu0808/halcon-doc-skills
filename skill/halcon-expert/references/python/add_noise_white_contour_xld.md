# add_noise_white_contour_xld (Operator)

## Name

`add_noise_white_contour_xld` — Add noise to XLD contours.

## Signature

`def add_noise_white_contour_xld(contours: HObject, num_regr_points: int, amp: float) -> HObject`

## Description

`add_noise_white_contour_xld` adds noise to the input XLD contours
*`contours`* and returns the noisy contours in
*`noisy_contours`*. For each point along the original contours
the local regression line (i.e., a least-squares approximating line)
based on *`num_regr_points`* neighboring points is determined.
Then the point is shifted perpendicular to this line. The length
of the shifts corresponds to white noise, equally distributed in the
interval [-*`amp`*,*`amp`*].

The random noise is generated using the C function “drand48()”.
See the parameter *"seed_rand"* of [`set_system`](set_system.md) for
information on the used random seed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` HObject

Original contours.

**`noisy_contours`** (output_object)  xld_cont(-array) `→` HObject

Noisy contours.

**`num_regr_points`** (input_control)  integer `→` int

Number of points used to calculate the regression
line.

Default:
5

Suggested values:
3, 5, 7, 9

Restriction:
`NumRegrPoints >= 3 && odd(NumRegrPoints)`

**`amp`** (input_control)  real `→` float

Maximum amplitude of the added noise (equally
distributed in [-Amp,Amp]).

Default:
1.0

Suggested values:
0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 10.0

Restriction:
`Amp > 0`

## Result

`add_noise_white_contour_xld` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`,
`gen_ellipse_contour_xld`

## Possible Successors

`smooth_contours_xld`

## See also

`smooth_contours_xld`,
`add_noise_white`

## Module

Foundation
