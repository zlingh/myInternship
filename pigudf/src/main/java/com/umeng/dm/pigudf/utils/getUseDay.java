/*************************************************************************
Author: HongYihong
Created Time: Thu 13 Dec 2012 03:37:38 PM CST
Description: calc days
 ************************************************************************/
package com.umeng.dm.pigudf.utils;
import java.io.*;
import java.util.*;
import java.text.*;
import java.util.Calendar;
import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;

public class getUseDay extends EvalFunc<Double>
{
    public Double exec(Tuple input) throws IOException
    {
        if (input==null || input.size() ==0)
            return new Double(29);
        try
        {
            String s_start = (String)input.get(0);
            String s_end = (String)input.get(1);
            SimpleDateFormat myFormatter = new SimpleDateFormat("yyyy-MM-dd");
            long day = 0;
            try
            {
                java.util.Date d_start = myFormatter.parse(s_start);
                java.util.Date d_end = myFormatter.parse(s_end);
                day = (d_end.getTime()-d_start.getTime())/(24*60*60*1000)+1;
                if (day>29)
                    day = 29;
                return new Double(day);
            }catch (Exception e1)
            {
                return new Double(29);
            }
        }catch (Exception e)
        {
            return new Double(29);
//            throw new IOException("Caught exception processing input row ", e);
        }
    }
}


