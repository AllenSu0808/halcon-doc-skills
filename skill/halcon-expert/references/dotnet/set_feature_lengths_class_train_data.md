# SetFeatureLengthsClassTrainData (Operator)

## Name

`SetFeatureLengthsClassTrainData` — Define subfeatures in training data.

## Signature

`static void HOperatorSet.SetFeatureLengthsClassTrainData(HTuple classTrainDataHandle, HTuple subFeatureLength, HTuple names)`

`void HClassTrainData.SetFeatureLengthsClassTrainData(HTuple subFeatureLength, HTuple names)`

## Description

`SetFeatureLengthsClassTrainData` defines subfeatures in the
training data in *`classTrainDataHandle`*. The subfeatures are defined
in *`subFeatureLength`* by a set of lengths that groups the previously
added columns subsequently into subfeatures. It is not possible
to group columns which are not subsequent.
The sum over all entries in *`subFeatureLength`*
must be equal to the number of dimensions set in
[`CreateClassTrainData`](create_class_train_data.md) with the parameter `numDim`.
Optionally, names for all subsets can be defined in *`names`*.

An exemplary situation in which this operator is helpful is described here:
Two different data sources are available. Both data sources
provide a vector of a certain length. The first data source provides
data of length n and the second of length m. In order
to automatically decide which of the data sources is more valuable for
a certain classification problem, training data can be created that contains
both data sources. E.g., if [`CreateClassTrainData`](create_class_train_data.md) was called with
`numDim` =n+m=w, then `SetFeatureLengthsClassTrainData`
can be called with *[n,m]* in *`subFeatureLength`*
and *[Name1, Name2]* in *`names`* to
describe this situation for a later usage of operators like
[`SelectFeatureSetKnn`](select_feature_set_knn.md) or [`SelectFeatureSetSvm`](select_feature_set_svm.md).
Then the classification problem has to be specified via calls of
[`AddSampleClassTrainData`](add_sample_class_train_data.md), by giving a vector of the first
data source and a vector of the second data source as the combined
feature vector of length w.
The result of the call of [`SelectFeatureSetKnn`](select_feature_set_knn.md) would then be
either *[Name1]* if the first is more relevant,
*[Name2]* if the second is more relevant
or *[Name1, Name2]* if both are necessary.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- classTrainDataHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`classTrainDataHandle`** (input_control, state is modified)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data that should be
partitioned into subfeatures.

**`subFeatureLength`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long)

Length of the subfeatures.

**`names`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

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
`SetFeatureLengthsClassTrainData`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateClassTrainData`,
`AddSampleClassTrainData`

## Possible Successors

`SelectFeatureSetKnn`,
`SelectFeatureSetSvm`,
`SelectFeatureSetMlp`,
`SelectFeatureSetGmm`

## Module

Foundation
