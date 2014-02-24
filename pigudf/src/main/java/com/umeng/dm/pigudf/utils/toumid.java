package com.umeng.dm.pigudf;

import java.io.*;
import java.security.*;
import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;

/**
 *
 * refer to  http://github.umeng.com/dm/iceberg/blob/master/src/main/java/com/umeng/dp/adhoc/DailyBasicStatMR.java line 261
 * input (device_info.id, device_info.idmd5)
 * if idmd5 is not null then convert idmd5 to umid
 * else convert device_info.id to md5 and then to umid
 * md5 to umid: if len(md5) small than 32 umid=imd5 ,
 * else delet the 0 at the odd index of md5
 *
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
 * B = foreach A generate com.umeng.dm.pigudf.toumid(name,b); 
 * dump B;
 * 
 * (c18573f104874a5fc576925f7541397) 
 * (4342) 
 * (d41d8cd98f0b24e980998ecf8427e) 
 * (de)
 * 
 * 
 * 
 * 
 * 
 */
public class toumid extends EvalFunc<String> {
	public static final String DEFAULT_DEVICE_ID = "unknown";
	public static final String EMPTY_MD5 = "d41d8cd98f00b204e9800998ecf8427e";
	//public static final String EMPTY_UMID = MD5ToUmid(EMPTY_MD5);
	public static final String EMPTY_UMID = "d41d8cd98f0b24e980998ecf8427e";

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

	public static String MD5ToUmid(String md5) {
		if (md5.length() < 32)
			return md5;
		if (md5.length() > 32)
			return "";

		StringBuffer sb = new StringBuffer();
		for (int i = 0; i < 32; i += 2) {
			if (md5.charAt(i) == '0') {
				sb.append(md5.charAt(i + 1));
			} else {
				sb.append(md5.substring(i, i + 2));
			}
		}
		return sb.toString();
	}

	public String exec(Tuple input) throws IOException {

		// String device_id = assignValidString(input.get(0).toString,
		// DEFAULT_DEVICE_ID);
		// actually, it's umid
		if (input == null || input.size() == 0)
			return null;		
		if(input.get(1)!=null&&!(((String) input.get(1)).equals("")))
			return MD5ToUmid((String) input.get(1));
		if(input.get(0)==null)
			return EMPTY_UMID;
		if(((String)input.get(0)).equals(""))
			return EMPTY_UMID;
		
		String device_id = (String) input.get(0);
		
		if(device_id.equals(DEFAULT_DEVICE_ID))
			return EMPTY_UMID;		
		else
			return MD5ToUmid(getMd5(device_id));		
	}
}
