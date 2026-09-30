# select_sub_feature_class_train_data (Operator)

## Name

`select_sub_feature_class_train_data` — Select certain features from training data to create
training data containing less features.

## Signature

`def select_sub_feature_class_train_data(class_train_data_handle: HHandle, sub_feature_indices: Sequence[Union[int, str]]) -> HHandle`

## Description

`select_sub_feature_class_train_data` selects certain features from
the training data in *`class_train_data_handle`* and returns the subset
in *`selected_class_train_data_handle`*.
The features that should be selected can be chosen by
*`sub_feature_indices`*. If [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md)
was not called before, the indices refer to the columns.
If [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md) was called before,
the grouping defined there is relevant for the meaning of the indices. The
entry `n` in the list selects then the `n`-th feature group.
If [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md) was called with names for
the feature groups, those names can be used instead of the
indices.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`class_train_data_handle`** (input_control)  class_train_data `→` HHandle

Handle of the training data.

**`sub_feature_indices`** (input_control)  number-array `→` Sequence[Union[int, str]]

Indices or names to select the subfeatures or
columns.

**`selected_class_train_data_handle`** (output_control)  class_train_data `→` HHandle

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
`select_sub_feature_class_train_data`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_class_train_data`,
`add_sample_class_train_data`,
`set_feature_lengths_class_train_data`

## Possible Successors

`add_class_train_data_gmm`,
`add_class_train_data_mlp`,
`add_class_train_data_svm`,
`add_class_train_data_knn`

## Module

Foundation
