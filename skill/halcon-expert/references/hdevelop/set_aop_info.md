# set_aop_info (Operator)

## Name

`set_aop_info` — Set AOP information for operators.

## Signature

`set_aop_info( : : OperatorName, IndexName, IndexValue, InfoName, InfoValue : )`

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
*`OperatorName`*, the iconic type, and
a parameter string value denoting a special mode or method supported by
the indexed operator. The latter two indices are passed by
*`IndexName`*
and *`IndexValue`*. *`IndexName`* holds the dimension
identifier whereas *`IndexValue`* addresses the index as returned
in [`query_aop_info`](query_aop_info.md). It is also possible to address multiple indices
on the same stage to set a specific information value to multiple knowledge
sets. Omitting an index name or passing an empty string as index value
addresses this stage in all. E.g., passing *''* to
*`OperatorName`*, the tuple *['iconic_type','iconic_type']* to
*`IndexName`*, and the tuple *['byte','uint2']* to
*`IndexValue`* addresses all operators processing byte or uint2
images.

`set_aop_info` sets the specific information parts of an operator's
AOP knowledge passed in *`InfoValue`*. The scope of information is
specified by *`InfoName`* and supports the following:

- ***'max_threads'*** —

  sets the maximum allowed thread number
  this operator is allowed to run with the specified iconic type and
  parameter value.
- ***'split_level'*** —

  sets the allowed data
  split levels of the automatic parallelization for this operator, the
  specified iconic type and parameter value. Possible levels are
  *'split_tuple'*, *'split_channel'*,
  *'split_domain'*, and *'split_partial'*.

## Attention

`set_aop_info` modifies the AOP system knowledge. These modifications
will also be stored by [`write_aop_knowledge`](write_aop_knowledge.md). It is advisable to
have a backup knowledge file before modifying the system knowledge.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`OperatorName`** (input_control)  string(-array) `→`  (string / integer)

Operator to set information to

Default:
''

**`IndexName`** (input_control)  string(-array) `→`  (string / integer)

Further specific index

Default:
''

Suggested values:
'iconic_type', ['iconic_type','parameter:0']

**`IndexValue`** (input_control)  string(-array) `→`  (string / integer)

Further specific address

Number of elements:
IndexName == IndexValue

Default:
''

Suggested values:
'byte', ['uint2','']

**`InfoName`** (input_control)  string `→`  (string)

Scope of information

Default:
'max_threads'

Suggested values:
'max_threads', 'model'

**`InfoValue`** (input_control)  integer(-array) `→`  (integer)

AOP information value

## Result

`set_aop_info` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Module

Foundation
