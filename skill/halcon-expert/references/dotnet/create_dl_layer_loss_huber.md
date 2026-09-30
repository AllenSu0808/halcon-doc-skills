# CreateDlLayerLossHuber (Operator)

## Name

`CreateDlLayerLossHuber` — Create a Huber loss layer.

## Signature

`static void HOperatorSet.CreateDlLayerLossHuber(HTuple DLLayerInput, HTuple DLLayerTarget, HTuple DLLayerWeights, HTuple DLLayerNormalization, HTuple layerName, HTuple lossWeight, HTuple beta, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerLossHuber)`

`HDlLayer HDlLayer.CreateDlLayerLossHuber(HDlLayer DLLayerTarget, HDlLayer DLLayerWeights, HDlLayer DLLayerNormalization, string layerName, double lossWeight, double beta, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerLossHuber(HDlLayer DLLayerTarget, HDlLayer DLLayerWeights, HDlLayer DLLayerNormalization, string layerName, double lossWeight, double beta, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerLossHuber` creates a Huber loss layer
whose handle is returned in *`DLLayerLossHuber`*.
The Huber loss is defined by
$$L_{Huber}(x,t,w,n) := \frac{\alpha}{n}\sum_{i=0}^{N-1} w_i l(x_i - t_i),\quad with\\ l(y) := \begin{cases} 0.5 y^2 / \beta & \text{if } |y| < \beta \\ |y| - 0.5 \beta & \text{else.} \\ \end{cases}$$ ![figure](../assets/e38e3d33c8726ec5.svg)

This layer expects multiple layers as input:

- *`DLLayerInput`*: Specifies $x$
  (usually a softmax layer).
- *`DLLayerTarget`*: Specifies the
  targets $t$.
- *`DLLayerWeights`*: Specifies the
  weights $w$.

The underlying data tensors are assumed to be of the same shape with
a total number of $N$ elements.

The parameter *`DLLayerNormalization`* can be used to determine the
normalization factor $n$. If *`DLLayerNormalization`* is set to an
empty tuple, the sum over all weights is used for the normalization
$n$.

The parameter *`lossWeight`* determines the scalar weight factor
$\alpha$.

The parameter *`beta`* sets the value for $\beta$ in the
formula.
If *`beta`* is set to *0*, the Huber loss is equal to an L1-loss.

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
`CreateDlLayerLossHuber` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md).
Note, the operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) require a model created by
[`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"beta"* (*`beta`*) | `x` | `x` |
| *"input_layer"* (*`DLLayerInput`*, *`DLLayerTarget`*, *`DLLayerWeights`*, and/or *`DLLayerNormalization`*) |  | `x` |
| *"loss_weight"* (*`lossWeight`*) | `x` | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"output_layer"* (*`DLLayerLossHuber`*) |  | `x` |
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

**`lossWeight`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Scalar weight factor.

Default:
1.0

**`beta`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Beta value in the loss-defining formula.

Default:
1.1

Restriction:
`Beta >= 0`

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

**`DLLayerLossHuber`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Huber loss layer.

## Module

Deep Learning Professional
