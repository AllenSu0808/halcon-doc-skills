# create_dl_layer_transposed_convolution (Operator)

## Name

`create_dl_layer_transposed_convolution` — Create a transposed convolution layer.

## Signature

`def create_dl_layer_transposed_convolution(dllayer_input: HHandle, layer_name: str, kernel_size: int, stride: int, kernel_depth: int, groups: int, padding: MaybeSequence[Union[str, int]], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_transposed_convolution` creates a
transposed convolution layer whose handle is returned in
*`dllayer_transposed_convolution`*.

The parameter *`dllayer_input`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`kernel_size`* specifies the filter kernel in the
dimensions `width` and `height`.
So far, only quadratic kernels are supported.

Restriction:
 This value must be a tuple of length 1.

The parameter *`stride`* determines how the filter is shifted in
`row` and `column` direction.

Restriction:
 This value must be a tuple of length 1.

The parameter *`kernel_depth`* defines the depth of the output feature
maps.

Restriction:
 This value must be a tuple of length 1.

The parameter *`groups`* determines the amount of filter groups.
So far, only a single filter group is supported.

Restriction:
 This value must be a tuple of length 1.

The parameter *`padding`* effectively appends
$\texttt{KernelSize}-1-\texttt{Padding}$
pixels with value 0 to each border of the input. This is set so that a
convolutional layer and a transposed convolution layer with the same
*`kernel_size`*, *`stride`* and *`padding`* values are
inverses of each other regarding their input and output shapes.
Supported *`padding`* values are:

- *"half_kernel_size"*: The integer value of
  $\texttt{Padding}$
  in the formula above depends on the specified *`kernel_size`*.
  More precisely, it is calculated as
  $\mathrm{KernelSize/2}$ ![figure](../assets/8d4511858617714b.svg).
- *"none"*: The value of
  $\texttt{Padding}$ in the formula above is 0.
- Number of pixels: Specify the integer value of
  $\texttt{Padding}$ in the formula above for each border.
  To do so, the following tuple lengths are supported:

  - Single number: $\texttt{Padding}$ value for all
    four directions left/right/top/bottom.
  - Two numbers: $\texttt{Padding}$ value for left/right
    and top/bottom: `[l/r, t/b]`.
  - Four numbers: $\texttt{Padding}$ value for left,
    right, top, bottom side: `[l,r,t,b]`.

    Restriction:
     *"runtime"* *"gpu"* does
    not support asymmetric padding, i.e., the padding values for the
    left and right side must be equal, as well as the padding values for
    the top and bottom side.

  Restriction:
   The integer padding values must be smaller
  than the value set for *`kernel_size`*.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"bias_term"*:** —

  Determines, whether the layer has bias terms.

  Default:
   *"true"*
- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"learning_rate_multiplier"*:** —

  Learning rate multiplier
  for this layer that is used during training.
  If *"learning_rate_multiplier"* is set to *0.0*, the layer is
  skipped during training.

  Default:
   *1.0*
- ***"output_padding"*:** —

  Can be used to resolve ambiguities in the
  output shape for *`kernel_size`* and *`stride`* larger than
  *1*. As mentioned above in the description of the parameter
  *`padding`*, with respect to the input and output shapes a transposed
  convolution layer can be seen as the inverse of a convolution layer if they
  have the same settings for *`kernel_size`*, *`stride`*, and
  *`padding`* (and dilation).
  However, a convolution layer can map several shapes to the same output
  spatial dimensions. E.g., for *`kernel_size`* *3*,
  *`padding`* *1*, and *`stride`* *2*, both inputs
  with spatial dimensions (H, W) = *"(4, 4)"* and (H, W) = *"(3, 3)"*
  are mapped to an output shape with (H, W) = *"(2, 2)"*. To get back to
  *"(4, 4)"* using a transposed convolution (with the same settings
  for *`kernel_size`*, *`stride`*, and *`padding`*)
  *"output_padding"* must be set to *1*.
  *"output_padding"* must not be larger than the bottom and right
  *`padding`* and can only be set larger than *0* if
  *`stride`* is larger than *1*.

  Default:
   *0*
- ***"weight_filler"*:** —

  Defines the mode how the weights are
  initialized.
  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *"xavier"*, *"msra"*,
  *"const"*

  Default:
   *"xavier"*
- ***"weight_filler_const_val"*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  Default:
   *0.5*
- ***"weight_filler_variance_norm"*:** —

  Value range for
  *"weight_filler"*.
  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *"norm_average"*, *"norm_in"*,
  *"norm_out"*, constant value (in combination with
  *"weight_filler"* = *"msra"*)

  Default:
   *"norm_in"*

Certain parameters of layers created using this operator
`create_dl_layer_transposed_convolution` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"groups"* (*`groups`*) |  | `x` |
| *"input_depth"* |  | `x` |
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"kernel_depth"* (*`kernel_depth`*) |  | `x` |
| *"kernel_size"* (*`kernel_size`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_transposed_convolution`*) |  | `x` |
| *"padding_type"* (*`padding`*) |  | `x` |
| *"shape"* |  | `x` |
| *"stride"* (*`stride`*) |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"bias_term"* |  | `x` |
| *"is_inference_output"* | `x` | `x` |
| *"learning_rate_multiplier"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"output_padding"* |  | `x` |
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

**`kernel_size`** (input_control)  number `→` int

Width and height of the filter kernels.

Default:
3

**`stride`** (input_control)  number `→` int

Amount of filter shift.

Default:
1

**`kernel_depth`** (input_control)  number `→` int

Depth of filter kernels.

Default:
64

**`groups`** (input_control)  number `→` int

Number of filter groups.

Default:
1

**`padding`** (input_control)  number(-array) `→` MaybeSequence[Union[str, int]]

Type of the padding.

Default:
"none"

List of values:
[all], [width,height], [left,right,top,bottom], "half_kernel_size", "none"

Suggested values:
"none", "half_kernel_size"

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"bias_term", "is_inference_output", "learning_rate_multiplier", "output_padding", "weight_filler", "weight_filler_const_val", "weight_filler_variance_norm"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"xavier", "msra", "const", "norm_in", "norm_out", "norm_average", "true", "false"

**`dllayer_transposed_convolution`** (output_control)  dl_layer `→` HHandle

Transposed convolutional layer.

## Module

Deep Learning Professional
