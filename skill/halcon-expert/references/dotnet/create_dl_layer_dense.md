# CreateDlLayerDense (Operator)

## Name

`CreateDlLayerDense` — Create a dense layer.

## Signature

`static void HOperatorSet.CreateDlLayerDense(HTuple DLLayerInput, HTuple layerName, HTuple numOut, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerDense)`

`HDlLayer HDlLayer.CreateDlLayerDense(string layerName, int numOut, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerDense(string layerName, int numOut, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerDense` creates a dense or fully connected
layer (sometimes also called gemm) with *`numOut`* output neurons whose
handle is returned in *`DLLayerDense`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"bias_filler"*:** —

  See [`CreateDlLayerConvolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *"xavier"*, *"msra"*,
  *"const"*.

  Default:
   *"const"*
- ***"bias_filler_const_val"*:** —

  Constant value if
  *"bias_filler"* = *"const"*.

  Default:
   *0*
- ***"bias_filler_variance_norm"*:** —

  See [`CreateDlLayerConvolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *"norm_out"*, *"norm_in"*,
  *"norm_average"*, or constant value (in combination with
  *"bias_filler"* = *"msra"*).

  Default:
   *"norm_in"*
- ***"bias_term"*:** —

  Determines whether the created dense
  layer has a bias term (*"true"*) or not (*"false"*).

  Default:
   *"true"*
- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"learning_rate_multiplier"*:** —

  Multiplier for the learning
  rate for this layer that is used during training.
  If *"learning_rate_multiplier"* is set to *0.0*, the layer is
  skipped during training.

  Default:
   *1.0*
- ***"learning_rate_multiplier_bias"*:** —

  Multiplier for the
  learning rate of the bias term. The total bias learning rate is the
  product of *"learning_rate_multiplier_bias"* and
  *"learning_rate_multiplier"*.

  Default:
   *1.0*
- ***"weight_filler"*:** —

  See [`CreateDlLayerConvolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *"xavier"*, *"msra"*,
  *"const"*.

  Default:
   *"xavier"*
- ***"weight_filler_const_val"*:** —

  See [`CreateDlLayerConvolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  Default:
   *0.5*
- ***"weight_filler_variance_norm"*:** —

  See [`CreateDlLayerConvolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *"norm_in"*, *"norm_out"*,
  *"norm_average"*, or constant value (in combination with
  *"bias_filler"* = *"msra"*).

  Default:
   *"norm_in"*

Certain parameters of layers created using
`CreateDlLayerDense` can be set and retrieved using
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
| *"neurons_in"* |  | `x` |
| *"neurons_out"* (*`numOut`*) |  | `x` |
| *"output_layer"* (*`DLLayerDense`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"bias_filler"* | `x` | `x` |
| *"bias_filler_const_val"* | `x` | `x` |
| *"bias_filler_variance_norm"* | `x` | `x` |
| *"bias_term"* |  | `x` |
| *"is_inference_output"* | `x` | `x` |
| *"learning_rate_multiplier"* | `x` | `x` |
| *"learning_rate_multiplier_bias"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"weight_filler"* | `x` | `x` |
| *"weight_filler_const_val"* | `x` | `x` |
| *"weight_filler_variance_norm"* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Feeding layer.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`numOut`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Number of output neurons.

Default:
100

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
"bias_filler", "bias_filler_const_val", "bias_filler_variance_norm", "bias_term", "is_inference_output", "learning_rate_multiplier", "learning_rate_multiplier_bias", "weight_filler", "weight_filler_const_val", "weight_filler_variance_norm"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Generic input parameter values.

Default:
[]

Suggested values:
"xavier", "msra", "const", "nearest_neighbor", "bilinear", "norm_in", "norm_out", "norm_average", "true", "false", 1.0, 0.9, 0.0

**`DLLayerDense`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Dense layer.

## Module

Deep Learning Professional
