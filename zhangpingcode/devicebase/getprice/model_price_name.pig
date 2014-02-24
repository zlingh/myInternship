A = load 'modelprice.csv' as (model:chararray, price:int); 
B = load 'match_two.csv' as (model2:chararray, name:chararray, os:chararray);  
B2 = foreach B generate LOWER(model2) as model2, name, (LOWER(os)=='ios'? 'ios':SUBSTRING(os, 0, 7)) as os ;
A2= foreach A generate LOWER(model) as model, price;
C = join A2 by model RIGHT, B2 by model2; 
C2= foreach C generate model2, name, os, price;
store C2 into 'test2';

