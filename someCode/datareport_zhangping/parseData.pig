--register 'parseData.py' using jython as parsefun;
/*************
 *  load logs *
 *************/
log = load 'newstat_10' as(os:chararray, os_version:chararray, model:chararray, cpu:chararray, resolution:chararray, city:chararray, carrier:chararray, access:chararray, jailbreak:int, modelNum:int, launchNum:int);

/****************
 * Android logs *
 ****************/
logAndroid = filter log by os matches 'android';

log_Android_model = group logAndroid by model;
Android_model_Dis = foreach log_Android_model generate group, SUM(logAndroid.modelNum) as sum;
--output to file
write_android_model = foreach Android_model_Dis generate $0, sum;
store write_android_model into 'Android_model_Distribution';

log_Android_osversion = group logAndroid by os_version;
Android_osversion_Dis = foreach log_Android_osversion generate group, SUM(logAndroid.modelNum) as sum;
--output to file
write_android_osversion = foreach Android_osversion_Dis generate $0, sum;
store write_android_osversion into 'Android_osversion_Distribution';

log_Android_resolution = group logAndroid by resolution;
Android_resolution_Dis = foreach log_Android_resolution generate group, SUM(logAndroid.modelNum) as sum;
--output to file
write_android_resolution = foreach Android_resolution_Dis generate $0, sum;
store write_android_resolution into 'Android_resolution_Distribution';

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

logAndroidNew = filter logAndroid by os_version matches '4.*';
log_AndroidNew_osversion_model = group logAndroidNew by (os_version, model);
AndroidNew_osversionModel_Dis = foreach log_AndroidNew_osversion_model generate group, SUM(logAndroidNew.modelNum) as sum;
--output to file
write_androidNew_osversionModel = foreach AndroidNew_osversionModel_Dis generate $0.os_version, $0.model, sum;
store write_androidNew_osversionModel into 'Android_New_osversion_model_Distribution';

/****************
 * IOS logs     *
 ****************/
logIOS = filter log by not os matches 'android' and not os matches 'windowsphone';

log_IOS_model = group logIOS by model;
IOS_model_Dis = foreach log_IOS_model generate group, SUM(logIOS.modelNum) as sum;
--output to file
write_ios_model = foreach IOS_model_Dis generate $0, sum;
store write_ios_model into 'IOS_model_Distribution';

log_IOS_osversion = group logIOS by os_version;
IOS_osversion_Dis = foreach log_IOS_osversion generate group, SUM(logIOS.modelNum) as sum;
--output to file
write_ios_osversion = foreach IOS_osversion_Dis generate $0, sum;
store write_ios_osversion into 'IOS_osversion_Distribution';

log_IOS_resolution = group logIOS by resolution;
IOS_resolution_Dis = foreach log_IOS_resolution generate group, SUM(logIOS.modelNum) as sum;
--output to file
write_ios_resolution = foreach IOS_resolution_Dis generate $0, sum;
store write_ios_resolution into 'IOS_resolution_Distribution';

log_IOS_access = group logIOS by access;
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
store write_ios_cityModel into 'IOS_city_model_Distribution';

logIOS = filter logIOS by os_version matches '5.*';
log_IOS_osversion_model = group logIOS by (os_version, model);
IOS_osversionModel_Dis = foreach log_IOS_osversion_model generate group, SUM(logIOS.modelNum) as sum;
--output to file
write_iosNew_osversionModel = foreach IOS_osversionModel_Dis generate $0.os_version, $0.model, sum;
store write_iosNew_osversionModel into 'IOS_New_osversion_model_Distribution';

log_IOS_jailbreak = group logIOS by jailbreak;
IOS_jailbreak_Dis = foreach log_IOS_jailbreak generate group, SUM(logIOS.modelNum) as sumModel,SUM(logIOS.launchNum) as sumLaunch;
--output to file
write_ios_jailbreak = foreach IOS_jailbreak_Dis generate $0, sumModel, sumLaunch;
store write_ios_jailbreak into 'IOS_jailbreak_Distribution';

log_IOS_jailbreak_model = group logIOS by (jailbreak, model);
IOS_jailbreakModel_Dis = foreach log_IOS_jailbreak_model generate group, SUM(logIOS.modelNum) as sum;
--output to file
write_iso_jailbreakModel = foreach IOS_jailbreakModel_Dis generate $0.jailbreak, $0.model, sum;
store write_iso_jailbreakModel into 'IOS_jailbreak_model_Distribution';

/********************
* WindowsPhone logs *
*********************/
logWindowsphone = filter log by os matches 'windowsphone';
log_Windowsphone_model = group logWindowsphone by model;
Windowsphone_model_Dis = foreach log_Windowsphone_model generate group, SUM(logWindowsphone.modelNum) as sum;
--output to file
write_windowsphone_model = foreach Windowsphone_model_Dis generate $0, sum;
store write_windowsphone_model into 'Windowsphone_model_Distribution';

log_Windowsphone_osversion = group logWindowsphone by os_version;
Windowsphone_osversion_Dis = foreach log_Windowsphone_osversion generate group, SUM(logWindowsphone.modelNum) as sum;
--output to file
write_windowsphone_osversion = foreach Windowsphone_osversion_Dis generate $0, sum;
store write_windowsphone_osversion into 'Windowsphone_osversion_Distribution';

log_Windowsphone_resolution = group logWindowsphone by resolution;
Windowsphone_resolution_Dis = foreach log_Windowsphone_resolution generate group, SUM(logWindowsphone.modelNum) as sum;
--output to file
write_windowsphone_resolution = foreach Windowsphone_resolution_Dis generate $0, sum;
store write_windowsphone_resolution into 'Windowsphone_resolution_Distribution';

log_Windowsphone_access = group logWindowsphone by access;
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
store write_windowsphone_cityModel into 'Windowsphone_city_model_Distribution';

logWindowsphoneNew = filter logWindowsphone by os_version matches '8.*';
log_WindowsphoneNew_osversion_model = group logWindowsphoneNew by (os_version, model);
WindowsphoneNew_osversionModel_Dis = foreach log_WindowsphoneNew_osversion_model generate group, SUM(logWindowsphoneNew.modelNum) as sum;
--output to file
write_windowsphoneNew_osversionModel = foreach WindowsphoneNew_osversionModel_Dis generate $0.os_version, $0.model, sum;
store write_windowsphoneNew_osversionModel into 'Windowsphone_New_osversion_model_Distribution';

