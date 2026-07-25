const {matterMarkdownAdapter} = require('@elog/plugin-adapter')

// 自定义文档处理器
// doc的类型定义为 DocDetail，详情见下方 DocDetail 类型定义
const format = (doc) => {
  doc.properties.urlname = doc.properties.date.split(' ')[0] + '-' + doc.properties.urlname
  //return doc.body;
  const newPost = matterMarkdownAdapter(doc);
  return newPost;
};

module.exports = {
  format,
};

