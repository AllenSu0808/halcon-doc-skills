# SelectSubFeatureClassTrainData (Operator)

## Name

`SelectSubFeatureClassTrainData` — Select certain features from training data to create
training data containing less features.

## Signature

`static void HOperatorSet.SelectSubFeatureClassTrainData(HTuple classTrainDataHandle, HTuple subFeatureIndices, out HTuple selectedClassTrainDataHandle)`

`HClassTrainData HClassTrainData.SelectSubFeatureClassTrainData(HTuple subFeatureIndices)`

## Description

`SelectSubFeatureClassTrainData` selects certain features from
the training data in *`classTrainDataHandle`* and returns the subset
in *`selectedClassTrainDataHandle`*.
The features that should be selected can be chosen by
*`subFeatureIndices`*. If [`SetFeatureLengthsClassTrainData`](set_feature_lengths_class_train_data.md)
was not called before, the indices refer to the columns.
If [`SetFeatureLengthsClassTrainData`](set_feature_lengths_class_train_data.md) was called before,
the grouping defined there is relevant for the meaning of the indices. The
entry `n` in the list selects then the `n`-th feature group.
If [`SetFeatureLengthsClassTrainData`](set_feature_lengths_class_train_data.md) was called with names for
the feature groups, those names can be used instead of the
indices.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`classTrainDataHandle`** (input_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data.

**`subFeatureIndices`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long / string)

Indices or names to select the subfeatures or
columns.

**`selectedClassTrainDataHandle`** (output_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the reduced training data.

## Example (HDevelop)

```
* Find out which of the two features distinguishes two Classes
NameFeature1 := 'Good Feature'
NameFeature2 := 'Bad Feature'
LengthFeature1 := 3
LengthFeature2 := 2
* Create training data
create_class_train_data (LengthFeature1+LengthFeature2,\
                         ClassTrainDataHandle)
* Define the features which are in the training data
set_feature_lengths_class_train_data (ClassTrainDataHandle, [LengthFeature1,\
                           LengthFeature2], [NameFeature1, NameFeature2])
* Add training data
*                                                          |Feat1| |Feat2|
add_sample_class_train_data (ClassTrainDataHandle, 'row', [1,1,1,  2,1  ], 0)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [2,2,2,  2,1  ], 1)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [1,1,1,  3,4  ], 0)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [2,2,2,  3,4  ], 1)
* Add more data
* ...
* Select one of the features
select_sub_feature_class_train_data (ClassTrainDataHandle, NameFeature1, \
                                     SelectedClassTrainDataHandle)
* Add training data to a classifier
create_class_knn (LengthFeature1, KNNHandle)
add_class_train_data_knn (KNNHandle, SelectedClassTrainDataHandle)
train_class_knn (KNNHandle, [], [])
* Use the classifier
* ...
```

## Result

If the parameters are valid, the operator
`SelectSubFeatureClassTrainData`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateClassTrainData`,
`AddSampleClassTrainData`,
`SetFeatureLengthsClassTrainData`

## Possible Successors

`AddClassTrainDataGmm`,
`AddClassTrainDataMlp`,
`AddClassTrainDataSvm`,
`AddClassTrainDataKnn`

## Module

Foundation
