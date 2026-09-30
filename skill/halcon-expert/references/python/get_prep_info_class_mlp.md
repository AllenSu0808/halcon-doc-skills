# get_prep_info_class_mlp (Operator)

## Name

`get_prep_info_class_mlp` — Compute the information content of the preprocessed feature vectors
of a multilayer perceptron.

## Signature

`def get_prep_info_class_mlp(mlphandle: HHandle, preprocessing: str) -> Tuple[Sequence[float], Sequence[float]]`

## Description

`get_prep_info_class_mlp` computes the information content of
the training vectors that have been transformed with the
preprocessing given by *`preprocessing`*.
*`preprocessing`* can be set to *"principal_components"*
or *"canonical_variates"*. The preprocessing methods are
described with [`create_class_mlp`](create_class_mlp.md). The information content is
derived from the variations of the transformed components of the
feature vector, i.e., it is computed solely based on the training
data, independent of any error rate on the training data. The
information content is computed for all relevant components of the
transformed feature vectors (`num_input` for
*"principal_components"* and min(`num_output` - 1,
`num_input`) for *"canonical_variates"*, see
[`create_class_mlp`](create_class_mlp.md)), and is returned in
*`information_cont`* as a number between 0 and 1. To convert
the information content into a percentage, it simply needs to be
multiplied by 100. The cumulative information content of the first
n components is returned in the n-th component of
*`cum_information_cont`*, i.e., *`cum_information_cont`*
contains the sums of the first n elements of
*`information_cont`*. To use `get_prep_info_class_mlp`, a
sufficient number of samples must be added to the multilayer
perceptron (MLP) given by *`mlphandle`* by using
[`add_sample_class_mlp`](add_sample_class_mlp.md) or [`read_samples_class_mlp`](read_samples_class_mlp.md).

*`information_cont`* and *`cum_information_cont`* can be used
to decide how many components of the transformed feature vectors
contain relevant information. An often used criterion is to require
that the transformed data must represent x% (e.g., 90%) of the
data. This can be decided easily from the first value of
*`cum_information_cont`* that lies above x%. The number thus
obtained can be used as the value for `num_components` in a
new call to [`create_class_mlp`](create_class_mlp.md). The call to
`get_prep_info_class_mlp` already requires the creation of an
MLP, and hence the setting of `num_components` in
[`create_class_mlp`](create_class_mlp.md) to an initial value. However, if
`get_prep_info_class_mlp` is called it is typically not known
how many components are relevant, and hence how to set
`num_components` in this call. Therefore, the following
two-step approach should typically be used to select
`num_components`: In a first step, an MLP with the maximum
number for `num_components` is created (`num_input` for
*"principal_components"* and
min(`num_output` - 1, `num_input`)
for *"canonical_variates"*). Then, the
training samples are added to the MLP and are saved in a file using
[`write_samples_class_mlp`](write_samples_class_mlp.md). Subsequently,
`get_prep_info_class_mlp` is used to determine the information
content of the components, and with this `num_components`.
After this, a new MLP with the desired number of components is
created, and the training samples are read with
[`read_samples_class_mlp`](read_samples_class_mlp.md). Finally, the MLP is trained with
[`train_class_mlp`](train_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mlphandle`** (input_control)  class_mlp `→` HHandle

MLP handle.

**`preprocessing`** (input_control)  string `→` str

Type of preprocessing used to transform the
feature vectors.

Default:
"principal_components"

List of values:
"canonical_variates", "principal_components"

**`information_cont`** (output_control)  real-array `→` Sequence[float]

Relative information content of the transformed
feature vectors.

**`cum_information_cont`** (output_control)  real-array `→` Sequence[float]

Cumulative information content of the transformed
feature vectors.

## Example (HDevelop)

```
* Create the initial MLP
create_class_mlp (NumIn, NumHidden, NumOut, 'softmax', \
                  'principal_components', NumIn, 42, MLPHandle)
* Generate and add the training data
for J := 0 to NumData-1 by 1
    * Generate training features and classes
    * Data = [...]
    * Class = [...]
    add_sample_class_mlp (MLPHandle, Data, Class)
endfor
write_samples_class_mlp (MLPHandle, 'samples.mtf')
* Compute the information content of the transformed features
get_prep_info_class_mlp (MLPHandle, 'principal_components',\
                         InformationCont, CumInformationCont)
* Determine NumComp by inspecting InformationCont and CumInformationCont
* NumComp = [...]
* Create the actual MLP
create_class_mlp (NumIn, NumHidden, NumOut, 'softmax', \
                  'principal_components', NumComp, 42, MLPHandle)
* Train the MLP
read_samples_class_mlp (MLPHandle, 'samples.mtf')
train_class_mlp (MLPHandle, 100, 1, 0.01, Error, ErrorLog)
write_class_mlp (MLPHandle, 'classifier.mlp')
```

## Result

If the parameters are valid, the operator
`get_prep_info_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

`get_prep_info_class_mlp` may return the error 9211 (Matrix is
not positive definite) if *`preprocessing`* =
*"canonical_variates"* is used. This typically indicates
that not enough training samples have been stored for each class.

## Possible Predecessors

`add_sample_class_mlp`,
`read_samples_class_mlp`

## Possible Successors

`clear_class_mlp`,
`create_class_mlp`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Andrew Webb: “Statistical Pattern Recognition”; Arnold, London;
1999.

## Module

Foundation
