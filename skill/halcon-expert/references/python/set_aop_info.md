# set_aop_info (Operator)

## Name

`set_aop_info` — Set AOP information for operators.

## Signature

`def set_aop_info(operator_name: MaybeSequence[Union[str, int]], index_name: MaybeSequence[Union[str, int]], index_value: MaybeSequence[Union[str, int]], info_name: str, info_value: MaybeSequence[int]) -> None`

## Description

HALCON supports a mechanism to adapt the behavior of automatic
parallelization of image processing operators (AOP) to the machine's
hardware capability. The
information for this adaption can be obtained by the operator
[`optimize_aop`](optimize_aop.md) and can also be partly read by the operator
`set_aop_info`.

To address specific AOP information the operator's optimization data
is indexed within
a 3-ary hierarchy that can be obtained by [`query_aop_info`](query_aop_info.md). The
three hierarchy stages are indexed by the operator name, passed in
*`operator_name`*, the iconic type, and
a parameter string value denoting a special mode or method supported by
the indexed operator. The latter two indices are passed by
*`index_name`*
and *`index_value`*. *`index_name`* holds the dimension
identifier whereas *`index_value`* addresses the index as returned
in [`query_aop_info`](query_aop_info.md). It is also possible to address multiple indices
on the same stage to set a specific information value to multiple knowledge
sets. Omitting an index name or passing an empty string as index value
addresses this stage in all. E.g., passing *""* to
*`operator_name`*, the tuple *["iconic_type","iconic_type"]* to
*`index_name`*, and the tuple *["byte","uint2"]* to
*`index_value`* addresses all operators processing byte or uint2
images.

`set_aop_info` sets the specific information parts of an operator's
AOP knowledge passed in *`info_value`*. The scope of information is
specified by *`info_name`* and supports the following:

- ***"max_threads"*** —

  sets the maximum allowed thread number
  this operator is allowed to run with the specified iconic type and
  parameter value.
- ***"split_level"*** —

  sets the allowed data
  split levels of the automatic parallelization for this operator, the
  specified iconic type and parameter value. Possible levels are
  *"split_tuple"*, *"split_channel"*,
  *"split_domain"*, and *"split_partial"*.

## Attention

`set_aop_info` modifies the AOP system knowledge. These modifications
will also be stored by [`write_aop_knowledge`](write_aop_knowledge.md). It is advisable to
have a backup knowledge file before modifying the system knowledge.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`operator_name`** (input_control)  string(-array) `→` MaybeSequence[Union[str, int]]

Operator to set information to

Default:
""

**`index_name`** (input_control)  string(-array) `→` MaybeSequence[Union[str, int]]

Further specific index

Default:
""

Suggested values:
"iconic_type", ["iconic_type","parameter:0"]

**`index_value`** (input_control)  string(-array) `→` MaybeSequence[Union[str, int]]

Further specific address

Number of elements:
IndexName == IndexValue

Default:
""

Suggested values:
"byte", ["uint2",""]

**`info_name`** (input_control)  string `→` str

Scope of information

Default:
"max_threads"

Suggested values:
"max_threads", "model"

**`info_value`** (input_control)  integer(-array) `→` MaybeSequence[int]

AOP information value

## Result

`set_aop_info` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Module

Foundation
