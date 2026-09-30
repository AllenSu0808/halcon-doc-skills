# TrainDlModelAnomalyDataset (Operator)

## Name

`TrainDlModelAnomalyDataset` — Train a deep learning model for anomaly detection.

## Signature

`static void HOperatorSet.TrainDlModelAnomalyDataset(HTuple DLModelHandle, HTuple DLSamples, HTuple DLTrainParam, out HTuple DLTrainResult)`

`HDict HDlModel.TrainDlModelAnomalyDataset(HDict[] DLSamples, HDict DLTrainParam)`

## Description

The operator `TrainDlModelAnomalyDataset` performs the training
of a deep learning model with *"type"*=*"anomaly_detection"*
contained in *`DLModelHandle`* (for deep learning models
with *"type"*=*"gc_anomaly_detection"* see
[`TrainDlModelBatch`](train_dl_model_batch.md)).

This operator processes the full training dataset at once.
This is in contrast to the operator [`TrainDlModelBatch`](train_dl_model_batch.md).
The iterations over the dataset are performed internally by the operator.
Consequently, you only need to call this operator once with the full training
dataset to train your anomaly detection model.

The training dataset is handed over in the tuple of dictionaries
*`DLSamples`*.
See the chapter [Deep Learning / Model](toc_deeplearning_model.md) for further information to the
used dictionaries and their keys.
The operator expects within the training dataset only images without anomaly
to train the anomaly detection model.

The dictionary *`DLTrainParam`* can be used to change the
hyperparameters.
The following values are supported:

- `max_num_epochs`:
  This parameter specifies the maximum number of epochs performed
  during training.
  In case the criterion specified by `error_threshold` is reached in
  an earlier epoch, the training will terminate regardless.

  Restriction:
   `max_num_epochs` >=*1*.

  Default:
   `max_num_epochs` = *30*.
- `error_threshold`:
  This parameter is a termination criterion for the training.
  If the training error is less than the specified
  `error_threshold`, the training terminates successfully.

  Restriction:
  *0.0* <= `error_threshold` <= *1.0*.

  Default:
   `error_threshold` = *0.001*.
- `domain_ratio`:
  This parameter determines the percentage of information of each image used
  for training.
  Since images tend to contain an abundance of information,
  it is advisable to reduce its amount.
  Additionally, reducing `domain_ratio` can decrease the time needed
  for training.
  Please note, however, sufficient information needs to remain and
  therefore this value should not be set too small either.
  Otherwise the training result might not be satisfactory or the training
  itself might even fail.

  Restriction:
   *0.0* < `domain_ratio` <= *1.0*.

  Default:
   `domain_ratio` = *0.1*.
- `regularization_noise`:
  This parameter can be set to regularize the training in order to
  improve robustness.

  Restriction:
   `regularization_noise` >=*0.0*.

  Default:
   `regularization_noise` = *0.0*.

The output dictionary *`DLTrainResult`* contains the following values:

- `final_error`:
  The best error received during training.
- `final_epoch`
  The epoch in which the error `final_error` was achieved.

## Attention

The operator `TrainDlModelAnomalyDataset` internally calls functions
that might not be deterministic.
Therefore, results from multiple calls of
`TrainDlModelAnomalyDataset` can slightly differ, although the same
input values have been used.

System requirements:
To run this operator on GPU by setting *"runtime"* to *"gpu"*
(see [`GetDlModelParam`](get_dl_model_param.md)), cuDNN and cuBLAS are required.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.
Alternatively, this operator
can also be run on CPU by setting *"runtime"* to *"cpu"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Deep learning model handle.

**`DLSamples`** (input_control)  dict-array `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Tuple of Dictionaries with input images and
corresponding information.

**`DLTrainParam`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Parameter for training the anomaly detection model.

Default:
[]

**`DLTrainResult`** (output_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary with the train result data.

## Result

If the parameters are valid, the operator
`TrainDlModelAnomalyDataset` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`ReadDlModel`,
`SetDlModelParam`,
`GetDlModelParam`

## Possible Successors

`ApplyDlModel`

## See also

`ApplyDlModel`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
Deep Learning Professional
