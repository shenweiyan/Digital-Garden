module.exports = {
  write: {
    platform: 'yuque',
    yuque: {
      token: process.env.YUQUE_TOKEN,
      baseUrl: '',
      login: process.env.YUQUE_LOGIN,
      repo: process.env.YUQUE_REPO,
      onlyPublic: true,
      onlyPublished: true,
    },
    notion: {
      token: process.env.NOTION_TOKEN,
      databaseId: process.env.NOTION_DATABASE_ID,
      filter: true, // {property: 'status', select: {equals: '已发布'}}
      sorts: true, // [{timestamp: 'created_time', direction: 'descending'}],
      catalog: false,
    },
  },
  deploy: {
    platform: 'local',
    local: {
      outputDir: './docs/cookbook',
      filename: 'urlname',
      format: 'matter-markdown',
      catalog: true,
      formatExt: './elog.format.js',
    },
    confluence: {
      user: process.env.CONFLUENCE_USER,
      password: process.env.CONFLUENCE_PASSWORD,
      baseUrl: process.env.CONFLUENCE_BASE_URL,
      spaceKey: process.env.CONFLUENCE_SPACE_KEY,
      rootPageId: process.env.CONFLUENCE_ROOT_PAGE_ID, // 可选
      formatExt: '', // 可选
    },
  },
  image: {
    enable: true,
    platform: 'cos',
    local: {
      outputDir: 'KnowledgeGarden',
      prefixKey: '',
    },
    oss: {
      secretId: process.env.OSS_SECRET_ID,
      secretKey: process.env.OSS_SECRET_KEY,
      bucket: process.env.OSS_BUCKET,
      region: process.env.OSS_REGION,
      host: process.env.OSS_HOST,
      prefixKey: 'elog-cookbook-img',
      secretExt: '', // 可选
    },
    cos: {
      secretId: process.env.COS_SECRET_ID,
      secretKey: process.env.COS_SECRET_KEY,
      bucket: process.env.COS_IMAGE_BUCKET,
      region: process.env.COS_IMAGE_REGION,
      host: process.env.COS_HOST,
      prefixKey: 'elog-cookbook-img',
      secretExt: '', // 可选
    },
    qiniu: {
      secretId: process.env.QINIU_SECRET_ID,
      secretKey: process.env.QINIU_SECRET_KEY,
      bucket: process.env.QINIU_BUCKET,
      region: process.env.QINIU_REGION,
      host: process.env.QINIU_HOST,
      prefixKey: '',
      secretExt: '', // 可选
    },
    upyun: {
      user: process.env.UPYUN_USER,
      password: process.env.UPYUN_PASSWORD,
      bucket: process.env.UPYUN_BUCKET,
      host: process.env.UPYUN_HOST,
      prefixKey: '',
      secretExt: '', // 可选
    },
    github: {
      user: process.env.GITHUB_USER,
      token: process.env.GITHUB_TOKEN,
      repo: process.env.GITHUB_REPO,
      branch: '',
      host: '',
      prefixKey: '',
      secretExt: '', // 可选
    },
  },
}
