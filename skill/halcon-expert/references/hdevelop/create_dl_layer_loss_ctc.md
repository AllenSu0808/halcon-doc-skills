# create_dl_layer_loss_ctc (Operator)

## Name

`create_dl_layer_loss_ctc` — Create a CTC loss layer.

## Signature

`create_dl_layer_loss_ctc( : : DLLayerInput, DLLayerInputLengths, DLLayerTarget, DLLayerTargetLengths, LayerName, GenParamName, GenParamValue : DLLayerLossCTC)`

## Description

The operator `create_dl_layer_loss_ctc` creates a Connectionist
Temporal Classification (CTC) loss layer whose handle is returned in
*`DLLayerLossCTC`*.
See the reference cited below for information about the CTC loss.

With this loss layer it is possible to train sequence to sequence models
(Seq2Seq). E.g., it can be used to train a model that is able to read text in
an image. In order to do so, the sequences are compared, thus the determined
network prediction *`DLLayerInput`* with sequence length
*`DLLayerInputLengths`* to the given *`DLLayerTarget`* with sequence
length *`DLLayerTargetLengths`*.

The following variables are important to understand the input shapes:

- *T:* Maximum input sequence length
  (i.e., `width` of *`DLLayerInput`*)
- *S:* Maximum output sequence length
  (i.e., `width` of *`DLLayerTarget`*)
- *C:* Number of classes including 0 as the blank class ID
  (i.e., `depth` of *`DLLayerInput`*)

This layer expects multiple layers as input:

- *`DLLayerInput`*: Specifies the network prediction.

  Shape: [*T*,1,*C*]
- *`DLLayerInputLengths`*: Specifies the input
  sequence length of each item in the batch.

  Shape: [1,1,1]
- *`DLLayerTarget`*: Specifies the target
  sequences.

  Shape: [*S*,1,1]
- *`DLLayerTargetLengths`*: Input layer which specifies the target
  sequence length of each item in the batch.

  Shape: [1,1,1]

The parameter *`LayerName`* sets an individual layer name. Note that if
creating a model using [`create_dl_model`](create_dl_model.md) each layer of the created
network must have a unique name.

The CTC loss is typically applied in a CNN as follows. The input sequence is
expected to be encoded in some CNN layer with the output shape
[`width`: *T*, `height`: 1, `depth`: *C*].
Typically the end of a large fully convolutional classifier is pooled in
`height` down to 1 with an average pooling layer.
It is important that the last layer is wide enough to hold enough information.
In order to obtain the sequence prediction in the output `depth` a 1x1
convolutional layer is added after the pooling with the number of
kernels set to *C*.
In this use case the CTC loss obtains this convolutional layer as input layer
*`DLLayerInput`*. The `width` of the input layer determines the
maximum output sequence of the model.

The CTC loss can be applied to a batch of input items with differing input and
target sequence lengths. *T* and *S* are the maximum lengths.
In *`DLLayerInputLengths`* and *`DLLayerTargetLengths`* the
individual length of each item in a batch needs to be specified.
Note that each individual loss within the batch is first normalized by dividing
it by its corresponding target length. The final output loss is then computed as
the mean of these normalized values across the entire batch.

- **Restrictions** —
  - A model containing this layer cannot be trained on a CPU.
  - A model containing this layer cannot be trained with a
    *'batch_size_multiplier'* != 1.0.
  - The input layer *`DLLayerInput`* must not be a softmax layer.
    The softmax calculation is done internally in this layer. For
    inference, there should be an extra softmax layer connected to the
    *`DLLayerInput`* (see [`create_dl_layer_softmax`](create_dl_layer_softmax.md)).

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*
- ***'zero_infinity'*:** —

  Determines whether infinite loss values are set to zero in order to
  stabilize the training. If set to *'true'*, the loss values and
  gradients of samples that would yield an infinite loss are set to zero.

  List of values:
   *'true'*, *'false'*

  Default:
   *'false'*
- ***'loss_weight'*:** —

  Determines the scalar weight factor with which the loss, calculated in
  this layer, is multiplied. This parameter can be used to specify the
  contribution of the CTC loss to the overall network loss in
  case multiple loss layers are used.

  Default:
   *1.0*

Certain parameters of layers created using this operator
`create_dl_layer_loss_ctc` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'input_layer'* (*`DLLayerInput`*, *`DLLayerInputLengths`*, *`DLLayerTarget`*, and/or *`DLLayerTargetLengths`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerLossCTC`*) |  | `x` |
| *'shape'* |  | `x` |
| *'type'* |  | `x` |
| *'zero_infinity'* | `x` | `x` |
| *'loss_weight'* | `x` | `x` |

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

Input layer with network predictions.

**`DLLayerInputLengths`** (input_control)  dl_layer `→`  (handle)

Input layer which specifies the input sequence length
of each item in the batch.

**`DLLayerTarget`** (input_control)  dl_layer `→`  (handle)

Input layer which specifies the target sequences. If
the input dimensions of the CNN are changed the width
of this layer is automatically resized to the same
width as the *`DLLayerInput`* layer.

**`DLLayerTargetLengths`** (input_control)  dl_layer `→`  (handle)

Input layer which specifies the target sequence length
of each item in the batch.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'is_inference_output', 'loss_weight', 'zero_infinity'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
'true', 'false'

**`DLLayerLossCTC`** (output_control)  dl_layer `→`  (handle)

CTC loss layer.

## Example (HDevelop)

```
* Create a simple Seq2Seq model which overfits to a single output sequence.

* Input sequence length
T := 6
* Number of classes including blank (blank is always class_id 0)
C := 3
* Batch Size
N := 1
* Maximum length of target sequences
S := 3

* Model creation
create_dl_layer_input ('input', [T,1,1], [], [], Input)
create_dl_layer_dense (Input, 'dense', T*C, [], [], DLLayerDense)
create_dl_layer_reshape (DLLayerDense, 'dense_reshape', [T,1,C], [], [],\
                         ConvFinal)

* Training part
create_dl_layer_input ('ctc_input_lengths', [1,1,1], [], [],\
                       DLLayerInputLengths)
create_dl_layer_input ('ctc_target', [S,1,1], ['allow_smaller_tuple'], ['true'], DLLayerTarget)
create_dl_layer_input ('ctc_target_lengths', [1,1,1], [], [],\
                       DLLayerTargetLengths)
* Create the loss layer
create_dl_layer_loss_ctc (ConvFinal, DLLayerInputLengths, DLLayerTarget,\
                          DLLayerTargetLengths, 'ctc_loss', [], [],\
                          DLLayerLossCTC)

* Inference part
create_dl_layer_softmax (ConvFinal, 'softmax', [], [], DLLayerSoftMax)
create_dl_layer_depth_max (DLLayerSoftMax, 'prediction', 'argmax', [], [],\
                           DLLayerDepthMaxArg, _)

* Setting a seed because the weights of the network are randomly initialized
set_system ('seed_rand', 35)

create_dl_model ([DLLayerLossCTC,DLLayerDepthMaxArg], DLModel)

set_dl_model_param (DLModel, 'batch_size', N)
set_dl_model_param (DLModel, 'runtime', 'gpu')
set_dl_model_param (DLModel, 'learning_rate', 1)

* Create input sample for training
InputSequence := [0,1,2,3,4,5]
TargetSequence := [1,2,1]
create_dict (InputSample)
InputSample.input := InputSequence
InputSample.ctc_input_lengths := |InputSequence|
InputSample.ctc_target := TargetSequence
InputSample.ctc_target_lengths := |TargetSequence|

PredictedSequence := []
dev_inspect_ctrl ([InputSequence, TargetSequence, CTCLoss, PredictedValues,\
                  PredictedSequence])
Eps := 0.01
MaxIterations := 15
for I := 0 to MaxIterations by 1
    apply_dl_model (DLModel, InputSample, ['prediction','softmax'], \
                    DLResultBatch)
    get_grayval (DLResultBatch.prediction, rep(0,T), [0:T-1], PredictedValues)

    train_dl_model_batch (DLModel, InputSample, DLTrainResult)
    CTCLoss := DLTrainResult.ctc_loss
    if (CTCLoss < Eps)
        break
    endif
    stop()
endfor

* Greedy decoding of predicted sequence
PredictedSequence := uniq(int(PredictedValues))
PredictedSequence := select_mask(PredictedSequence, PredictedSequence [#] 0)
```

## References

Graves Alex et al., "Connectionist temporal classification: labelling
unsegmented sequence data with recurrent neural networks." Proceedings of the
23rd international conference on Machine learning. 2006.

## Module

Deep Learning Professional
