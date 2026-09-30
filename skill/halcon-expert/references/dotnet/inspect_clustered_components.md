# InspectClusteredComponents (Operator)

## Name

`InspectClusteredComponents` — Inspect the rigid model components obtained from the training.

## Warning

**`InspectClusteredComponents` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.InspectClusteredComponents(out HObject modelComponents, HTuple componentTrainingID, HTuple ambiguityCriterion, HTuple maxContourOverlap, HTuple clusterThreshold)`

`HRegion HComponentTraining.InspectClusteredComponents(string ambiguityCriterion, double maxContourOverlap, double clusterThreshold)`

## Description

`InspectClusteredComponents` creates a representation of the
rigid model components based on the training result
*`componentTrainingID`* in form of contour regions. The
resulting rigid model components are computed depending on the
criterion that is used to solve the ambiguities
*`ambiguityCriterion`*, the maximum allowable contour overlap
*`maxContourOverlap`*, and the cluster threshold
*`clusterThreshold`* (see [`TrainModelComponents`](train_model_components.md)). The
cluster threshold, for example, influences the merging of the
initial components. The greater the threshold is chosen, the fewer
initial components are merged. The determined rigid model components
are returned in *`modelComponents`*.

Hence, after the components have been trained once by using
[`TrainModelComponents`](train_model_components.md), `InspectClusteredComponents`
can be used to estimate the effect of different values for the
parameters *`ambiguityCriterion`*, *`maxContourOverlap`*,
and *`clusterThreshold`* without performing the complete
training procedure several times. Once the desired parameter values
have been found, they can be efficiently adopted into the training
result by using [`ClusterModelComponents`](cluster_model_components.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelComponents`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Contour regions of rigid model components.

**`componentTrainingID`** (input_control)  component_training `→` [HComponentTraining](HComponentTraining.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training result.

**`ambiguityCriterion`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Criterion for solving the ambiguities.

Default:
"rigidity"

List of values:
"distance", "distance_orientation", "orientation", "rigidity"

**`maxContourOverlap`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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

**`clusterThreshold`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Threshold for clustering the initial components.

Default:
0.5

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`0 <= ClusterThreshold && ClusterThreshold <= 1`

## Result

If the handle of the training result is valid, the operator
`InspectClusteredComponents` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
