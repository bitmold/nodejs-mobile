{
  'variables': {
    'nbytes_sources': [ 'src/nbytes.cpp' ],
  },
  'targets': [
    {
      'target_name': 'nbytes',
      'type': 'static_library',
      'include_dirs': ['include'],
      'direct_dependent_settings': {
        'include_dirs': ['include'],
      },
      # nodejs-mobile patch: add C++17 standard
      "cflags_cc": ["-std=c++17"],  
      'sources': [ '<@(nbytes_sources)' ]
    },
  ]
}
