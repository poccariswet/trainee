var path = require('path');

module.exports = {
    mode: 'production',
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
          {
            test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
            loader: 'file-loader'
          },
        ]
     },
     devServer: {
        contentBase: path.resolve(__dirname, 'public'),
        port: 8000,
     },
};
