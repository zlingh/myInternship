/*************************************************************************
Author: HongYihong
Created Time: Thu 13 Dec 2012 03:37:38 PM CST
Description: convert device_id to umid 
 ************************************************************************/
package com.umeng.dm.pigudf.utils;
import java.io.*;
import java.security.*;
import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;

public class to_umid extends EvalFunc<String>
{
    public String exec(Tuple input) throws IOException
    {
        if (input==null || input.size() ==0)
            return null;
        try
        {
            String s = (String)input.get(0);
            MessageDigest md = null;
            try
            {
                md = MessageDigest.getInstance("MD5");
                md.reset();
                md.update(s.getBytes("UTF-8"));
            }
            catch (NoSuchAlgorithmException e)
            {
                System.out.println("NoSuchAlgorithmException caught!");
                System.exit(-1);
            }
            catch (UnsupportedEncodingException e)
            {
                e.printStackTrace();  
            } 

            byte[] byteArray = md.digest();

            StringBuffer md5StrBuff = new StringBuffer();
            for (int i=0;i<byteArray.length;i++)
            {
                if (Integer.toHexString(0xFF & byteArray[i]).length()==1)
                    md5StrBuff.append("0").append(Integer.toHexString(0xFF & byteArray[i]));
                else
                    md5StrBuff.append(Integer.toHexString(0xFF & byteArray[i]));
            }
            if (md5StrBuff.length()<32)
                return md5StrBuff.toString();
            String ss = "";
            for (int i=0;i<md5StrBuff.length();i++)
            {
                if (i%2==0)
                {
                    if (md5StrBuff.charAt(i)!='0')
                        ss +=md5StrBuff.charAt(i);
                }
                else
                    ss +=md5StrBuff.charAt(i);
            }
            return ss;
        }catch (Exception e)
        {
            return null;
//            throw new IOException("Caught exception processing input row ", e);
        }
    }
}


