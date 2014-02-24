--register 'parseData.py' using jython as parsefun;
/***********************
 *  datareport for Nov *
 ***********************/

/*************
 *  load logs *
 *************/
log = load 'out' as(os:chararray, os_version:chararray, model:chararray, cpu:chararray, resolution:chararray, modelNum:int, launchNum:int);

DEFINE logFun1(log, gro, num) RETURNS out{
groupAns = group $log by $gro;
$out = foreach groupAns generate flatten(group), SUM($log.$num) as sum;
}

DEFINE logFun2(log, gro1, gro2, num) RETURNS out{
groupAns = group $log by ($gro1, $gro2);
$out = foreach groupAns generate flatten(group), SUM($log.$num) as sum;
}

/****************
 * Android logs *
 ****************/
logAndroid = filter log by LOWER(os) matches 'android';


write_android_model = logFun1(logAndroid, model, modelNum);
--output to file
store write_android_model into 'Android_model_Distribution';

write_android_osversion = logFun1(logAndroid, os_version, modelNum);
--output to file
store write_android_osversion into 'Android_osversion_Distribution';

write_android_resolution = logFun1(logAndroid, resolution, modelNum);
--output to file
store write_android_resolution into 'Android_resolution_Distribution';

/*
log_Android_access = group logAndroid by access;
Android_access_Dis = foreach log_Android_access generate group, SUM(logAndroid.launchNum) as sum;
--output to file
write_android_access = foreach Android_access_Dis generate $0, sum;
store write_android_access into 'Android_access_Distribution';

log_Android_city = group logAndroid by city;
Android_city_Dis = foreach log_Android_city generate group, SUM(logAndroid.launchNum) as sum;
--output to file
write_android_city = foreach Android_city_Dis generate $0, sum;
store write_android_city into 'Android_city_Distribution';

log_Android_city_access = group logAndroid by (city, access);
Android_cityAccess_Dis = foreach log_Android_city_access generate group, SUM(logAndroid.launchNum) as sum;
--output to file
write_android_cityAccess = foreach Android_cityAccess_Dis generate $0.city, $0.access, sum;
store write_android_cityAccess into 'Android_city_access_Distribution';

log_Android_city_model = group logAndroid by (city, model);
Android_cityModel_Dis = foreach log_Android_city_model generate group, SUM(logAndroid.modelNum) as sum;
--output to file
write_android_cityModel = foreach Android_cityModel_Dis generate $0.city, $0.model, sum;
store write_android_cityModel into 'Android_city_model_Distribution';
*/

logAndroidNew = filter logAndroid by os_version matches '4.*';
write_androidNew_osversionModel = logFun2(logAndroidNew, os_version, model, modelNum);
--output to file
store write_androidNew_osversionModel into 'Android_New_osversion_model_Distribution';

/****************
 * IOS logs     *
 ****************/
logIOS = filter log by not LOWER(os) matches 'android' and not LOWER(os) matches 'windowsphone';

write_ios_model = logFun1(logIOS, model, modelNum);
store write_ios_model into 'IOS_model_Distribution';

write_ios_osversion = logFun1(logIOS, os_version, modelNum);
store write_ios_osversion into 'IOS_osversion_Distribution';

write_ios_resolution = logFun1(logIOS, resolution, modelNum);
--output to file
store write_ios_resolution into 'IOS_resolution_Distribution';

/*log_IOS_access = group logIOS by access;
IOS_access_Dis = foreach log_IOS_access generate group, SUM(logIOS.launchNum) as sum;
--output to file
write_ios_access = foreach IOS_access_Dis generate $0, sum;
store write_ios_access into 'IOS_access_Distribution';

log_IOS_city = group logIOS by city;
IOS_city_Dis = foreach log_IOS_city generate group, SUM(logIOS.launchNum) as sum;
--output to file
write_ios_city = foreach IOS_city_Dis generate $0, sum;
store write_ios_city into 'IOS_city_Distribution';

log_IOS_city_access = group logIOS by (city, access);
IOS_cityAccess_Dis = foreach log_IOS_city_access generate group, SUM(logIOS.launchNum) as sum;
--output to file
write_ios_cityAccess = foreach IOS_cityAccess_Dis generate $0.city, $0.access, sum;
store write_ios_cityAccess into 'IOS_city_access_Distribution';

log_IOS_city_model = group logIOS by (city, model);
IOS_cityModel_Dis = foreach log_IOS_city_model generate group, SUM(logIOS.modelNum) as sum;
--output to file
write_ios_cityModel = foreach IOS_cityModel_Dis generate $0.city, $0.model, sum;
store write_ios_cityModel into 'IOS_city_model_Distribution';*/

logIOS = filter logIOS by os_version matches '5.*';
write_iosNew_osversionModel = logFun2(logIOS, os_version, model, modelNum);
--output to file
store write_iosNew_osversionModel into 'IOS_New_osversion_model_Distribution';
/*
log_IOS_jailbreak = group logIOS by jailbreak;
write_ios_jailbreak = foreach log_IOS_jailbreak generate flatten(group), SUM(logIOS.modelNum) as sumModel,SUM(logIOS.launchNum) as sumLaunch;
--output to file
store write_ios_jailbreak into 'IOS_jailbreak_Distribution';

write_iso_jailbreakModel = logFun2(logIOS,jailbreak, model, modelNum);
--output to file
store write_iso_jailbreakModel into 'IOS_jailbreak_model_Distribution';
*/
/********************
* WindowsPhone logs *
*********************/
logWindowsphone = filter log by LOWER(os) matches 'windowsphone';

write_windowsphone_model = logFun1(logWindowsphone, model, modelNum);
--output to file
store write_windowsphone_model into 'Windowsphone_model_Distribution';

write_windowsphone_osversion = logFun1(logWindowsphone, os_version, modelNum);
--output to file
store write_windowsphone_osversion into 'Windowsphone_osversion_Distribution';

write_windowsphone_resolution = logFun1(logWindowsphone, resolution, modelNum);
--output to file
store write_windowsphone_resolution into 'Windowsphone_resolution_Distribution';

/*log_Windowsphone_access = group logWindowsphone by access;
Windowsphone_access_Dis = foreach log_Windowsphone_access generate group, SUM(logWindowsphone.launchNum) as sum;
--output to file
write_windowsphone_access = foreach Windowsphone_access_Dis generate $0, sum;
store write_windowsphone_access into 'Windowsphone_access_Distribution';

log_Windowsphone_city = group logWindowsphone by city;
Windowsphone_city_Dis = foreach log_Windowsphone_city generate group, SUM(logWindowsphone.launchNum) as sum;
--output to file
write_windowsphone_city = foreach Windowsphone_city_Dis generate $0, sum;
store write_windowsphone_city into 'Windowsphone_city_Distribution';

log_Windowsphone_city_access = group logWindowsphone by (city, access);
Windowsphone_cityAccess_Dis = foreach log_Windowsphone_city_access generate group, SUM(logWindowsphone.launchNum) as sum;
--output to file
write_windowsphone_cityAccess = foreach Windowsphone_cityAccess_Dis generate $0.city, $0.access, sum;
store write_windowsphone_cityAccess into 'Windowsphone_city_access_Distribution';

log_Windowsphone_city_model = group logWindowsphone by (city, model);
Windowsphone_cityModel_Dis = foreach log_Windowsphone_city_model generate group, SUM(logWindowsphone.modelNum) as sum;
--output to file
write_windowsphone_cityModel = foreach Windowsphone_cityModel_Dis generate $0.city, $0.model, sum;
store write_windowsphone_cityModel into 'Windowsphone_city_model_Distribution';*/

logWindowsphoneNew = filter logWindowsphone by os_version matches '8.*';
write_windowsphoneNew_osversionModel = logFun2(logWindowsphoneNew,os_version, model, modelNum);
--output to file
store write_windowsphoneNew_osversionModel into 'Windowsphone_New_osversion_model_Distribution';


