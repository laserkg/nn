Component({
  properties: {
    // 这里定义了innerText属性，属性值可以在组件使用时指定
    itemId: {
      type: String,
      value: 'default value'
    },
    title: {
      type: String,
      value: 'default value'
    },
    publisher: {
      type: String,
      value: 'default value'
    },
    audioUrl: {
      type: String,
      value: 'default value'
    },
    imageUrl: {
      type: String,
      value: 'default value'
    }
  },
  data: {
    // 这里是一些组件内部数据
    //播放状态: 0：play, 1:pause, 2:stop
    playStatus: 0,
    duration: 0.0,
    playTime:0.0,
    historyItems: {}
  },
  methods: {
    // 这里是一个自定义方法
    customMethod: function () { },
    formatPlayTime:function(minute, second){
      // var playTime = '00:00'
      var m, s = ''
      if(minute < 10){
        m = `0${minute}`
      }else{
        m = `${minute}`
      }
      if(second < 10){
        m = `0${second}`
      }else {
        m = `${second}`
      }
      return `${m}:${n}`
    },

    formatSecond:function(f_time){
      var f = f_time.toString().split(".")
      if (f.length == 2){
        var minute = f[0];
        var second = parseFloat(f[1]* 60)
        return formatPlayTime(minute, second);
      }else {
        return '00:00';
      }
    },
    autoPlay: function () {
      console.log("autoPlayAudio")
      this.innerAudioContext.src = this.data.audioUrl;
      this.innerAudioContext.play();
    },
    pausePlay: function () {
      console.log("pauseAudio");
      this.innerAudioContext.pause();
    },
    stopPlay: function () {
      console.log("stopAudio");
      this.innerAudioContext.stop();
    },
    destoryPlayer: function () {
      console.log("destory audio");
      this.innerAudioContext.destroy();
    },
    playAudioController: function () {
      console.log("playAudio函数")
      var status_code = 0
      if (this.data.playStatus == 0) {
        status_code = 1
        //记录播放进度
        this.pausePlay();
      } else if (this.data.playStatus == 1) {
        status_code = 2
        this.stopPlay();
      } else {//2
        status_code = 0
        //记录播放进度设置为0
        this.autoPlay();
      }
      this.setData({
        playStatus: status_code
      })
      console.log(this.data)
    },
  },

  ready: function () {
    console.log("主件播放器ready")
    console.log(this.data)
    // 获取 audio 上下文 context
    // https://mp.weixin.qq.com/debug/wxadoc/dev/api/createInnerAudioContext.html
    this.innerAudioContext = wx.createInnerAudioContext();
    this.innerAudioContext.autoplay = true;
    //监听事件
    this.innerAudioContext.onError((res) => {
      console.log(res.errMsg)
      console.log(res.errCode)
    });
    this.innerAudioContext.onPlay(() => {
      console.log('开始播放');
    });

    this.innerAudioContext.onTimeUpdate(() => {
      console.log("音频播放进度更新事件");
      if(this.data.duration == 0){
        console.log("音频播放进度更新duration:" + this.innerAudioContext.duration)
        this.setData({
          duration: this.innerAudioContext.duration
        })
      }
      var currentTime = this.innerAudioContext.currentTime;
      var playTime = currentTime * 60 | 0;
      if (this.data.playTime < playTime){
        console.log(`播放长度: ${playTime}`)
        this.setData({
          playTime: playTime
        })
      }
    });
    this.autoPlay();
  },
})