# set_feature_lengths_class_train_data (Operator)

## Name

`set_feature_lengths_class_train_data` — Define subfeatures in training data.

## Signature

`def set_feature_lengths_class_train_data(class_train_data_handle: HHandle, sub_feature_length: Sequence[int], names: Sequence[str]) -> None`

## Description

`set_feature_lengths_class_train_data` defines subfeatures in the
training data in *`class_train_data_handle`*. The subfeatures are defined
in *`sub_feature_length`* by a set of lengths that groups the previously
added columns subsequently into subfeatures. It is not possible
to group columns which are not subsequent.
The sum over all entries in *`sub_feature_length`*
must be equal to the number of dimensions set in
[`create_class_train_data`](create_class_train_data.md) with the parameter `num_dim`.
Optionally, names for all subsets can be defined in *`names`*.

An exemplary situation in which this operator is helpful is described here:
Two different data sources are available. Both data sources
provide a vector of a certain length. The first data source provides
data of length n and the second of length m. In order
to automatically decide which of the data sources is more valuable for
a certain classification problem, training data can be created that contains
both data sources. E.g., if [`create_class_train_data`](create_class_train_data.md) was called with
`num_dim` =n+m=w, then `set_feature_lengths_class_train_data`
can be called with *[n,m]* in *`sub_feature_length`*
and *[Name1, Name2]* in *`names`* to
describe this situation for a later usage of operators like
[`select_feature_set_knn`](select_feature_set_knn.md) or [`select_feature_set_svm`](select_feature_set_svm.md).
Then the classification problem has to be specified via calls of
[`add_sample_class_train_data`](add_sample_class_train_data.md), by giving a vector of the first
data source and a vector of the second data source as the combined
feature vector of length w.
The result of the call of [`select_feature_set_knn`](select_feature_set_knn.md) would then be
either *[Name1]* if the first is more relevant,
*[Name2]* if the second is more relevant
or *[Name1, Name2]* if both are necessary.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- class_train_data_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`class_train_data_handle`** (input_control, state is modified)  class_train_data `→` HHandle

Handle of the training data that should be
partitioned into subfeatures.

**`sub_feature_length`** (input_control)  number-array `→` Sequence[int]

Length of the subfeatures.

**`names`** (input_control)  string-array `→` Sequence[str]

Names of the subfeatures.

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
* Select the better feature
select_feature_set_knn (ClassTrainDataHandle, 'greedy', [], [], KNNHandle,\
  SelectedFeature, Score)
classify_class_knn (KNNHandle, [1,1,1], Result, Rating)
classify_class_knn (KNNHandle, [2,2,2], Result, Rating)
* Use the classifier
* ...
```

## Result

If the parameters are valid, the operator
`set_feature_lengths_class_train_data`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_class_train_data`,
`add_sample_class_train_data`

## Possible Successors

`select_feature_set_knn`,
`select_feature_set_svm`,
`select_feature_set_mlp`,
`select_feature_set_gmm`

## Module

Foundation
