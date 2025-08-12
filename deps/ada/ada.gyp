{
  'variables': {
    'v8_enable_i18n_support%': 1,
    'ada_sources': [ 'ada.cpp' ],
  },
  'targets': [
    {
      'target_name': 'ada',
      'type': 'static_library',
      'include_dirs': ['.'],
      'direct_dependent_settings': {
        'include_dirs': ['.'],
      },
      # nodejs-mobile patch: add C++17 standard
      "cflags_cc": ["-std=c++17"],  
      'sources': [ '<@(ada_sources)' ]
    },
  ]
}
