
# 埋点日志Topbuzz
   
   * 从"我"跳到主主页
   
    {
      "Event Name": "Tab Click", #事件名
      "View Tab": "General",
      "Source Tab": "Me",# 从哪个Tab跳转过来的
      "Language": "en",  # app的language，内置的
      "Region": "US",   # app的region，内置的
      "Network Radio": "CTRadioAccessTechnologyLTE",  #网络
      "System Language": "zh", #手机系统语言 
      "Network Access": "WIFI",  #手机系统网络接入方式
      "System Region": "CN",  #手机系统设置的region
      "Network Carrier": "中国移动",  #手机网络供应商，即SIM的供应商
      "_client_ip": "10.2.192.183", #客户端IP地址
      "Badge Show": "False",
      "Badge Number": "",
      "custom_event_index": "15121133310576522__7",
    }
    
    
   
   * 在ForYou页刷新
   
    {
    "_client_ip": "10.2.192.183",
    "refresh_type": "pull",
    "category_name": "0",
    "V3 Event Name": "category_refresh",
    "event_index": "38", # 对event的编号
    "_staging_flag": "1",
    }
 
 
 * 广告请求
 
 
     {
      "Event Name": "AD Slot Fill",
      "Impr ID": "6494477132129896713",
      "Language": "en",  
      "Region": "US",  
      "Network Radio": "CTRadioAccessTechnologyLTE",  
      "System Language": "zh",  
      "Network Access": "WIFI",  
      "System Region": "CN",  
      "Network Carrier": "中国移动",  
      "_client_ip": "10.2.192.183",
      "Abtest Versions": "217119,215642,216351,205417,219219,211696,213594,214273,216794,195324", # abtest的版本号
      "Rating": "0",
      "AD Platform": "admob",
      "Admob Native AD ID": "1512113291342",
      "AD ID": "1512113291342",
      "Admob AD Unit ID": "ca-app-pub-1436854326312437/2959551909",
      "AD Substyle": "5",
      "Advertiser": "EF英孚教育",
      "Body": "[仅限北京] 免费订阅《每日英语》，不用死记硬背就能学，零基础轻松学 ",
      "AD Type": "Admob Native AD",
      "AD Provider Id": "2100",
      "AD Style": "2",
      "CallToAction": "访问网站",
      "AD Priority": "Balance",
      "AD Request Time": "2.084735155105591",
      "Title": "出国不会说英语怎么办？",
      "ImageUrl": "https://tpc.googlesyndication.com/daca_images/simgad/11240355511297091352?w=600&h=314",
      "Admob Native AD Type": "Content",
      "Fill Sort": "2000,1000,2100,1100,2200,1200,5000,6000",
      "AD Slot Type": "stream_right_image",
      "Admob Native AD Style": "2",
    }

    
* v3"我"是mine


    {
      "Event Name": "Tab Click",
      "View Tab": "Me",
      "Source Tab": "General",
      "Language": "en",  "Region": "US",  "Network Radio": "CTRadioAccessTechnologyLTE",  "System Language": "zh",  "Network Access": "WIFI",  "System Region": "CN",  "Network Carrier": "中国移动",  "_client_ip": "10.2.192.183",
      "Badge Show": "False",
      "Badge Number": "",
      "custom_event_index": "151211437550844066__134",
    }
    {
      "_client_ip": "10.2.192.183",
      "view_tab": "mine",
      "V3 Event Name": "enter_tab",
      "event_index": "341",
      "tab_from": "home",
      "custom_event_index": "151211437550844066__134",
      "_staging_flag": "1",
    }


    
    
