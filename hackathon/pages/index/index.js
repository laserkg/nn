import { getLatestContent, getTechnology } from '../../utils/request.js';

const app = getApp()

Page({
  /**
   * 页面的初始数据
   */
  data: {
    lists: [],
    loadedIdMap: {},
    lock: false,
    randomHotWord: '',
    channels: [],
    channelActiveIndex: 0,
    showRefreshInfo: false,
    refreshNum: 0,
    //音频相关
    audioInfo: {
      enableAudioPlayerView: false,
      currentProgress: 0,
      currentItem: {},
      historyItems: {},
      audioAction: {
        method: 'pause'
      }
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log('index onload');
    // 获取频道信息
    app.getSettings().then((settings) => {
      console.log(settings);
      //根据频道信息初始化各频道的内容
      var init_lists = []
      for (var i = 0; i < settings.channels.length; i++) {
        init_lists[i] = []
      }
      this.setData({
        lists: init_lists,
        channels: settings.channels
      });
      console.log(this.data.lists)
    });
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    console.log("onReady")
    //初始化channel:0频道页
    this.refresh(this.data.channelActiveIndex);
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  /*
  * 用户添加函数区
  */
  onTapChannel(e) {
    console.log("index onTapChannel");
    var index = e.currentTarget.dataset.index;
    if (this.data.channelActiveIndex != index) {
      this.setData({
        channelActiveIndex: index
      })
    }

    if (this.data.lists[index].length == 0) {
      this.refresh(index)
    }
  },

  // 刷新频道页面
  refresh: function (index) {
    var channels = this.data.channels;
    var url = channels[index].url;
    getLatestContent(url).then((item_list) => {
      if (item_list.length == 0) {
        console.log(`refresh[${index}] no more found`)
        return;
      } else {
        console.log(this.data.lists)
        var channel_item_list = this.data.lists[index]
        this.data.lists[index] = channel_item_list.concat(item_list.reverse())
        this.setData({
          lists: this.data.lists
        })
      }
    })
  },
  //音频
  audioController(e) {
    e.currentTarget.className = 'headset rotating'
    var id = e.currentTarget.id;
    var active_ch_index = this.data.channelActiveIndex;
    var list = this.data.lists[active_ch_index];
    var _this = this;
    for (var i = 0, len = list.length; i < len; ++i) {
      if (list[i].item_id == id) {
        if (list[i].play_status == 0) {
          //在正式下载完之前，应该设置为转圈的状态,通过callback方法设置为1
          list[i].play_status = 1;
          list[i].loading = true;
          this.audioLoading(list[i])
            .then(function (item_index) {
              return (resolve, reject) => {
                console.log("audio loading")
                _this.data.lists[active_ch_index][item_index].loading = false;
                _this.setData({
                  lists: _this.data.lists
                })
              }
            }(i))
        } else {
          console.log('弹出下面的播放框')
          // 播放器做到全局唯一地播放一个音频
          this.audioPlay(list[i])
        }
      }
    }
    this.setData({
      lists: this.data.lists
    });
    //监控下载方法状态,再次设置playStatus。loading完自动播放的
    // 开始下载，如果下载失败呢？
    //下载成功，则设置zhuan
    //触发下载方法，
  },
  audioLoading: function (item) {
    // Promise.resolve().then()
    return new Promise(resolve => setTimeout(resolve, 2000))
  },
  //弹出播放页，音频播放,
  // 添加到播放器中
  audioPlay: function (item) {
    console.log("audio play")
    var audio_info = this.data.audioInfo;

    if (!audio_info.enableAudioPlayerView) {
      audio_info.enableAudioPlayerView = true;
    } else {
      console.log("audioPlay: add to list")
      //将正在播放的加入到 播放历史中
      var progress = 0;//获取正在播放的进度
      item['progress'] = progress
      audio_info.historyItems[item.item_id] = item;
      console.log(audio_info.historyItems)
    }
    console.log("audioPlay: play new")
    //设置将要播放的音频url
    audio_info.currentItem = item;
    audio_info.currentProgress = 0;
    //刷新播放的view
    this.setData({
      audioInfo: audio_info
    })
  },
  
  playerExit: function (e) {
    console.log("playerExit")
    var audio_info = this.data.audioInfo;
    audio_info.enableAudioPlayerView = false;
    var item = audio_info.currentItem;
    var progress = 0;//获取正在播放的进度
    item['progress'] = progress
    audio_info.historyItems[item.item_id] = item;
    this.setData({
      audioInfo: audio_info
    })
  },
})