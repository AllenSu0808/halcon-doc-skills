# create_dl_layer_gather (Operator)

## Name

`create_dl_layer_gather` — Create a gather layer.

## Signature

`create_dl_layer_gather( : : DLLayerInput, Indices, LayerName, Axis, GenParamName, GenParamValue : DLLayerGather)`

## Description

The operator `create_dl_layer_gather` creates a gather layer that
extracts slices from the input tensor *`DLLayerInput`* along a
specified axis, according to the indices provided.
The handle of the gather layer is returned in *`DLLayerGather`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as its value.

The parameter *`Indices`* defines the indices to be gathered from the
axis. The indices must be either of rank 0 or rank 1, i.e., a scalar or a
list. The indices input can be a layer handle (*`Indices`*) or a tuple
of integers.
If *`Indices`* is given as a tuple of integers, internally a constant
input layer is created.

The axis along which the gathering is performed is specified by the parameter
*`Axis`*. *`Axis`* can either be specified by a string
(*'width'*, *'height'*, *'depth'* or *'batch'*) or an
integer, where 0 corresponds to the batch size, 1 to depth, 2 to height and 3
to width. Negative values for *`Axis`* indicate counting dimensions from
the back. The accepted range is [-4,3].

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md), each layer
of the created network must have a unique name.

**Gather semantics**

Given a 4-dimensional input tensor *`DLLayerInput`* of shape
(N, C, H, W) and an indices tensor or tuple,
the gather layer selects elements from the *`Axis`* dimension indexed
by elements of *`Indices`*.

If the indices are given as a tuple
$$(i_{0},...,i_{k})$$
and
*`Axis`* $=a$, the output tensor is constructed by replacing dimension
$a$ with the indices dimensions, resulting in an output of shape
$$(d_{0},...,d_{a-1},k+1,d_{a+1},...,d_{r-1})$$

All index values in *`Indices`* must be within the bounds
$[-s,s-1]$, where $s$ is the size of the *`Axis`*
dimension. Negative indices are interpreted by adding $s$, i.e.,
*'index'* = *'index'*$+s$ if *'index'* < 0.

**Index Processing**

- **Adjusting Axis** —

  Negative values for *`Axis`* are made non-negative by adding the
  number of dimensions r of the input tensor:
  $$\text{axis}\leftarrow\text{axis}+r\text{if axis}<0$$
- **Clamping Indices** —

  Negative values in *`Indices`* are adjusted by adding the size s
  of the corresponding axis:
  $$\text{indices}[j]\leftarrow\text{indices}[j]+s\text{if indices}[j]<0$$

  All values in *`Indices`* must satisfy
  $$0\le\text{indices}[j]<s$$
  Otherwise, an error will be raised.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying
  this layer in `Outputs` (*'true'*) or not (*'false'*).

  List of values:
   *'true'*, *'false'*

  Default:
   *'false'*

Certain parameters of layers created using this operator
`create_dl_layer_gather` can be set and retrieved using further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved using
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'input_layer'* (*`DLLayerInput`*,*`Indices`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'axis'* (*`Axis`*) |  | `x` |
| *'output_layer'* (*`DLLayerGather`*) |  | `x` |
| *'shape'* |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'is_inference_output'* | `x` | `x` |
| *'num_trainable_params'* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→`  (handle)

Feeding data input layer.

Default:
'DLLayerInput'

**`Indices`** (input_control)  number(-array) `→`  (integer / handle)

Indices for the gather operation. This input can be a layer or
tuple of integers.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`Axis`** (input_control)  number `→`  (integer / string)

Axis along which to gather.

Default:
0

Suggested values:
0, 'batch', 1, 'depth', 2, 'height', 3, 'width'

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'is_inference_output'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
'true', 'false'

**`DLLayerGather`** (output_control)  dl_layer `→`  (handle)

Output layer.

## Module

Deep Learning Professional
