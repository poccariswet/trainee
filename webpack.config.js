var path = require('path');

module.exports = {
    mode: 'production',
    entry: './src/main.js',
    performance: { hints: false },
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
     module: {
        rules: [
          {
            test: /\.(css|scss)$/,
            loader: 'style-loader!css-loader'
          },
          {
            test: /\.vue$/,
            use: 'vue-loader',
          },
          {
            test: /\.(jpe?g|png|gif|svg|ico)(\?.+)?$/,
            loader: 'url-loader',
          },
          {
            test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
            loader: 'file-loader'
          },
          {
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader'
          },
        ]
     },
     devServer: {
        contentBase: path.resolve(__dirname, 'dist'),
        port: 8000,
     },
};
