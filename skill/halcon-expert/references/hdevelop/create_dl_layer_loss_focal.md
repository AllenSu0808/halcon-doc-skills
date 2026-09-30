# create_dl_layer_loss_focal (Operator)

## Name

`create_dl_layer_loss_focal` — Create a focal loss layer.

## Signature

`create_dl_layer_loss_focal( : : DLLayerInput, DLLayerTarget, DLLayerWeights, DLLayerNormalization, LayerName, LossWeight, Gamma, ClassWeights, Type, GenParamName, GenParamValue : DLLayerLossFocal)`

## Description

The operator `create_dl_layer_loss_focal` creates a focal loss layer
whose handle is returned in *`DLLayerLossFocal`*.
See the reference cited below for further
information about its definition and parameter meanings.

This layer expects multiple layers as input:

- *`DLLayerInput`*: Specifies the prediction (e.g., a
  sigmoid or softmax layer).
- *`DLLayerTarget`*: Specifies the target sequences
  (originating from the ground truth information).
- *`DLLayerWeights`*: Specifies the weight sequences. This parameter
  is optional. If an empty tuple *[]* is passed for all values the
  weighting factor *1.0* is used.
- *`DLLayerNormalization`*: Specifies the factor to normalize the
  loss. This parameter is optional, it
  can be given by the layer handle as value or ignored handing over an empty
  tuple *[]*.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`LossWeight`* is a overall loss weight if there are
multiple losses in the network.

The parameter *`Gamma`* is the exponent of the focal factor.

The parameter *`ClassWeights`* defines class specific weights. All
loss contributions of foreground samples of a class are weighted with
the given factor. The background samples are weighted by 1 - *`ClassWeights`*.
Typically, this is set to *1.0/(Number of samples of the class)*.
Note, the length of this array has to be either 1, then its broadcasted
to the number of classes, or it has to correspond to the number of classes.
The default value *[]* corresponds to a factor of *0.5* for
all classes.
Note, if the number of classes are changed on a network then the number of
class specific weights are also adapted and reset with the default value
*0.5* for each class.

The parameter *`Type`* sets the focal loss options:

- ***'focal_binary'*:** —

  Focal loss.
- ***'sigmoid_focal_binary'*:** —

  Focal loss fused with sigmoid.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*

Certain parameters of layers created using this operator
`create_dl_layer_loss_focal` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'focal_type'* (*`Type`*) |  | `x` |
| *'gamma'* (*`Gamma`*) | `x` | `x` |
| *'input_layer'* (*`DLLayerInput`*, *`DLLayerTarget`*, *`DLLayerWeights`*, and/or *`DLLayerNormalization`*) |  | `x` |
| *'loss_weight'* (*`LossWeight`*) | `x` | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerLossFocal`*) |  | `x` |
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

Input layer.

**`DLLayerTarget`** (input_control)  dl_layer `→`  (handle)

Target layer.

**`DLLayerWeights`** (input_control)  dl_layer `→`  (handle)

Weights layer.

**`DLLayerNormalization`** (input_control)  dl_layer `→`  (handle)

Normalization layer.

Default:
[]

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`LossWeight`** (input_control)  number `→`  (real / integer)

Overall loss weight if there are multiple losses in the
network.

Default:
1.0

**`Gamma`** (input_control)  number `→`  (real / integer)

Exponent of the focal factor.

Default:
2.0

**`ClassWeights`** (input_control)  number(-array) `→`  (real / integer)

Class specific weight.

Default:
[]

**`Type`** (input_control)  string `→`  (string)

Focal loss type.

Default:
'focal_binary'

List of values:
'focal_binary', 'sigmoid_focal_binary'

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'is_inference_output'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string)

Generic input parameter values.

Default:
[]

Suggested values:
'true', 'false'

**`DLLayerLossFocal`** (output_control)  dl_layer `→`  (handle)

Focal loss layer.

## References

T. Lin, P. Goyal, R. Girshick, K. He and P. Dollar,
"Focal Loss for Dense Object Detection," in IEEE Transactions on Pattern
Analysis and Machine Intelligence, vol. 42, no. 2, pp. 318-327, 1 Feb. 2020,
doi: 10.1109/TPAMI.2018.2858826.

## Module

Deep Learning Professional
