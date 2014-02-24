package com.umeng.dm.pigudf;
import java.util.Iterator;
import java.io.*;
import java.util.*;
import java.text.*;
import java.util.Calendar;
import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;
import org.apache.pig.data.DataBag;

public class getUsrMonth extends EvalFunc<Integer> {
	public Integer exec(Tuple input) throws IOException
    {        
        if (input==null || input.size()<2)
            return null;
        int birth=0;
        try
        {   
        	DataBag date_list=(DataBag)input.get(0);        	
        	String s_now =(String)input.get(1);
        	
        if(date_list.size()>=1)
        {
        	for(Iterator<Tuple> iter = date_list.iterator();iter.hasNext();)
        	{
        		
        		Tuple usrlog= iter.next();
        		String s_start =(String) usrlog.get(1);
        		SimpleDateFormat myFormatter = new SimpleDateFormat("yyyy-MM-dd");
                int mage = 0;
                try
                {                	
                    java.util.Date d_start = myFormatter.parse(s_start);
                    java.util.Date d_now = myFormatter.parse(s_now);
                    if(d_now.getTime()-d_start.getTime()<0)
                    		continue;
                    mage = (int)((d_now.getTime()-d_start.getTime())/(24*60*60*1000)/30)+1;
                    if(mage>birth)
                    	birth=mage;
                }catch (Exception e1)
                {
                    return null;
                }        		
        	}      	
        	
        }
        return new Integer(birth);
        }catch (Exception e)
        {
            return null;
        }
    }
}
