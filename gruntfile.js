//Gruntfile.js based on https://lincolnloop.com/blog/simplifying-your-django-frontend-tasks-grunt/

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),


    jshint: {
      // define the files to lint
      files: ['gruntfile.js', '/static/js/app/**/*.js', '/static/js/vendor/**/*.js'],
    }

    uglify: {
      dev {
        options: {
          sourceMap: true
        }
        files: {
          '/static/js/app.min.js': ['myproject/static/js/app/**/*.js'],
          '/static/js/lib.min.js': ['myproject/static/js/vendor/**/*.js']
        }
      }
      // production config
      production {
        files: {
          '/static/js/app.min.js': ['myproject/static/js/app/**/*.js'],
          '/static/js/lib.min.js': ['myproject/static/js/vendor/**/*.js']
        }
      }
    }

    sass: {
      dev: {
        options: {
          includePaths: ['/node_modules/bootstrap/css/'],
          sourceMap: true
        },
        src: [ '/static/css/scss/main.scss' ],
        dest: '/static/css/main.css',
      },
      production: {
        options: {
          outputStyle: 'compressed',
          sourceMap: false
        },
        src: [ '/static/css/scss/main.scss' ],
        dest: '/static/css/main.css',
      }
    },

    watch: {
      files: ['<%= sass.dev.files %>', '<%= jshint.files %>'],
      tasks: ['jshint', 'uglify:dev', 'sass:dev']
    }

  // End config here

  });

  // Load plugins here.
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks here.
  grunt.registerTask('default', ['jshint', 'uglify:dev', 'sass:dev']);
  grunt.registerTask('production', ['jshint', 'uglify:production', 'sass:production'])

};