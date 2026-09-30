# create_dl_layer_gather (Operator)

## Name

`create_dl_layer_gather` — Create a gather layer.

## Signature

`def create_dl_layer_gather(dllayer_input: HHandle, indices: MaybeSequence[Union[int, HHandle]], layer_name: str, axis: Union[int, str], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_gather` creates a gather layer that
extracts slices from the input tensor *`dllayer_input`* along a
specified axis, according to the indices provided.
The handle of the gather layer is returned in *`dllayer_gather`*.

The parameter *`dllayer_input`* determines the feeding input layer and
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

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md), each layer
of the created network must have a unique name.

**Gather semantics**

Given a 4-dimensional input tensor *`dllayer_input`* of shape
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

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying
  this layer in `outputs` (*"true"*) or not (*"false"*).

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*

Certain parameters of layers created using this operator
`create_dl_layer_gather` can be set and retrieved using further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved using
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`dllayer_input`*,*`indices`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"axis"* (*`axis`*) |  | `x` |
| *"output_layer"* (*`dllayer_gather`*) |  | `x` |
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

**`dllayer_input`** (input_control)  dl_layer `→` HHandle

Feeding data input layer.

Default:
"DLLayerInput"

**`indices`** (input_control)  number(-array) `→` MaybeSequence[Union[int, HHandle]]

Indices for the gather operation. This input can be a layer or
tuple of integers.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`axis`** (input_control)  number `→` Union[int, str]

Axis along which to gather.

Default:
0

Suggested values:
0, "batch", 1, "depth", 2, "height", 3, "width"

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

**`dllayer_gather`** (output_control)  dl_layer `→` HHandle

Output layer.

## Module

Deep Learning Professional
