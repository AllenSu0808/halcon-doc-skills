# create_dl_layer_elementwise (Operator)

## Name

`create_dl_layer_elementwise` — Create an elementwise layer.

## Signature

`def create_dl_layer_elementwise(dllayer_inputs: MaybeSequence[HHandle], layer_name: str, operation: str, coefficients: MaybeSequence[float], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_elementwise` creates an element-wise
layer whose handle is returned in *`dllayer_element_wise`*.

An elementwise layer applies a certain operation to every data tensor of
the input layers handles and to each element of the data tensor.
As a consequence, all input data tensors should be of the same shape and
the output tensor has the same shape as the first input tensor.

The parameter *`dllayer_inputs`* determines the feeding input layers.
This layer expects multiple layers as input. For *`operation`* =
*"division"* exactly two input layers are expected.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`operation`* specifies the operation that is applied.
Depending on *`operation`*, the layer supports implicit unidirectional
broadcasting, i.e. there must be one input that has the "full" shape, which
is also the output shape (`batch_size`, `depth`,
`height`, `width`). All other inputs can have for each dimension
a size equal to this dimension or 1. If one of the dimensions is 1, the values
are implicitly broadcasted along that dimension to match the full shape.
The supported values are:

- *"division"*: Element-wise division. Broadcasting is supported,
  but only from the first to the second input, i.e., the first input must have
  the full shape.
- *"maximum"*: Element-wise maximum. Broadcasting is fully
  supported.
- *"minimum"*: Element-wise minimum. Broadcasting is fully
  supported.
- *"product"*: Element-wise product. Broadcasting is
  supported, but all inputs that do not have the full shape must have the
  same shape. Either all inputs have the full shape or only exactly one.
- *"sum"*: Element-wise summation. Broadcasting is fully
  supported.

Note, that broadcasting may be slower than all inputs having the same shape.

The optional parameter *`coefficients`* determines a weighting
coefficient for every input tensor.
The number of values in *`coefficients`* must match the number of feeding
layers in *`dllayer_inputs`*.
Set *`coefficients`* equal to *[]* if
no coefficients shall be used in the element-wise operation.

Restriction:
 No coefficients can be set for
*`operation`* = *"product"*.

*Example:* for *`operation`* = *"sum"*,
the $i$-th element of the output data tensor is given by
$$output[i] = \sum_{n=0}^{N-1} Coefficients[n] · DLayerInputs_n[i],$$ ![figure](../assets/c7106eefccf4000d.svg)
where $N$ is the number of input data tensors.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"div_eps"*:** —

  Small scalar value that is added to the elements of the denominator to
  avoid a division by zero (for *`operation`* = *"division"*).

  Default:
   *1e-10*
- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`create_dl_layer_elementwise` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"coefficients"* (*`coefficients`*) | `x` | `x` |
| *"input_layer"* (*`dllayer_inputs`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"operation"* (*`operation`*) |  | `x` |
| *"output_layer"* (*`dllayer_element_wise`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"div_eps"* | `x` | `x` |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_inputs`** (input_control)  dl_layer(-array) `→` MaybeSequence[HHandle]

Feeding input layers.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`operation`** (input_control)  string `→` str

Element-wise operations.

Default:
"sum"

List of values:
"division", "maximum", "minimum", "product", "sum"

**`coefficients`** (input_control)  number(-array) `→` MaybeSequence[float]

Optional input tensor coefficients.

Default:
[]

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`dllayer_element_wise`** (output_control)  dl_layer `→` HHandle

Elementwise layer.

## Module

Deep Learning Professional
