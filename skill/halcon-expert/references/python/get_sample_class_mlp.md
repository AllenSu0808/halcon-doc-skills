# get_sample_class_mlp (Operator)

## Name

`get_sample_class_mlp` — Return a training sample from the training data of a multilayer
perceptron.

## Signature

`def get_sample_class_mlp(mlphandle: HHandle, index_sample: int) -> Tuple[Sequence[float], Sequence[float]]`

## Description

`get_sample_class_mlp` reads out a training sample from the
multilayer perceptron (MLP) given by *`mlphandle`* that was
added with [`add_sample_class_mlp`](add_sample_class_mlp.md) or
[`read_samples_class_mlp`](read_samples_class_mlp.md). The index of the sample is
specified with *`index_sample`*. The index is counted from 0,
i.e., *`index_sample`* must be a number between 0 and
`num_samples` - 1, where `num_samples` can be
determined with [`get_sample_num_class_mlp`](get_sample_num_class_mlp.md). The training
sample is returned in *`features`* and *`target`*.
*`features`* is a feature vector of length `num_input`,
while *`target`* is a target vector of length
`num_output` (see [`add_sample_class_mlp`](add_sample_class_mlp.md) and
[`create_class_mlp`](create_class_mlp.md)).

`get_sample_class_mlp` can, for example, be used to reclassify
the training data with [`classify_class_mlp`](classify_class_mlp.md) in order to
determine which training samples, if any, are classified
incorrectly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mlphandle`** (input_control)  class_mlp `→` HHandle

MLP handle.

**`index_sample`** (input_control)  integer `→` int

Number of stored training sample.

**`features`** (output_control)  real-array `→` Sequence[float]

Feature vector of the training sample.

**`target`** (output_control)  real-array `→` Sequence[float]

Target vector of the training sample.

## Example (HDevelop)

```
* Train an MLP
create_class_mlp (NumIn, NumHidden, NumOut, 'softmax', \
                  'canonical_variates', NumComp, 42, MLPHandle)
read_samples_class_mlp (MLPHandle, 'samples.mtf')
train_class_mlp (MLPHandle, 100, 1, 0.01, Error, ErrorLog)
* Reclassify the training samples
get_sample_num_class_mlp (MLPHandle, NumSamples)
for I := 0 to NumSamples-1 by 1
    get_sample_class_mlp (MLPHandle, I, Data, Target)
    classify_class_mlp (MLPHandle, Data, 1, Class, Confidence)
    Result := gen_tuple_const(NumOut,0)
    Result[Class] := 1
    Diffs := Target-Result
    if (sum(fabs(Diffs)) > 0)
        * Sample has been classified incorrectly
    endif
endfor
```

## Result

If the parameters are valid, the operator
`get_sample_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`add_sample_class_mlp`,
`read_samples_class_mlp`,
`get_sample_num_class_mlp`

## Possible Successors

`classify_class_mlp`,
`evaluate_class_mlp`

## See also

`create_class_mlp`

## Module

Foundation
