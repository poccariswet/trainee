var AWS = require('aws-sdk')
var _ = require('lodash');
var fs = require('fs');
var path = require('path');

var s3 = new AWS.S3();

var myBucket = 'soe-pra-backet'
var myKey = '811431.jpg';

s3.listObjects({Bucket: myBucket}, function (err, data) {
  if(_.isNull(err)) {
    _.forEach(data.Contents, function(object) {

      if(object.Size > 0) {

//        var ws = fs.createWriteStream(path.basename(object.Key), {flags: 'a'});
        var ws = fs.createWriteStream(path.basename(myKey), {flags: 'a'});

        s3.getObject({Bucket: myBucket, Key:myKey}, function(err, result){
          ws.write(result.Body);
        });

      }

    });
  }
});
