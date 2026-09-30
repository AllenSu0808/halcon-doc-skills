# CreateDlLayerGather (Operator)

## Name

`CreateDlLayerGather` — Create a gather layer.

## Signature

`static void HOperatorSet.CreateDlLayerGather(HTuple DLLayerInput, HTuple indices, HTuple layerName, HTuple axis, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerGather)`

`HDlLayer HDlLayer.CreateDlLayerGather(HTuple indices, string layerName, HTuple axis, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerGather(int indices, string layerName, int axis, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerGather` creates a gather layer that
extracts slices from the input tensor *`DLLayerInput`* along a
specified axis, according to the indices provided.
The handle of the gather layer is returned in *`DLLayerGather`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as its value.

The parameter *`indices`* defines the indices to be gathered from the
axis. The indices must be either of rank 0 or rank 1, i.e., a scalar or a
list. The indices input can be a layer handle (*`indices`*) or a tuple
of integers.
If *`indices`* is given as a tuple of integers, internally a constant
input layer is created.

The axis along which the gathering is performed is specified by the parameter
*`axis`*. *`axis`* can either be specified by a string
(*"width"*, *"height"*, *"depth"* or *"batch"*) or an
integer, where 0 corresponds to the batch size, 1 to depth, 2 to height and 3
to width. Negative values for *`axis`* indicate counting dimensions from
the back. The accepted range is [-4,3].

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md), each layer
of the created network must have a unique name.

**Gather semantics**

Given a 4-dimensional input tensor *`DLLayerInput`* of shape
(N, C, H, W) and an indices tensor or tuple,
the gather layer selects elements from the *`axis`* dimension indexed
by elements of *`indices`*.

If the indices are given as a tuple
$$(i_{0},...,i_{k})$$
and
*`axis`* $=a$, the output tensor is constructed by replacing dimension
$a$ with the indices dimensions, resulting in an output of shape
$$(d_{0},...,d_{a-1},k+1,d_{a+1},...,d_{r-1})$$

All index values in *`indices`* must be within the bounds
$[-s,s-1]$, where $s$ is the size of the *`axis`*
dimension. Negative indices are interpreted by adding $s$, i.e.,
*"index"* = *"index"*$+s$ if *"index"* < 0.

**Index Processing**

- **Adjusting Axis** —

  Negative values for *`axis`* are made non-negative by adding the
  number of dimensions r of the input tensor:
  $$\text{axis}\leftarrow\text{axis}+r\text{if axis}<0$$
- **Clamping Indices** —

  Negative values in *`indices`* are adjusted by adding the size s
  of the corresponding axis:
  $$\text{indices}[j]\leftarrow\text{indices}[j]+s\text{if indices}[j]<0$$

  All values in *`indices`* must satisfy
  $$0\le\text{indices}[j]<s$$
  Otherwise, an error will be raised.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying
  this layer in `outputs` (*"true"*) or not (*"false"*).

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerGather` can be set and retrieved using further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved using
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md).
Note, the operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) require a model created by [`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`DLLayerInput`*,*`indices`*) |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"axis"* (*`axis`*) |  | `x` |
| *"output_layer"* (*`DLLayerGather`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Feeding data input layer.

Default:
"DLLayerInput"

**`indices`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / HHandle)

Indices for the gather operation. This input can be a layer or
tuple of integers.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`axis`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / string)

Axis along which to gather.

Default:
0

Suggested values:
0, "batch", 1, "depth", 2, "height", 3, "width"

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

**`DLLayerGather`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Output layer.

## Module

Deep Learning Professional
