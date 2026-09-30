# create_dl_layer_reduce (Operator)

## Name

`create_dl_layer_reduce` — Create a reduce layer.

## Signature

`create_dl_layer_reduce( : : DLLayerInput, LayerName, Operation, Axes, GenParamName, GenParamValue : DLLayerReduce)`

## Description

The operator `create_dl_layer_reduce` creates a reduce
layer whose handle is returned in *`DLLayerReduce`*.

A reduce layer applies a given operation to the input data tensor to
reduce it along one or multiple axes to a single value.
Hence, the output tensor has the same shape as the input tensor, but at the
axes given by *`Axes`* the dimension equals one.

The parameter *`DLLayerInput`* determines the feeding input layer.
This layer expects a single layer as input.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`Operation`* specifies the operation that is applied.
The operation is applied to the values along the axes given by *`Axes`*
of the input tensor and the result is written to the corresponding position
in the output tensor.
The supported values for *`Operation`* are:

- *'norm_l2'*: Computes the L2 norm of the input values.
- *'sum'*: Computes the sum of the input values.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*
- ***'div_eps'*:** —

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
| *'axes'* (*`Axes`*) |  | `x` |
| *'input_layer'* (*`DLLayerInput`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'operation'* (*`Operation`*) |  | `x` |
| *'output_layer'* (*`DLLayerReduce`*) |  | `x` |
| *'shape'* |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'is_inference_output'* | `x` | `x` |
| *'num_trainable_params'* |  | `x` |
| *'div_eps'* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→`  (handle)

Feeding input layer.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`Operation`** (input_control)  string `→`  (string)

Reduce operation.

Default:
'norm_l2'

List of values:
'norm_l2', 'sum'

**`Axes`** (input_control)  integer(-array) `→`  (integer / string)

Axes to which the reduce operation is applied.

Default:
[2,3]

List of values:
0, 1, 2, 3, 'batch', 'depth', 'height', 'width'

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'div_eps', 'is_inference_output'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
1e-10, 'true', 'false'

**`DLLayerReduce`** (output_control)  dl_layer `→`  (handle)

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
