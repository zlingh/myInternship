package com.umeng.dm.pigudf;

import java.io.*;
import java.security.*;
import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;

/**
 * refer to http://github.umeng.com/dp/umid/blob/80262d354704eeeab0bab6af32ea914112433f5d/src/main/java/com/umeng/dp/util/StringHelper.java 
 * input (device_info.id, device_info.idmd5) 
 * if idmd5 is not null use idmd5
 * else convert device_info.id to md5
 * 
 * Example usage:
 * 
 * register pigudf.jar; 
 * A = load 'a' as (name:chararray,b:chararray); 
 * dump A;
 * 
 * (356708045613393,)
 * (357516040271961,4342) 
 * (,)
 * (abc,de)
 * 
 * C = foreach A generate com.umeng.dm.pigudf.str2md5(name,b);
 * dump C;
 * (0c18573f104874a5fc576925f7541397)
 * (4342)
 * (d41d8cd98f00b204e9800998ecf8427e)
 * (de)

 * 
 */

public class str2md5 extends EvalFunc<String> {
	public static final String DEFAULT_DEVICE_ID = "unknown";
	public static final String EMPTY_MD5 = "d41d8cd98f00b204e9800998ecf8427e";
	
	public String getMd5(String str) {
		try {
			// Create MD5 Hash
			MessageDigest digest = java.security.MessageDigest
					.getInstance("MD5");
			digest.update(str.getBytes());
			byte messageDigest[] = digest.digest();

			// Create Hex String
			StringBuffer hexString = new StringBuffer();
			for (int i = 0; i < messageDigest.length; i++) {
				int var = 0xFF & messageDigest[i];
				if (var < 16)
					hexString.append("0");
				hexString.append(Integer.toHexString(var));
			}

			return hexString.toString();
		} catch (java.security.NoSuchAlgorithmException e) {
			//throw new RuntimeException(e);
			return EMPTY_MD5;
		}
	}	

	public String exec(Tuple input) throws IOException {

		// String device_id = assignValidString(input.get(0).toString,
		// DEFAULT_DEVICE_ID);
		// actually, it's umid
		if (input == null || input.size() == 0)
			return null;		
		if(input.get(1)!=null&&!(((String) input.get(1)).equals("")))
			return (String) input.get(1);
		if(input.get(0)==null)
			return EMPTY_MD5;
		if(((String)input.get(0)).equals(""))
			return EMPTY_MD5;
		
		String device_id = (String) input.get(0);
		
		if(device_id.equals(DEFAULT_DEVICE_ID))
			return EMPTY_MD5;		
		else
			return getMd5(device_id);		
	}
}
