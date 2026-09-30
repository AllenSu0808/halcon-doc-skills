# select_feature_set_gmm (Operator)

## Name

`select_feature_set_gmm` — Selects an optimal combination from a set of features to classify the
provided data.

## Signature

`select_feature_set_gmm( : : ClassTrainDataHandle, SelectionMethod, GenParamName, GenParamValue : GMMHandle, SelectedFeatureIndices, Score)`

## Description

`select_feature_set_gmm` selects an optimal subset from a set of
features to solve a given classification problem.
The classification problem has to be specified with annotated training data
in *`ClassTrainDataHandle`* and will be classified by a
Gaussian Mixture Model. Details of the properties of this
classifier can be found in [`create_class_gmm`](create_class_gmm.md).

The result of the operator is a trained classifier that is returned in
*`GMMHandle`*. Additionally, the list of indices or names of
the selected features
is returned in *`SelectedFeatureIndices`*. To use this classifier,
calculate for new input data all features mentioned in
*`SelectedFeatureIndices`* and pass them to the classifier.

A possible application of this operator can be a comparison of
different parameter sets for certain feature extraction techniques. Another
application is to search for a feature that is discriminating between
different classes.

To define the features that should be selected from
*`ClassTrainDataHandle`*, the dimensions of the
feature vectors in *`ClassTrainDataHandle`* can be grouped into
subfeatures by calling [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md).
A subfeature can contain several subsequent elements of a feature vector.
`select_feature_set_gmm` decides for each of these subfeatures,
if it is better to use it for the classification or leave it out.

The indices of the selected subfeatures are returned in
*`SelectedFeatureIndices`*.
If names were set in [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md), these
names are returned instead of the indices.
If [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md) was not called for
*`ClassTrainDataHandle`* before, each element of the feature vector
is considered as a subfeature.

The selection method
*`SelectionMethod`* is either a greedy search *'greedy'*
(iteratively add the feature with highest gain)
or the dynamically oscillating search *'greedy_oscillating'*
(add the feature with highest gain and test then if any of the already added
features can be left out without great loss).
The method *'greedy'* is generally preferable, since it is faster.
Only in cases when the subfeatures are low-dimensional or redundant,
the method *'greedy_oscillating'* should be chosen.

The optimization criterion is the classification rate of
a two-fold cross-validation of the training data.
The best achieved value is returned in *`Score`*.

The following generic parameters can be set in *`GenParamName`* and
*`GenParamValue`*:

- ***'min_centers'*:** —

  Minimal number of clusters to represent a class in the training data.

  Suggested values:
   *'1'*, *'2'*

  Default:
   *'1'*
- ***'max_center'*:** —

  Maximal number of clusters to represent a class in the training data.

  Suggested values:
   *'1'*, *'5'*, *'10'*

  Default:
   *'1'*
- ***'covar_type'*:** —

  Type of the covariance to represent the size of a cluster.

  List of values:
   *'spherical'*, *'diag'*,
  *'full'*

  Default:
   *'spherical'*
- ***'random_seed'*:** —

  Random seed.

  Default:
   *'42'*
- ***'threshold'*:** —

  Training threshold.

  Default:
   *'0.001'*
- ***'regularize'*:** —

  Regularization value.

  Default:
   *'0.0001'*
- ***'randomize'*:** —

  Randomize the input vector.

  Default:
   *'0'*
- ***'class_priors'*:** —

  Mode to determine the a-priori probabilities of the classes.

  List of values:
   *'training'*, *'uniform'*

  Default:
   *'training'*

A more exact description of those parameters can be found in
[`create_class_gmm`](create_class_gmm.md) and [`train_class_gmm`](train_class_gmm.md).

## Attention

This operator may take considerable time, depending on the size of the
data set in the training file, and the number of features.

Please note, that this operator should not be called, if only a small
set of training data is available. Due to the risk of overfitting the
operator `select_feature_set_gmm` may deliver a classifier with
a very high score. However, the classifier may perform poorly when tested.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`ClassTrainDataHandle`** (input_control)  class_train_data `→`  (handle)

Handle of the training data.

**`SelectionMethod`** (input_control)  string `→`  (string)

Method to perform the selection.

Default:
'greedy'

List of values:
'greedy', 'greedy_oscillating'

**`GenParamName`** (input_control)  string(-array) `→`  (string)

Names of generic parameters to configure
the classifier.

Default:
[]

List of values:
'class_priors', 'covar_type', 'max_center', 'min_centers', 'random_seed', 'randomize', 'regularize', 'threshold'

**`GenParamValue`** (input_control)  number(-array) `→`  (real / integer / string)

Values of generic parameters to configure
the classifier.

Default:
[]

Suggested values:
1, 2, 3, 'spherical', 'diag', 'full', 42, 0.001, 0.0001, 0

**`GMMHandle`** (output_control)  class_gmm `→`  (handle)

A trained GMM classifier using only the selected
features.

**`SelectedFeatureIndices`** (output_control)  string-array `→`  (string)

The selected feature set, contains indices or names.

**`Score`** (output_control)  real-array `→`  (real)

The achieved score using two-fold cross-validation.

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
* Select the better feature with a GMM
select_feature_set_gmm (ClassTrainDataHandle, 'greedy', [], [], GMMHandle,\
  SelectedFeatureGMM, Score)
* Use the classifier
* ...
```

## Result

If the parameters are valid, the operator `select_feature_set_gmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_class_train_data`,
`add_sample_class_train_data`,
`set_feature_lengths_class_train_data`

## Possible Successors

`classify_class_gmm`

## Alternatives

`select_feature_set_mlp`,
`select_feature_set_knn`,
`select_feature_set_svm`

## See also

`create_class_gmm`,
`gray_features`,
`region_features`

## Module

Foundation
