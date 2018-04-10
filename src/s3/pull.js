const AWS = require('aws-sdk')

const s3 = new AWS.S3();

const params = {
  Bucket: process.env.BUCKET_NAME,
  Key: '811431.jpg' // example key
}

function pull(params) {
  return new Promise((resolve, reject) => {
    s3.getObject(params, (err, data) => {
      if (err) reject(err);
      else {
        resolve(data.Body)
      }
    })
  })
}

pull(params).then( res => {
  console.log(res)
}).catch(function onRejected(error) {
  console.error(error)
})

