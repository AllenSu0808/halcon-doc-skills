# get_params_class_gmm (Operator)

## Name

`get_params_class_gmm` — Return the parameters of a Gaussian Mixture Model.

## Signature

`def get_params_class_gmm(gmmhandle: HHandle) -> Tuple[int, int, Sequence[int], Sequence[int], str]`

## Description

`get_params_class_gmm` returns the parameters of a Gaussian
Mixture Model (GMM) that were specified when the GMM was created
with [`create_class_gmm`](create_class_gmm.md). This is particularly useful if the
GMM was read with [`read_class_gmm`](read_class_gmm.md). The output of
`get_params_class_gmm` can, for example, be used to check
whether the feature vectors and/or the target data to be used have
appropriate dimensions to be used with GMM. For a description of
the parameters, see [`create_class_gmm`](create_class_gmm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`gmmhandle`** (input_control)  class_gmm `→` HHandle

GMM handle.

**`num_dim`** (output_control)  integer `→` int

Number of dimensions of the feature space.

**`num_classes`** (output_control)  integer `→` int

Number of classes of the GMM.

**`min_centers`** (output_control)  integer-array `→` Sequence[int]

Minimum number of centers per GMM class.

**`max_centers`** (output_control)  integer-array `→` Sequence[int]

Maximum number of centers per GMM class.

**`covar_type`** (output_control)  string `→` str

Type of the covariance matrices.

## Result

If the parameters are valid, the operator
`get_params_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_class_gmm`,
`read_class_gmm`

## Possible Successors

`add_sample_class_gmm`,
`train_class_gmm`

## See also

`evaluate_class_gmm`,
`classify_class_gmm`

## Module

Foundation
