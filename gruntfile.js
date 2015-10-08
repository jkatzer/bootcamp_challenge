//Gruntfile.js based on https://lincolnloop.com/blog/simplifying-your-django-frontend-tasks-grunt/

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),


    jshint: {
      // define the files to lint
      files: ['gruntfile.js', 'frontend/js/app/**/*.js', 'frontend/js/vendor/**/*.js'],
    },

    uglify: {
      dev: {
        options: {
          sourceMap: true
        },
        files: {
          'frontend/js/app.min.js': ['frontend/js/app/**/*.js'],
          'frontend/js/lib.min.js': ['frontend/js/vendor/**/*.js']
        }
      },
      // production config
      production: {
        files: {
          'frontend/js/app.min.js': ['frontend/js/app/**/*.js'],
          'frontend/js/lib.min.js': ['frontend/js/vendor/**/*.js']
        }
      }
    },

    sass: {
      dev: {
        options: {
          includePaths: ['node_modules/bootstrap/css/'],
          sourceMap: true,
        },
        src: [ 'frontend/css/scss/main.scss' ],
        dest: 'frontend/css/main.css',
      },
      production: {
        options: {
          outputStyle: 'compressed',
          sourceMap: false
        },
        src: [ 'frontend/css/scss/main.scss' ],
        dest: 'frontend/css/main.css',
      }
    },

    watch: {
      js: {
        files: ['gruntfile.js', 'frontend/js/app/**/*.js', 'frontend/js/vendor/**/*.js'],
        tasks: ['jshint', 'uglify:dev']
      },
      css: {
        files: ['static/css/scss/main.scss'],
        tasks: ['sass:dev']
      }
    },

  // End config here

  });

  // Load plugins here.
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks here.
  grunt.registerTask('default', ['jshint', 'uglify:dev', 'sass:dev']);
  grunt.registerTask('production', ['jshint', 'uglify:production', 'sass:production']);
  //grunt.registerTask('watch', ['watch']);
  grunt.registerTask('helloworld', 'Log some stuff.', function() {
    grunt.log.write('hello world!').ok(); });

};