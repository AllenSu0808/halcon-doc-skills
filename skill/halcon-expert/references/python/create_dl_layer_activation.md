# create_dl_layer_activation (Operator)

## Name

`create_dl_layer_activation` — Create an activation layer.

## Signature

`def create_dl_layer_activation(dllayer_input: HHandle, layer_name: str, activation_type: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_activation` creates an activation layer
whose handle is returned in *`dllayer_activation`*.

The parameter *`dllayer_input`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`activation_type`* sets the type of the activation.
Every activation mode defines a pointwise function.
Supported activation types are:

- ***"abs"*:** —

  Absolute value.
  $$Abs(x):=|x|$$
- ***"acos"*:** —

  Arccosine activation.
- ***"asin"*:** —

  Arcsine activation.
- ***"atan"*:** —

  Arctangent activation.
- ***"ceil"*:** —

  Rounds the input up to the nearest integer.
- ***"celu"*:** —

  Continuously differentiable exponential linear unit (Celu) activation,
  which is defined as follows:
  $$Celu(x) := \left\{ \alpha\left(e^{\frac{x}{\alpha}}-1\right) \quad \text{if } x<0,\\ x \quad \text{else.} \right.$$ ![figure](../assets/cc901fe7750e77d1.svg)
  Setting the generic parameter *"alpha"* determines the value
  $\alpha$ (default: 1.0). For $\alpha=1$ a Celu
  activation is identical to an ELU.
- ***"clip"*:** —

  Clip the input to a given interval:
  $$Clip(x) := {\n min if x \le min,\n max if x \ge max,\n x else.}$$ ![figure](../assets/e08bef77287bf08d.svg)
  Setting the generic parameters *"min"* and *"max"* determines
  the values $min$ and $max$, respectively.
- ***"cos"*:** —

  Cosine activation.
- ***"cosh"*:** —

  Hyperbolic cosine activation.
- ***"elu"*:** —

  Exponential linear unit (ELU) activation, which is defined as follows:
  $$ELU(x) := {\alpha(e^x - 1) \quad \text{if } x < 0, \\ \ x \quad \text{else.}$$ ![figure](../assets/5562276826c9cdbe.svg)
  Setting the generic parameter *"alpha"* determines the value
  $\alpha$ (default: 1.0).
- ***"erf"*:** —

  Gauss error function, which is defined
  as follows:
  $$erf(x) := \frac{2}{\sqrt{\pi}} \int_{0}^{x} e^{-t^2} \, dt$$ ![figure](../assets/4d492dc407c2a6ea.svg)
- ***"exp"*:** —

  Exponential function:
  $$Exp(x):=e^{x}$$
- ***"floor"*:** —

  Rounds the input down to the nearest integer.
- ***"gelu"*:** —

  Gaussian error linear unit (Gelu) activation,
  which is defined as follows:
  $$Gelu(x) := 0.5 * x * (1 + erf(x / sqrt{2}))$$ ![figure](../assets/d01ba337f233fa2a.svg)
  Setting the generic parameter *"approximate"* to *"tanh"*
  determines whether an approximate function estimation is used:
  $$Gelu(x) := 0.5 * x * (1 + tanh( sqrt{2 over pi} * (x + 0.04715 * x^3 )))$$ ![figure](../assets/692a468d85cf1c5e.svg)
- ***"hard_sigmoid"*:** —

  HardSigmoid activation:
  $$HardSigmoid(x):=\max (0,\min (1,\alpha x+\beta))$$
  Setting the generic parameters *"alpha"* and *"beta"*
  determines the values $\alpha$ (default: 0.2) and $\beta$
  (default: 0.5).
- ***"hard_swish"*:** —

  HardSwish activation:
  $$HardSwish(x):=x\ast HardSigmoid(x)$$
  with fixed $\alpha = \frac{1}{6}$ ![figure](../assets/536eaee2eb1c7c15.svg) and $\beta=0.5$.
- ***"log"*:** —

  Natural logarithm:
  $$Log(x):=\log (x)$$
- ***"mish"*:** —

  Mish activation:
  $$Mish(x):=x\ast\tanh (Softplus(x))$$
- ***"neg"*:** —

  Negative of input:
  $$Neg(x):=-x$$
- ***"pow"*:** —

  Power function:
  $$Pow(x):=x^{exponent}$$
  Setting the generic parameter *"exponent"* determines the value
  $exponent$.
- ***"reciprocal"*:** —

  Reciprocal function:
  $$\mathrm{Reciprocal}(x) := \frac{1}{x}$$ ![figure](../assets/dbac24f6247a012e.svg)
- ***"relu"*:** —

  Rectified linear unit (ReLU) activation.
  By setting a specific ReLU parameter, another type can be specified
  instead of the standard ReLU:

  - Standard ReLU, defined as follows:
    $$ReLU(x):=\max (0,x)$$
  - Bounded ReLU, defined as follows:
    $$ReLU(x):=\left\{\begin{array}{ll}0 & \text{if } x\le 0,\\ x & \text{if } 0<x\le \beta,\\ \beta & \text{else.}\end{array}\right.$$ ![figure](../assets/af357fbd382f38ac.svg)
    Setting the generic parameter *"upper_bound"* will result in a
    bounded ReLU and determines the value of $\beta$.
  - Leaky ReLU, defined as follows:
    $$ReLU(x) := { \alpha x if x ≤ 0, \\ x if else. }$$ ![figure](../assets/d9b9e0ed9f961a15.svg)
    Setting the generic parameter *"alpha"* results in a leaky ReLU
    and determines the value $\alpha$. When the generic parameter
    *"upper_bound"* is set, *"alpha"* will be ignored and the
    result will be a bounded ReLU.
- ***"round"*:** —

  Rounds the input to the nearest integer.
  Values with '.5' are rounded to the nearest even integer, e.g.:
  $Round(2.5)=2$,
  $Round(3.5)=4$.
- ***"sigmoid"*:** —

  Sigmoid activation, which is defined as follows:
  $$\mathrm{Sigmoid}(x) := \frac{1}{1 + e^{-x}}$$ ![figure](../assets/4f0efa368047f67f.svg)
- ***"sin"*:** —

  Sine activation.
- ***"sinh"*:** —

  Hyperbolic sine activation.
- ***"softplus"*:** —

  Softplus activation function, which is defined
  as follows:
  $$Softplus(x):=\log (e^{x}+1)$$
- ***"softsign"*:** —

  Softsign activation function, which is defined
  as follows:
  $$\operatorname{Softsign}(x) := \frac{x}{1+|x|}$$ ![figure](../assets/2cb6287e830d2ec5.svg)
- ***"sqrt"*:** —

  Square root of the input:
  $$\mathsqrt{\x} := \sqrt{x}$$ ![figure](../assets/a4d0526dc82b9177.svg)
- ***"swish"*:** —

  Swish activation function, which is defined as
  follows:
  $$\mathrm{Switch}(x) := x * \mathrm{sigmoid}(ax) = \frac{x}{1 + e^{-ax}}$$ ![figure](../assets/5ff8645180b37190.svg)
  Setting the generic parameter *"alpha"* determines the value
  $\alpha$ (default: 1.0).
- ***"tan"*:** —

  Tangent activation.
- ***"tanh"*:** —

  Tanh activation, which is defined as follows:
  $$\tanh(x) := 1 - \frac{2}{e^{2x}+1}$$ ![figure](../assets/6b50b143eddb3aa1.svg)
- ***"thresholded_relu"*:** —

  Thresholded ReLU, defined as follows:
  $$ThresholdedReLU(x) := { 0 if x ≤ α, x else. }$$ ![figure](../assets/5e2b441de2eb338e.svg)
  Setting the generic parameter *"alpha"* determines the value
  $\alpha$ (default: 1.0).

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"upper_bound"* (*"relu"*):** —

  Float value defining an upper bound for a rectified linear unit.
  If the activation layer is part of a model which has been created using
  [`create_dl_model`](create_dl_model.md), the upper bound can be unset. To do so, use
  [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and set an empty tuple for
  *"upper_bound"*.

  Default:
   *[]*
- ***"alpha"* (*"relu"*, *"elu"*, *"celu"*,
  *"thresholded_relu"*, *"swish"*, *"hard_sigmoid"*):** —

  Float value defining the alpha parameter of a leaky ReLU, thresholded
  ReLU, ELU, CELU, Swish or HardSigmoid-activation.

  Restriction:
   The value of *"alpha"* must be
  positive or zero for all activations except for *`activation_type`*
  *"thresholded_relu"*.
  This parameter is incompatible with and overridden by
  *"upper_bound"* for *`activation_type`* *"relu"*.

  Default:
   *0.2* for *"hard_sigmoid"*, else *1.0*
- ***"beta"* (*"hard_sigmoid"*):** —

  Float value defining the beta parameter of a HardSigmoid activation.

  Default:
   *0.5*
- ***"min"* (*"clip"*):** —

  Float value defining the min parameter of a clip activation.
- ***"max"* (*"clip"*):** —

  Float value defining the max parameter of a clip activation.
- ***"approximate"* (*"gelu"*):** —

  This value determines whether an approximate function estimation is used.

  List of values:
   *"tanh"*, *"false"*

  Default:
   *"false"*
- ***"exponent"* (*"pow"*):** —

  Float value defining the exponent parameter of a pow activation.

Certain parameters of layers created using this operator
`create_dl_layer_activation` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"activation_type"* (*`activation_type`*) | `x` | `x` |
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_activation`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"alpha"* | `x` | `x` |
| *"beta"* | `x` | `x` |
| *"upper_bound"* | `x` | `x` |
| *"min"* | `x` | `x` |
| *"max"* | `x` | `x` |
| *"approximate"* | `x` | `x` |
| *"exponent"* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_input`** (input_control)  dl_layer `→` HHandle

Feeding layer.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`activation_type`** (input_control)  string `→` str

Activation type.

Default:
"relu"

List of values:
"abs", "acos", "asin", "atan", "ceil", "celu", "clip", "cos", "cosh", "elu", "erf", "exp", "floor", "gelu", "hard_sigmoid", "hard_swish", "log", "mish", "neg", "pow", "reciprocal", "relu", "round", "sigmoid", "sin", "sinh", "softplus", "softsign", "sqrt", "swish", "tan", "tanh", "thresholded_relu"

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"alpha", "approximate", "beta", "exponent", "is_inference_output", "max", "min", "upper_bound"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false", "tanh"

**`dllayer_activation`** (output_control)  dl_layer `→` HHandle

Activation layer.

## Module

Deep Learning Professional
