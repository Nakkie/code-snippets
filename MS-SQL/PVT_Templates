--pivot
select period,'+string+'
from (
select fields
from pivotsource
) as sourcetable
PIVOT
(sum(Mth_Val) for CostCentreName in ('+@string+')
) as Pivottable


--unpivot
select period,'+string+'
from (
select fields
from pivotsource
) as sourcetable
UNPIVOT
(this for that in ('+@string+')
) as unPivottable
