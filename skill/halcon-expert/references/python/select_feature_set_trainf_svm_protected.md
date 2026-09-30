# select_feature_set_trainf_svm_protected (Operator)

## Name

`select_feature_set_trainf_svm_protected` — Select an optimal combination of features to classify OCR data
from a (protected) training file.

## Signature

`def select_feature_set_trainf_svm_protected(training_file: MaybeSequence[str], password: MaybeSequence[str], feature_list: MaybeSequence[str], selection_method: str, width: int, height: int, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, str, float]]) -> Tuple[HHandle, Sequence[str], Sequence[float]]`

## Description

`select_feature_set_trainf_svm_protected` selects an optimal
combination of features to classify the data given in the training files
*`training_file`* with a support vector machine (SVM). Its functionality
corresponds to the functionality of [`select_feature_set_trainf_svm`](select_feature_set_trainf_svm.md),
with the addition that `select_feature_set_trainf_svm_protected`
can process unprotected and protected training files. Protected
training files can be used only with the correct user password
*`password`*. If the number of passwords *`password`*
equals 1, then every input file *`training_file`* is checked
with that password, otherwise the number of passwords has to be
equal to the number of input files and the input file at position
n is checked with the password at position n. For unprotected
training files the passwords are ignored.

For a more detailed description of the operator's functionality see
[`select_feature_set_trainf_svm`](select_feature_set_trainf_svm.md). The concept of protecting OCR
training data in HALCON is described in [`protect_ocr_trainf`](protect_ocr_trainf.md).

## Attention

This operator may take considerable time, depending on the size of the
data set in the training file, and the number of features.

Please note, that this operator should not be called, if only a small
set of training data is available. Due to the risk of overfitting the
operator `select_feature_set_trainf_svm_protected` may deliver a
classifier with a very high score. However, the classifier may perform
poorly when tested.

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

**`password`** (input_control)  string(-array) `→` MaybeSequence[str]

Passwords for protected training files.

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
`select_feature_set_trainf_svm_protected` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`protect_ocr_trainf`

## Alternatives

`select_feature_set_trainf_mlp_protected`

## See also

`select_feature_set_trainf_svm`,
`select_feature_set_svm`

## Module

OCR/OCV
