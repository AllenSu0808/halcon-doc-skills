# scene_flow_uncalib (Operator)

## Name

`scene_flow_uncalib` — Compute the uncalibrated scene flow between two stereo image pairs.

## Signature

`def scene_flow_uncalib(image_rect_1t1: HObject, image_rect_2t1: HObject, image_rect_1t2: HObject, image_rect_2t2: HObject, disparity: HObject, smoothing_flow: Union[float, int], smoothing_disparity: Union[float, int], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> Tuple[HObject, HObject]`

## Description

`scene_flow_uncalib` computes the uncalibrated scene flow
between two consecutive rectified stereo image pairs. The scene
flow is the three-dimensional position and motion of surface points
in a dynamic scene. The movement in the images can be caused by
objects that move in the world or by a movement of the camera (or
both) between the acquisition of the two image pairs. To calculate
the calibrated scene flow, [`scene_flow_calib`](scene_flow_calib.md) can be used.

The two consecutive stereo image pairs of the image sequence are
passed in *`image_rect_1t1`*, *`image_rect_2t1`*,
*`image_rect_1t2`*, and *`image_rect_2t2`*. Each stereo image
pair must be rectified. Note that the images can be rectified by
using the operators [`calibrate_cameras`](calibrate_cameras.md),
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md), and [`map_image`](map_image.md).
Furthermore, a single-channel *`disparity`* image is required,
which specifies for each pixel (r,c1) of the image
*`image_rect_1t1`* a matching pixel (r,c2) of
*`image_rect_2t1`* according to the equation c2=c1+d(r,c1),
where d(r,c) is the *`disparity`* at pixel (r,c). The
disparity image can be computed using [`binocular_disparity`](binocular_disparity.md) or
[`binocular_disparity_mg`](binocular_disparity_mg.md).

The computed uncalibrated scene flow is returned in
*`optical_flow`* and *`disparity_change`*. The vectors in
the vector field *`optical_flow`* represent the movement in the
image plane between *`image_rect_1t1`* and *`image_rect_1t2`*.
The single-channel image *`disparity_change`* describes the
change in disparity between *`image_rect_2t1`* and
*`image_rect_2t2`*. A world point is projected into
*`image_rect_1t1`* at position (r,c). The same point is
projected into

- *`image_rect_2t1`* at position (r,c+d(r,c)),
- *`image_rect_1t2`* at position (r+u(r,c),c+v(r,c)),
- *`image_rect_2t2`* at position
  (r+u(r,c),c+v(r,c)+d(r,c)+dc(r,c)),

where u(r,c) and v(r,c) denote the values of the row and column
components of the vector field image *`optical_flow`*, d(r,c)
denotes the *`disparity`*, and dc(r,c) the
*`disparity_change`* at the pixel (r,c).

![figure](../assets/41073ad8f842cf14.svg)

Relations between the four images and the optical flow as well as
the disparities in the disparity images.

### Parameter Description

The rectified input images are passed in *`image_rect_1t1`*,
*`image_rect_2t1`*, *`image_rect_1t2`*, and
*`image_rect_2t2`*. The computation of the scene flow is
performed on the domain of *`image_rect_1t1`*, which is
also the domain of the scene flow in *`optical_flow`* and
*`disparity_change`*. *`disparity`* describes the
disparity between the rectified images *`image_rect_1t1`* and
*`image_rect_2t1`*.

*`smoothing_flow`* and *`smoothing_disparity`* specify the
regularization weights $\lambda$ and $\gamma$
with respect to the data term. The larger the value of these
parameters, the smoother the computed scene flow is. For byte
images with a gray value range of $[0,255]$, values
around 40 typically yield good results.

The parameters of the iteration scheme and for the coarse-to-fine
warping strategy can be specified with the generic parameters
*`gen_param_name`* and *`gen_param_value`*.

Usually, it is sufficient to use one of the default parameter sets
for the parameters by using *`gen_param_name`* =
*"default_parameters"* and *`gen_param_value`* =
*"very_accurate"*, *"accurate"*, *"fast"*, or
*"very_fast"*. If necessary, individual parameters can be
modified after the default parameter set has been chosen by
specifying a subset of the parameters and corresponding values after
*"default_parameters"* in *`gen_param_name`* and
*`gen_param_value`* (e.g., *`gen_param_name`* =
*["default_parameters","warp_zoom_factor"]* and
*`gen_param_value`* = *["accurate",0.6]*). The meaning of
the individual parameters is described in detail below. The default
parameter sets are given by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *"default_parameters"* | *"very_accurate"* | *"accurate"* | *"fast"* | *"very_fast"* |
| *"warp_zoom_factor"* | 0.75 | 0.5 | 0.5 | 0.5 |
| *"warp_levels"* | 0 | 0 | 0 | 0 |
| *"warp_last_level"* | 1 | 1 | 1 | 2 |
| *"outer_iter"* | 10 | 7 | 5 | 4 |
| *"inner_iter"* | 2 | 2 | 2 | 2 |
| *"sor_iter"* | 3 | 3 | 3 | 3 |
| *"omega"* | 1.9 | 1.9 | 1.9 | 1.9 |

If the parameters should be specified individually,
*`gen_param_name`* and *`gen_param_value`* must be set to
tuples of the same length. The values corresponding to the
parameters specified in *`gen_param_name`* must be specified at
the corresponding position in *`gen_param_value`*. For a deeper
understanding of the following parameters, please refer to the
section *Algorithm* below.

- *`gen_param_name`* = *"warp_zoom_factor"* can be
  used to specify the resolution ratio between two consecutive
  warping levels in the coarse-to-fine warping hierarchy.
  *"warp_zoom_factor"* must be selected from the open interval
  (0,1). For performance reasons, *"warp_zoom_factor"* is
  typically set to 0.5, i.e., the number of pixels is halved in each
  direction for each coarser warping level. Values for
  *"warp_zoom_factor"* close to 1 can lead to slightly better
  results. However, they require a disproportionately larger
  computation time.
- *`gen_param_name`* = *"warp_levels"* can be used
  to restrict the warping hierarchy to a maximum number of levels.
  For *"warp_levels"* = 0, the largest possible number of
  levels is used. If the image size does not allow to use the
  specified number of levels (taking the resolution ratio
  *"warp_zoom_factor"* into account), the largest possible
  number of levels is used. Usually, *"warp_levels"* should
  be set to 0.
- *`gen_param_name`* = *"warp_last_level"* can be used
  to specify the number of warping levels for which the flow
  increment should no longer be computed. Usually,
  *"warp_last_level"* is set to 1 or 2, i.e., a flow increment
  is computed for each warping level, or the finest warping level is
  skipped in the computation. In the latter case, the computation
  is performed on an image of half the resolution of the original
  image and then interpolated to the full resolution.
- *`gen_param_name`* = *"outer_iter"* can be used to
  specify the number of outer iterations in the minimization scheme.
  Typically, the larger *"outer_iter"*, the more accurate the
  numerical results are. Higher values for this parameter lead to
  an increase in the computation time. Typically,
  *"outer_iter"* is set to values between 5 and 10.
- *`gen_param_name`* = *"inner_iter"* can be used to
  specify the number of inner iterations in the minimization scheme.
  Typically, the larger *"inner_iter"*, the more accurate the
  numerical results are. Higher values for this parameter lead to
  an increase in the computation time. Usually, two inner
  iterations are sufficient.
- *`gen_param_name`* = *"sor_iter"* can be used to
  specify the number of SOR iterations for solving the linear system
  of equations. Typically, the larger *"sor_iter"*, the more
  accurate the numerical results are. Higher values for this
  parameter lead to an increase in the computation time. Usually,
  three SOR iterations are sufficient.
- *`gen_param_name`* = *"omega"* can be used to
  specify the relaxation factor $\omega$ of the SOR
  method. *"omega"* must be selected from the open interval
  (1,2). Typically, *"omega"* is set to 1.9.

### Algorithm

The scene flow is estimated by minimizing a suitable energy
functional:
$$E(f) = \int E_D(f) + E_S(f) \, drdc$$ ![figure](../assets/459597bd8dff0831.svg)
where f=(u,v,dc) is the optical flow field and the disparity
change. $E_{D}(f)$ denotes the data term and
$E_{S}(f)$ the smoothness (regularization) term. The
algorithm is based on the following assumptions, which lead to the
data and smoothness terms:

- **Brightness Constancy** —

  It is assumed that the gray value of a
  point remains constant in all four input images, resulting in the
  following four constraints:
  $$C_{D1} = I_{1,t1}(r,c) - I_{2,t1}(r,c + d(r,c)) = 0\nC_{F1} = I_{1,t2}(r + u(r,c), c + v(r,c)) - I_{1,t1}(r,c) = 0\nC_{F2} = I_{2,t2}(r + u(r,c), c + v(r,c) + d(r,c) + dc(r,c)) - I_{2,t1}(r,c + d(r,c)) = 0\nC_{D2} = I_{2,t2}(r + u(r,c), c + v(r,c) + d(r,c) + dc(r,c)) - I_{1,t2}(r + u(r,c), c + v(r,c)) = 0$$ ![figure](../assets/bd7c2a9d41ee5ba9.svg)
  Here, $I_{1,t1}$, $I_{2,t1}$,
  $I_{1,t2}$, and $I_{2,t2}$ denote
  *`image_rect_1t1`*, *`image_rect_2t1`*, *`image_rect_1t2`*,
  and *`image_rect_2t2`*, respectively.
- **Piecewise smoothness of the scene flow** —

  The solution is
  assumed to be piecewise smooth. This smoothness is achieved by
  penalizing the first derivatives of the flow $\nabla(u)^{2},\nabla(v)^{2},\nabla(dc)^{2}$. The use of a statistically robust (linear) penalty
  function $\\Psi(s) = \\sqrt{s^2 + \varepsilon}$ ![figure](../assets/c8ddc4b73ebef32e.svg) with $\varepsilon=0.001$ provides the desired preservation of edges in the movement
  in the scene flow to be determined.

Because the disparity image d is given, the first constraint
$C_{D1}$ can be omitted. Taking into account all of the
above assumptions, the energy functional can be written as
$$E(f) = \int \Psi(C_F^2) + \Psi(C_{F2}^2) + \Psi(C_D^2) + \Psi(\lambda(\nabla(u)^2 + \nabla(v)^2) + \gamma\nabla(dc)^2)\,drdC$$ ![figure](../assets/ffd7288637a87d0b.svg)
where $\lambda$ and $\gamma$ are the
regularization parameters passed in *`smoothing_flow`* and
*`smoothing_disparity`*.

To calculate large displacements, coarse-to-fine warping strategies
use two concepts that are closely interlocked: The successive
refinement of the problem (coarse-to-fine) and the successive
compensation of the current image pair by already computed
displacements (warping). Algorithmically, such coarse-to-fine
warping strategies can be described as follows:

1. First, all images are zoomed down to a very coarse resolution
   level.
2. Then, the scene flow is computed on this coarse resolution.
3. The scene flow is required on the next resolution level: It is
   applied there to the second image pair of the image sequence,
   i.e., the problem on the finer resolution level is compensated by
   the already computed scene flow. This step is also known as
   warping.
4. The modified problem (difference problem) is now solved on the
   finer resolution level, i.e., the scene scene flow is computed
   there.
5. The steps 3-4 are repeated until the finest resolution level
   is reached.
6. The final result is computed by adding up the scene flow from
   all resolution levels.

This incremental computation of the scene flow has the following
advantage: While the coarse-to-fine strategy ensures that the
displacements on the finest resolution level are very small, the
warping strategy ensures that the displacements remain small for the
incremental displacements (scene flow of the difference problems).
Since small displacements can be computed much more accurately than
larger displacements, the accuracy of the results typically
increases significantly by using such a coarse-to-fine warping
strategy. However, instead of having to solve a single
correspondence problem, an entire hierarchy of these problems must
be solved.

The minimization of functionals is mathematically very closely
related to the minimization of functions: Like the fact that the
zero crossing of the first derivative is a necessary condition for
the minimum of a function, the fulfillment of the so called
Euler-Lagrange equations is a necessary condition for the minimizing
function of a functional (the minimizing function corresponds to the
desired scene flow in this case). The Euler-Lagrange equations are
partial differential equations. By discretizing these
Euler-Lagrange equations using finite differences, large sparse
nonlinear equation systems have to be solved in this algorithm.

For each warping level a single equation system must be solved. The
algorithm uses an iteration scheme consisting of two nested
iterations (called the outer and inner iteration) and the SOR
(Successive Over-Relaxation) method. The outer loop contains the
linearization of the nonlinear terms resulting from the data
constraints. The nonlinearity of $\Psi^{\prime}$ is removed by
the inner fixed point iteration scheme. The resulting linear system
of equations can be solved efficiently by the SOR method.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image_rect_1t1`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image 1 at time $t_{1}$.

**`image_rect_2t1`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image 2 at time $t_{1}$.

**`image_rect_1t2`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image 1 at time $t_{2}$.

**`image_rect_2t2`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image 2 at time $t_{2}$.

**`disparity`** (input_object)  singlechannelimage(-array) `→` HObject (real)

Disparity between input images 1 and 2 at time
$t_{1}$.

**`optical_flow`** (output_object)  singlechannelimage(-array) `→` HObject (vector_field)

Estimated optical flow.

**`disparity_change`** (output_object)  singlechannelimage(-array) `→` HObject (real)

Estimated change in disparity.

**`smoothing_flow`** (input_control)  number `→` Union[float, int]

Weight of the regularization term relative to
the data term (derivatives of the optical
flow).

Default:
40.0

Suggested values:
10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0

Restriction:
`SmoothingFlow > 0.0`

**`smoothing_disparity`** (input_control)  number `→` Union[float, int]

Weight of the regularization term relative to
the data term (derivatives of the disparity
change).

Default:
40.0

Suggested values:
10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0

Restriction:
`SmoothingDisparity > 0.0`

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Parameter name(s) for the algorithm.

Default:
"default_parameters"

Suggested values:
"default_parameters", "warp_levels", "warp_zoom_factor", "warp_last_level", "outer_iter", "inner_iter", "sor_iter", "omega"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Parameter value(s) for the algorithm.

Default:
"accurate"

Suggested values:
"very_accurate", "accurate", "fast", "very_fast", 0, 1, 2, 3, 4, 5, 6, 0.5, 0.6, 0.7, 0.75, 3, 5, 7, 2, 3, 1.9

## Result

If the parameter values are correct, the operator
`scene_flow_uncalib` returns the value 2 (
H_MSG_TRUE)
. If the input is
empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`binocular_disparity`,
`binocular_disparity_mg`

## Possible Successors

`threshold`,
`vector_field_length`

## Alternatives

`scene_flow_calib`,
`optical_flow_mg`

## References

A. Wedel, C. Rabe, T. Vaudrey, T. Brox, U. Franke and D. Cremers:
“Efficient dense scene flow from sparse or dense stereo data”;
In: Proceedings of the 10th European Conference on Computer Vision:
Part I, pages 739-751. Springer-Verlag, 2008.

## Module

Foundation
