# create_dl_layer_identity (Operator)

## Name

`create_dl_layer_identity` — Create an identity layer.

## Signature

`def create_dl_layer_identity(dllayer_input: HHandle, layer_name: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_identity` creates an identity layer
whose handle is returned in *`dllayer_identity`*.

The parameter *`dllayer_input`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

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
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_identity`*) |  | `x` |
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

**`dllayer_identity`** (output_control)  dl_layer `→` HHandle

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
