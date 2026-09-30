# create_dl_layer_reduce (Operator)

## Name

`create_dl_layer_reduce` — Create a reduce layer.

## Signature

`def create_dl_layer_reduce(dllayer_input: HHandle, layer_name: str, operation: str, axes: MaybeSequence[Union[int, str]], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_reduce` creates a reduce
layer whose handle is returned in *`dllayer_reduce`*.

A reduce layer applies a given operation to the input data tensor to
reduce it along one or multiple axes to a single value.
Hence, the output tensor has the same shape as the input tensor, but at the
axes given by *`axes`* the dimension equals one.

The parameter *`dllayer_input`* determines the feeding input layer.
This layer expects a single layer as input.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`operation`* specifies the operation that is applied.
The operation is applied to the values along the axes given by *`axes`*
of the input tensor and the result is written to the corresponding position
in the output tensor.
The supported values for *`operation`* are:

- *"norm_l2"*: Computes the L2 norm of the input values.
- *"sum"*: Computes the sum of the input values.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"div_eps"*:** —

  Small scalar value that is used to stabilize the training. I.e., in case of
  a division, the value is added to the denominator to prevent a division by
  zero.

  Default:
   *1e-10*

Certain parameters of layers created using this operator
`create_dl_layer_reduce` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"axes"* (*`axes`*) |  | `x` |
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"operation"* (*`operation`*) |  | `x` |
| *"output_layer"* (*`dllayer_reduce`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"div_eps"* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_input`** (input_control)  dl_layer `→` HHandle

Feeding input layer.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`operation`** (input_control)  string `→` str

Reduce operation.

Default:
"norm_l2"

List of values:
"norm_l2", "sum"

**`axes`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Axes to which the reduce operation is applied.

Default:
[2,3]

List of values:
0, 1, 2, 3, "batch", "depth", "height", "width"

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"div_eps", "is_inference_output"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
1e-10, "true", "false"

**`dllayer_reduce`** (output_control)  dl_layer `→` HHandle

Reduce layer.

## Example (HDevelop)

```
* Minimal example for reduce-layer.
create_dl_layer_input ('input', [64, 32, 10], [], [], DLLayerInput)
create_dl_layer_reduce (DLLayerInput, 'reduce_width', 'sum', 'width', [], [], \
                         DLLayerReduceWidth)
create_dl_layer_reduce (DLLayerReduceWidth, 'reduce_height_depth', 'norm_l2',  [1,2], [], \
                         [], DLLayerReduceHeightDepth)
* Create a model and change the batch-size.
create_dl_model (DLLayerReduceHeightDepth, DLModel)
set_dl_model_param (DLModel, 'batch_size', 2)
get_dl_model_layer_param (DLModel, 'reduce_height_depth', 'shape', ShapeReduceHeightWidth)
```

## Possible Predecessors

`create_dl_layer_input`

## Possible Successors

`create_dl_model`

## Module

Deep Learning Professional
