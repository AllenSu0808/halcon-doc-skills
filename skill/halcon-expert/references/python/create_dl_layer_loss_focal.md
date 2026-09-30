# create_dl_layer_loss_focal (Operator)

## Name

`create_dl_layer_loss_focal` — Create a focal loss layer.

## Signature

`def create_dl_layer_loss_focal(dllayer_input: HHandle, dllayer_target: HHandle, dllayer_weights: HHandle, dllayer_normalization: HHandle, layer_name: str, loss_weight: Union[int, float], gamma: Union[int, float], class_weights: MaybeSequence[Union[int, float]], type: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[str]) -> HHandle`

## Description

The operator `create_dl_layer_loss_focal` creates a focal loss layer
whose handle is returned in *`dllayer_loss_focal`*.
See the reference cited below for further
information about its definition and parameter meanings.

This layer expects multiple layers as input:

- *`dllayer_input`*: Specifies the prediction (e.g., a
  sigmoid or softmax layer).
- *`dllayer_target`*: Specifies the target sequences
  (originating from the ground truth information).
- *`dllayer_weights`*: Specifies the weight sequences. This parameter
  is optional. If an empty tuple *[]* is passed for all values the
  weighting factor *1.0* is used.
- *`dllayer_normalization`*: Specifies the factor to normalize the
  loss. This parameter is optional, it
  can be given by the layer handle as value or ignored handing over an empty
  tuple *[]*.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`loss_weight`* is a overall loss weight if there are
multiple losses in the network.

The parameter *`gamma`* is the exponent of the focal factor.

The parameter *`class_weights`* defines class specific weights. All
loss contributions of foreground samples of a class are weighted with
the given factor. The background samples are weighted by 1 - *`class_weights`*.
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

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

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
| *"focal_type"* (*`type`*) |  | `x` |
| *"gamma"* (*`gamma`*) | `x` | `x` |
| *"input_layer"* (*`dllayer_input`*, *`dllayer_target`*, *`dllayer_weights`*, and/or *`dllayer_normalization`*) |  | `x` |
| *"loss_weight"* (*`loss_weight`*) | `x` | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_loss_focal`*) |  | `x` |
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

Input layer.

**`dllayer_target`** (input_control)  dl_layer `→` HHandle

Target layer.

**`dllayer_weights`** (input_control)  dl_layer `→` HHandle

Weights layer.

**`dllayer_normalization`** (input_control)  dl_layer `→` HHandle

Normalization layer.

Default:
[]

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`loss_weight`** (input_control)  number `→` Union[int, float]

Overall loss weight if there are multiple losses in the
network.

Default:
1.0

**`gamma`** (input_control)  number `→` Union[int, float]

Exponent of the focal factor.

Default:
2.0

**`class_weights`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Class specific weight.

Default:
[]

**`type`** (input_control)  string `→` str

Focal loss type.

Default:
"focal_binary"

List of values:
"focal_binary", "sigmoid_focal_binary"

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[str]

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`dllayer_loss_focal`** (output_control)  dl_layer `→` HHandle

Focal loss layer.

## References

T. Lin, P. Goyal, R. Girshick, K. He and P. Dollar,
"Focal Loss for Dense Object Detection," in IEEE Transactions on Pattern
Analysis and Machine Intelligence, vol. 42, no. 2, pp. 318-327, 1 Feb. 2020,
doi: 10.1109/TPAMI.2018.2858826.

## Module

Deep Learning Professional
