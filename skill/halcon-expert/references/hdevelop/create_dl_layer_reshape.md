# create_dl_layer_reshape (Operator)

## Name

`create_dl_layer_reshape` — Create a reshape layer.

## Signature

`create_dl_layer_reshape( : : DLLayerInput, LayerName, Shape, GenParamName, GenParamValue : DLLayerReshape)`

## Description

The operator `create_dl_layer_reshape` creates a reshape layer whose
handle is returned in *`DLLayerReshape`*.

The parameter *`DLLayerInput`* determines the feeding input layer
and expects the layer handle as value.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`Shape`* determines the output shape, into which the
input data is converted.

The value of *`Shape`* has to be given in the form [`width`,
`height`, `depth`, `batch_size`], where the fourth value
for the batch size is optional (see below).
The overall size of the data has to remain constant, i.e.,
`width_out` * `height_out` * `depth_out` * `batch_size_out`
=
`width_in` * `height_in` * `depth_in` * `batch_size_in`.

The following options are available for setting the values of *`Shape`*:

- Setting a value for each of the four dimensions,
- One or several values are set to *0* in order to keep
  the value of the input dimension,
- By setting a maximum of one value to *-1*, this value will be
  determined automatically. It will be calculated in a way that the
  overall size remains constant. Note that this is only possible if the
  computed value is an integer.

For a model that was created using [`create_dl_model`](create_dl_model.md) the model's batch
size should always be settable with [`set_dl_model_param`](set_dl_model_param.md).
Hence, either the output batch size of the reshape layer equals the batch
size of the model (batch size in *`Shape`* set to *0*), or at
least one reshape dimension should be calculated automatically (one value in
*`Shape`* set to *-1*).

If the batch size is specified and it is not set to *0*, at least one
dimension of *`Shape`* must be set to *-1*. This is necessary,
because for a model created with [`create_dl_model`](create_dl_model.md), the model's batch
size should always be settable with [`set_dl_model_param`](set_dl_model_param.md). Hence,
either the output batch size of the reshape layer equals the batch size of
the model (batch size in *`Shape`* set to *0*), or at least one
reshape dimension should be calculated automatically (one value in
*`Shape`* set to *-1*).
In case the batch size is not specified it is set to *0*, which leads
to an output batch size equal to the input one.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*

Certain parameters of layers created using this operator
`create_dl_layer_reshape` can be set and retrieved using
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
| *'output_depth'* (*`Shape`*) |  | `x` |
| *'output_height'* (*`Shape`*) |  | `x` |
| *'output_layer'* (*`DLLayerReshape`*) |  | `x` |
| *'output_width'* (*`Shape`*) |  | `x` |
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

**`Shape`** (input_control)  number-array `→`  (integer)

Shape of the output graph layer data.

Default:
[224,224,3]

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

**`DLLayerReshape`** (output_control)  dl_layer `→`  (handle)

Reshape layer.

## Example (HDevelop)

```
* Minimal example for reshape-layer.
create_dl_layer_input ('input', [64, 32, 10], [], [], DLLayerInput)
create_dl_layer_reshape (DLLayerInput, 'reshape_wh', [32, 64, 0], [], [], \
                         DLLayerReshapeWH)
create_dl_layer_reshape (DLLayerInput, 'reshape_bs', [64, 32, 1, -1], [], \
                         [], DLLayerReshapeBS)
* DLLayerReshapeBS has batch size 10 and depth 1.
get_dl_layer_param (DLLayerReshapeBS, 'shape', ShapeReshapeBS)
* Create a model and change the batch-size.
create_dl_model (DLLayerReshapeBS, DLModel)
set_dl_model_param (DLModel, 'batch_size', 2)
* DLLayerReshapeBS has batch size 20 now.
get_dl_model_layer_param (DLModel, 'reshape_bs', 'shape', ShapeReshapeBS)
```

## Possible Predecessors

`create_dl_layer_input`,
`create_dl_layer_concat`

## Possible Successors

`create_dl_layer_convolution`,
`create_dl_layer_dense`

## Module

Deep Learning Professional
