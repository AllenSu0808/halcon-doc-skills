# CreateDlLayerPermutation (Operator)

## Name

`CreateDlLayerPermutation` — Create a permutation layer.

## Signature

`static void HOperatorSet.CreateDlLayerPermutation(HTuple DLLayerInput, HTuple layerName, HTuple permutation, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerPermutation)`

`HDlLayer HDlLayer.CreateDlLayerPermutation(string layerName, HTuple permutation, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerPermutation(string layerName, HTuple permutation, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerPermutation` creates a permutation layer
whose handle is returned in *`DLLayerPermutation`*.

The parameter *`DLLayerInput`* determines the feeding input layer
and expects the layer handle as value.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`permutation`* specifies the order in which the axes of
*`DLLayerInput`* appear after permutation.

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

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

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

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying
  this layer in `outputs` (*"true"*) or not
  (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerPermutation` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md). Note,
the operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) require a model created by
[`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"fall_back_to_baseline"* |  | `x` |
| *"input_layer"* (*`DLLayerInput`*) |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
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

**`DLLayerInput`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Feeding layer.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`permutation`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long)

Order of the permuted axes.

Default:
["batch","depth","height","width"]

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
"axes_format", "is_inference_output"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false", "nchw", "whcn"

**`DLLayerPermutation`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

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

`CreateDlLayerInput`,
`CreateDlLayerConcat`,
`CreateDlLayerReshape`

## Possible Successors

`CreateDlLayerConvolution`,
`CreateDlLayerDense`,
`CreateDlLayerReshape`

## See also

`CreateDlLayerReshape`

## Module

Deep Learning Professional
