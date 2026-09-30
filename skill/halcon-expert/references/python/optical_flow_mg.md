# optical_flow_mg (Operator)

## Name

`optical_flow_mg` — Compute the optical flow between two images.

## Signature

`def optical_flow_mg(image_t1: HObject, image_t2: HObject, algorithm: str, smoothing_sigma: float, integration_sigma: float, flow_smoothness: float, gradient_constancy: float, mgparam_name: MaybeSequence[str], mgparam_value: MaybeSequence[Union[str, float, int]]) -> HObject`

## Description

`optical_flow_mg` computes the optical flow between two
images. The optical flow represents information about the movement
between two consecutive images of a monocular image sequence. The
movement in the images can be caused by objects that move in the
world or by a movement of the camera (or both) between the
acquisition of the two images. The projection of these 3D movements
into the 2D image plane is called the optical flow.

The two consecutive images of the image sequence are passed in
*`image_t1`* and *`image_t2`*. The computed optical flow is
returned in *`vector_field`*. The vectors in the vector field
*`vector_field`* represent the movement in the image plane
between *`image_t1`* and *`image_t2`*. The point in
*`image_t2`* that corresponds to the point (r,c) in
*`image_t1`* is given by (r',c') = (r+u(r,c),c+v(r,c)), where
u(r,c) and v(r,c) denote the value of the row and column
components of the vector field image *`vector_field`* at the
point (r,c).

The parameter *`algorithm`* allows the selection of three
different algorithms for computing the optical flow. All three
algorithms are implemented by using multigrid solvers to ensure an
efficient solution of the underlying partial differential equations.

For *`algorithm`* = *"fdrig"*, the method proposed by
Brox, Bruhn, Papenberg, and Weickert is used. This approach is
**f**low-**d**riven, **r**obust, **i**sotropic,
and uses a **g**radient constancy term.

For *`algorithm`* = *"ddraw"*, a robust variant of the
method proposed by Nagel and Enkelmann is used. This approach is
**d**ata-**d**riven, **r**obust,
**a**nisotropic, and uses **w**arping (in contrast to the
original approach).

For *`algorithm`* = *"clg"* the **c**ombined
**l**ocal-**g**lobal method proposed by Bruhn, Weickert,
Feddern, Kohlberger, and Schnörr is used.

In all three algorithms, the input images can first be smoothed by a
Gaussian filter with a standard deviation of *`smoothing_sigma`*
(see [`derivate_gauss`](derivate_gauss.md)).

All three approaches are variational approaches that compute the
optical flow as the minimizer of a suitable energy functional. In
general, the energy functionals have the following form:
$$E(\mathbf{w})=E_{\mathrm{D}}(\mathbf{w})+\alpha E_{\mathrm{S}}(\mathbf{w}),$$
where w=(u,v,1) is the optical flow vector
field to be determined (with a time step of 1 in the third
coordinate). The image sequence is regarded as a continuous
function f(x), where
x=(r,c,t) and (r,c) denotes the position
and t the time. Furthermore,
$E_{\mathrm{D}}(\mathbf{w})$ denotes the data term,
while $E_{\mathrm{S}}(\mathbf{w})$ denotes the
smoothness term, and $\alpha$ is a regularization
parameter that determines the smoothness of the solution. The
regularization parameter $\alpha$ is passed in
*`flow_smoothness`*. While the data term encodes assumptions
about the constancy of the object features in consecutive images,
e.g., the constancy of the gray values or the constancy of the first
spatial derivative of the gray values, the smoothness term encodes
assumptions about the (piecewise) smoothness of the solution, i.e.,
the smoothness of the vector field to be determined.

The **FDRIG algorithm** is based on the minimization of an
energy functional that contains the following assumptions:

*Constancy of the gray values*: It is assumed that
corresponding pixels in consecutive images of an image sequence have
the same gray value, i.e., that f(r+u,c+v,t+1) = f(r,c,t). This
can be written more compactly as f(x+w) = f(x) using vector notation.

*Constancy of the spatial gray value derivatives*: It is
assumed that corresponding pixels in consecutive images of an image
sequence additionally have have the same spatial gray value
derivatives, i.e, that
$\nabla_{2}f(x+u,y+v,t+1)=\nabla_{2}f(x,y,t)$ also holds, where
$\nabla_{2}f=(\partial_{x}f,\partial_{y}f)$. This can be written more compactly as
$\nabla_{2}f(\mathbf{x}+\mathbf{w})=\nabla_{2}f(\mathbf{x})$. In contrast to the gray value
constancy, the gradient constancy has the advantage that it is
invariant to additive global illumination changes.

*Large displacements*: It is assumed that large
displacements, i.e., displacements larger than one pixel, occur.
Under this assumption, it makes sense to consciously abstain from
using the linearization of the constancy assumptions in the model
that is typically proposed in the literature.

*Statistical robustness in the data term*: To reduce the
influence of outliers, i.e., points that violate the constancy
assumptions, they are penalized in a statistically robust manner,
i.e., the customary non-robust square penalization
$\Psi_{\mathrm{D}}(s^{2})=s^{2}$ is replaced by a
linear penalization via
$\Psi_S(s^2) = \sqrt{s^2 + \varepsilon^2}$ ![figure](../assets/ac961991f678958b.svg), where $\epsilon=0.001$ is a
fixed regularization constant.

*Preservation of discontinuities in the flow field I*: The
solution is assumed to be piecewise smooth. While the actual
smoothness is achieved by penalizing the first derivatives of the
flow $|\nabla_{2}u|^{2}+|\nabla_{2}v|^{2}$,
the use of a statistically robust (linear) penalty function
$\Psi_S(s^2) = \sqrt{s^2 + \varepsilon^2}$ ![figure](../assets/ac961991f678958b.svg) with $\epsilon=0.001$
provides the desired preservation of edges in the movement in the
flow field to be determined. This type of smoothness term is called
flow-driven and isotropic.

Taking into account all of the above assumptions, the energy
functional of the FDRIG algorithm can be written as
$$E_{FDRIG}(w) = \int \Psi_S\left( |f(x+w) - f(x)|^2 + \gamma \left| \nabla_2 f(x+w) - \nabla_2 f(x)\right|^2 \right) drdc \\ + \alpha \int \Psi_S\left( \left| \nabla_2 u(x) \right|^2 + \left| \nabla_2 v(x)\right|^2 \right) drdc$$ ![figure](../assets/dee6a3cf8bed039a.svg)

Here, $\alpha$ is the regularization parameter passed in
*`flow_smoothness`*, while $\gamma$ is the gradient
constancy weight passed in *`gradient_constancy`*. These two
parameters, which constitute the model parameters of the FDRIG
algorithm, are described in more detail below.

The **DDRAW algorithm** is based on the minimization of an
energy functional that contains the following assumptions:

*Constancy of the gray values*: It is assumed that
corresponding pixels in consecutive images of an image sequence have
the same gray value, i.e., that f(x+w) = f(x).

*Large displacements*: It is assumed that large
displacements, i.e., displacements larger than one pixel, occur.
Under this assumption, it makes sense to consciously abstain from
using the linearization of the constancy assumptions in the model
that is typically proposed in the literature.

*Statistical robustness in the data term*: To reduce the
influence of outliers, i.e., points that violate the constancy
assumptions, they are penalized in a statistically robust manner,
i.e., the customary non-robust square penalization
$\Psi_{\mathrm{D}}(s^{2})=s^{2}$ is replaced by a
linear penalization via
$\Psi_S(s^2) = \sqrt{s^2 + \varepsilon^2}$ ![figure](../assets/ac961991f678958b.svg), where $\epsilon=0.001$ is a
fixed regularization constant.

*Preservation of discontinuities in the flow field II*: The
solution is assumed to be piecewise smooth. In contrast to the
FDRIG algorithm, which allows discontinuities everywhere, the DDRAW
algorithm only allows discontinuities at the edges in the original
image. Here, the local smoothness is controlled in such a way that
the flow field is sharp across image edges, while it is smooth along
the image edges. This type of smoothness term is called data-driven
and anisotropic.

All assumptions of the DDRAW algorithm can be combined into the
following energy functional:
$$E_{DDRAW}(w)=\int\Psi_S\left(|f(x+w)-f(x)|^2\right)\,drdc +\alpha\int\left(\nabla_2u(x)^T P_{NE}(\nabla_2f(x))\nabla_2u(x)+\nabla_2v(x)^T P_{NE}(\nabla_2f(x))\nabla_2v(x)\right)\,drdc$$ ![figure](../assets/141ef970efc66ec4.svg)

where $P_{\mathrm{NE}}(\nabla_{2}f(\mathbf{x}))$ is a normalized projection matrix orthogonal to
$\nabla_{2}f(\mathbf{x})$, for which
$$P_{NE}(\nabla_{2} f(x)) = \frac{1}{|\nabla_{2} f(x)|^{2} + 2 \epsilon_{S}^{2}} \left( f_{c}^{2}(x) + \epsilon_{S}^{2} - f_{r}(x) f_{c}(x) \right)\n$$ ![figure](../assets/114a25fe0a0ebf2e.svg)

holds. This matrix ensures that the smoothness of the flow field is
only assumed along the image edges. In contrast, no assumption is
made with respect to the smoothness across the image edges,
resulting in the fact that discontinuities in the solution may occur
across the image edges. In this respect,
$\epsilon_{\mathrm{S}}=0.001$ serves as a
regularization parameter that prevents the projection matrix
$P_{\mathrm{NE}}(\nabla_{2}f(\mathbf{x}))$
from becoming singular. In contrast to the FDRIG algorithm, there
is only one model parameter for the DDRAW algorithm: the
regularization parameter $\alpha$. As mentioned above,
$\alpha$ is described in more detail below.

As for the two approaches described above, the **CLG algorithm**
uses certain assumptions:

*Constancy of the gray values*: It is assumed that
corresponding pixels in consecutive images of an image sequence have
the same gray value, i.e., that f(x+w) = f(x).

*Small displacements*: In contrast to the two approaches
above, it is assumed that only small displacements can occur, i.e.,
displacements in the order of a few pixels. This facilitates a
linearization of the constancy assumptions in the model, and leads
to the approximation $f(\mathbf{x})+\nabla_{3}f(\mathbf{x})^{\top}\mathbf{w}(\mathbf{x})=f(\mathbf{x})$, i.e., $\nabla_{3}f(\mathbf{x})^{\top}\mathbf{w}(\mathbf{x})=0$ should hold. Here, $\nabla_{3}f(\mathbf{x})$ denotes the gradient in the spatial as well as the
temporal domain.

*Local constancy of the solution*: Furthermore, it is assumed
that the flow field to be computed is locally constant. This
facilitates the integration of the image data in the data term over
the respective neighborhood of each pixel. This, in turn, increases
the robustness of the algorithm against noise. Mathematically, this
can be achieved by reformulating the quadratic data term as
$(\nabla_{3}f(\mathbf{x})^{\top}\mathbf{w}(\mathbf{x}))^{2}=\mathbf{w}(\mathbf{x})^{\top}\nabla_{3}f(\mathbf{x})\nabla_{3}f(\mathbf{x})^{\top}\mathbf{w}(\mathbf{x})$. By performing a local
Gaussian-weighted integration over a neighborhood specified by the
$\rho$ (passed in *`integration_sigma`*), the following
data term is obtained: $\mathbf{w}(\mathbf{x})^{\top}G_{\rho}\ast(\nabla_{3}f(\mathbf{x})\nabla_{3}f(\mathbf{x})^{\top})\mathbf{w}(\mathbf{x})$. Here, $G_{\rho}\ast...$ denotes a convolution of the 3x3 matrix
$\nabla_{3}f(\mathbf{x})\nabla_{3}f(\mathbf{x})^{\top}$ with a Gaussian filter with a standard
deviation of $\rho$ (see [`derivate_gauss`](derivate_gauss.md)).

*General smoothness of the flow field*: Finally, the solution
is assumed to be smooth everywhere in the image. This particular
type of smoothness term is called homogeneous.

All of the above assumptions can be combined into the following
energy functional:
$$E_{CLG}(w) = \int (w(x)^T G_{\rho} * (\nabla_3 f(x) \nabla_3 f(x)^T) w(x)) \, dr\, dc + \alpha \int (|\nabla_2 u(x)|^2 + |\nabla_2 v(x)|^2) \, dr\, dc$$ ![figure](../assets/d26efa1222ea666c.svg)
The corresponding model parameters are the regularization parameter
$\alpha$ as well as the integration scale $\rho$
(passed in *`integration_sigma`*), which determines the size of
the neighborhood over which to integrate the data term. These two
parameters are described in more detail below.

To compute the optical flow vector field for two consecutive images
of an image sequence with the FDRIG, DDRAW, or CLG algorithm, the
solution that best fulfills the assumptions of the respective
algorithm must be determined. From a mathematical point of view,
this means that a minimization of the above energy functionals
should be performed. For the FDRIG and DDRAW algorithms, so called
coarse-to-fine warping strategies play an important role in this
minimization, because they enable the calculation of large
displacements. Thus, they are a suitable means to handle the
omission of the linearization of the constancy assumptions
numerically in these two approaches.

To calculate large displacements, coarse-to-fine warping strategies
use two concepts that are closely interlocked: The successive
refinement of the problem (coarse-to-fine) and the successive
compensation of the current image pair by already computed
displacements (warping). Algorithmically, such coarse-to-fine
warping strategies can be described as follows:

1. First, both images of the current image pair are zoomed down to
a very coarse resolution level.

2. Then, the optical flow vector field is computed on this coarse
resolution.

3. The vector field is required on the next resolution level: It is
applied there to the second image of the image sequence, i.e., the
problem on the finer resolution level is compensated by the already
computed optical flow field. This step is also known as warping.

4. The modified problem (difference problem) is now solved on the
finer resolution level, i.e., the optical flow vector field is
computed there.

5. The steps 3-4 are repeated until the finest resolution level is
reached.

6. The final result is computed by adding up the vector fields from
all resolution levels.

This incremental computation of the optical flow vector field has
the following advantage: While the coarse-to-fine strategy ensures
that the displacements on the finest resolution level are very
small, the warping strategy ensures that the displacements remain
small for the incremental displacements (optical flow vector fields
of the difference problems). Since small displacements can be
computed much more accurately than larger displacements, the
accuracy of the results typically increases significantly by using
such a coarse-to-fine warping strategy. However, instead of having
to solve a single correspondence problem, an entire hierarchy of
these problems must now be solved. For the CLG algorithm, such a
coarse-to-fine warping strategy is unnecessary since the model
already assumes small displacements.

The maximum number of resolution levels (warping levels), the
resolution ratio between two consecutive resolution levels, as well
as the finest resolution level can be specified for the FDRIG as
well as the DDRAW algorithm. Details can be found below.

The minimization of functionals is mathematically very closely
related to the minimization of functions: Like the fact that the
zero crossing of the first derivative is a necessary condition for
the minimum of a function, the fulfillment of the so called
Euler-Lagrange equations is a necessary condition for the minimizing
function of a functional (the minimizing function corresponds to the
desired optical flow vector field in this case). The Euler-Lagrange
equations are partial differential equations. By discretizing these
Euler-Lagrange equations using finite differences, large sparse
nonlinear equation systems result for the FDRIG and DDRAW
algorithms. Because coarse-to-fine warping strategies are used,
such an equation system must be solved for each resolution level,
i.e., for each warping level. For the CLG algorithm, a single
sparse linear equation system must be solved.

To ensure that the above nonlinear equation systems can be solved
efficiently, the FDRIG and DDRAW use bidirectional multigrid
methods. From a numerical point of view, these strategies are among
the fastest methods for solving large linear and nonlinear equation
systems. In contrast to conventional non-hierarchical iterative
methods, e.g., the different linear and nonlinear Gauss-Seidel
variants, the multigrid methods have the advantage that corrections
to the solution can be determined efficiently on coarser resolution
levels. This, in turn, leads to a significantly faster convergence.
The basic idea of multigrid methods additionally consists of
hierarchically computing these correction steps, i.e., the
computation of the error on a coarser resolution level itself uses
the same strategy and efficiently computes its error (i.e., the
error of the error) by correction steps on an even coarser
resolution level. Depending on whether one or two error correction
steps are performed per cycle, a so called V or W cycle is obtained.
The corresponding strategies for stepping through the resolution
hierarchy are as follows for two to four resolution levels (where
1 is a fine and 4 is a coarse resolution level):
![figure](../assets/e67e2bd4638830d5.svg)
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
manner. Starting from a very coarse variant of the original
(non)linear equation system (level 4), the solution is successively
refined.
To do so, interpolated solutions of coarser variants of the equation
system are used as the initialization of the next finer variant. On
each resolution level itself, the V or W cycles described above are
used to efficiently solve the (non)linear equation system on that
resolution level. The corresponding multigrid methods are called
full multigrid methods in the literature. The full multigrid
algorithm can be visualized as follows:
$$\text{No explicit formulas present in the image.}$$ ![figure](../assets/25bdf305cf119249.svg)
This example represents a full multigrid algorithm that uses two W
correction cycles per resolution level of the hierarchical
initialization. The interpolation steps of the solution from one
resolution level to the next are denoted by i and the two W
correction cycles by $\mathrm{w}_{1}$ and
$\mathrm{w}_{2}$. Iterations on the original problem are
denoted by large markers, while small markers denote iterations on
error correction problems.

In the multigrid implementation of the FDRIG, DDRAW, and CLG
algorithm, the following parameters can be set: whether a
hierarchical initialization is performed; the number of coarse grid
correction steps; the maximum number of correction levels
(resolution levels); the number of pre-relaxation steps; the
number of post-relaxation steps. These parameters are described in
more detail below.

The basic solver for the FDRIG algorithm is a point-coupled
fixed-point variant of the linear Gauss-Seidel algorithm. The basic
solver for the DDRAW algorithm is an alternating line-coupled
fixed-point variant of the same type. The number of fixed-point
steps can be specified for both algorithms with a further parameter.
The basic solver for the CLG algorithm is a point-coupled linear
Gauss-Seidel algorithm. The transfer of the data between the
different resolution levels is performed by area-based interpolation
and area-based averaging, respectively.

After the algorithms have been described, the effects of the
individual parameters are discussed in the following.

The input images, along with their domains (regions of interest) are
passed in *`image_t1`* and *`image_t2`*. The computation of
the optical flow vector field *`vector_field`* is performed on
the smallest surrounding rectangle of the intersection of the
domains of *`image_t1`* and *`image_t2`*. The domain of
*`vector_field`* is the intersection of the two domains. Hence,
by specifying reduced domains for *`image_t1`* and
*`image_t2`*, the processing can be focused and runtime can
potentially be saved. It should be noted, however, that all methods
compute a global solution of the optical flow. In particular, it
follows that the solution on a reduced domain need not (and cannot)
be identical to the resolution on the full domain restricted to the
reduced domain.

*`smoothing_sigma`* specifies the standard deviation of the
Gaussian kernel that is used to smooth both input images. The
larger the value of *`smoothing_sigma`*, the larger the low-pass
effect of the Gaussian kernel, i.e., the smoother the preprocessed
image. Usually, *`smoothing_sigma`* = 0.8 is a suitable
choice. However, other values in the interval [0,2] are also
possible. Larger standard deviations should only be considered if
the input images are very noisy. It should be noted that larger
values of *`smoothing_sigma`* lead to slightly longer execution
times.

*`integration_sigma`* specifies the standard deviation
$\rho$ of the Gaussian kernel $G_{\rho}$ that is
used for the local integration of the neighborhood information of
the data term. This parameter is used only in the CLG algorithm and
has no effect on the other two algorithms. Usually,
*`integration_sigma`* = 1.0 is a suitable choice. However,
other values in the interval [0,3] are also possible. Larger
standard deviations should only be considered if the input images
are very noisy. It should be noted that larger values of
*`integration_sigma`* lead to slightly longer execution times.

*`flow_smoothness`* specifies the weight $\alpha$ of
the smoothness term with respect to the data term. The larger the
value of *`flow_smoothness`*, the smoother the computed optical
flow field. It should be noted that choosing
*`flow_smoothness`* too small can lead to unusable results, even
though statistically robust penalty functions are used, in
particular if the warping strategy needs to predict too much
information outside of the image. For byte images with a gray value
range of [0,255], values of *`flow_smoothness`* around 20 for
the flow-driven FDRIG algorithm and around 1000 for the data-driven
DDRAW algorithm and the homogeneous CLG algorithm typically yield
good results.

*`gradient_constancy`* specifies the weight $\gamma$
of the gradient constancy with respect to the gray value constancy.
This parameter is used only in the FDRIG algorithm. For the other
two algorithms, it does not influence the results. For byte images
with a gray value range of [0,255], a value of
*`gradient_constancy`* = 5 is typically a good choice, since
then both constancy assumptions are used to the same extent. For
large changes in illumination, however, significantly larger values
of *`gradient_constancy`* may be necessary to achieve good
results. It should be noted that for large values of the gradient
constancy weight the smoothness parameter *`flow_smoothness`*
must also be chosen larger.

The parameters of the multigrid solver and for the coarse-to-fine
warping strategy can be specified with the generic parameters
*`mgparam_name`* and *`mgparam_value`*. Usually, it
suffices to use one of the four default parameter sets via
*`mgparam_name`* = *"default_parameters"* and
*`mgparam_value`* = *"very_accurate"*,
*"accurate"*, *"fast_accurate"*, or *"fast"*.
The default parameter sets are described below. If the parameters
should be specified individually, *`mgparam_name`* and
*`mgparam_value`* must be set to tuples of the same length. The
values corresponding to the parameters specified in
*`mgparam_name`* must be specified at the corresponding position
in *`mgparam_value`*.

*`mgparam_name`* = *"warp_zoom_factor"* can be used to
specify the resolution ratio between two consecutive warping levels
in the coarse-to-fine warping hierarchy.
*"warp_zoom_factor"* must be selected from the open interval
(0,1). For performance reasons, *"warp_zoom_factor"* is
typically set to 0.5, i.e., the number of pixels is halved in each
direction for each coarser warping level. This leads to an increase
of 33% in the calculations that need to be performed with respect
to an algorithm that does not use warping. Values for
*"warp_zoom_factor"* close to 1 can lead to slightly better
results. However, they require a disproportionately larger
computation time, e.g., 426% for *"warp_zoom_factor"* =
0.9.

*`mgparam_name`* = *"warp_levels"* can be used to
restrict the warping hierarchy to a maximum number of levels. For
*"warp_levels"* = 0, the largest possible number of levels
is used. If the image size does not allow to use the specified
number of levels (taking the resolution ratio
*"warp_zoom_factor"* into account), the largest possible
number of levels is used. Usually, *"warp_levels"* should be
set to 0.

*`mgparam_name`* = *"warp_last_level"* can be used to
specify the number of warping levels for which the flow increment
should *no longer* be computed. Usually,
*"warp_last_level"* is set to 1 or 2, i.e., a flow increment
is computed for each warping level, or the finest warping level is
skipped in the computation. Since in the latter case the
computation is performed on an image of half the resolution of the
original image, the gained computation time can be used to compute a
more accurate solution, e.g., by using a full multigrid algorithm
with additional iterations. The more accurate solution is then
interpolated to the full resolution.

The three parameters that specify the coarse-to-fine warping
strategy are only used in the FDRIG and DDRAW algorithms. They are
ignored for the CLG algorithm.

*`mgparam_name`* = *"mg_solver"* can be used to specify
the general multigrid strategy for solving the (non)linear equation
system (in each warping level). For *"mg_solver"* =
*"multigrid"*, a normal multigrid algorithm (*without*
coarse-to-fine initialization) is used, while for
*"mg_solver"* = *"full_multigrid"* a full multigrid
algorithm (*with* coarse-to-fine initialization) is used.
Since a resolution reduction of 0.5 is used between two consecutive
levels of the coarse-to-fine initialization (in contrast to the
resolution reduction in the warping strategy, this value is
hard-coded into the algorithm), the use of a full multigrid
algorithm results in an increase of the computation time by
approximately 33% with respect to the normal multigrid algorithm.
Using *"mg_solver"* to *"full_multigrid"* typically
yields numerically more accurate results than *"mg_solver"*
= *"multigrid"*.

*`mgparam_name`* = *"mg_cycle_type"* can be used to
specify whether a V or W correction cycle is used per multigrid
level. Since a resolution reduction of 0.5 is used between two
consecutive levels of the respective correction cycle, using a W
cycle instead of a V cycle increases the computation time by
approximately 50%. Using *"mg_cycle_type"* = *"w"*
typically yields numerically more accurate results than
*"mg_cycle_type"* = *"v"*.

*`mgparam_name`* = *"mg_levels"* can be used to
restrict the multigrid hierarchy for the coarse-to-fine
initialization as well as for the actual V or W correction cycles.
For *"mg_levels"* = 0, the largest possible number of
levels is used. If the image size does not allow to use the
specified number of levels, the largest possible number of levels is
used. Usually, *"mg_levels"* should be set to 0.

*`mgparam_name`* = *"mg_cycles"* can be used to specify
the total number of V or W correction cycles that are being
performed. If a full multigrid algorithm is used,
*"mg_cycles"* refers to *each* level of the
coarse-to-fine initialization. Usually, one or two cycles are
sufficient to yield a sufficiently accurate solution of the equation
system. Typically, the larger *"mg_cycles"*, the more
accurate the numerical results. This parameter enters almost
linearly into the computation time, i.e., doubling the number of
cycles leads approximately to twice the computation time.

*`mgparam_name`* = *"mg_pre_relax"* can be used to
specify the number of iterations that are performed on each level of
the V or W correction cycles using the iterative basic solver
*before* the actual error correction is performed. Usually,
one or two pre-relaxation steps are sufficient. Typically, the
larger *"mg_pre_relax"*, the more accurate the numerical
results.

*`mgparam_name`* = *"mg_post_relax"* can be used to
specify the number of iterations that are performed on each level of
the V or W correction cycles using the iterative basic solver
*after* the actual error correction is performed. Usually, one
or two post-relaxation steps are sufficient. Typically, the larger
*"mg_post_relax"*, the more accurate the numerical results.

Like when increasing the number of correction cycles, increasing the
number of pre- and post-relaxation steps increases the computation
time asymptotically linearly. However, no additional restriction
and prolongation operations (zooming down and up of the error
correction images) are performed. Consequently, a moderate increase
in the number of relaxation steps only leads to a slight increase in
the computation times.

*`mgparam_name`* = *"mg_inner_iter"* can be used to
specify the number of iterations to solve the linear equation
systems in each fixed-point iteration of the nonlinear basic solver.
Usually, one iteration is sufficient to achieve a sufficient
convergence speed of the multigrid algorithm. The increase in
computation time is slightly smaller than for the increase in the
relaxation steps. This parameter only influences the FDRIG and
DDRAW algorithms since for the CLG algorithm no nonlinear equation
system needs to be solved.

*`mgparam_name`* = *"parallel_solver"* can be used to
enable a parallel processing of the FDRIG algorithm.
This changes the results of the operator slightly, but can allow
for a faster processing.
The value can be set to *"true"* or *"false"* (default).

As described above, usually it is sufficient to use one of the
default parameter sets for the parameters described above by using
*`mgparam_name`* = *"default_parameters"* and
*`mgparam_value`* = *"very_accurate"*,
*"accurate"*, *"fast_accurate"*, or *"fast"*.
If necessary, individual parameters can be modified after the
default parameter set has been chosen by specifying a subset of the
above parameters and corresponding values after
*"default_parameters"* in *`mgparam_name`* and
*`mgparam_value`* (e.g., *`mgparam_name`* =
*["default_parameters","warp_zoom_factor"]* and
*`mgparam_value`* = *["accurate",0.6]*).

The default parameter sets use the following values for the above
parameters:

*"default_parameters"* = *"very_accurate"*:
*"warp_zoom_factor"* = 0.5, *"warp_levels"* = 0,
*"warp_last_level"* = 1, *"mg_solver"* =
*"full_multigrid"*, *"mg_cycle_type"* =
*"w"*, *"mg_levels"* = 0, *"mg_cycles"* =
1, *"mg_pre_relax"* = 2, *"mg_post_relax"* = 2,
*"mg_inner_iter"* = 1.

*"default_parameters"* = *"accurate"*:
*"warp_zoom_factor"* = 0.5, *"warp_levels"* = 0,
*"warp_last_level"* = 1, *"mg_solver"* =
*"multigrid"*, *"mg_cycle_type"* = *"v"*,
*"mg_levels"* = 0, *"mg_cycles"* = 1,
*"mg_pre_relax"* = 1, *"mg_post_relax"* = 1,
*"mg_inner_iter"* = 1.

*"default_parameters"* = *"fast_accurate"*:
*"warp_zoom_factor"* = 0.5, *"warp_levels"* = 0,
*"warp_last_level"* = 2, *"mg_solver"* =
*"full_multigrid"*, *"mg_cycle_type"* =
*"w"*, *"mg_levels"* = 0, *"mg_cycles"* =
1, *"mg_pre_relax"* = 2, *"mg_post_relax"* = 2,
*"mg_inner_iter"* = 1.

*"default_parameters"* = *"fast"*:
*"warp_zoom_factor"* = 0.5, *"warp_levels"* = 0,
*"warp_last_level"* = 2, *"mg_solver"* =
*"multigrid"*, *"mg_cycle_type"* = *"v"*,
*"mg_levels"* = 0, *"mg_cycles"* = 1,
*"mg_pre_relax"* = 1, *"mg_post_relax"* = 1,
*"mg_inner_iter"* = 1.

It should be noted that for the CLG algorithm the two modes
*"fast_accurate"* and *"fast"* are identical to the
modes *"very_accurate"* and *"accurate"* since the CLG
algorithm does not use a coarse-to-fine warping strategy.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image_t1`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image 1.

**`image_t2`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image 2.

**`vector_field`** (output_object)  singlechannelimage(-array) `→` HObject (vector_field)

Optical flow.

**`algorithm`** (input_control)  string `→` str

Algorithm for computing the optical flow.

Default:
"fdrig"

List of values:
"clg", "ddraw", "fdrig"

**`smoothing_sigma`** (input_control)  real `→` float

Standard deviation for initial Gaussian smoothing.

Default:
0.8

Suggested values:
0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0

Restriction:
`SmoothingSigma >= 0.0`

**`integration_sigma`** (input_control)  real `→` float

Standard deviation of the integration filter.

Default:
1.0

Suggested values:
0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0

Restriction:
`IntegrationSigma >= 0.0`

**`flow_smoothness`** (input_control)  real `→` float

Weight of the smoothing term relative to the
data term.

Default:
20.0

Suggested values:
10.0, 20.0, 30.0, 50.0, 70.0, 100.0, 200.0, 300.0, 500.0, 700.0, 1000.0, 1500.0, 2000.0

Restriction:
`FlowSmoothness >= 0.0`

**`gradient_constancy`** (input_control)  real `→` float

Weight of the gradient constancy relative to
the gray value constancy.

Default:
5.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 70.0, 100.0

Restriction:
`GradientConstancy >= 0.0`

**`mgparam_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Parameter name(s) for the multigrid algorithm.

Default:
"default_parameters"

List of values:
"default_parameters", "mg_cycle_type", "mg_cycles", "mg_inner_iter", "mg_levels", "mg_post_relax", "mg_pre_relax", "mg_solver", "parallel_solver", "warp_last_level", "warp_levels", "warp_zoom_factor"

**`mgparam_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[str, float, int]]

Parameter value(s) for the multigrid algorithm.

Default:
"accurate"

Suggested values:
"very_accurate", "accurate", "fast_accurate", "fast", "multigrid", "full_multigrid", "v", "w", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, "true", "false"

## Example (HDevelop)

```
grab_image (ImageT1, AcqHandle)
while (true)
  grab_image (ImageT2, AcqHandle)
  optical_flow_mg (ImageT1, ImageT2, VectorField, 'fdrig', 0.8, 1, 10, \
                   5, 'default_parameters', 'accurate')
  threshold (VectorField, Region, 1, 10000)
  copy_obj (ImageT2, ImageT1, 1, 1)
endwhile
```

## Result

If the parameter values are correct, the operator
`optical_flow_mg` returns the value 2 (
H_MSG_TRUE)
. If the input is
empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Successors

`threshold`,
`vector_field_length`

## See also

`unwarp_image_vector_field`

## References

T. Brox, A. Bruhn, N. Papenberg, and J. Weickert: High accuracy
optical flow estimation based on a theory for warping. In T. Pajdla
and J. Matas, editors, Computer Vision - ECCV 2004, volume 3024 of
Lecture Notes in Computer Science, pages 25--36. Springer, Berlin,
2004.
  
A. Bruhn, J. Weickert, C. Feddern, T. Kohlberger, and C. Schnörr:
Variational optical flow computation in real-time. IEEE
Transactions on Image Processing, 14(5):608-615, May 2005.
  
H.-H. Nagel and W. Enkelmann: An investigation of smoothness
constraints for the estimation of displacement vector fields from
image sequences. IEEE Transactions on Pattern Analysis and Machine
Intelligence, 8(5):565-593, September 1986.
  
Ulrich Trottenberg, Cornelis Oosterlee, Anton Schüller: Multigrid.
Academic Press, Inc., San Diego, 2000.

## Module

Foundation
