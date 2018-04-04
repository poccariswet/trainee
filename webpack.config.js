var path = require('path');

module.exports = [{
    entry: ['./src/main.js'],
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'public')
    },
     module: {
        rules: [{
            test: /\.(css|scss)$/,
            use: [
                'style-loader',
                'css-loader'
            ]
        }]
    }
}];
