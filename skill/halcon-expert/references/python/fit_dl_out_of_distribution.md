# fit_dl_out_of_distribution (Operator)

## Name

`fit_dl_out_of_distribution` — Extend a deep learning model for Out-of-Distribution Detection.

## Signature

`def fit_dl_out_of_distribution(dlmodel_handle: HHandle, dldataset: HHandle, gen_param: HHandle) -> None`

## Description

`fit_dl_out_of_distribution` extends a trained deep learning model
*`dlmodel_handle`* of *"type"* = *"classification"*
for Out-of-Distribution Detection. This functionality allows the model to
detect samples that
differ significantly from the classes it was trained on, known as
“Out-of-Distribution” (OOD) samples.

When [`apply_dl_model`](apply_dl_model.md) is called subsequently, the results will include
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
  the execution of `fit_dl_out_of_distribution` and stored within the
  model handle *`dlmodel_handle`* as `'ood_threshold'`.
  If required, the threshold can be adjusted manually using
  the operator [`set_dl_model_param`](set_dl_model_param.md).

For `fit_dl_out_of_distribution` to work properly, it
is important that *`dldataset`* is the same dataset with the same split
and preprocessing parameters, as the one used for training
*`dlmodel_handle`*.
It is crucial that the provided dataset *`dldataset`* contains diverse
and sufficient samples for each class to ensure reliable Out-of-Distribution
Detection. If the provided *`dldataset`* contains less than or equal to
15 training samples per class and no validation samples, `fit_dl_out_of_distribution`
will return an error. In such cases, additional training data should be added
to the dataset.

`fit_dl_out_of_distribution` can be applied to any classification model
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

*`gen_param`* is a dictionary for setting generic parameters.
Currently no generic parameters are supported.

## Attention

If `fit_dl_out_of_distribution` is called for a model that has already
been extended with Out-of-Distribution Detection, the previous internal
calculations are discarded and the model is adapted anew

Certain modifications to the model, such as changing the number of classes
or continuing training of the model,
cannot be performed once the model has been extended for
Out-of-Distribution Detection.
To make such changes possible, the model internal Out-of-Distribution Detection
must first be removed from the model using the parameter
*"clear_ood"* in [`set_dl_model_param`](set_dl_model_param.md).
Once removed, `fit_dl_out_of_distribution`
can be called again to re-enable Out-of-Distribution Detection.

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

Dataset, which was used for training the model.

**`gen_param`** (input_control)  dict `→` HHandle

Dictionary for generic parameters.

## Possible Predecessors

`read_dl_model`

## Module

Deep Learning Professional
