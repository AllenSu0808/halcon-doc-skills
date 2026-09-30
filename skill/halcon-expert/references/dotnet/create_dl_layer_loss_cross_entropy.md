# CreateDlLayerLossCrossEntropy (Operator)

## Name

`CreateDlLayerLossCrossEntropy` — Create a cross entropy loss layer.

## Signature

`static void HOperatorSet.CreateDlLayerLossCrossEntropy(HTuple DLLayerInput, HTuple DLLayerTarget, HTuple DLLayerWeights, HTuple layerName, HTuple lossWeight, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerLossCrossEntropy)`

`HDlLayer HDlLayer.CreateDlLayerLossCrossEntropy(HDlLayer DLLayerTarget, HDlLayer DLLayerWeights, string layerName, double lossWeight, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerLossCrossEntropy(HDlLayer DLLayerTarget, HDlLayer DLLayerWeights, string layerName, double lossWeight, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerLossCrossEntropy` creates a cross
entropy loss layer whose handle is returned in
*`DLLayerLossCrossEntropy`*.
This layer computes the two dimensional cross entropy loss on the input
(provided by *`DLLayerInput`*) given the corresponding target
(provided by *`DLLayerTarget`*) and weight
(provided by *`DLLayerWeights`*).

Cross entropy is commonly used to measure the similarity between two
vectors.

- ***Example:*** —

  Illustrative example, where we have a
  pixel-level classification problem with three classes.

  The input vector for a single pixel is
  $\mathbf{x}=[0.7,0.1,0.2]$
  (e.g., the output of a softmax layer) which means that the predicted
  value (e.g., probability) is 0.7 for the class at index 0, 0.1 for the class
  at index 1 and 0.2 for the class at index 2.

  The target vector is
  $\mathbf{t}=[1.0,0.0,0.0]$
  with a probability of 1.0 for the actual class and 0.0 else.
  Entropy is calculated by the dot product of these two vectors. Since the
  target vector has only one non-zero entry, it can be given by the
  index of the actual class instead of a vector, in this case
  $t=0$.

  The cross entropy is then simply the value of the input vector at the target
  class index, hence
  $\mathbf{x}[t]=0.7$.
  Using this simplification, the cross entropy loss function over an input
  image can be defined by
  $$L_{cross_entropy}(x,t,w) := -\frac{1}{W} \sum_{i=0}^{N-1} w_i \cdot x_i [t_i],$$ ![figure](../assets/649b3668521d540d.svg)
  where the input $\mathbf{x}$ consists of one prediction vector
  $\mathbf{x}_{i}$ for each pixel, the target $\mathbf{t}$
  and weight $\mathbf{w}$ consist of one value $t_{i}$ and
  $w_{i}$ for each input pixel, $N$ is the number of pixels
  and
  $W = \sum_{i=0}^{N-1} w_i$ ![figure](../assets/6b08aa1553680a31.svg)
  is the sum over all weights.

Hence, this layer expects multiple incoming layers:

- *`DLLayerInput`*: Specifies the
  prediction (e.g., a softmax layer, commonly with logarithmized results).
- *`DLLayerTarget`*: Specifies the
  target sequences (originating from the ground truth information).
- *`DLLayerWeights`*: Specifies the weight sequences. This parameter
  is optional. If an empty tuple *[]* is passed for all values the
  weighting factor *1.0* is used.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`lossWeight`* determines the scalar weight factor with
which the loss, calculated in this layer, is multiplied.
This parameter can be used to specify the contribution of the cross entropy
loss to the overall network loss in case multiple loss layers are used.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerLossCrossEntropy` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md).
Note, the operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) require a model created by
[`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`DLLayerInput`*, *`DLLayerTarget`*, and/or *`DLLayerWeights`*) |  | `x` |
| *"loss_weight"* (*`lossWeight`*) | `x` | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"output_layer"* (*`DLLayerLossCrossEntropy`*) |  | `x` |
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

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`lossWeight`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Overall loss weight if there are multiple losses
in the network.

Default:
1.0

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

**`DLLayerLossCrossEntropy`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Cross entropy loss layer.

## Module

Deep Learning Professional
