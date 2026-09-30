# create_dl_layer_identity (Operator)

## Name

`create_dl_layer_identity` — Create an identity layer.

## Signature

`create_dl_layer_identity( : : DLLayerInput, LayerName, GenParamName, GenParamValue : DLLayerIdentity)`

## Description

The operator `create_dl_layer_identity` creates an identity layer
whose handle is returned in *`DLLayerIdentity`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*

Certain parameters of layers created using this operator
`create_dl_layer_identity` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'input_layer'* (*`DLLayerInput`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerIdentity`*) |  | `x` |
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

Feeding layer.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

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

**`DLLayerIdentity`** (output_control)  dl_layer `→`  (handle)

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

`create_dl_layer_elementwise`,
`create_dl_layer_concat`

## Module

Deep Learning Professional
