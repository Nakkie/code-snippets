with stg as
(
select Dealership
,Revenue_Target
,Month
,
 [STRUCT('Range_Rover_Velar_Sales_Target' as Metric, Range_Rover_Velar_Sales_Target as Data)
,STRUCT('Discovery_Sales_Target' as Metric, Discovery_Sales_Target as Data)
,STRUCT('Range_Rover_Sport_Sales_Target' as Metric, Range_Rover_Sport_Sales_Target as Data)
,STRUCT('Jaguar_XE_Sales_Target' as Metric, Jaguar_XE_Sales_Target as Data)
,STRUCT('Jaguar_F_Pace_Sales_Target' as Metric, Jaguar_F_Pace_Sales_Target as Data)
,STRUCT('Jaguar_E_Pace_Sales_Target' as Metric, Jaguar_E_Pace_Sales_Target as Data)
,STRUCT('Range_Rover_Sales_Target' as Metric, Range_Rover_Sales_Target as Data)
,STRUCT('Jaguar_XF_Sales_Target' as Metric, Jaguar_XF_Sales_Target as Data)
,STRUCT('Range_Rover_Evoque_Sales_Target' as Metric, Range_Rover_Evoque_Sales_Target as Data)
,STRUCT('Jaguar_F_Type_Sales_Target' as Metric, Jaguar_F_Type_Sales_Target as Data)
,STRUCT('Defender_Sales_Target' as Metric, Defender_Sales_Target as Data)
,STRUCT('Freelander_Sales_Target' as Metric, Freelander_Sales_Target as Data)
,STRUCT('Jaguar_XJ_Sales_Target' as Metric, Jaguar_XJ_Sales_Target as Data)
,STRUCT('Discovery_Sport_Sales_Target' as Metric, Discovery_Sport_Sales_Target as Data)
 ] as Metrics_Data
from SheetsInput.dealership_sales_target_static
)

select stg.Dealership
,stg.Revenue_Target
,stg.Month
,replace(replace(Metric_Data.Metric,'_Sales_Target',''),'_',' ') as Model
,Metric_Data.Data as Sales_Target
from stg
cross join unnest(stg.Metrics_Data) AS Metric_Data
