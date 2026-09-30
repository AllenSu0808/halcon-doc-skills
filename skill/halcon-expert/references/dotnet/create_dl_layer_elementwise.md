# CreateDlLayerElementwise (Operator)

## Name

`CreateDlLayerElementwise` — Create an elementwise layer.

## Signature

`static void HOperatorSet.CreateDlLayerElementwise(HTuple DLLayerInputs, HTuple layerName, HTuple operation, HTuple coefficients, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerElementWise)`

`static HDlLayer HDlLayer.CreateDlLayerElementwise(HDlLayer[] DLLayerInputs, string layerName, string operation, HTuple coefficients, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerElementwise(string layerName, string operation, double coefficients, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerElementwise` creates an element-wise
layer whose handle is returned in *`DLLayerElementWise`*.

An elementwise layer applies a certain operation to every data tensor of
the input layers handles and to each element of the data tensor.
As a consequence, all input data tensors should be of the same shape and
the output tensor has the same shape as the first input tensor.

The parameter *`DLLayerInputs`* determines the feeding input layers.
This layer expects multiple layers as input. For *`operation`* =
*"division"* exactly two input layers are expected.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
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
layers in *`DLLayerInputs`*.
Set *`coefficients`* equal to *[]* if
no coefficients shall be used in the element-wise operation.

Restriction:
 No coefficients can be set for
*`operation`* = *"product"*.

*Example:* for *`operation`* = *"sum"*,
the $i$-th element of the output data tensor is given by
$$output[i] = \sum_{n=0}^{N-1} Coefficients[n] · DLayerInputs_n[i],$$ ![figure](../assets/c7106eefccf4000d.svg)
where $N$ is the number of input data tensors.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"div_eps"*:** —

  Small scalar value that is added to the elements of the denominator to
  avoid a division by zero (for *`operation`* = *"division"*).

  Default:
   *1e-10*
- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerElementwise` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md).
Note, the operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) require a model created by
[`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"coefficients"* (*`coefficients`*) | `x` | `x` |
| *"input_layer"* (*`DLLayerInputs`*) |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"operation"* (*`operation`*) |  | `x` |
| *"output_layer"* (*`DLLayerElementWise`*) |  | `x` |
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

**`DLLayerInputs`** (input_control)  dl_layer(-array) `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Feeding input layers.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`operation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Element-wise operations.

Default:
"sum"

List of values:
"division", "maximum", "minimum", "product", "sum"

**`coefficients`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Optional input tensor coefficients.

Default:
[]

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`DLLayerElementWise`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Elementwise layer.

## Module

Deep Learning Professional
