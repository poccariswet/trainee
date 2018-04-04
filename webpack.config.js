var path = require('path');

module.exports = {
    entry: './src/main.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'public')
    },
     module: {
        rules: [
          {
            test: /\.(css|scss)$/,
            loader: 'style-loader!css-loader'
          },
          {
            test: /\.(jpe?g|png|gif|svg|ico)(\?.+)?$/,
            loader: 'url-loader',
          },
        ]
     }
};
