# inspect_clustered_components (Operator)

## Name

`inspect_clustered_components` — Inspect the rigid model components obtained from the training.

## Warning

**`inspect_clustered_components` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`inspect_clustered_components( : ModelComponents : ComponentTrainingID, AmbiguityCriterion, MaxContourOverlap, ClusterThreshold : )`

## Description

`inspect_clustered_components` creates a representation of the
rigid model components based on the training result
*`ComponentTrainingID`* in form of contour regions. The
resulting rigid model components are computed depending on the
criterion that is used to solve the ambiguities
*`AmbiguityCriterion`*, the maximum allowable contour overlap
*`MaxContourOverlap`*, and the cluster threshold
*`ClusterThreshold`* (see [`train_model_components`](train_model_components.md)). The
cluster threshold, for example, influences the merging of the
initial components. The greater the threshold is chosen, the fewer
initial components are merged. The determined rigid model components
are returned in *`ModelComponents`*.

Hence, after the components have been trained once by using
[`train_model_components`](train_model_components.md), `inspect_clustered_components`
can be used to estimate the effect of different values for the
parameters *`AmbiguityCriterion`*, *`MaxContourOverlap`*,
and *`ClusterThreshold`* without performing the complete
training procedure several times. Once the desired parameter values
have been found, they can be efficiently adopted into the training
result by using [`cluster_model_components`](cluster_model_components.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelComponents`** (output_object)  region(-array) `→` object

Contour regions of rigid model components.

**`ComponentTrainingID`** (input_control)  component_training `→`  (handle)

Handle of the training result.

**`AmbiguityCriterion`** (input_control)  string `→`  (string)

Criterion for solving the ambiguities.

Default:
'rigidity'

List of values:
'distance', 'distance_orientation', 'orientation', 'rigidity'

**`MaxContourOverlap`** (input_control)  real `→`  (real)

Maximum contour overlap of the found initial
components.

Default:
0.2

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= MaxContourOverlap && MaxContourOverlap <= 1`

**`ClusterThreshold`** (input_control)  real `→`  (real)

Threshold for clustering the initial components.

Default:
0.5

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`0 <= ClusterThreshold && ClusterThreshold <= 1`

## Result

If the handle of the training result is valid, the operator
`inspect_clustered_components` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
