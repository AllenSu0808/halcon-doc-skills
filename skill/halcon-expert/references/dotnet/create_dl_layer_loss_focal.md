# CreateDlLayerLossFocal (Operator)

## Name

`CreateDlLayerLossFocal` — Create a focal loss layer.

## Signature

`static void HOperatorSet.CreateDlLayerLossFocal(HTuple DLLayerInput, HTuple DLLayerTarget, HTuple DLLayerWeights, HTuple DLLayerNormalization, HTuple layerName, HTuple lossWeight, HTuple gamma, HTuple classWeights, HTuple type, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerLossFocal)`

`HDlLayer HDlLayer.CreateDlLayerLossFocal(HDlLayer DLLayerTarget, HDlLayer DLLayerWeights, HDlLayer DLLayerNormalization, string layerName, HTuple lossWeight, HTuple gamma, HTuple classWeights, string type, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerLossFocal(HDlLayer DLLayerTarget, HDlLayer DLLayerWeights, HDlLayer DLLayerNormalization, string layerName, double lossWeight, double gamma, double classWeights, string type, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerLossFocal` creates a focal loss layer
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

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`lossWeight`* is a overall loss weight if there are
multiple losses in the network.

The parameter *`gamma`* is the exponent of the focal factor.

The parameter *`classWeights`* defines class specific weights. All
loss contributions of foreground samples of a class are weighted with
the given factor. The background samples are weighted by 1 - *`classWeights`*.
Typically, this is set to *1.0/(Number of samples of the class)*.
Note, the length of this array has to be either 1, then its broadcasted
to the number of classes, or it has to correspond to the number of classes.
The default value *[]* corresponds to a factor of *0.5* for
all classes.
Note, if the number of classes are changed on a network then the number of
class specific weights are also adapted and reset with the default value
*0.5* for each class.

The parameter *`type`* sets the focal loss options:

- ***"focal_binary"*:** —

  Focal loss.
- ***"sigmoid_focal_binary"*:** —

  Focal loss fused with sigmoid.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerLossFocal` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md).
Note, the operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) require a model created by
[`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"focal_type"* (*`type`*) |  | `x` |
| *"gamma"* (*`gamma`*) | `x` | `x` |
| *"input_layer"* (*`DLLayerInput`*, *`DLLayerTarget`*, *`DLLayerWeights`*, and/or *`DLLayerNormalization`*) |  | `x` |
| *"loss_weight"* (*`lossWeight`*) | `x` | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"output_layer"* (*`DLLayerLossFocal`*) |  | `x` |
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

Input layer.

**`DLLayerTarget`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Target layer.

**`DLLayerWeights`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Weights layer.

**`DLLayerNormalization`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Normalization layer.

Default:
[]

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`lossWeight`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Overall loss weight if there are multiple losses in the
network.

Default:
1.0

**`gamma`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Exponent of the focal factor.

Default:
2.0

**`classWeights`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Class specific weight.

Default:
[]

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Focal loss type.

Default:
"focal_binary"

List of values:
"focal_binary", "sigmoid_focal_binary"

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string*)

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`DLLayerLossFocal`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Focal loss layer.

## References

T. Lin, P. Goyal, R. Girshick, K. He and P. Dollar,
"Focal Loss for Dense Object Detection," in IEEE Transactions on Pattern
Analysis and Machine Intelligence, vol. 42, no. 2, pp. 318-327, 1 Feb. 2020,
doi: 10.1109/TPAMI.2018.2858826.

## Module

Deep Learning Professional
