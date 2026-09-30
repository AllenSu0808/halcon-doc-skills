# create_dl_layer_loss_huber (Operator)

## Name

`create_dl_layer_loss_huber` — Create a Huber loss layer.

## Signature

`create_dl_layer_loss_huber( : : DLLayerInput, DLLayerTarget, DLLayerWeights, DLLayerNormalization, LayerName, LossWeight, Beta, GenParamName, GenParamValue : DLLayerLossHuber)`

## Description

The operator `create_dl_layer_loss_huber` creates a Huber loss layer
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

The parameter *`LossWeight`* determines the scalar weight factor
$\alpha$.

The parameter *`Beta`* sets the value for $\beta$ in the
formula.
If *`Beta`* is set to *0*, the Huber loss is equal to an L1-loss.

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
`create_dl_layer_loss_huber` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'beta'* (*`Beta`*) | `x` | `x` |
| *'input_layer'* (*`DLLayerInput`*, *`DLLayerTarget`*, *`DLLayerWeights`*, and/or *`DLLayerNormalization`*) |  | `x` |
| *'loss_weight'* (*`LossWeight`*) | `x` | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerLossHuber`*) |  | `x` |
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

**`LossWeight`** (input_control)  number `→`  (real)

Scalar weight factor.

Default:
1.0

**`Beta`** (input_control)  number `→`  (real)

Beta value in the loss-defining formula.

Default:
1.1

Restriction:
`Beta >= 0`

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

**`DLLayerLossHuber`** (output_control)  dl_layer `→`  (handle)

Huber loss layer.

## Module

Deep Learning Professional
