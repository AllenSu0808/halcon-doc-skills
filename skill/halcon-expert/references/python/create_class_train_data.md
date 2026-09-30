# create_class_train_data (Operator)

## Name

`create_class_train_data` — Create a handle for training data for classifiers.

## Signature

`def create_class_train_data(num_dim: int) -> HHandle`

## Description

`create_class_train_data` creates a handle for training data
for classifiers. The handle is
returned in *`class_train_data_handle`*.
The dimension of the feature vectors is specified
with *`num_dim`*. Only feature vectors of this length can be added
to the handle.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`num_dim`** (input_control)  number `→` int

Number of dimensions of the feature vector.

Default:
10

**`class_train_data_handle`** (output_control)  class_train_data `→` HHandle

Handle of the training data.

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
*                                                         |Feat1| |Feat2|
add_sample_class_train_data (ClassTrainDataHandle, 'row', [1,1,1,  2,1  ], 0)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [2,2,2,  2,1  ], 1)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [1,1,1,  3,4  ], 0)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [2,2,2,  3,4  ], 1)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [0,0,1,  5,6  ], 0)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [2,3,2,  5,6  ], 1)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [0,0,1,  5,6  ], 0)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [2,3,2,  5,6  ], 1)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [0,0,1,  5,6  ], 0)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [2,3,2,  5,6  ], 1)
* Add more data
* ...
* Select the better feature with the classifier of your choice
select_feature_set_knn (ClassTrainDataHandle, 'greedy', [], [], KNNHandle,\
  SelectedFeature, Score)
select_feature_set_svm (ClassTrainDataHandle, 'greedy', [], [], SVMHandle,\
  SelectedFeature, Score)
select_feature_set_mlp (ClassTrainDataHandle, 'greedy', [], [], MLPHandle,\
  SelectedFeature, Score)
select_feature_set_gmm (ClassTrainDataHandle, 'greedy', [], [], GMMHandle,\
  SelectedFeature, Score)
* Use the classifier
* ...
```

## Result

If the parameters are valid, the operator `create_class_train_data`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`add_sample_class_knn`,
`train_class_knn`

## Alternatives

`create_class_svm`,
`create_class_mlp`

## See also

`select_feature_set_knn`,
`read_class_knn`

## Module

Foundation
