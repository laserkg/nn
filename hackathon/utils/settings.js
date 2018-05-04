const SETTINGS = {
  channels: [{
    name: '最新',
    url: `https://m.toutiao.com/list/wxapp/?tag=__all__&ac=wap&count=20&format=json_raw&as=$[as]&cp=$[cp]&enable_stick`
  }, {
    name: '科技',
    url: `https://m.toutiao.com/list/wxapp/?tag=news_hot&ac=wap&count=20&format=json_raw&as=$[as]&cp=$[cp]&enable_stick`
  }, {
    name: '财经',
    url: `https://m.toutiao.com/list/wxapp/?tag=news_local&ac=wap&count=20&format=json_raw&as=$[as]&cp=$[cp]&enable_stick`
  }, {
    name: '社会',
    url: `https://m.toutiao.com/list/wxapp/?tag=news_society&ac=wap&count=20&format=json_raw&as=$[as]&cp=$[cp]&enable_stick`
  }, {
    name: '娱乐',
    url: `https://m.toutiao.com/list/wxapp/?tag=news_entertainment&ac=wap&count=20&format=json_raw&as=$[as]&cp=$[cp]&enable_stick`
  }]
}

/*
 * 调用时this需要是app
 */
export function getSettings(){
  var that = this;
  console.log("getSettings")
  return new Promise((resolve, reject)=>{
    if (that.globalData.settings.channels.length){
      console.log("getSettings 直接返回")
      resolve(SETTINGS)
    }else{
      //设置到global变量中
      console.log('getSettings 设置global变量')
      that.globalData.settings = SETTINGS
      resolve(that.globalData.settings)
    }
  })
}