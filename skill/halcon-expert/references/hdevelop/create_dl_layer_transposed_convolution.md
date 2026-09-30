# create_dl_layer_transposed_convolution (Operator)

## Name

`create_dl_layer_transposed_convolution` — Create a transposed convolution layer.

## Signature

`create_dl_layer_transposed_convolution( : : DLLayerInput, LayerName, KernelSize, Stride, KernelDepth, Groups, Padding, GenParamName, GenParamValue : DLLayerTransposedConvolution)`

## Description

The operator `create_dl_layer_transposed_convolution` creates a
transposed convolution layer whose handle is returned in
*`DLLayerTransposedConvolution`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`KernelSize`* specifies the filter kernel in the
dimensions `width` and `height`.
So far, only quadratic kernels are supported.

Restriction:
 This value must be a tuple of length 1.

The parameter *`Stride`* determines how the filter is shifted in
`row` and `column` direction.

Restriction:
 This value must be a tuple of length 1.

The parameter *`KernelDepth`* defines the depth of the output feature
maps.

Restriction:
 This value must be a tuple of length 1.

The parameter *`Groups`* determines the amount of filter groups.
So far, only a single filter group is supported.

Restriction:
 This value must be a tuple of length 1.

The parameter *`Padding`* effectively appends
$\texttt{KernelSize}-1-\texttt{Padding}$
pixels with value 0 to each border of the input. This is set so that a
convolutional layer and a transposed convolution layer with the same
*`KernelSize`*, *`Stride`* and *`Padding`* values are
inverses of each other regarding their input and output shapes.
Supported *`Padding`* values are:

- *'half_kernel_size'*: The integer value of
  $\texttt{Padding}$
  in the formula above depends on the specified *`KernelSize`*.
  More precisely, it is calculated as
  $\mathrm{KernelSize/2}$ ![figure](../assets/8d4511858617714b.svg).
- *'none'*: The value of
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
     *'runtime'* *'gpu'* does
    not support asymmetric padding, i.e., the padding values for the
    left and right side must be equal, as well as the padding values for
    the top and bottom side.

  Restriction:
   The integer padding values must be smaller
  than the value set for *`KernelSize`*.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'bias_term'*:** —

  Determines, whether the layer has bias terms.

  Default:
   *'true'*
- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*
- ***'learning_rate_multiplier'*:** —

  Learning rate multiplier
  for this layer that is used during training.
  If *'learning_rate_multiplier'* is set to *0.0*, the layer is
  skipped during training.

  Default:
   *1.0*
- ***'output_padding'*:** —

  Can be used to resolve ambiguities in the
  output shape for *`KernelSize`* and *`Stride`* larger than
  *1*. As mentioned above in the description of the parameter
  *`Padding`*, with respect to the input and output shapes a transposed
  convolution layer can be seen as the inverse of a convolution layer if they
  have the same settings for *`KernelSize`*, *`Stride`*, and
  *`Padding`* (and dilation).
  However, a convolution layer can map several shapes to the same output
  spatial dimensions. E.g., for *`KernelSize`* *3*,
  *`Padding`* *1*, and *`Stride`* *2*, both inputs
  with spatial dimensions (H, W) = *'(4, 4)'* and (H, W) = *'(3, 3)'*
  are mapped to an output shape with (H, W) = *'(2, 2)'*. To get back to
  *'(4, 4)'* using a transposed convolution (with the same settings
  for *`KernelSize`*, *`Stride`*, and *`Padding`*)
  *'output_padding'* must be set to *1*.
  *'output_padding'* must not be larger than the bottom and right
  *`Padding`* and can only be set larger than *0* if
  *`Stride`* is larger than *1*.

  Default:
   *0*
- ***'weight_filler'*:** —

  Defines the mode how the weights are
  initialized.
  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *'xavier'*, *'msra'*,
  *'const'*

  Default:
   *'xavier'*
- ***'weight_filler_const_val'*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  Default:
   *0.5*
- ***'weight_filler_variance_norm'*:** —

  Value range for
  *'weight_filler'*.
  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *'norm_average'*, *'norm_in'*,
  *'norm_out'*, constant value (in combination with
  *'weight_filler'* = *'msra'*)

  Default:
   *'norm_in'*

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
| *'groups'* (*`Groups`*) |  | `x` |
| *'input_depth'* |  | `x` |
| *'input_layer'* (*`DLLayerInput`*) |  | `x` |
| *'kernel_depth'* (*`KernelDepth`*) |  | `x` |
| *'kernel_size'* (*`KernelSize`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerTransposedConvolution`*) |  | `x` |
| *'padding_type'* (*`Padding`*) |  | `x` |
| *'shape'* |  | `x` |
| *'stride'* (*`Stride`*) |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'bias_term'* |  | `x` |
| *'is_inference_output'* | `x` | `x` |
| *'learning_rate_multiplier'* | `x` | `x` |
| *'num_trainable_params'* |  | `x` |
| *'output_padding'* |  | `x` |
| *'weight_filler'* | `x` | `x` |
| *'weight_filler_const_val'* | `x` | `x` |
| *'weight_filler_variance_norm'* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→`  (handle)

Feeding layer.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`KernelSize`** (input_control)  number `→`  (integer)

Width and height of the filter kernels.

Default:
3

**`Stride`** (input_control)  number `→`  (integer)

Amount of filter shift.

Default:
1

**`KernelDepth`** (input_control)  number `→`  (integer)

Depth of filter kernels.

Default:
64

**`Groups`** (input_control)  number `→`  (integer)

Number of filter groups.

Default:
1

**`Padding`** (input_control)  number(-array) `→`  (string / integer)

Type of the padding.

Default:
'none'

List of values:
[all], [width,height], [left,right,top,bottom], 'half_kernel_size', 'none'

Suggested values:
'none', 'half_kernel_size'

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'bias_term', 'is_inference_output', 'learning_rate_multiplier', 'output_padding', 'weight_filler', 'weight_filler_const_val', 'weight_filler_variance_norm'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
'xavier', 'msra', 'const', 'norm_in', 'norm_out', 'norm_average', 'true', 'false'

**`DLLayerTransposedConvolution`** (output_control)  dl_layer `→`  (handle)

Transposed convolutional layer.

## Module

Deep Learning Professional
