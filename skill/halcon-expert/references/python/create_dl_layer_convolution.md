# create_dl_layer_convolution (Operator)

## Name

`create_dl_layer_convolution` — Create a convolutional layer.

## Signature

`def create_dl_layer_convolution(dllayer_input: HHandle, layer_name: str, kernel_size: MaybeSequence[int], dilation: MaybeSequence[int], stride: MaybeSequence[int], num_kernel: int, groups: int, padding: MaybeSequence[Union[str, int]], activation: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_convolution` creates a convolutional
layer with *`num_kernel`* kernels in
*`groups`* filter groups whose handle is returned in
*`dllayer_convolution`*.

The parameter *`dllayer_input`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`kernel_size`* specifies the filter kernel in the
dimensions `width` and `height`.

The parameter *`dilation`* specifies the factor
of filter dilation in the dimensions `width` and `height`.

The parameter *`stride`* specifies how the filter is shifted.

The values for *`kernel_size`*, *`dilation`*, and *`stride`*
can be set as

- a single value which is used for both dimensions
- a tuple `[width, height]` and `[column, row]`,
  respectively.

The parameter *`groups`* specifies the number of filter groups.

The parameter *`num_kernel`* specifies the number of filter kernels.
*`num_kernel`* must be a multiple of *`groups`*.

The parameter *`padding`* determines the padding, thus
how many pixels with value 0 are appended on the border of the
processed input image. Supported values are:

- *"half_kernel_size"*: The number of appended pixels
  depends on the specified *`kernel_size`*.
  More precisely, it is calculated as
  $\mathrm{KernelSize/2}$ ![figure](../assets/8d4511858617714b.svg),
  where for the padding on the left / right border the value of
  *`kernel_size`* in dimension `width` is regarded
  and for the padding on the upper / lower border the value of
  *`kernel_size`* in `height`.
- *"none"*: No pixels are appended.
- Number of pixels: Specify the number of pixels
  appended on each border. To do so, the following tuple lengths are
  supported:

  - Single number: Padding in all four directions
    left/right/top/bottom.
  - Two numbers: Padding in left/right and top/bottom:
    `[l/r, t/b]`.
  - Four numbers: Padding on left, right, top, bottom side:
    `[l,r,t,b]`.

    Restriction:
     *"runtime"* *"gpu"* does
    not support asymmetric padding, i.e., the padding values for the
    left and right side must be equal, as well as the padding values for
    the top and bottom side.

  Restriction:
   The integer padding values must be smaller
  than the value set for *`kernel_size`* in the corresponding dimension.

The output dimensions of the convolution layer are given by
$$output_dim = \left[ \frac{input_dim + 2(padding_begin + padding_end)}{Stride} \right] \left|\_KernelSize + (KernelSize - 1)(Dilation - 1) \right| + 1$$ ![figure](../assets/752e6d7cfe174562.svg)
Thereby we use the following values:
$output\_dim$: output width/height,
$input\_dim$: input width/height,
$padding\_begin$: number of pixels added to the left/top of
the input image, and
$padding\_end$: number of pixels added to the right/bottom of
the input image.

The parameter *`activation`* determines whether an activation is
performed after the convolution in order to optimize the runtime
performance.
The following values are supported:

- *"relu"*: perform a ReLU activation after the convolution.
- *"sigmoid"*: perform a Sigmoid activation after the convolution.
- *"tanh"*: perform a Tanh activation after the convolution.

  It is possible to specify an upper bound to the ReLU operation
  (see [`create_dl_layer_activation`](create_dl_layer_activation.md)) via the generic parameter
  *"upper_bound"*. Note: It is not possible to specify a leaky ReLU.
- *"none"*: no activation operation is performed.

We refer to the `“Solution Guide on Classification”` for more
general information about the convolution layer and the
reference given below for more detailed information about the arithmetic
of the layer.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"bias_filler"*:** —

  See *"weight_filler"* for an
  explanation of the values.

  List of values:
   *"xavier"*, *"msra"*,
  *"const"*.

  Default:
   *"const"*
- ***"bias_filler_variance_norm"*:** —

  See *"weight_filler_variance_norm"* for an explanation of the
  values.

  List of values:
   *"norm_in"*, *"norm_out"*,
  *"norm_average"*.

  Default:
   *"norm_in"*
- ***"bias_filler_const_val"*:** —

  Specifies the constant bias term
  initialization value if *"bias_filler"* has been set to
  *"const"*.

  Restriction:
   Ignored for other values of *"bias_filler"*.

  Default:
   *0*
- ***"bias_term"*:** —

  Determines whether the created
  convolutional layer has a bias term (*"true"*) or not
  (*"false"*).

  Default:
   *"true"*
- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"learning_rate_multiplier"*:** —

  Multiplier for the learning
  rate for this layer that is used during training.
  If *"learning_rate_multiplier"* is set to *0.0*, the layer is
  skipped during training.

  Default:
   *1.0*
- ***"learning_rate_multiplier_bias"*:** —

  Multiplier for the
  learning rate of the bias term. The total bias learning rate is the
  product of *"learning_rate_multiplier_bias"* and
  *"learning_rate_multiplier"*.

  Default:
   *1.0*
- ***"upper_bound"*:** —

  Float value, which defines the upper bound
  for ReLU. To unset the upper bound, set *"upper_bound"* to an
  empty tuple.

  Default:
   *[]*
- ***"weight_filler"*:** —

  This parameter defines the mode how the
  weights are initialized. The following values are supported:

  - *"const"*: The weights are filled with constant values.
  - *"msra"*: The weights are drawn from a Gaussian distribution.
  - *"xavier"*: The weights are drawn from a uniform
    distribution.

  Default:
   *"xavier"*
- ***"weight_filler_const_val"*:** —

  Specifies the constant weight
  initialization value.

  Restriction:
   Only applied if *"weight_filler"* =
  *"const"*.

  Default:
   *0.5*
- ***"weight_filler_variance_norm"*:** —

  This parameter determines
  the value range for *"weight_filler"*. The following values are
  supported:

  - *"norm_average"*: the values are based on the average of the
    input and output size
  - *"norm_in"*: the values are based on the input size
  - *"norm_out"*: the values are based on the output size.

  Default:
   *"norm_in"*

Certain parameters of layers created using
`create_dl_layer_convolution` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"activation_mode"* (*`activation`*) |  | `x` |
| *"dilation"* (*`dilation`*) |  | `x` |
| *"groups"* (*`groups`*) |  | `x` |
| *"input_depth"* |  | `x` |
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"kernel_size"* (*`kernel_size`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"num_kernels"* (*`num_kernel`*) |  | `x` |
| *"output_layer"* (*`dllayer_convolution`*) |  | `x` |
| *"padding"* (*`padding`*) |  | `x` |
| *"padding_type"* (*`padding`*) |  | `x` |
| *"shape"* |  | `x` |
| *"stride"* (*`stride`*) |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"bias_filler"* | `x` | `x` |
| *"bias_filler_const_val"* | `x` | `x` |
| *"bias_filler_variance_norm"* | `x` | `x` |
| *"bias_term"* |  | `x` |
| *"is_inference_output"* | `x` | `x` |
| *"learning_rate_multiplier"* | `x` | `x` |
| *"learning_rate_multiplier_bias"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"upper_bound"* | `x` | `x` |
| *"weight_filler"* | `x` | `x` |
| *"weight_filler_const_val"* | `x` | `x` |
| *"weight_filler_variance_norm"* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_input`** (input_control)  dl_layer `→` HHandle

Feeding layer.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`kernel_size`** (input_control)  number(-array) `→` MaybeSequence[int]

Width and height of the filter kernels.

Default:
3

**`dilation`** (input_control)  number(-array) `→` MaybeSequence[int]

Amount of filter dilation for width and height.

Default:
1

**`stride`** (input_control)  number(-array) `→` MaybeSequence[int]

Amount of filter shift in width and height direction.

Default:
1

**`num_kernel`** (input_control)  number `→` int

Number of filter kernels.

Default:
64

**`groups`** (input_control)  number `→` int

Number of filter groups.

Default:
1

**`padding`** (input_control)  number(-array) `→` MaybeSequence[Union[str, int]]

Padding type or specific padding size.

Default:
"none"

List of values:
[all], [width,height], [left,right,top,bottom], "half_kernel_size", "none"

Suggested values:
"none", "half_kernel_size"

**`activation`** (input_control)  number `→` str

Enable optional ReLU, sigmoid or tanh activations.

Default:
"none"

List of values:
"none", "relu", "sigmoid", "tanh"

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"bias_filler", "bias_filler_const_val", "bias_filler_variance_norm", "bias_term", "is_inference_output", "learning_rate_multiplier", "learning_rate_multiplier_bias", "upper_bound", "weight_filler", "weight_filler_const_val", "weight_filler_variance_norm"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"xavier", "msra", "const", "nearest_neighbor", "bilinear", "norm_in", "norm_out", "norm_average", "true", "false", 1.0, 0.9, 0.0

**`dllayer_convolution`** (output_control)  dl_layer `→` HHandle

Convolutional layer.

## References

V. Dumoulin, F. Visin: "A guide to convolution arithmetic for deep
learning", 2018, http://arxiv.org/abs/1603.07285

## Module

Deep Learning Professional
