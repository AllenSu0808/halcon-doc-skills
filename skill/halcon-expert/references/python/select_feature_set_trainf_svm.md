# select_feature_set_trainf_svm (Operator)

## Name

`select_feature_set_trainf_svm` — Selects an optimal combination of features to classify OCR data.

## Signature

`def select_feature_set_trainf_svm(training_file: MaybeSequence[str], feature_list: MaybeSequence[str], selection_method: str, width: int, height: int, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, str, float]]) -> Tuple[HHandle, Sequence[str], Sequence[float]]`

## Description

`select_feature_set_trainf_svm` selects an optimal combination of
features, to classify the data given in the training file
*`training_file`* with a Support Vector Machine (SVM),
for details see [`create_ocr_class_svm`](create_ocr_class_svm.md).

Possible features are all OCR features listed and explained in
[`create_ocr_class_svm`](create_ocr_class_svm.md). All candidates which should be tested can be
specified in *`feature_list`*. A subset of these features is
returned as selected features in *`feature_set`*.

`select_feature_set_trainf_svm` is specialized on OCR problems and
only supports the features in the list mentioned before.
In order to use other features, please use the more general operator
[`select_feature_set_svm`](select_feature_set_svm.md).

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

The parameters *"nu"* and *"gamma"* for the SVM that is used
to classify can be set to *"auto"* by using the
parameters *`gen_param_name`* and *`gen_param_value`*. If they are
set to *"auto"*, the estimated optimal *"nu"* and/or
*"gamma"* is estimated. The automatic estimation of *"nu"*
and *"gamma"* can take a substantial amount of time (up to days,
depending on the data set and the number of features). Alternatively,
a certain value for both can be set the same way.
An explanation of the parameters *"nu"* and
*"gamma"* as the kernel parameter of the radial basis function (RBF)
kernel can be found in [`create_class_svm`](create_class_svm.md).

## Attention

This operator may take considerable time, depending on the size of the
data set in the training file, and the number of features.

Please note, that this operator should not be called, if only a small
set of training data is available. Due to the risk of overfitting the
operator `select_feature_set_trainf_svm` may deliver a classifier with
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
"gamma", "nu"

**`gen_param_value`** (input_control)  number-array `→` Sequence[Union[int, str, float]]

Values of generic parameters to configure the selection
process and the classifier.

Default:
[]

Suggested values:
"auto", "0.1", "0.3"

**`ocrhandle`** (output_control)  ocr_svm `→` HHandle

Trained OCR-SVM Classifier.

**`feature_set`** (output_control)  string-array `→` Sequence[str]

Selected feature set, contains only entries from
*`feature_list`*.

**`score`** (output_control)  real-array `→` Sequence[float]

Achieved score using tow-fold cross-validation.

## Result

If the parameters are valid, the operator
`select_feature_set_trainf_svm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Alternatives

`select_feature_set_trainf_mlp`,
`select_feature_set_trainf_knn`,
`select_feature_set_trainf_mlp_protected`

## See also

`select_feature_set_trainf_svm_protected`,
`select_feature_set_svm`

## Module

OCR/OCV
