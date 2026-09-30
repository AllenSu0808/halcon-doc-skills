# init_dl_continual_learning (Operator)

## Name

`init_dl_continual_learning` — Converts a deep learning model to a model suitable for Continual Learning.

## Signature

`def init_dl_continual_learning(dlmodel_handle: HHandle, dldataset: HHandle, gen_param: HHandle) -> None`

## Description

`init_dl_continual_learning` initializes a deep learning model
*`dlmodel_handle`* of *"type"* = *"classification"*
for Continual Learning. With Continual Learning, it is possible to extend
a model with new classes or changes within known classes without having to
retrain it from scratch, even if the model has been optimized for an
AI
2-interface.
See [Deep Learning / Continual Learning](toc_deeplearning_continuallearning.md) for further information.

If a *`dldataset`* is provided, it must be preprocessed and split.
`init_dl_continual_learning` can be called with either one of
the pretrained classification models provided with HALCON or with a
model that has previously been trained with `train_dl_model` (fine-tuned).
The internal architecture of the model will be slightly changed such that
Continual Learning becomes possible. At this process, the internal ability
of the model to distinguish between previously learned classes will be removed
unless the dataset previously used to fine-tune the model is provided. The
internal knowledge for feature extraction is retained in all cases. If no
*`dldataset`* is provided, the resulting Continual Learning model will not
be able to perform any kind of classification, regardless of being a pretrained
or fine-tuned model. To prevent potentially unwanted changes when passing no
*`dldataset`* or a dataset with different classes than the ones previously
known to the model, it is only possible by a further confirmation via setting the
GenParam *"reset_class_information"* to *"true"*. If a
*`dldataset`* is provided, the Continual Learning model will learn from the
provided data in a special way. Note that providing an initial *`dldataset`*
within `init_dl_continual_learning` will achieve a similar model to providing
no DLDataset within `init_dl_continual_learning`, but within
[`extend_dl_continual_learning`](extend_dl_continual_learning.md). If a fine-tuned model is provided,
*`dldataset`* must be the same dataset (including split and preprocessing
parameters) that was used during fine-tuning.

In general, it is recommended to start with a pretrained model and
initialize it for Continual Learning with the dataset that should be learned.
The model can be evaluated with `evaluate_dl_model`.
If the model accuracy is not sufficient, a fine-tuning on the initial dataset
before initializing the model for Continual Learning may help. However, extensive
fine-tuning can reduce the ability of the model to learn new classes compared to
a pretrained model.

Due to changes in the model architecture, the predictions of the initialized
model may differ from those of the originally fine-tuned model. While the overall accuracy
remains similar if the original training dataset is provided, the confidence values
may be lower. This is because the confidence values are calculated differently and does
not mean that the model is less reliable. Confidence values should
always be interpreted relative to the dataset in order to draw any
conclusions from them. If sufficient samples are available, the model performs an
internal calibration to ensure that correctly classified samples fall into a defined
confidence range.

`init_dl_continual_learning` also extends the model for
Out-of-Distribution Detection. Thus, when [`apply_dl_model`](apply_dl_model.md) is called,
the result will include the additional entries related to
Out-of-Distribution Detection.
See [`fit_dl_out_of_distribution`](fit_dl_out_of_distribution.md) for further information. Note that it
is crucial that the provided *`dldataset`* contains diverse
and sufficient samples for each class to ensure reliable Out-of-Distribution
Detection.

The usage of validation images differs within `init_dl_continual_learning`
compared to fine-tuning a model with `train_dl_model`. To be more specific,
validation images are only used for model confidence calibration and the calculation
of *"ood_threshold"* within Out-of-Distribution Detection.
If neither is required for your particular use-case,
you can also only split the dataset into training and test images. Note that if
the provided *`dldataset`* contains less than or equal to 15 training samples
per class and no validation samples, the Out-of-Distribution Detection threshold
calculation will fail and the threshold will be set to a very high value. In result,
the model will never predict a sample as Out-of-Distribution, unless the threshold
is changed by the user.

`init_dl_continual_learning` can be applied to any classification model
supported by HALCON. For models created using
[Deep Learning / Framework](toc_deeplearning_framework.md) operators or read from an
ONNX model file, Continual Learning compatibility may
vary depending on the architecture.

*`gen_param`* is a dictionary for setting generic parameters.
The following *`gen_param`* are currently supported:

- ***"‘reset_class_information’"*:** —

  Determines whether the parameter
  *`dldataset`* can be set to an empty tuple or to a dataset with different
  classes than the ones previously known to the model.
  This serves as a protection, as without a dataset, the existing class knowledge
  is reset when `init_dl_continual_learning` is called.
  In order to allow a model initialization with no dataset or a dataset with classes
  that differ from the ones known by the model,
  *"‘reset_class_information’"* must be set to *"‘true’"*.
  This can be useful, for example, if a pretrained model should be
  initialized for Continual Learning at a point in time at which samples
  of the initial classes are not yet available.

  List of values:
   *"false"*, *"true"*

  Default:
   *"false"*

## Attention

If [`fit_dl_out_of_distribution`](fit_dl_out_of_distribution.md) is called for a model before calling
`init_dl_continual_learning`, the previous internal
calculations for Out-of-Distribution Detection are discarded and the model is
adapted anew.

Certain modifications to the model, such as continuing standard fine-tuning
with `train_dl_model`, cannot be performed once the model has been
initialized for Continual Learning. Also note that calculating a classification
heatmap is currently not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- dlmodel_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`dlmodel_handle`** (input_control, state is modified)  dl_model `→` HHandle

Handle of a deep learning classification model.

**`dldataset`** (input_control)  dict `→` HHandle

Dataset for initial Continual Learning training step.

**`gen_param`** (input_control)  dict `→` HHandle

Dictionary for generic parameters.

Default:
[]

## Possible Predecessors

`read_dl_model`

## Possible Successors

`extend_dl_continual_learning`,
`apply_dl_model`

## Module

Deep Learning Professional
