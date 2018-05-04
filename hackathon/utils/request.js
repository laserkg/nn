var dataset = {
  'latest': [{
    mode: 'more_mode',
    item_id: '0',
    title: '住建部部长：每天上班要看一下各地房价，年轻时也租房',
    publisher: '上观',
    summary: 'How not to feel queasy in a self-driving motor car',
    image_url: '../images/0.gif',
    // audio_url: 'http://ws.stream.qqmusic.qq.com/M500001VfvsJ21xFqb.mp3?guid=ffffffff82def4af4b12b3cd9337d5e7&uin=346897220&vkey=6292F51E1E384E061FF02C31F716658E5C81F5594D561F2E88B854E81CAAB7806D5E4F103E55D33C16F3FAC506D1AB172DE8600B37E43FAD&fromtag=46',
    audio_url: '../auido/0.mp3',
    detail_url: 'http://www.shobserver.com/detail/82927.html?tt_group_id=6533676751124431368',
    play_status: 0
  },
  {
    mode: 'more_mode',
    item_id: '1',
    title: '前联想集团中国区总裁陈旭东加盟美团任高级副总裁',
    publisher: '雷帝触网',
    summary: 'Carmakers, tech companies and ride-hailing firms are all fighting for a piece of the action' + 'Carmakers, tech companies and ride-hailing firms are all fighting for a piece of the action'
    ,
    image_url: '../images/1.jpg',
    play_status: 0,
    audio_url: '../auido/1.mp3',
    detail_url: 'https://www.toutiao.com/a6533737620994785800/'
  },
  {
    mode: 'more_mode',
    item_id: '2',
    title: '百度在前几年还能和腾讯、阿里并称三驾马车，为什么这几年衰落得这么厉害？',
    publisher: '悟空问答',
    summary: 'Pakistan’s biggest private-sector firm is betting on a fabled coal mine',
    image_url: '../images/2.jpeg',
    play_status: 0,
    audio_url: '../auido/2.mp3',
    detail_url: 'https://www.toutiao.com/a6532901976131240205/'
  },
  {
    mode: 'more_mode',
    item_id: '3',
    title: '张国立宠他、邓婕为他打掉孩子，“幸运”的张默后来怎样了？',
    publisher: '原创：妈咪Jane黄静洁',
    summary: 'The rules-based system is in grave danger',
    image_url: '../images/3.jpeg',
    detail_url: 'https://www.toutiao.com/a6533737436910977543/',
    play_status: 0,
    audio_url: '../audio/3.mp3',
  },
  {
    mode: 'more_mode',
    item_id: '4',
    title: '孙正义的江湖，或许已经落幕了',
    publisher: '鸡窝投行',
    summary: 'Which of the world’s two superpowers has the most powerful technology industry?',
    image_url: '../images/4.jpeg',
    detail_url: 'https://gbr.businessreview.global/articles/view/5a98b45e73a9cff23b232e1c/en_GB/zh_CN',
    play_status: 0,
    audio_url: '../audio/4.mp3',
    detail_url: 'https://www.toutiao.com/a6506062810986840590/'
  }
  ],
  'technology': [
    {

    }
  ],
  'finance': [
    {}
  ],
  'society': [
    {}
  ],
  'entertain': [
    {}
  ]
}

export function getLatestContent(url) {
  console.log('getLatestContent')
  return new Promise((resolve, reject) => {
    resolve(dataset.latest)
  })
}

export function getTechnology(url) {
  console.log('getTechnology')
  return new Promise((resolve, reject) => {
    resolve(dataset.technology)
  })
}

export function getFinance(url) {
  console.log('getFinance')
  return new Promise((resolve, reject) => {
    resolve(dataset.finance)
  })
}
export function getSociety(url) {
  console.log('getSociety')
  return new Promise((resolve, reject) => {
    resolve(dataset.society)
  })
}

export function getEntertain(url) {
  console.log('getEntertain')
  return new Promise((resolve, reject) => {
    resolve(dataset.entertain)
  })
}