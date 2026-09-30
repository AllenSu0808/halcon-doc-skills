# FitDlOutOfDistribution (Operator)

## Name

`FitDlOutOfDistribution` — Extend a deep learning model for Out-of-Distribution Detection.

## Signature

`static void HOperatorSet.FitDlOutOfDistribution(HTuple DLModelHandle, HTuple DLDataset, HTuple genParam)`

## Description

`FitDlOutOfDistribution` extends a trained deep learning model
*`DLModelHandle`* of *"type"* = *"classification"*
for Out-of-Distribution Detection. This functionality allows the model to
detect samples that
differ significantly from the classes it was trained on, known as
“Out-of-Distribution” (OOD) samples.

When [`ApplyDlModel`](apply_dl_model.md) is called subsequently, the results will include
the following additional entries related to Out-of-Distribution Detection:

- ***"ood_result"*:** —

  Indicates whether the sample is predicted as out-of-distribution.
- ***"ood_score"*:** —

  Indicates how much the sample differs from the trained classes.
  The higher this score, the more likely it is that the sample is
  out-of-distribution.
- ***"ood_threshold"*:** —

  If *"ood_score"* exceeds this threshold, the sample is
  predicted as out-of-distribution.
  The out-of-distribution threshold is computed during
  the execution of `FitDlOutOfDistribution` and stored within the
  model handle *`DLModelHandle`* as `'ood_threshold'`.
  If required, the threshold can be adjusted manually using
  the operator [`SetDlModelParam`](set_dl_model_param.md).

For `FitDlOutOfDistribution` to work properly, it
is important that *`DLDataset`* is the same dataset with the same split
and preprocessing parameters, as the one used for training
*`DLModelHandle`*.
It is crucial that the provided dataset *`DLDataset`* contains diverse
and sufficient samples for each class to ensure reliable Out-of-Distribution
Detection. If the provided *`DLDataset`* contains less than or equal to
15 training samples per class and no validation samples, `FitDlOutOfDistribution`
will return an error. In such cases, additional training data should be added
to the dataset.

`FitDlOutOfDistribution` can be applied to any classification model
supported by HALCON. For models created using
[Deep Learning / Framework](toc_deeplearning_framework.md) operators or read from an
ONNX model file, Out-of-Distribution Detection compatibility may
vary depending on the architecture.

The performance of the model for Out-of-Distribution Detection can be
evaluated using the procedure `evaluate_dl_model`.
To evaluate the model on out-of-distribution data, these can be added
to the `DLDataset` using
the procedure `add_dl_out_of_distribution_data`,
allowing for testing whether the model can accurately separate
in-distribution from out-of-distribution data.
Adjustments to the *"ood_threshold"* will affect evaluation results.
Therefore, it is recommended to re-evaluate the model after making
such changes.

*`genParam`* is a dictionary for setting generic parameters.
Currently no generic parameters are supported.

## Attention

If `FitDlOutOfDistribution` is called for a model that has already
been extended with Out-of-Distribution Detection, the previous internal
calculations are discarded and the model is adapted anew

Certain modifications to the model, such as changing the number of classes
or continuing training of the model,
cannot be performed once the model has been extended for
Out-of-Distribution Detection.
To make such changes possible, the model internal Out-of-Distribution Detection
must first be removed from the model using the parameter
*"clear_ood"* in [`SetDlModelParam`](set_dl_model_param.md).
Once removed, `FitDlOutOfDistribution`
can be called again to re-enable Out-of-Distribution Detection.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- DLModelHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`DLModelHandle`** (input_control, state is modified)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a deep learning classification model.

**`DLDataset`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dataset, which was used for training the model.

**`genParam`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary for generic parameters.

## Possible Predecessors

`ReadDlModel`

## Module

Deep Learning Professional
