# CreateDlLayerIdentity (Operator)

## Name

`CreateDlLayerIdentity` — Create an identity layer.

## Signature

`static void HOperatorSet.CreateDlLayerIdentity(HTuple DLLayerInput, HTuple layerName, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerIdentity)`

`HDlLayer HDlLayer.CreateDlLayerIdentity(string layerName, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerIdentity(string layerName, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerIdentity` creates an identity layer
whose handle is returned in *`DLLayerIdentity`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerIdentity` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md). Note, the
operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and [`GetDlModelLayerParam`](get_dl_model_layer_param.md)
require a model created by [`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`DLLayerInput`*) |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"output_layer"* (*`DLLayerIdentity`*) |  | `x` |
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

**`DLLayerIdentity`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Identity layer.

## Example (HDevelop)

```
* Create a model that concatinates the output of a convolution layer.
create_dl_layer_input ('input', [10,10,3], [], [], DLLayerInput)
create_dl_layer_convolution (DLLayerInput, 'conv', 3, 1, 1, 8, 1, 'none', \
                            'none', [], [], DLLayerConvolution)
* Using the same layer multiple times as input does not work, so make a copy.
create_dl_layer_identity (DLLayerConvolution, 'conv_copy', [], [], \
                          DLLayerIdentity)
create_dl_layer_concat ([DLLayerConvolution, DLLayerIdentity], 'concat', \
                        'depth', [], [], DLLayerConcat)
create_dl_model (DLLayerConcat, DLModelHandle)
```

## Possible Successors

`CreateDlLayerElementwise`,
`CreateDlLayerConcat`

## Module

Deep Learning Professional
