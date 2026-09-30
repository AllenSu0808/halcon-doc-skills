# create_dl_layer_permutation (Operator)

## Name

`create_dl_layer_permutation` — Create a permutation layer.

## Signature

`def create_dl_layer_permutation(dllayer_input: HHandle, layer_name: str, permutation: Sequence[int], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_permutation` creates a permutation layer
whose handle is returned in *`dllayer_permutation`*.

The parameter *`dllayer_input`* determines the feeding input layer
and expects the layer handle as value.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`permutation`* specifies the order in which the axes of
*`dllayer_input`* appear after permutation.

*`permutation`* accepts a list of strings or integers that lists the axes
in the desired output order.
For example, *["width", "height", "batch", "depth"]* leads to
swapping the depth and the batch axes.
Each axis must be unique and be taken from the set $[0,1,2,3]$ or
$[^{\prime}width^{\prime},^{\prime}height^{\prime},^{\prime}depth^{\prime},^{\prime}batch^{\prime}]$.

Using a CPU device, for some values of *`permutation`* the internal code
can not be optimized which can lead to an increased runtime. In this case,
the layer parameter *"fall_back_to_baseline"* is set to
*"true"*.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"axes_format"*:** —

  Compatibility parameter that determines whether the specified *`permutation`*
  is given in WHCN format (default) or in NCHW format.
  The parameter changes how the specified axes are interpreted.
  For example, with permutation *[0, 1, 3, 2]* and *"axes_format"*
  *"nchw"*, the height and width dimensions will be swapped.
  If *"axes_format"* is set to *"whcn"* or left unspecified,
  the required permutation to get the same effect is *[1, 0, 2, 3]*.
  Instead of indices, strings can also be used to specify the permutation.

  List of values:
   *"nchw"*, *"whcn"*

  Default:
   *"whcn"*
- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying
  this layer in `outputs` (*"true"*) or not
  (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`create_dl_layer_permutation` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note,
the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"fall_back_to_baseline"* |  | `x` |
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"permutation"* (*`permutation`*) |  | `x` |
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

Feeding layer.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`permutation`** (input_control)  number-array `→` Sequence[int]

Order of the permuted axes.

Default:
["batch","depth","height","width"]

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"axes_format", "is_inference_output"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false", "nchw", "whcn"

**`dllayer_permutation`** (output_control)  dl_layer `→` HHandle

Permutation layer.

## Example (HDevelop)

```
* Swap the batch and depth axes with a permutation layer.
create_dl_layer_input ('input_a', [1, 1, 4], ['input_type', 'const_val'], \
                       ['constant', 1.0], DLLayerInputA)
create_dl_layer_input ('input_b', [1, 1, 4], ['input_type', 'const_val'], \
                       ['constant', 2.0], DLLayerInputB)
create_dl_layer_concat ([DLLayerInputA, DLLayerInputB], 'concat', 'batch', \
                        [], [], DLLayerConcat)
create_dl_layer_permutation (DLLayerConcat, 'permute', ['width','height','batch','depth'], \
                             [], [], DLLayerPermute)
create_dl_layer_depth_max (DLLayerPermute, 'depth_max', 'value', \
                           [], [], _, DLLayerDepthMaxValue)
create_dl_model (DLLayerDepthMaxValue, DLModel)
* The expected output values in DLResultBatch.depth_max are [2.0,2.0,2.0,2.0]
query_available_dl_devices (['runtime'], ['cpu'], DLDeviceHandles)
set_dl_model_param (DLModel, 'device', DLDeviceHandles[0])
apply_dl_model (DLModel, dict{}, [], DLResultBatch)
```

## Possible Predecessors

`create_dl_layer_input`,
`create_dl_layer_concat`,
`create_dl_layer_reshape`

## Possible Successors

`create_dl_layer_convolution`,
`create_dl_layer_dense`,
`create_dl_layer_reshape`

## See also

`create_dl_layer_reshape`

## Module

Deep Learning Professional
