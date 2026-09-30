# DerivateVectorField (Operator)

## Name

`DerivateVectorField` — Convolve a vector field with derivatives of the Gaussian.

## Signature

`static void HOperatorSet.DerivateVectorField(HObject vectorField, out HObject result, HTuple sigma, HTuple component)`

`HImage HImage.DerivateVectorField(HTuple sigma, string component)`

`HImage HImage.DerivateVectorField(double sigma, string component)`

## Description

`DerivateVectorField` convolves the components of a vector field with
the derivatives of a Gaussian and calculates various features derived
therefrom.
`DerivateVectorField` only accepts vector fields of the semantic
type `vector_field_relative`.
The *`vectorField`* $F(r,c)=(u(r,c),v(r,c))$ is defined as in
[`OpticalFlowMg`](optical_flow_mg.md).
*`sigma`* is the parameter of the Gaussian
(i.e., the amount of smoothing). If a single value is passed in
*`sigma`*, the amount of smoothing in the column and row direction is
identical. If two values are passed in *`sigma`*, the first value
specifies the amount of smoothing in the column direction, while the second
value specifies the amount of smoothing in the row direction. The possible
values for *`component`* are:

- ***"curl"*:** —

  The curl of the vector field. One application of using *"curl"* is to
  analyze optical flow fields.
  Metaphorically speaking, the curl is how much a small boat would rotate if
  the vector field was a fluid.

  $$curl_l = \frac{\partial u(r,c)}{\partial c} - \frac{\partial v(r,c)}{\partial r}$$ ![figure](../assets/70810e9fff63d954.svg)
- ***"divergence"*:** —

  The divergence of the vector field. One application of using
  *"divergence"* is to analyze optical flow fields.
  Metaphorically speaking, the divergence is where the source and sink would be
  if the vector field was a fluid.

  $$div = \frac{\partial u(r,c)}{\partial r} + \frac{\partial v(r,c)}{\partial c}$$ ![figure](../assets/d29980c4a664b9f7.svg)

When used in context of photometric stereo, the operator
`DerivateVectorField` offers two more parameters, which are
especially designed to process the gradient field that is returned by
[`PhotometricStereo`](photometric_stereo.md). In this case, we interpret the input vector
field as gradient of the underlying surface.

In the following formulas, the input vector field is
therefore noted as $$G(r,c) = \nabla f = \left( \frac{\partial f(r,c)}{\partial r}, \frac{\partial f(r,c)}{\partial c} \right)$$ ![figure](../assets/1d67fcee932460bc.svg)
where the first and second component of the input is the gradient field of the
surface $f(r,c)$. In the formulas below f_rc denotes the first
derivative in column direction of the first component of the gradient field.

- ***"mean_curvature"*:** —

  Mean curvature $H$ of the underlying surface when the input vector field
  *`vectorField`* is interpreted as gradient field. One application of
  using *"mean_curvature"* is to process the vector field that is returned by
  [`PhotometricStereo`](photometric_stereo.md). After filtering the vector field, even tiny
  scratches or bumps can be segmented.

  $$A = \left(1 + \frac{\partial f(r,c)^2}{\partial r}\frac{\partial f(r,c)}{\partial c} \right)\\ B = \frac{\partial f(r,c)}{\partial r}\frac{\partial f(r,c)}{\partial c}\left( \frac{\partial^2 f(r,c)}{\partial r\partial c} + \frac{\partial^2 f(r,c)}{\partial c\partial r} \right)\\ C = \left(1 + \frac{\partial f(r,c)^2}{\partial c}\right)\frac{\partial f(r,c)}{\partial r^2}\\ D = \left(1 + \frac{\partial f(r,c)^2}{\partial r} + \frac{\partial f(r,c)^2}{\partial c}\right)^{3/2} \\ H = \frac{A - B + C}{D}$$ ![figure](../assets/88e9c855d1a2ce6a.svg)
- ***"gauss_curvature"*:** —

  Gaussian curvature $K$ of the underlying surface when the input vector
  field *`vectorField`* is interpreted as gradient field. One application
  of using *"gauss_curvature"* is to process the vector field that is
  returned by [`PhotometricStereo`](photometric_stereo.md). After filtering the vector field,
  even tiny scratches or bumps can be segmented. If the underlying surface of
  the vector field is developable, the Gaussian curvature is zero.

  $$K = \frac{\frac{\partial f(r,c)^2}{\partial r \partial r} * \frac{\partial f(r,c)^2}{\partial c \partial c} - \frac{\partial f(r,c)^2}{\partial r \partial c} * \frac{\partial f(r,c)^2}{\partial c \partial r}}{\Big(1 + \frac{\partial f(r,c)^2}{\partial r} + \frac{\partial f(r,c)^2}{\partial c}\Big)^2}$$ ![figure](../assets/0af5501b779cafca.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.
- Automatically parallelized on tuple level.

## Parameters

**`vectorField`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (vector_field)

Input vector field.

**`result`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

Filtered result images.

**`sigma`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Sigma of the Gaussian.

Default:
1.0

Suggested values:
0.7, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0

Value range:
`0.01
≤
sigma
≤
50.0`

**`component`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Component to be calculated.

Default:
"mean_curvature"

List of values:
"curl", "divergence", "gauss_curvature", "mean_curvature"

## Result

If the parameters are valid, the operator `DerivateVectorField`
returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available)
is set via the operator `set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`OpticalFlowMg`,
`PhotometricStereo`

## Possible Successors

`Threshold`

## Module

Foundation
