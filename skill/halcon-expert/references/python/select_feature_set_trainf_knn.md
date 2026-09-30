# select_feature_set_trainf_knn (Operator)

## Name

`select_feature_set_trainf_knn` — Select an optimal combination of features to classify OCR data.

## Signature

`def select_feature_set_trainf_knn(training_file: MaybeSequence[str], feature_list: MaybeSequence[str], selection_method: str, width: int, height: int, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, str, float]]) -> Tuple[HHandle, Sequence[str], Sequence[float]]`

## Description

`select_feature_set_trainf_knn` selects an optimal combination of
features, to classify the data given in the training file
*`training_file`* with a k-Nearest Neighbor classifier,
for details see [`create_ocr_class_knn`](create_ocr_class_knn.md).

Possible features are all OCR features listed and explained in
[`create_ocr_class_knn`](create_ocr_class_knn.md). All candidates which should be tested can be
specified in *`feature_list`*. A subset of these features is
returned as selected features in *`feature_set`*.

`select_feature_set_trainf_knn` is specialized on OCR problems and
only supports the features in the list mentioned before.
In order to use other features, please use the more general operator
[`select_feature_set_knn`](select_feature_set_knn.md).

The selection method
*`selection_method`* is either a greedy search *"greedy"*
(iteratively add the feature with highest gain)
or the dynamically oscillating search *"greedy_oscillating"*
(add the feature with highest gain and test then if any of the already added
features can be left out without great loss).
The method *"greedy"* is generally preferable, since it is faster.
Only in cases when a large training set is available
the method *"greedy_oscillating"* might return better results.

The optimization criterion is the classification rate of a two-fold
cross-validation of the training data. The best achieved value
is returned in *`score`*.

The k-NN classifier can be parametrized using the following values in
*`gen_param_name`* and *`gen_param_value`*:

- ***"num_neighbors"*:** —

  The number of minimally evaluated
  nodes, increase this value for high dimensional data.

  Suggested values:
   *1*, *2*, *5*,
  *10*

  Default:
   *1*
- ***"num_trees"*:** —

  Number of search trees in the k-NN
  classifier

  Suggested values:
   *1*, *4*, *10*

  Default:
   *4*

## Attention

This operator may take considerable time, depending on the size of the
data set in the training file, and the number of features.

Please note, that this operator should not be called, if only a small
set of training data is available. Due to the risk of overfitting the
operator `select_feature_set_trainf_knn` may deliver a classifier with
a very high score. However, the classifier may perform poorly when tested.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`training_file`** (input_control)  filename.read(-array) `→` MaybeSequence[str]

Names of the training files.

Default:
""

File extension:
.`trf`, .`otr`

**`feature_list`** (input_control)  string(-array) `→` MaybeSequence[str]

List of features that should be considered for selection.

Default:
["zoom_factor","ratio","width","height","foreground","foreground_grid_9","foreground_grid_16","anisometry","compactness","convexity","moments_region_2nd_invar","moments_region_2nd_rel_invar","moments_region_3rd_invar","moments_central","phi","num_connect","num_holes","projection_horizontal","projection_vertical","projection_horizontal_invar","projection_vertical_invar","chord_histo","num_runs","pixel","pixel_invar","pixel_binary","gradient_8dir","cooc","moments_gray_plane"]

List of values:
"anisometry", "chord_histo", "compactness", "convexity", "cooc", "default", "foreground", "foreground_grid_16", "foreground_grid_9", "gradient_8dir", "height", "moments_central", "moments_gray_plane", "moments_region_2nd_invar", "moments_region_2nd_rel_invar", "moments_region_3rd_invar", "num_connect", "num_holes", "num_runs", "phi", "pixel", "pixel_binary", "pixel_invar", "projection_horizontal", "projection_horizontal_invar", "projection_vertical", "projection_vertical_invar", "ratio", "width", "zoom_factor"

**`selection_method`** (input_control)  string `→` str

Method to perform the selection.

Default:
"greedy"

List of values:
"greedy", "greedy_oscillating"

**`width`** (input_control)  integer `→` int

Width of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
15

**`height`** (input_control)  integer `→` int

Height of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
16

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

Names of generic parameters to configure the selection
process and the classifier.

Default:
[]

List of values:
"num_neighbors"

**`gen_param_value`** (input_control)  number-array `→` Sequence[Union[int, str, float]]

Values of generic parameters to configure the selection
process and the classifier.

Default:
[]

Suggested values:
1, 2, 3

**`ocrhandle`** (output_control)  ocr_knn `→` HHandle

Trained OCR-k-NN classifier.

**`feature_set`** (output_control)  string-array `→` Sequence[str]

Selected feature set, contains only entries from
*`feature_list`*.

**`score`** (output_control)  real-array `→` Sequence[float]

Achieved score using tow-fold cross-validation.

## Result

If the parameters are valid, the operator
`select_feature_set_trainf_knn` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Alternatives

`select_feature_set_trainf_svm`,
`select_feature_set_trainf_mlp`

## See also

`select_feature_set_knn`

## Module

OCR/OCV
