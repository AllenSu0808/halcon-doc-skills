# CreateDlLayerSoftmax (Operator)

## Name

`CreateDlLayerSoftmax` — Create a softmax layer.

## Signature

`static void HOperatorSet.CreateDlLayerSoftmax(HTuple DLLayerInput, HTuple layerName, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerSoftMax)`

`HDlLayer HDlLayer.CreateDlLayerSoftmax(string layerName, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerSoftmax(string layerName, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerSoftmax` creates a softmax layer whose
handle is returned in *`DLLayerSoftMax`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The softmax layer applies the softmax function which is defined for each input
$x_{i}$ as follows:
$$Softmax(x_i) = \frac{\exp(x_i)}{\sum_{j=0}^{N-1} \exp(x_j)}$$ ![figure](../assets/19c685431d9ee439.svg)
where $N$ is the number of inputs. During training, the result of the
softmax function is transformed by a logarithm
function, such that the values are suitable as input to e.g., a cross
entropy loss layer.
This behavior can be changed by setting the generic parameter
*"output_mode"*, see below.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"output_mode"*:** —

  This parameter determines if and in which case the output is transformed
  by a logarithm function:

  - *"default"*: During inference, the result of the softmax
    function is returned as output while during training, the softmax is
    further transformed by a logarithm function.
  - *"no_log_training"*: During training the result of the
    softmax function is not transformed by a logarithm function.
  - *"log_inference"*: The logarithm of the softmax is
    calculated during inference in the same way as during training.

  Default:
   *"default"*.
- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerSoftmax` can be set and retrieved using
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
| *"output_layer"* (*`DLLayerSoftMax`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"output_mode"* |  | `x` |

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
"is_inference_output", "output_mode"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Generic input parameter values.

Default:
[]

Suggested values:
"default", "no_log_training", "log_inference", "true", "false"

**`DLLayerSoftMax`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Softmax layer.

## Module

Deep Learning Professional
