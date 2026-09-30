# CreateDlModel (Operator)

## Name

`CreateDlModel` — Create a deep learning model.

## Signature

`static void HOperatorSet.CreateDlModel(HTuple outputLayers, out HTuple DLModelHandle)`

`public HDlModel(HDlLayer[] outputLayers)`

`public HDlModel(HDlLayer outputLayers)`

`void HDlModel.CreateDlModel(HDlLayer[] outputLayers)`

`void HDlModel.CreateDlModel(HDlLayer outputLayers)`

## Description

The operator `CreateDlModel` creates a deep learning model from a
graph and returns its handle in *`DLModelHandle`*.

A deep learning model in HALCON mainly consists of a directed acyclic
graph that defines the networks architecture.
Further components of a deep learning model in HALCON are parameters as
*"class_names"*, *"class_ids"*, and many others,
or hyperparameters that are needed to train a model, as for example the
*"learning_rate"*.
While parameters and hyperparameters can be set after creation of the model
using [`SetDlModelParam`](set_dl_model_param.md), the model itself can only be created
using `CreateDlModel` if its network architecture is given in form of
a graph.

To build a graph that defines the models network architecture, one needs to
put together the networks layers. In general, a graph starts with an input
layer. A subsequent layer that follows after the input layer uses the
input layer as feeding layer, and the new layer itself might be used as
a feeding layer for the next layer, and so on. This is repeated until
the graphs output layers (e.g., softmax or loss layers) are
appended to the graph.
To create a layer, use its specified creation operator, e.g., an input
layer is created using [`CreateDlLayerInput`](create_dl_layer_input.md), a convolution layer
is created using [`CreateDlLayerConvolution`](create_dl_layer_convolution.md), and so on.

When the graph is defined, a model can be created using
`CreateDlModel` by passing over the graphs output layer handles in
*`outputLayers`*.
Note that the output layer handles save all other layers that directly or
indirectly serve as feeding input layers for the output layers during
their creation. This means that the output layer handles keep the
whole network architecture necessary for the creation of the model
using `CreateDlModel`.

The type of the created model, hence the task the model is designed for
(classification, object detection, segmentation), is only given by the
networks architecture.
However, if the networks architecture allows it, the type of the model,
*"type"*, can be set using [`SetDlModelParam`](set_dl_model_param.md).
A specified model type allows a more user friendly usage in the HALCON
deep learning workflow.
Supported types are:

- ***"generic"*:** —

  This is the default model type. The task the
  model's neuronal network can solve is defined by its architecture.
  When [`ApplyDlModel`](apply_dl_model.md) is applied for inference, the operator
  returns the activations of the output layers. To train the model
  using [`TrainDlModelBatch`](train_dl_model_batch.md), the underlying graph requires
  loss layers.
- ***"classification"*:** —

  The model is specified for
  classification and all layers required for training the model
  are adapted to the model.
  When [`ApplyDlModel`](apply_dl_model.md) is applied for inference,
  the output is adapted according to the type, see [`ApplyDlModel`](apply_dl_model.md)
  for more details.
  See [Deep Learning / Classification](toc_deeplearning_classification.md) for further information.

  In addition, the operator [`GenDlModelHeatmap`](gen_dl_model_heatmap.md) can be used to
  display the models heatmap.
- ***"detection"*:** —

  The model is specified for object detection
  and instance segmentation and all layers and anchors required for
  training the model are adapted to the model.
  When [`ApplyDlModel`](apply_dl_model.md) is applied for inference,
  the output is adapted according to the type, see [`ApplyDlModel`](apply_dl_model.md)
  for more details.
  Further information on advanced object detection and instance
  segmentation can be found in the chapters
  [Deep Learning / Advanced Object Detection](toc_deeplearning_objectdetection.md) and
  [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md).
- ***"multi_label_classification"*:** —

  The model is specified for
  multi-label classification and all layers required for training the model
  are adapted to the model.
  When [`ApplyDlModel`](apply_dl_model.md) is applied for inference,
  the output is adapted according to the type, see [`ApplyDlModel`](apply_dl_model.md)
  for more details.
  See [Deep Learning / Multi-Label Classification](toc_deeplearning_multilabelclassification.md) for
  further information.
- ***"segmentation"*:** —

  The model is specified for semantic
  segmentation or edge extraction respectively and all layers required for
  training the model are adapted to the model.
  When [`ApplyDlModel`](apply_dl_model.md) is applied for inference,
  the output is adapted according to the type, see [`ApplyDlModel`](apply_dl_model.md)
  for more details.
  See [Deep Learning / Semantic Segmentation and Edge Extraction](toc_deeplearning_semanticsegmentation.md) for further information.

Furthermore, many deep learning procedures provide more functionality for the
model if its type is set. As an example, `dev_display_dl_data`
can be used to display the inferred results more nicely.

Note that setting a model type requires that the graph fulfills certain
structure conditions. We recommend to follow the architecture of our
delivered neuronal networks if the model type should be set to one of these
types.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`outputLayers`** (input_control)  dl_layer(-array) `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Output layers of the graph.

**`DLModelHandle`** (output_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deep learning model.

## Result

If the parameters are valid, the operator `CreateDlModel`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateDlLayerSoftmax`,
`CreateDlLayerLossCrossEntropy`,
`CreateDlLayerLossFocal`,
`CreateDlLayerLossHuber`

## Possible Successors

`SetDlModelParam`

## Module

Deep Learning Professional
