# binocular_disparity_mg (Operator)

## Name

`binocular_disparity_mg` — Compute the disparities of a rectified stereo image pair using multigrid
methods.

## Signature

`def binocular_disparity_mg(image_rect_1: HObject, image_rect_2: HObject, gray_constancy: float, gradient_constancy: float, smoothness: float, initial_guess: float, calculate_score: str, mgparam_name: MaybeSequence[str], mgparam_value: MaybeSequence[Union[str, float, int]]) -> Tuple[HObject, HObject]`

## Description

`binocular_disparity_mg` calculates the disparity between two
rectified stereo images *`image_rect_1`* and *`image_rect_2`* and
returns it in *`disparity`*. In contrast to
[`binocular_disparity`](binocular_disparity.md), a variational approach based on
multigrid methods is used. This approach returns disparity values
also for image parts that contain no texture. In contrast to
[`binocular_distance_mg`](binocular_distance_mg.md), the results are not transformed into
distance values.

The input images must be a pair of rectified stereo images, i.e.,
corresponding points must have the same vertical coordinate. The
images can have different widths, but must have the same height.
The runtime of the operator is approximately linear in the size of
the images.

The disparity is the amount by which each point in the first image
*`image_rect_1`* needs to be moved to reach its corresponding point
in the second image *`image_rect_2`*. Two points are called
corresponding if they are the image of the same point in the
original scene. The calculated disparity field is dense and
estimates the disparity also for points that do not have a
corresponding point. The disparity is calculated only for those
lines that are part of the domains of both input images. More
exactly, the domain of the disparity map is calculated as the
intersection of heights of the smallest enclosing rectangles of the
domains of the input images.

The calculated disparity field is usually not perfect. If the
parameter *`calculate_score`* is set to *"true"*, a
quality measure for the disparity is estimated for each pixel and
returned in *`score`*, which is a gray value image with a range
from 0 to 10, where 0 is the best quality and 10 the worst. For
this, the reverse disparity field from the second to the first image
is calculated and compared to the returned disparity field. Because
of this, the runtime roughly doubles when computing the score.

The operator uses a variational approach, where an energy value is
assigned to each possible disparity field. Disparity fields with a
lower energy are better than those with a high energy. The operator
calculates a disparity field with the minimum energy and returns
it.

The energy assigned to a disparity field consists of a data term and
a smoothness term. The data term models the fact that corresponding
points are images of the same part of the scene and thus have equal
gray values. The smoothness term models the fact that the imaged
scene and with it its disparity field is piecewise smooth, which
leads to an interpolation of the disparity into areas with low
information from the data term, e.g., areas with no texture.

The details of the assumptions are as follows:

*Constancy of the gray values*: It is assumed that
corresponding points have the same gray value, i.e., that
$I_{1}(x,y)=I_{2}(x+u(x,y),y)$.

*Constancy of the gray value gradients*: It is assumed that
corresponding points have the same gray value gradient, i.e., that
$\nabla I_{1}(x,y)=\nabla I_{2}(x+u(x,y),y))$. Discrepancies from this assumption are
modeled using the $L_{2}$ norm of the difference of the two
gradients. The gray value gradient has the advantage of being
invariant to additive illumination changes between the two images.

*Statistical robustness in the data term*: To reduce the
influence of outliers, i.e., points that violate the constancy
assumptions, they are penalized in a statistically robust manner via
the total variation
$\Psi(x) = \sqrt{x + e^2$ ![figure](../assets/a60e937873d2edfb.svg), where
$\epsilon=0.01$ is a fixed regularization constant.

*Smoothness of the disparity field*: It is assumed that the
resulting disparity field is piecewise smooth. This is modeled by
the $L_{2}$ norm of the derivative of the disparity field.

*Statistical robustness in the smoothness term*: Analogously
to the data term, the statistically robust total variation is
applied to the smoothness term to reduce the influence of outliers.
This is especially important for preserving edges in the disparity
field that appear on object boundaries.

The energy functional is the integral of a linear combination of the
above terms over the area of the first image. The coefficients of
the linear combination are parameters of the operator and allow a
fine tuning of the model to a specific situation.
*`gray_constancy`* determines the influence of the gray value
constancy, *`gradient_constancy`* the influence of the constancy
of the gray value gradient, and *`smoothness`* the influence of
the smoothness term. The first two parameters need to be adapted to
the gray value interval of the images. The proposed parameters are
valid for images with a gray value range of 0 to 255.

Let $I_{1}(x,y)$ be the gray value of the first image
at the coordinates (x,y), $I_{2}(x,y)$ the gray value
of the second image, and u(x,y) the value of the disparity at the
coordinate (x,y). Then, the energy functional is then given by
$$E = \int \Psi\left( GrayConstancy\cdot( I_{2}(x+u(x,y),y) - I_{1}(x,y) )^{2} + \\ \n GradientConstancy\cdot|\\nabla I_2(x+u(x,y)) - \\ abla I_1(x,y)|^{2} \\ n + Smoothness\cdot\Psi\left(|\\nabla u(x,y)|^{2}\right) dx dy$$ ![figure](../assets/5f10b29605f6f166.svg)

It is assumed that the disparity field u that minimizes the
functional E satisfies the above assumptions and is thus a good
approximation of the disparity between the two images.

The above functional is minimized by finding the roots of the
Euler-Lagrange equation (ELE) of the integral. This is comparable
to finding the extremal values of a one-dimensional function by
searching the roots of its derivative. The ELE is a nonlinear
partial differential equation over the region of the integral, which
needs to be 0 for extrema of E. Since the functional typically
does not have any maxima, the corresponding roots of the ELE
correspond to the minima of the functional.

The following techniques are used to find the roots of the ELE:

*Fixed point iteration*: The ELE is solved by converting it
to a fixed point iteration that iteratively approaches the solution.
The number of iterations can be used to balance between speed and
accuracy of the solution. Each step of the fixed point iteration
consists of solving a linear partial differential equation.

*Coarse-to-fine process*: A Gaussian image pyramid of the
stereo images is created. The ELE is first solved on a coarse level
of the pyramid and the solution is taken as the initial value of the
fixed point iteration of the next level. This has a number of
advantages and disadvantages:

1. Since the fixed point iteration of the next level receives a
good initial value, fewer iterations are necessary to archive a good
accuracy. The iteration must perform only small corrections of the
disparity.

2. Large disparities on the original images become small disparities
on the coarse grid levels and can thus be calculated more easily.

3. The robustness against noise in the images is increased because
most kinds of noise disappear on the coarse version of the images.

4. Problems arise with small structures that have a large disparity
difference to their surroundings since they disappear on coarse
versions of the image and thus the disparity of the surroundings is
calculated. This error will not be corrected on the finer levels of
the image pyramid since only small corrections are calculated there.

*Multigrid methods*: The linear partial differential
equations that arise in the fixed point iteration at each pyramid
level are converted into a linear system of equations through
linearization. These linear systems are solved using iterative
solvers. Multigrid methods are among the most efficient solvers for
the kind of linear systems that arise here. They use the fact that
classic iterative solvers, like the Gauss-Seidel solver, quickly
reduce the high frequency parts of the error, but only slowly reduce
the low frequency parts. Multigrid methods thus calculate the error
on a coarser grid where the low frequency part of the error appears
as high frequencies and can be reduced quickly by the classical
solvers. This is done hierarchically, i.e., the computation of the
error on a coarser resolution level itself uses the same strategy
and efficiently computes its error (i.e., the error of the error) by
correction steps on an even coarser resolution level. Depending on
whether one or two error correction steps are performed per cycle, a
so called V or W cycle is obtained. The corresponding strategies
for stepping through the resolution hierarchy are as follows for two
to four resolution levels: ![figure](../assets/6ea2b8106f9a3a40.svg)
Here, iterations on the original problem are denoted by large
markers, while small markers denote iterations on error correction
problems.

Algorithmically, a correction cycle can be described as follows:

1. In the first step, several (few) iterations using an interactive
linear or nonlinear basic solver are performed (e.g., a variant of
the Gauss-Seidel solver). This step is called pre-relaxation step.

2. In the second step, the current error is computed to correct the
current solution (the solution after step 1). For efficiency
reasons, the error is calculated on a coarser resolution level.
This step, which can be performed iteratively several times, is
called coarse grid correction step.

3. In a final step, again several (few) iterations using the
interactive linear or nonlinear basic solver of step 1 are performed.
This step is called post-relaxation step.

In addition, the solution can be initialized in a hierarchical
manner. Starting from a very coarse variant of the original linear
equation system, the solution is successively refined. To do so,
interpolated solutions of coarser variants of the equation system
are used as the initialization of the next finer variant. On each
resolution level itself, the V or W cycles described above are used
to efficiently solve the linear equation system on that resolution
level. The corresponding multigrid methods are called full
multigrid methods in the literature. The full multigrid algorithm
can be visualized as follows:
$$\mathrm{Full\;multigrid\;algorithm}$$ ![figure](../assets/9be1d8061777e2bf.svg)
This example represents a full multigrid algorithm that uses two W
correction cycles per resolution level of the hierarchical
initialization. The interpolation steps of the solution from one
resolution level to the next are denoted by i and the two W
correction cycles by $\mathrm{w}_{1}$ and
$\mathrm{w}_{2}$. Iterations on the original problem are
denoted by large markers, while small markers denote iterations on
error correction problems.

Depending on the selected multigrid solver, a number of parameters
for fine tuning the solver are available and are described in the
following.

The parameter *`initial_guess`* gives a initial value for the
initialization of the fixed point iteration on the coarsest grid.
Usually 0 is sufficient, but to avoid local minima other values can
be used.

Using the parameters *`mgparam_name`* and *`mgparam_value`*,
the solver is controlled, i.e., the coarse-to-fine process, the
fixed point iteration, and the multigrid solver. It is usually
sufficient to use one of the predefined parameter sets, which are
available by setting *`mgparam_name`* =
*"default_parameters"* and *`mgparam_value`* =
*"very_accurate"*, *"accurate"*,
*"fast_accurate"*, or *"fast"*.

If the parameters should be specified individually,
*`mgparam_name`* and *`mgparam_value`* must be set to tuples
of the same length. The values corresponding to the parameters
specified in *`mgparam_name`* must be specified at the
corresponding position in *`mgparam_value`*. The parameters are
evaluated in the given order. Therefore, it is possible to first
select a group of default parameters (see above) and then change
only some of the parameters. in the following, the possible
parameters are described.

*`mgparam_name`* = *"mg_solver"* sets the solver for
the linear system. Possible values for *`mgparam_value`* are
*"multigrid"* for a simple multigrid solver,
*"full_multigrid"* for a full multigrid solver, and
*"gauss_seidel"* for the plain Gauss-Seidel solver. The
multigrid methods have the advantage of a faster convergence, but
incur the overhead of coarsening the linear system.

*`mgparam_name`* = *"mg_cycle_type"* selects the type
of recursion for the multigrid solvers. Possible values for
*`mgparam_value`* are *"v"* for a V-Cycle, *"w"*
for a W-Cycle, and *"none"* for no recursion.

*`mgparam_name`* = *"mg_pre_relax"* sets the number of
iterations of the pre-relaxation step in multigrid solvers, or the
number of iterations for the Gauss-Seidel solver, depending on which
is selected.

*`mgparam_name`* = *"mg_post_relax"* sets the number of
iterations of the post-relaxation step.

Increasing the number of pre- and post-relaxation steps increases
the computation time asymptotically linearly. However, no
additional restriction and prolongation operations (zooming down and
up of the error correction images) are performed. Consequently, a
moderate increase in the number of relaxation steps only leads to a
slight increase in the computation times.

*`mgparam_name`* = *"initial_level"* sets the coarsest
level of the image pyramid where the coarse-to-fine process starts.
The value can be positive, in which case it directly gives the
initial level. Level 0 is the finest level with the original
images. If the value is negative, then it is used relative to the
maximum number of pyramid levels. The coarsest available pyramid
level is the one where both images have a size of at least 4 pixels
in both directions. As described below, the default value of
*"initial_level"* is *-2*. This facilitates the
calculation of the correct disparity for images that have very large
disparities. In some cases, e.g., for repeating textures, this may
lead to the fact that too large disparities are calculated for some
parts of the image. In this case, *"initial_level"* should
be set to a smaller value.

The standard parameters zoom the image with a factor of 0.6 per
pyramid level. If a guess of the maximum disparity d exists, then
the initial level s should be selected so that
$0.6^{-s}$ is greater than d.

*`mgparam_name`* = *"iterations"* sets the number of
iterations of the fixed point iteration per pyramid level. The exact
number of iterations is $steps=\min (10,\text{iterations}+\text{le v el}^{2})$, where
level is the current level in the image pyramid. If this value is
set to 0, then no iteration is performed on the finest pyramid level
0. Instead, the result of level 1 is scaled to the original image
size and returned, which can be used if speed is crucial. The
runtime of the operator is approximately linear in the number of
iterations.

*`mgparam_name`* = *"pyramid_factor"* determines the
factor by which the images are scaled when creating the image
pyramid for the coarse-to-fine process. The width and height of the
next smaller image is scaled by the given factor. The value must
lie between 0.1 and 0.9.

The predefined parameter sets for *`mgparam_name`* =
*"default_parameters"* contain the following values:

*"default_parameters"* = *"very_accurate"*:
*"mg_solver"* = *"full_multigrid"*,
*"mg_cycle_type"* = *"w"*,
*"mg_pre_relax"* = 5,
*"mg_post_relax"* = 5,
*"initial_level"* = -2,
*"iterations"* = 5,
*"pyramid_factor"* = 0.6.

*"default_parameters"* = *"accurate"*:
*"mg_solver"* = *"full_multigrid"*,
*"mg_cycle_type"* = *"w"*,
*"mg_pre_relax"* = 5,
*"mg_post_relax"* = 5,
*"initial_level"* = -2,
*"iterations"* = 2,
*"pyramid_factor"* = 0.6.

*"default_parameters"* = *"fast_accurate"*:
*"mg_solver"* = *"full_multigrid"*,
*"mg_cycle_type"* = *"v"*,
*"mg_pre_relax"* = 2,
*"mg_post_relax"* = 2,
*"initial_level"* = -2,
*"iterations"* = 1,
*"pyramid_factor"* = 0.6.
These are the default parameters of the algorithm if the default
parameter set is not specified.

*"default_parameters"* = *"fast"*:
*"mg_solver"* = *"full_multigrid"*,
*"mg_cycle_type"* = *"v"*,
*"mg_pre_relax"* = 1,
*"mg_post_relax"* = 1,
*"initial_level"* = -2,
*"iterations"* = 0,
*"pyramid_factor"* = 0.6.

*Weaknesses of the operator*: Large jumps in the disparity,
which correspond to large jumps in the distance of the observed
objects, are smoothed rather strongly. This leads to problems with
thin objects that have a large distance to their background.

Distortions can occur at the left and right border of the image in
the parts that are visible in only one of the images.

Additionally, general problems of stereo vision should be avoided,
including horizontally repetitive patterns, areas with little
texture as well as reflections.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image_rect_1`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Rectified image of camera 1.

**`image_rect_2`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Rectified image of camera 2.

**`disparity`** (output_object)  singlechannelimage(-array) `→` HObject (real)

Disparity map.

**`score`** (output_object)  singlechannelimage(-array) `→` HObject (real)

Score of the calculated disparity if
*`calculate_score`* is set to *"true"*.

**`gray_constancy`** (input_control)  real `→` float

Weight of the gray value constancy in the data
term.

Default:
1.0

Suggested values:
0.0, 1.0, 2.0, 10.0

Restriction:
`GrayConstancy >= 0.0`

**`gradient_constancy`** (input_control)  real `→` float

Weight of the gradient constancy in the data
term.

Default:
30.0

Suggested values:
0.0, 1.0, 5.0, 10.0, 30.0, 50.0, 70.0

Restriction:
`GradientConstancy >= 0.0`

**`smoothness`** (input_control)  real `→` float

Weight of the smoothness term in relation to
the data term.

Default:
5.0

Suggested values:
1.0, 3.0, 5.0, 10.0

Restriction:
`Smoothness > 0.0`

**`initial_guess`** (input_control)  real `→` float

Initial guess of the disparity.

Default:
0.0

Suggested values:
-30.0, -20.0, -10.0, 0.0, 10.0, 20.0, 30.0

**`calculate_score`** (input_control)  string `→` str

Should the quality
measure should be returned in *`score`*?

Default:
"false"

Suggested values:
"true", "false"

**`mgparam_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Parameter name(s) for the multigrid algorithm.

Default:
"default_parameters"

List of values:
"default_parameters", "initial_level", "iterations", "mg_cycle_type", "mg_post_relax", "mg_pre_relax", "mg_solver", "pyramid_factor"

**`mgparam_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[str, float, int]]

Parameter value(s) for the multigrid algorithm.

Default:
"fast_accurate"

Suggested values:
"very_accurate", "accurate", "fast_accurate", "fast", "v", "w", "none", "gauss_seidel", "multigrid", "full_multigrid", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, -1, -2, -3, -4, -5

## Example (HDevelop)

```
read_image (BaseballL, 'stereo/epipolar/baseball_l')
read_image (BaseballR, 'stereo/epipolar/baseball_r')
binocular_disparity_mg (BaseballL, BaseballR, Disparity, Score, \
                        0.25, 30, 5, 0, 'true', \
                        'default_parameters','fast_accurate')
```

## Result

If the parameter values are correct, `binocular_disparity_mg`
returns the value 2 (
H_MSG_TRUE)
. If the input is empty (no input images are
available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`map_image`

## Possible Successors

`threshold`,
`disparity_to_distance`,
`disparity_image_to_xyz`

## Alternatives

`binocular_disparity`,
`binocular_disparity_ms`,
`binocular_distance`,
`binocular_distance_mg`,
`binocular_distance_ms`

## See also

`map_image`,
`gen_binocular_rectification_map`,
`binocular_calibration`

## Module

3D Metrology
