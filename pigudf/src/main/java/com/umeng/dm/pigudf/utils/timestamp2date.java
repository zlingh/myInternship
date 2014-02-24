/****************************************
 *Author: wanghaiyang
 *Created Time: wed 3 April 2013
 *Description: convert timestamp to local time 
 * **************************************/

package com.umeng.dm.pigudf.utils;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;
import org.apache.pig.impl.logicalLayer.schema.Schema;
import org.apache.pig.data.DataType;
import org.apache.pig.data.TupleFactory;



public class timestamp2date extends EvalFunc<Tuple>
{
	public Tuple exec(Tuple input) throws IOException{
		if(input==null||input.size()<2)
			return null;
		try{
			Tuple output = TupleFactory.getInstance().newTuple(2);//defined the output type
		 
			long timestamp = (Long)input.get(0);//input the first parameter:timestamp(long type)
			Integer TimeZone = (Integer)input.get(1);//input the second parameter:timezone(integer type)
		 
			if(timestamp<0)
			{
				return null;
				}
			timestamp = timestamp - (8-TimeZone)*3600*1000;
			String date = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss").format(new Date(timestamp));
			String Date[] = date.split(" ");
    	 
			output.set(0, Date[0]);
			output.set(1, Date[1]);
			return output;
			}catch(Exception e){
				// throw new IOException("Caught exception processing input row "
				//                      + input.toDelimitedString(",")
				//                    , e);
				return null;
				}
		}
	
	//define the output schema
	public Schema outputSchema(Schema input){
		try{
			Schema tupleSchema = new Schema();
			tupleSchema.add(new Schema.FieldSchema("Date", DataType.CHARARRAY));
			tupleSchema.add(new Schema.FieldSchema("Time", DataType.CHARARRAY));
			return new Schema(new Schema.FieldSchema(getSchemaName(this.getClass().getName().toLowerCase(),input), tupleSchema, DataType.TUPLE));
			}catch(Exception e)
			{
				return null;
				}
		}
   
}