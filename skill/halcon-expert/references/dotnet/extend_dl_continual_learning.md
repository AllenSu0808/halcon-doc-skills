# ExtendDlContinualLearning (Operator)

## Name

`ExtendDlContinualLearning` — Extend a Continual Learning model with with new data.

## Signature

`static void HOperatorSet.ExtendDlContinualLearning(HTuple DLModelHandle, HTuple DLDataset, HTuple genParam)`

## Description

`ExtendDlContinualLearning` extends a Continual Learning model
*`DLModelHandle`* of *"type"* = *"classification"*
with new data provided by *`DLDataset`*. The new data can either
contain new classes that the model should learn to predict, or new samples
of an existing class to improve the model for that particular class.
*`DLModelHandle`* learns from the provided data in a manner specific to
Continual Learning. After calling `ExtendDlContinualLearning`, the model
will either be able to predict more classes or the internal knowledge of existing
classes will have been extended, depending on the dataset provided.
See [Deep Learning / Continual Learning](toc_deeplearning_continuallearning.md) for further information.

*`DLDataset`* must only contain new data which the model should
learn. It is not necessary to provide data samples from previous Continual Learning
training steps, because the model preserves previously learned classes.
Besides `ExtendDlContinualLearning` can be called
with a *`DLModelHandle`* optimized for an AI
2-interface. As a result,
you can extend your Continual Learning model directly on an edge device.

The operator expects a dataset that is preprocessed by the supplied
procedure `preprocess_dl_dataset`. Changes made within the procedure
to the path of the samples are not supported and lead to errors.
`ExtendDlContinualLearning` will change the ClassIDs of the provided
*`DLDataset`* internally to match the ClassIDs of the provided model. New unknown
classes will receive a new and unused ClassID. The ClassID
of known classes within *`DLDataset`* will be changed to the ClassID given by the
model. These changes are applied both to the provided *`DLDataset`* dictionary
and to all preprocessed samples on disk. This is required for correct evaluation.

The performance of the Continual Learning model can be
evaluated using the procedure `evaluate_dl_model`. You can provide one or
more datasets, containing all classes the model has been trained on or only a subset
of those. It is strongly recommended to evaluate the model with test data
corresponding to all classes and Continual Learning steps, so that the evaluation
result accurately reflects the capabilities of the model on all relevant data.

The operator also recalculates the Out-of-Distribution threshold. Any
threshold value previously set by the user will be overwritten.
Confidence calibration is done only once (either in [`InitDlContinualLearning`](init_dl_continual_learning.md), if
a dataset was provided, or in the first call to `ExtendDlContinualLearning`)
and not repeated. As more classes are added,
the absolute confidence values will generally decrease.

*`genParam`* is a dictionary for setting generic parameters.
Currently no generic parameters are supported.

## Attention

The operator makes changes to the samples of the provided dataset.
If an error occurs during the changes, the dataset is incompletely adjusted and corrupted.
It must then be re-read and pre-processed again. This is indicated by the operator's error
message in the event of an error.

Note that the operator does not behave additively. Adding images of the same class
in several calls does not result in an identical model compared to adding the same,
combined images in a single call.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameters:

- DLModelHandle
- DLDataset

During execution of this operator, access to the values of these parameters must be synchronized if it is used across multiple threads.

## Parameters

**`DLModelHandle`** (input_control, state is modified)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a deep learning classification model initialized
for Continual Learning.

**`DLDataset`** (input_control, state is modified)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dataset for new Continual Learning training step.

**`genParam`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary for generic parameters.

Default:
[]

## Possible Predecessors

`InitDlContinualLearning`

## Possible Successors

`ApplyDlModel`

## Module

Deep Learning Professional
