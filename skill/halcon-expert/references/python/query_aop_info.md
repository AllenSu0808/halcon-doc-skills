# query_aop_info (Operator)

## Name

`query_aop_info` — Query indexing structure of AOP information for operators.

## Signature

`def query_aop_info(operator_name: Union[str, int], index_name: MaybeSequence[Union[str, int]], index_value: MaybeSequence[Union[str, int]]) -> Tuple[Sequence[str], Sequence[str]]`

## Description

HALCON supports a mechanism to adapt the behavior of automatic
parallelization of image processing operators (AOP) to the machine's
hardware capability. The
information for this adaption can be obtained by the operator
[`optimize_aop`](optimize_aop.md) and can be partly read and modified by the operators
[`get_aop_info`](get_aop_info.md) and [`set_aop_info`](set_aop_info.md), respectively. To address
specific AOP information the operator's optimization data is indexed within
a 3-ary hierarchy that can be obtained by `query_aop_info`. The
three hierarchy stages are indexed by the operator name, the iconic type,
and a parameter string value denoting a special mode or method supported by
the operator.

If an empty string *""* is passed to *`operator_name`*,
the parameters *`index_name`* and *`index_value`* are ignored and
all operator names in *`value`* are returned, for which optimization
data is stored.
*`name`* contains the index identifier *"operator"* as many
times as operator names are returned. Specifying a single operator
name in *`operator_name`* and passing an empty string *""* to the
parameters
*`index_name`* and *`index_value`* queries all iconic types
the operator holds optimization data for. *`value`* contains the type
strings, *`name`* the index identifier *"iconic_type"*,
respectively. Finally, when specifying a certain
operator in *`operator_name`* and a specific iconic type by passing the
dimension identifier *"iconic_type"* to *`index_name`* and
the specific iconic type to *`index_value`*, *`name`* contains
the parameter index identifier *`value`* holds the parameter string
values supported by the operator. The format of the parameter identifier
string is compound containing the string *parameter*, followed by
a colon separator *:* and a digit, denoting the
parameter index (starting with 1). If the operator does not
support any mode parameter or the operator's parameter values were not
varied during optimization process of [`optimize_aop`](optimize_aop.md) the string
*"parameter:0"* is returned for *`name`* and *`value`*
contains an empty string. In case no AOP information is stored for the
specified index, *`name`* returns an empty string.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`operator_name`** (input_control)  string `→` Union[str, int]

Operator to get information for

Default:
""

**`index_name`** (input_control)  string(-array) `→` MaybeSequence[Union[str, int]]

Further specific index

Default:
""

Suggested values:
"", "iconic_type"

**`index_value`** (input_control)  string(-array) `→` MaybeSequence[Union[str, int]]

Further specific address

Number of elements:
IndexName == IndexValue

Default:
""

Suggested values:
"", "byte", "int1", "int2", "uint2", "int4", "int8", "direction", "cyclic", "vector_field", "complex", "region", "xld", "xld_cont", "xld_poly"

**`name`** (output_control)  string-array `→` Sequence[str]

Name of next index stage

**`value`** (output_control)  string-array `→` Sequence[str]

Values of next index stage

## Result

`query_aop_info` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Module

Foundation
